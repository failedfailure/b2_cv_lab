import numpy as np
import tensorflow as tf
from keras.api.preprocessing import image
from keras.api.models import load_model
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
from PIL import Image, ImageTk

model = load_model("food-101_model.keras")

class_names = [
    "apple_pie", "baby_back_ribs", "baklava", "beef_carpaccio", "beef_tartare",
    "beet_salad", "beignets", "bibimbap", "bread_pudding", "breakfast_burrito",
    "bruschetta", "caesar_salad", "cannoli", "caprese_salad", "carrot_cake",
    "ceviche", "cheesecake", "cheese_plate", "chicken_curry", "chicken_quesadilla",
    "chicken_wings", "chocolate_cake", "chocolate_mousse", "churros", "clam_chowder",
    "club_sandwich", "crab_cakes", "creme_brulee", "croque_madame", "cup_cakes",
    "deviled_eggs", "donuts", "dumplings", "edamame", "eggs_benedict",
    "escargots", "falafel", "filet_mignon", "fish_and_chips", "foie_gras",
    "french_fries", "french_onion_soup", "french_toast", "fried_calamari", "fried_rice",
    "frozen_yogurt", "garlic_bread", "gnocchi", "greek_salad", "grilled_cheese_sandwich",
    "grilled_salmon", "guacamole", "gyoza", "hamburger", "hot_and_sour_soup",
    "hot_dog", "huevos_rancheros", "hummus", "ice_cream", "lasagna",
    "lobster_bisque", "lobster_roll_sandwich", "macaroni_and_cheese", "macarons", "miso_soup",
    "mussels", "nachos", "omelette", "onion_rings", "oysters",
    "pad_thai", "paella", "pancakes", "panna_cotta", "peking_duck",
    "pho", "pizza", "pork_chop", "poutine", "prime_rib",
    "pulled_pork_sandwich", "ramen", "ravioli", "red_velvet_cake", "risotto",
    "samosa", "sashimi", "scallops", "seaweed_salad", "shrimp_and_grits",
    "spaghetti_bolognese", "spaghetti_carbonara", "spring_rolls", "steak", "strawberry_shortcake",
    "sushi", "tacos", "takoyaki", "tiramisu", "tuna_tartare",
    "waffles"
]

allergens = {
    "Apple pie": ["小麦", "卵", "乳", "大豆"],
    "Baby back ribs": ["小麦", "大豆"],
    "Baklava": ["小麦", "卵", "くるみ"],
    "Beef carpaccio": ["乳", "くるみ"],
    "Beef tartare": ["卵", "大豆", "小麦", "乳"],
    "Beet salad": ["くるみ", "大豆"],
    "Beignets": ["小麦", "卵", "乳"],
    "Bibimbap": ["卵", "乳", "大豆", "ごま"],
    "Bread pudding": ["小麦", "卵", "乳", "大豆"],
    "Breakfast burrito": ["小麦", "卵", "乳", "大豆"],
    "Bruschetta": ["小麦", "乳", "大豆"],
    "Caesar salad": ["卵", "乳", "小麦", "魚介類", "大豆", "くるみ"],
    "Cannoli": ["小麦", "卵", "乳", "大豆"],
    "Caprese salad": ["乳", "大豆"],
    "Carrot cake": ["小麦", "卵", "乳"],
    "Ceviche": ["魚介類", "大豆"],
    "Cheesecake": ["小麦", "卵", "乳"],
    "Cheese plate": ["乳"],
    "Chicken curry": ["鶏肉", "乳", "大豆"],
    "Chicken quesadilla": ["小麦", "乳", "鶏肉", "大豆"],
    "Chicken wings": ["鶏肉", "小麦", "大豆"],
    "Chocolate cake": ["小麦", "卵", "乳", "大豆", "くるみ"],
    "Chocolate mousse": ["卵", "乳", "大豆"],
    "Churros": ["小麦", "卵", "乳", "大豆", "落花生"],
    "Clam chowder": ["乳", "小麦", "魚", "貝"],
    "Club sandwich": ["小麦", "卵", "乳", "大豆"],
    "Crab cakes": ["かに", "卵", "小麦", "魚", "大豆", "マスタード"],
    "Creme brulee": ["卵", "乳", "大豆", "小麦", "くるみ"],
    "Croque madame": ["小麦", "卵", "乳"],
    "Cup cakes": ["小麦", "卵", "乳", "大豆", "くるみ"],
    "Deviled eggs": ["卵", "乳", "大豆", "マスタード"],
    "Donuts": ["小麦", "卵", "乳", "大豆", "くるみ"],
    "Dumplings": ["小麦", "卵", "大豆", "ごま"],
    "Edamame": ["大豆"],
    "Eggs benedict": ["卵", "乳", "小麦", "大豆", "マスタード"],
    "Escargots": ["乳", "小麦"],
    "Falafel": ["ごま", "小麦"],
    "Filet mignon": ["乳", "小麦"],
    "Fish and chips": ["魚", "小麦", "乳"],
    "Foie gras": ["卵", "乳", "小麦"],
    "French fries": ["大豆"],
    "French onion soup": ["乳", "小麦", "大豆", "くるみ"],
    "French toast": ["小麦", "卵", "乳", "大豆"],
    "Fried calamari": ["いか", "小麦", "卵", "乳"],
    "Fried rice": ["卵", "大豆", "小麦", "魚"],
    "Frozen yogurt": ["乳", "卵", "小麦", "大豆", "落花生", "くるみ"],
    "Garlic bread": ["小麦", "乳", "大豆"],
    "Gnocchi": ["小麦", "卵", "乳"],
    "Greek salad": ["乳", "大豆"],
    "Grilled cheese sandwich": ["小麦", "乳"],
    "Grilled salmon": ["さけ"],
    "Guacamole": [],
    "Gyoza": ["小麦", "大豆", "ごま"],
    "Hamburger": ["小麦", "牛肉", "大豆"],
    "Hot and sour soup": ["大豆", "ごま"],
    "Hot dog": ["小麦", "乳", "大豆"],
    "Huevos rancheros": ["卵", "乳", "小麦"],
    "Hummus": ["ごま"],
    "Ice cream": ["乳", "卵", "大豆", "小麦", "くるみ"],
    "Lasagna": ["小麦", "乳", "卵", "牛肉", "大豆"],
    "Lobster bisque": ["えび", "乳", "小麦"],
    "Lobster roll sandwich": ["えび", "小麦", "卵"],
    "Macaroni and cheese": ["小麦", "乳"],
    "Macarons": ["卵", "アーモンド"],
    "Miso soup": ["大豆", "魚", "小麦"],
    "Mussels": ["貝"],
    "Nachos": ["乳", "小麦"],
    "Omelette": ["卵", "乳"],
    "Onion rings": ["小麦", "乳", "大豆"],
    "Oysters": ["貝"],
    "Pad thai": ["卵", "落花生", "えび", "小麦", "大豆"],
    "Paella": ["魚", "えび", "貝"],
    "Pancakes": ["小麦", "卵", "乳"],
    "Panna cotta": ["乳", "卵", "小麦", "大豆", "くるみ"],
    "Peking duck": ["小麦", "大豆"],
    "Pho": ["牛肉", "魚", "小麦"],
    "Pizza": ["小麦", "乳", "大豆"],
    "Pork chop": ["豚肉", "小麦", "大豆"],
    "Poutine": ["乳", "小麦"],
    "Prime rib": ["牛肉", "小麦"],
    "Pulled pork sandwich": ["豚肉", "小麦", "大豆"],
    "Ramen": ["小麦", "卵", "大豆", "魚", "ごま"],
    "Ravioli": ["小麦", "卵", "乳", "大豆"],
    "Red velvet cake": ["小麦", "卵", "乳", "大豆"],
    "Risotto": ["乳"],
    "Samosa": ["小麦", "卵", "乳"],
    "Sashimi": ["魚"],
    "Scallops": ["貝"],
    "Seaweed salad": ["大豆", "小麦", "ごま"],
    "Shrimp and grits": ["えび", "乳", "卵"],
    "Spaghetti bolognese": ["小麦", "乳", "卵", "牛肉", "大豆"],
    "Spaghetti carbonara": ["小麦", "卵", "乳", "大豆"],
    "Spring rolls": ["小麦", "卵", "大豆", "ごま"],
    "Steak": ["牛肉"],
    "Strawberry shortcake": ["小麦", "卵", "乳", "大豆"],
    "Sushi": ["魚", "えび", "かに", "卵", "小麦", "大豆", "ごま"],
    "Tacos": ["小麦", "乳", "大豆", "牛肉"],
    "Takoyaki": ["小麦", "卵", "乳", "たこ", "大豆"],
    "Tiramisu": ["小麦", "卵", "乳"],
    "Tuna tartare": ["魚", "卵", "大豆"],
    "Waffles": ["小麦", "卵", "乳", "大豆"]
}

def normalize_class_name(name):
    name_with_spaces = name.replace('_', ' ')
    return name_with_spaces[0].upper() + name_with_spaces[1:].lower()

def predict_allergens(model, img_path, class_names, allergen_dict):
    img = tf.keras.preprocessing.image.load_img(img_path, target_size=(224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])

    predicted_class_lower = predicted_class.lower()

    matched_name = None
    for food_name in allergen_dict:
        if food_name.lower() == predicted_class_lower.replace("_", " "):
            matched_name = food_name
            break

    if matched_name is None:
        matched_name = predicted_class.replace("_", " ").capitalize()  # fallback
    
    allergens = allergen_dict.get(matched_name, [])

    return matched_name, confidence, allergens

def create_gui():
    def on_file_drop():
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
        if file_path:
            img = Image.open(file_path)
            img.thumbnail((280, 280))
            tk_img = ImageTk.PhotoImage(img)
            image_label.config(image=tk_img)
            image_label.image = tk_img

            predicted_class, confidence, found_allergens = predict_allergens(
                model, file_path, class_names, allergens
            )
            result_text = (
                f"料理名: {predicted_class}\n"
                f"信頼度: {confidence:.2f}\n"
                f"アレルゲン: {'、'.join(found_allergens) if found_allergens else 'N/A'}"
            )
            result_label.config(text=result_text)

    root = tk.Tk()
    root.title("Food Detection & Allergen")

    jp_font = tkFont.Font(family="Noto Sans CJK JP", size=12)

    instruction = tk.Label(root, text="Please select your picture.", font=("Arial", 12))
    instruction.pack()

    select_button = tk.Button(root, text="Select", command=on_file_drop)
    select_button.pack()

    global image_label
    image_label = tk.Label(root)
    image_label.pack()

    global result_label
    result_label = tk.Label(root, text="", font=jp_font, justify="left")
    result_label.pack()

    root.mainloop()

create_gui()
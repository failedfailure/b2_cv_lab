import numpy as np
import tensorflow as tf
from keras.api.models import load_model
from keras.applications.vgg16 import preprocess_input
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
from PIL import Image, ImageTk

model = load_model("food-101_model.keras")

class_names = [...]  # 元の class_names をそのまま貼り付けてください（長いため省略）

allergens = {...}  # 元の allergen 辞書をそのまま貼り付けてください（長いため省略）

def normalize_class_name(name):
    name_with_spaces = name.replace('_', ' ')
    return name_with_spaces[0].upper() + name_with_spaces[1:].lower()

def predict_topk_allergens(model, img_path, class_names, allergen_dict, top_k=3):
    img = Image.open(img_path).convert("RGB")
    img = img.resize((224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    predictions = model.predict(img_array)[0]
    top_indices = predictions.argsort()[-top_k:][::-1]
    results = []

    for idx in top_indices:
        confidence = predictions[idx]
        if confidence < 0.5:
            results.append(("判別不能", confidence, []))
            continue

        class_name = class_names[idx]
        formatted = class_name.replace('_', ' ')

        matched_name = None
        for food_name in allergen_dict:
            if food_name.lower() == formatted.lower():
                matched_name = food_name
                break
        if not matched_name:
            matched_name = formatted.capitalize()

        allergens = allergen_dict.get(matched_name, [])
        results.append((matched_name, confidence, allergens))

    return results

def create_gui():
    def on_file_drop():
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
        if file_path:
            img = Image.open(file_path).convert("RGB")
            img = img.resize((224, 224))
            tk_img = ImageTk.PhotoImage(img)
            image_label.config(image=tk_img)
            image_label.image = tk_img

            results = predict_topk_allergens(model, file_path, class_names, allergens)

            result_text = "\n".join([
                f"候補 {i+1}: {name}\n信頼度: {conf:.2f}\nアレルゲン: {'、'.join(allgs) if allgs else 'N/A'}"
                for i, (name, conf, allgs) in enumerate(results)
            ])
            result_label.config(text=result_text)

    root = tk.Tk()
    root.title("Food Detection & Allergen (Enhanced)")

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

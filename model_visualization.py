import visualkeras
from keras.models import load_model
from PIL import ImageFont

model = load_model('food-101_model.keras')

# 可选字体
font = None
try:
    font = ImageFont.truetype("arial.ttf", 360)
except:
    pass

visualkeras.layered_view(model, legend=True, font=font, to_file='output.png')
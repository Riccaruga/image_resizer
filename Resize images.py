from PIL import Image
import os

directory = os.getcwd()

# desired width and height
width = 2048
height = 2048

for filename in os.listdir(directory):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        img = Image.open(os.path.join(directory, filename))
        img_resized = img.resize((width, height))
        new_filename = filename
        img_resized.save(os.path.join(directory, new_filename))
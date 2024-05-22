from PIL import Image
import os 

files = os.listdir('dataset/Testing/white_mushroom')

for i in range(len(files)):
    img = Image.open(f'dataset/Testing/white_mushroom/{str(i)}.jpg')
    if img.format != 'JPEG':
        print(img.filename, img.format)

#os.getcwd()
#collection = "dataset/Training/white_mushroom"
#for i, filename in enumerate(os.listdir(collection)):
#    os.rename("dataset/Training/white_mushroom/" + filename, "dataset/Training/white_mushroom/" + str(i) + ".jpg")
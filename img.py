from PIL import Image
import os 

name = 'gruzdi'
var = 'Training'

os.getcwd()
collection = f"dataset1/{var}/{name}"
for i, filename in enumerate(os.listdir(collection)):
    os.rename(f"dataset1/{var}/{name}/" + filename, f"dataset1/{var}/{name}/" + str(i) +str(i)+str(i)+ ".jpg")
    

for i, filename in enumerate(os.listdir(collection)):
    os.rename(f"dataset1/{var}/{name}/" + filename, f"dataset1/{var}/{name}/" + str(i) + ".jpg")

files = os.listdir(f'dataset1/{var}/{name}')

for i in range(len(files)):
    img = Image.open(f'dataset1/{var}/{name}/{str(i)}.jpg')
    if img.format != 'JPEG' and img.format != 'PNG':
        print(img.filename, img.format)
        img.close()
        os.remove(f'dataset1/{var}/{name}/{str(i)}.jpg')
        print('Удален')
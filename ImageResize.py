from PIL import Image

def resizeImage(img_name, height, width):
    img = Image.open(img_name)

    newImage = img.resize((height,width), resample=0)
    newImage.save(img_name,'png')

for i in range(10):
    resizeImage('n'+str(i)+'.png',62,50)

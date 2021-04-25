
from PIL import Image, ImageOps
try: 
    img  = Image.open("TestImage.png") 
except IOError:
    pass
im2 = ImageOps.grayscale(img)
im2.show()
 








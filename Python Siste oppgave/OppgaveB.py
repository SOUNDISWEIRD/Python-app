from PIL import Image
import pilgram

im = Image.open('FJELL.jpeg')
pilgram.willow(im).save('Willow.jpeg')
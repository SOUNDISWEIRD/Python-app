from PIL import Image
import pilgram

im = Image.open('FJELL.jpeg')
pilgram._1977(im).save('FERDIG.jpg')
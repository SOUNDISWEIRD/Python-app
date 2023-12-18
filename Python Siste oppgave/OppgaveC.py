from PIL import Image
import pilgram
 
im = Image.open('Willow.jpeg')
 
direction = input("Skriv in hvor mange grader du vil at bilde skla snus, enten, 90, 180, 270 og 360:")

if direction == "90":
    im = im.rotate(90)
elif direction == "180":
    im = im.rotate(180)
elif direction == "270":
    im = im.rotate(270)
elif direction == "360":
    im = im.rotate(360)

else:
    print("Skriv in hvor mange grader du vil at bilde skla snus, enten 90, 180, 270 og 360")
pilgram.inkwell(im).save('Rotate.jpg')
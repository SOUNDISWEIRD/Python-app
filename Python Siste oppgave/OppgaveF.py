from PIL import Image, ImageDraw, ImageFont

text = input("Enter text on image: ")

im = Image.open("FJELL.jpeg")

draw = ImageDraw.Draw(im)

font = ImageFont.load_default().font_variant(size=50)
draw.text((0, 0), text, fill="black", font=font)
im.save("FJELL_text.jpg")
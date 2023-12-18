from PIL import Image
import pilgram, os

path = "FJELL.jpeg"
im = Image.open(path)

if im.width < 1080:
    add = 1080 - im.width
    fn, fex = os.path.splitext(path)
    im.resize((add + im.width, add + im.height)).save(f"{fn}_resized{fex}")
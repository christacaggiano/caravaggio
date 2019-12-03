from PIL import Image

im = Image.open("test/Caravaggio_2.jpg", "r")
im2 = im.copy()

im2.thumbnail(size=(64, 64), resample=0)
im2.show()

# im = im.resize(size=(50, 100), resample=Image.NEAREST)
# im.show()

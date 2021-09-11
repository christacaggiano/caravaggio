from PIL import Image
import os

Image.MAX_IMAGE_PIXELS = 933120000

output_directories = ["test_bw", "training_bw"]
input_directories = ["test", "training"]

# make black and white directories for first version
if not os.path.exists(output_directories[0]):
    os.makedirs(output_directories[0])
if not os.path.exists(output_directories[1]):
    os.makedirs(output_directories[1])

for input_dir, output_dir in zip(input_directories, output_directories):
    for filename in os.listdir(input_dir):
        output_name = output_dir + "/" + filename.split(".")[0] + "_bw_1000x1000.png"

        im2 = Image.open(input_dir + "/" + filename, "r").copy()  # open image
        im2_resize = im2.resize(size=(1000, 1000))  # resize to 64 pixels by 64 pixels
        im2_bw = im2_resize.convert('LA')  # make greyscale

        im2_bw.save(output_name, "PNG")

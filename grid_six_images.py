from PIL import Image, ImageDraw, ImageFont
import glob
import os
import sys

if len(sys.argv) < 8:
    print("expected 6 input directories and 1 output directory, got:", len(sys.argv) - 1)
    exit()

six_dirs = [sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6]]
output_dir = sys.argv[7]

ref_files = glob.glob(six_dirs[0] + "/*.jpg")
for file in ref_files:
    ref_name = os.path.basename(file)
    images = []
    for i in range(6):
        images.append(Image.open(os.path.join(six_dirs[i], ref_name)).resize((400, 400)))
    # Create a new blank image
    new_image = Image.new('RGB', (1200, 800))

    # Paste each image onto the new image in the correct position
    new_image.paste(images[0], (0, 0))
    new_image.paste(images[1], (400, 0))
    new_image.paste(images[2], (800, 0))
    new_image.paste(images[3], (0, 400))
    new_image.paste(images[4], (400, 400))
    new_image.paste(images[5], (800, 400))

    # Add titles to each image
    draw = ImageDraw.Draw(new_image)
    draw.text((20, 10), os.path.normpath(six_dirs[0]).split(os.sep)[-3], fill='black')
    draw.text((420, 10), os.path.normpath(six_dirs[1]).split(os.sep)[-3], fill='black')
    draw.text((820, 10), os.path.normpath(six_dirs[2]).split(os.sep)[-3], fill='black')
    draw.text((20, 410), os.path.normpath(six_dirs[3]).split(os.sep)[-3], fill='black')
    draw.text((420, 410), os.path.normpath(six_dirs[4]).split(os.sep)[-3], fill='black')
    draw.text((820, 410), os.path.normpath(six_dirs[5]).split(os.sep)[-3], fill='black')

    new_image.save(os.path.join(output_dir, ref_name))

from PIL import Image
import os, sys
import glob

if len(sys.argv) < 2:
    print("no directory specified, please input target directory")
    exit()

root_dir = sys.argv[1]

out_size = 640
for filename in os.listdir(root_dir):
    print(filename)
    im = Image.open(root_dir + filename)
    imResize = im.resize((out_size,out_size), Image.ANTIALIAS)
    imResize.save(root_dir + filename , 'JPEG', quality=90)
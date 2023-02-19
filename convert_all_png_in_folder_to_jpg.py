import glob
import os
from PIL import Image

path = '/data2/projects/YOLOX/datasets/VOCdevkit/VOC2007/JPEGImages/'
png_files = glob.glob(path + '/*.png')

for file in png_files:
    im = Image.open(file)
    im.save(file[:-3]+'jpg')
    os.remove(file)

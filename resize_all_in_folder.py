from PIL import Image
import os, sys
import glob

root_dir = "/home/yz9qvs/pothole_dataset/test_data/Roboflow-Pavement-Surface/"


for filename in os.listdir(root_dir):
    print(filename)
    im = Image.open(root_dir + filename)
    imResize = im.resize((640,640), Image.ANTIALIAS)
    imResize.save(root_dir + filename , 'JPEG', quality=90)
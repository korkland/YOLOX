import os
import random
import sys
import shutil

if len(sys.argv) < 2:
    print("no directory specified, please input target directory")
    exit()

root_path = sys.argv[1]
# root_path = "~/YOLOX/datasets/VOCdevkit/VOC2007"
if not os.path.exists(root_path):
    print("cannot find such directory: " + root_path)
    exit()

jpgfilepath = root_path + '/JPEGImages/'
if not os.path.exists(jpgfilepath):
    print("cannot find such directory: " + jpgfilepath)
    exit()

xmlfilepath = root_path + '/Annotations/'
if not os.path.exists(xmlfilepath):
    print("cannot find such directory: " + xmlfilepath)
    exit()

valid_copy_path = root_path + "/ValidCopy/"
if not os.path.exists(valid_copy_path):
    os.makedirs(valid_copy_path)

txtsavepath = root_path + '/ImageSets/Main'
if not os.path.exists(txtsavepath):
    os.makedirs(txtsavepath)

train_percent = 0.85
total_xml = os.listdir(xmlfilepath)
num = len(total_xml)
list = range(num)
tr = int(num * train_percent)
train_idxs = random.sample(list, tr)

print("train size:", tr)
print("valid size:", num - tr)

ftrain = open(txtsavepath + '/train.txt', 'w')
fvalid = open(txtsavepath + '/valid.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in train_idxs or 'NoLabel' in name:
        ftrain.write(name)
    else:
        fvalid.write(name)
        shutil.copyfile(jpgfilepath + total_xml[i][:-4] + ".jpg", valid_copy_path + total_xml[i][:-4] + ".jpg")
        

ftrain.close()
fvalid.close()
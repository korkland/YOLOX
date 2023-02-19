import os
import sys
import glob

'''
This script will remove all jpg that do not have matched xml
'''

if len(sys.argv) < 2:
    print("no directory specified, please input target directory")
    exit()

root_path = sys.argv[1]
if not os.path.exists(root_path):
    print("cannot find such directory: " + root_path)
    exit()

xml_files = glob.glob(root_path + '/*.xml')
img_files = glob.glob(root_path + '/*.jpg') + glob.glob(root_path + '/*.png')

for file in img_files:
    if file[:-3] + 'xml' in xml_files:
        continue
    os.remove(file)

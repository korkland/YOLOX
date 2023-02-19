import os
import sys
import glob
from lxml import etree

if len(sys.argv) < 3:
    print("no directory specified, please input target directory")
    exit()

root_dir = sys.argv[1]
prefix = sys.argv[2]

if len(sys.argv) == 5:
    xml_path = sys.argv[3]
    img_path = sys.argv[4]
else:
    xml_path = img_path = root_dir

xml_files = glob.glob(xml_path + '/*.xml')
img_files = glob.glob(img_path + '/*.jpg') + glob.glob(img_path + '/*.png')

parser = etree.XMLParser(remove_blank_text=True, remove_comments=True)

idx_name = 0
for img in img_files:
    xml = img[:-4] + '.xml'
    if xml not in xml_files:
        print("directory contain", img, "file, with no matching xml", xml, "SKIPPING!")
        continue

    new_name = prefix + f'{idx_name:06d}'

    img_new_name = new_name + img[-4:]
    xml_new_name = new_name + xml[-4:]

    tree = etree.parse(xml, parser)
    root = tree.getroot()

    labels = root.findall("object")
    if not labels:
        print(img_new_name, "is unlabeled, NoLabel attached")
        img_new_name = "NoLabel_" + img_new_name
        xml_new_name = "NoLabel_" + xml_new_name

    root.find("filename").text = img_new_name
    root.find("path").text = img_new_name
    tree.write(xml, encoding='UTF-8', xml_declaration=False, pretty_print=True)

    os.rename(img, os.path.join(img_path, img_new_name))  # image
    os.rename(xml, os.path.join(xml_path, xml_new_name))  # annotation

    idx_name += 1

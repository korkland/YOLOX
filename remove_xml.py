import os
import sys
import xml.etree.ElementTree as ET

'''
This script will move unlabel files to NoLabel dir
In addition it will move labels files that are diff than 'Crack' and 'Pothole' to SpecialLabels dir
Input: directory - contains Annotations (.xml) and JPEGImages (.jpg)
'''

if len(sys.argv) < 2:
    print("no directory specified, please input target directory")
    exit()

root_path = sys.argv[1]
if not os.path.exists(root_path):
    print("cannot find such directory: " + root_path)
    exit()

xml_file_path = root_path + '/Annotations/'
if not os.path.exists(xml_file_path):
    print("cannot find such directory: " + xml_file_path)
    exit()

jpg_file_path = root_path + '/JPEGImages/'
if not os.path.exists(jpg_file_path):
    print("cannot find such directory: " + jpg_file_path)
    exit()

no_label_path = root_path + '/NoLabel/'
if not os.path.exists(no_label_path):
    os.mkdir(no_label_path)

special_label_path = root_path + '/SpecialLabels/'
if not os.path.exists(special_label_path):
    os.mkdir(special_label_path)

total_xml = os.listdir(xml_file_path)

num_of_deleted_files = 0
for xml_file_name in total_xml:
    tree = ET.parse(xml_file_path + xml_file_name)
    root = tree.getroot()
    labels = root.findall("object")
    jpg_file_name = root.find("filename").text
    if not labels:
        print("No label", jpg_file_name)
        os.rename(jpg_file_path + jpg_file_name, no_label_path + jpg_file_name) #image
        os.rename(xml_file_path + xml_file_name, no_label_path + xml_file_name) #annotation
        num_of_deleted_files += 1
        continue
    for object in labels:
        object_name = object.find("name").text
        if object_name != "Crack" and object_name != "Pothole":
            os.rename(jpg_file_path + jpg_file_name, special_label_path + jpg_file_name) #image
            os.rename(xml_file_path + xml_file_name, special_label_path + xml_file_name) #annotation
            num_of_deleted_files += 1
            break

print("num of deleted files:", num_of_deleted_files)
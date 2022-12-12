from PIL import Image
import os, sys
import glob
from lxml import etree

root_dir = "/home/yz9qvs/pothole_dataset/Roboflow-Pavement-Surface/train/"
prefix = 'Pavement_'

xml_path = root_dir + "xml/"
xml = os.listdir(xml_path)

jpg_path = root_dir + "jpg/"
jpg = os.listdir(jpg_path)
num = len(xml)
list = range(num)

for i in list:
    xml_name = xml[i]
    xml_path_name = xml_path + xml_name
    
    jpg_name = xml_name[:-4] + ".jpg"
    jpg_path_name = jpg_path + jpg_name

    new_name = prefix + f'{i:06d}'
    xml_new_name = new_name + ".xml"
    jpg_new_name = new_name + ".jpg"

    parser = etree.XMLParser(remove_blank_text=True, remove_comments=True)
    tree = etree.parse(xml_path_name, parser)
    root = tree.getroot()
    root.find("filename").text = jpg_new_name
    root.find("path").text = jpg_new_name
    tree.write(xml_path_name, encoding='UTF-8', xml_declaration=False, pretty_print=True)

    os.rename(jpg_path_name, jpg_path + jpg_new_name) #image
    os.rename(xml_path_name, xml_path + xml_new_name) #annotation
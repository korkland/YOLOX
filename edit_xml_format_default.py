import os
from lxml import etree


root_dir = "/home/yz9qvs/YOLOX/datasets/VOCdevkit/VOC2007/Annotations/"

xml = os.listdir(root_dir)
num = len(xml)
list = range(num)

for i in list:
    name = xml[i]
    xml_path_name = root_dir + name

    parser = etree.XMLParser(remove_blank_text=True, remove_comments=True)
    tree = etree.parse(xml_path_name, parser)
    root = tree.getroot()
    
    labels = root.findall('object')
    write = False
    for object in labels:
        pose = object.find('pose')
        if pose is None:
            pose = etree.SubElement(object, 'pose')
            pose.text = 'Unspecified'
            write = write or True

        truncated = object.find('truncated')
        if truncated is None:
            truncated = etree.SubElement(object, 'truncated')
            truncated.text = '0'
            write = write or True

        difficult = object.find('difficult')
        if difficult is None:
            difficult = etree.SubElement(object, 'difficult')
            difficult.text = '0'
            write = write or True

    if write:
        tree.write(xml_path_name, encoding='UTF-8', xml_declaration=True, pretty_print=True)
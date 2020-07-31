import xml.etree.ElementTree as ET
import argparse
import os

ap = argparse.ArgumentParser()
ap.add_argument("-x", "--xml", required=True, help="path to XML file")
args = vars(ap.parse_args())

ymin, xmin, ymax, xmax = None, None, None, None

tree = ET.parse(args["xml"])
root = tree.getroot()
for obj in root.iter('object'):
	xml_box = obj.find('bndbox')
	xmin = (int(xml_box.find('xmin').text) - 1)
	ymin = (int(xml_box.find('ymin').text) - 1)
	xmax = (int(xml_box.find('xmax').text) - 1)
	ymax = (int(xml_box.find('ymax').text) - 1) 

result = "boat " + str(xmin) + " " + str(ymin) + " " + str(xmax) + " " + str(ymax)
print(result)
files = os.path.splitext(args["xml"])[0] + ".txt"
file = open(files, "w")
file.write(result)
file.close

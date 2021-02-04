# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import os

file = os.path.dirname(__file__)
os.chdir(file)

tree = ET.parse("data.xml")
root = tree.getroot()

print("Root[0][1]: ", root[0][1])

for child in root:
    print(f"tag: {child.tag}, attrib: {child.attrib}")
    for tags in list(child):
        print(tags.text)


for user in root.findall('users'):
    nom = user.find('nom')
    prix = user.find('metier')
    print(f"User: [nom: {nom}, prix: {prix}]")
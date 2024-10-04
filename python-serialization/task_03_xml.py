#!/usr/bin/python3
"""This Module countain serialization and deserialization using XML"""
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """Serialize dict python to xml frome a file"""
    root = ET.Element("racine")  # Créer une "Racine"

    for key, value in dictionary.items():  # Itérer pour chaque key dans le dict
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)  # tree = le dictionnaire
    tree.write(filename)  # écrire la data

def deserialize_from_xml(filename):
    """Deserialize xml data to python dict"""
    tree = ET.parse(filename)
    root = tree.getroot()

    for child in root:
    key = child.tag
    value = child.text

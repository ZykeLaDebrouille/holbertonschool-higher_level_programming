#!/usr/bin/python3
"""Module that countain a script that add arg in the file add_item.json"""
# Load, add, save
import sys
import os.path
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


filename = "add_item.json"

# Charger la liste existante ou créer une nouvelle liste
if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Ajouter les nouveaux arguments à la liste
my_list.extend(sys.argv[1:])

# Sauvegarder la liste mise à jour
save_to_json_file(my_list, filename)

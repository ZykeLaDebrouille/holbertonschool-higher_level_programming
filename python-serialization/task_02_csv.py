#!/usr/bin/python3
"""This Module countain focus on converting CSV data 
        into JSON format using serialization techniques."""
import csv, json


def convert_csv_to_json(csv_filename):
    """converting CSV data into JSON format using serialization"""
    with open(csv_filename, mode='w') as file:
        json.dumps(csv_filename)

#!/usr/bin/python3
"""
Module for adds all arguments to a Python list.
"""
import json
import os.path
import sys
save_json_file = __import__('5-save_to_json_file').save_to_json_file
load_jason_file = __import__('6-load_from_json_file').load_from_json_file

file = "add_item.json"
jsonlist = []
if os.path.exists(file):
    jsonlist = load_jason_file(file)

for element in range(1, len(sys.argv)):
    jsonlist.append(sys.argv[element])

save_json_file(jsonlist, file)

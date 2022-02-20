#!/usr/bin/python3
import os

# Load items line by line from file 
def file2list(filepath):
    items = []
    if not os.path.exists(filepath): print('No file exists!')
    else:
        with open(filepath, "r") as file:
            lines = file.readlines()
            for line in lines:
                items.append(line.split('\n')[0])
    return items

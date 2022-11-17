#!/usr/bin/env python3
#coding=utf-8

'''

Reads the directory and outputs all sub-dir and
files within into a .txt file in a clean style

Nothing fancy, nothing complex -> simple & straightforward. 

How to:
- Put the file into a root folder
- Run Script
- Output.txt will be generated in root folder

'''

import os

absolute_path = os.path.dirname(__file__)

with open("output.txt", "w", newline='', encoding="utf-8") as a:
    for path, subdirs, files in os.walk(absolute_path):
        a.write('.\\' + os.path.relpath(path + os.linesep, start=absolute_path)) 
        for filename in files:
            a.write('\t%s\n' % filename)
print("Done")

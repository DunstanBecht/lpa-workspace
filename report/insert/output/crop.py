#!/usr/bin/env python
# coding: utf-8

with open("output_data.dat", 'r') as f:
    content = f.readlines()

for i in range(len(content)):
    if len(content[i])>69:
        content[i] = content[i][:68]+"... \n"

with open("output_data.dat", 'w') as f:
    f.write(''.join(content[:17]))
    f.write('...')

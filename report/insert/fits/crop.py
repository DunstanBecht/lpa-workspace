#!/usr/bin/env python
# coding: utf-8

with open("output_data_analysis/fits_data_GUW2.dat", 'r') as f:
    content = f.readlines()

with open("fits_data_GUW2.dat", 'w') as f:
    f.write(''.join(content[:10]))
    f.write('...')

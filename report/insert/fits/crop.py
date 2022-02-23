#!/usr/bin/env python
# coding: utf-8

with open("output_data_analysis/fits_data_W.dat", 'r') as f:
    content = f.readlines()

with open("croped/fits_data_W.dat", 'w') as f:
    f.write(''.join(content[:15]))
    f.write('...')

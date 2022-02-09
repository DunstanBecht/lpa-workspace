#!/usr/bin/env python
# coding: utf-8

with open("input_data.txt", 'r') as f:
    content = f.readlines()

with open("croped/input_data.txt", 'w') as f:
    f.write(''.join(content[:15]))
    f.write('...')

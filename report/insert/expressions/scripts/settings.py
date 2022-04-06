#!/usr/bin/env python
# coding: utf-8

import numpy as np

a, b = 0, 3200

geoord = (
    #'circle',
    'square',
)
geoedgord = {
    'circle': ('NEC', 'WOA'),
    'square': ('NEC', 'WOA', 'GBB'),
}
disord = (
    'RDD',
    'RRDD-E',
    'RRDD-R',
)
metord = (
    'simulation',
    'expression',
)
funord = {
    #"M": (0, {"++": 0, "+-": 1}),
    #"K": (1, {"++": 0, "+-": 1}),
    "g": (2, {"++": 0, "+-": 1}),
    "G": (3, {"A": 0, "S": 1}),
}

geosiz = {
    'circle': 1000,
    'square': 3200,
}
metmrk = {
    'simulation': '-',
    'expression': '.',
}
metrad = {
    'simulation': np.linspace(a, b, 200),
    'expression': np.linspace(a, b, 50),
}
dismodprm = {
    'RDD': {'d': 5e-5},
    'RRDD-E': {'d': 5e-5, 's': 200, 'v': 'E'},
    'RRDD-R': {'d': 5e-5, 's': 200, 'v': 'R'},
}
dismodfun = {
    'RDD': 'RDD',
    'RRDD-E': 'RRDD',
    'RRDD-R': 'RRDD',
}

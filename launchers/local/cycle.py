#!/usr/bin/env python
# coding: utf-8

"""
Manage data.
"""

import os
from datetime import datetime

stem = 'cycle_'
root = "../../"

idffmt = '%Y-%m-%d_%H%M%S'

def directory(idf):
    """Return the directory corresponding to the cycle."""
    return f"{root}{stem}{idf}"

def init():
    """Create a new cycle and return its identifier."""
    idf = datetime.now().strftime(idffmt)
    os.mkdir(directory(idf))
    return idf

def select():
    """Let the user choose a cycle and return its identifier."""
    idflst = [e.replace(stem, '') for e in os.listdir(root) if stem in e]
    print("Available cycles:")
    for idf in idflst:
        print(f"> {idf}")
    return input("Choosen cycle: ")

def groups(idf, stp):
   """Return the groups for step 'stp' in cycle 'idf'."""
   lst =  os.listdir(directory(idf))
   return [g.replace(stp+'_', '') for g in lst if stp+'_' in g]

def header(idf):
    """Return a cycle header."""
    hdr = (f"Cycle of generation, simulation and analysis started on "
           f"{datetime.strptime(idf, idffmt).strftime('%B %d, %Y at %H:%M')}.\n"
           f"Identifier: {idf}\n"
           f"The distribution models below are studied.")
    return hdr

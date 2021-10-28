#!/usr/bin/env python
# coding: utf-8

"""
Distribution parameter values.
"""

import numpy as np
from lpa.input import models, notation

densities_m = [ # studied dislocation densities [m^-2]
    5e13,
    5e14,
    #5e15,
]

densities = [d*1e-18 for d in densities_m] # [nm^-2]

densities_csl = [notation.quantity(d, "m-2", 'csl') for d in densities_m]
densities_stm = [notation.quantity(d, "m-2", 'stm') for d in densities_m]

def arguments(
    d: float,
    s: int = 3200,
    b: str = None,
) -> list:
    """
    Return a list of tuples containing the instantiation arguments.

    Input:
        d (float): dislocation density [nm^-2]
        s (int): side of the region of interest [nm] (default: 3200)
        b (NoneType|str): boundary conditions (default: None)

    Output:
        t (tuple): tuples containing the instantiation arguments
    """
    intdis = 1/np.sqrt(d) # mean inter dislocation distance [nm]
    # parameters for RRDD-*
    subsid = (200, 400) # subareas side [nm]
    # parameters for RCDD-*
    p = 0.2 # ratio of the area occupied by the cell walls
    q = (1+np.sqrt(1-p))/p # multiplier of wall thickness for cell side
    k = (0.5, 1, 2) # multiplier of the inter dislocation distance for dipoles
    celsid = s/4 # cell sides [nm]
    walthc = celsid/q # thickness of the cell walls [nm]
    diplen = [m*intdis for m in k] # dipole lengths [nm]
    # instantiation arguments
    prmtup = []
    # RDD
    prmtup.append(('square', s, models.RDD, {'d': d}, 'edge', b))
    # RRDD
    for modvar in ('E', 'R'):
        for sid in subsid:
            r = {'d': d, 'v': modvar, 's': sid}
            prmtup.append(('square', s, models.RRDD, r, 'edge', b))
    # RCDD
    for modvar in ('E', 'R'):
        r = {'d': d, 'v': modvar, 's': celsid, 't': walthc}
        prmtup.append(('square', s, models.RCDD, r, 'edge', b))
    for i in range(len(k)):
        r = {'d': d, 'v': 'D', 's': celsid, 't': walthc, 'l': diplen[i]}
        prmtup.append(('square', s, models.RCDD, r, 'edge', b))
    return prmtup

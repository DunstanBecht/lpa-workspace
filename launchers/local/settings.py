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
    5e15,
]

densities = [d*1e-18 for d in densities_m] # [nm^-2]

densities_csl = [notation.quantity(d, "m-2", 'csl') for d in densities_m]
densities_stm = [notation.quantity(d, "m-2", 'stm') for d in densities_m]

def arguments(
    d: float,
) -> list:
    """
    Return a list of tuples containing the instantiation arguments.

    Input:
        d (float): dislocation density [nm^-2]

    Output:
        t (tuple): tuples containing the instantiation arguments
    """

    # general parameters
    roisid = 3200 # side of the ROI [nm]
    bdrcnd = None # boundary conditions
    intdis = 1/np.sqrt(d) # mean inter dislocation distance [nm]

    # RRDD parameters
    subsid = ( # subareas side [nm]
         200,
         400,
         800,
        1600,
        3200,
    )
    modvar1 = (
        'E',
        #'R',
    )

    # RCDD parameters
    p = 0.2 # ratio of the area occupied by the cell walls
    q = (1+np.sqrt(1-p))/p # multiplier of wall thickness for cell side
    k = ( # multiplier of the inter dislocation distance for dipoles
        0.5,
        1,
        2,
    )
    modvar2 = (
        #'E',
        #'R',
    )
    celsid = ( # subareas side [nm]
        # 200,
        # 400,
        # 800,
        #1600,
        #3200,
    )
    # instantiation arguments
    prmtup = []

    # RDD arguments
    #prmtup.append(('square', roisid, models.RDD, {'d': d}, 'edge', bdrcnd))

    # RRDD arguments
    for modvar in modvar1:
        for sid in subsid:
            r = {'d': d, 'v': modvar, 's': sid}
            prmtup.append(('square', roisid, models.RRDD, r, 'edge', bdrcnd))

    # RCDD arguments
    for sid in celsid:
        walthc = round(sid/q) # thickness of the cell walls [nm]
        diplen = [round(m*intdis) for m in k] # dipole lengths [nm]
        for modvar in modvar2:
            r = {'d': d, 'v': modvar, 's': sid, 't': walthc}
            prmtup.append(('square', roisid, models.RCDD, r, 'edge', bdrcnd))
        for i in range(len(k)):
            r = {'d': d, 'v': 'D', 's': sid, 't': walthc, 'l': diplen[i]}
            prmtup.append(('square', roisid, models.RCDD, r, 'edge', bdrcnd))

    return prmtup

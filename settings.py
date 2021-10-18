#!/usr/bin/env python
# coding: utf-8

"""
Default parameter values.
"""

import copy
import numpy as np
import math
import fractions

from lpa.input import models
from lpa.input import notation

densities_m = [ # studied dislocation densities [m^-2]
    5e13,
    5e14,
    5e15,
]

densities = [d*1e-18 for d in densities_m] # [nm^-2]

def arguments(
    d: float,
    s: int = 3200,
    b: str = None,
) -> list:
    """
    Return a list of tuples containing the instantiation arguments.

    Input:
        d: dislocation density [nm^-2]
        s: side of the region of interest [nm] (RDD, RRDD-*)
        b: boundary conditions

    Output:
        t: tuples containing the instantiation arguments
    """
    intdis = 1/np.sqrt(d) # inter dislocation distance [nm]
    # parameters for RRDD-*
    subsid = (200, 400) # subareas side [nm]
    # parameters for RCDD-*
    p = 0.2 # ratio of the area occupied by the cell walls
    q = (1+np.sqrt(1-p))/p # multiplier of wall thickness for cell side
    k = (0.5, 1, 2) # multiplier of the inter dislocation distance
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

if __name__ == "__main__":

    print("[SETTINGS]")

    for i in range(len(densities_m)):
        print(f"\nDensity of {notation.quantity(densities_m[i], 'nm^-2')}:")
        for args in arguments(densities[i]):
                print((f"{args[0]} {args[1]}nm {args[4]} {args[5]} "
                       f"{args[2].__name__}{notation.parameters(args[3])}"))

    input("\nPress 'enter' to exit...")

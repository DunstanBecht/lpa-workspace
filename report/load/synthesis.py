#!/usr/bin/env python
# coding: utf-8

"""
Load fits data.
"""

from load import *
from lpa.input import notation

# methods to find best values
def closer(lst, val):
    return list(lst==lst[np.argmin(np.abs(lst-val))])
def minimal(lst, *args):
    return list(lst==np.min(lst))
def nope(lst, *args):
    return [False]*len(lst)

# synthesis approaches
def mean_values(rho, data):
    val = [np.abs(data[i_d].mean()*1e18-rho)/rho, data[i_r].mean()]
    if len(data)>i_f:
        val.append(data[i_f].mean())
    return tuple(val)
def deviations(rho, data):
    val = [data[i_d].std()*1e18/rho, data[i_r].std()]
    if len(data)>i_f:
        val.append(data[i_f].std())
    return tuple(val)
tfmtex1 = r"$ \left. \left|VALUE-DST\right| \right/ DST $"
tfmtex2 = r"$ \left. VALUE \right/ DST $"
tfmtex3 = r"$ VALUE $"
sym1 = r"DST^{\mathrm{FIT}}"
sym2 = r"CUTRAD^{\mathrm{FIT}}"
sym0 = r"\delta"
fmtrep = lambda x: x.replace("EXPVAL", r"\gls{expval}").replace("DST", r"\gls{dst}").replace("CUTRAD", r"\gls{cutrad}").replace("STDDEV", r"\gls{stddev}")
fmtfig = lambda x: x.replace("EXPVAL", r"E").replace("DST", r"\rho").replace("CUTRAD", r"R_e").replace("STDDEV", r"\sigma")
appmtdord = (
    {
        'nam': "Mean effective cut-off radius and relative mean density deviation",
        'stm': 'avg',
        'fun': mean_values,
        'sym': (
            tfmtex1.replace("VALUE", fr"\hat{{EXPVAL}} \left( {sym1} \right)"),
            tfmtex3.replace("VALUE", fr"\hat{{EXPVAL}} \left( {sym2} \right)")+" (nm)",
            tfmtex3.replace("VALUE", fr"\hat{{EXPVAL}} \left( {sym0} \right)"),
        ),
        'fmt': ('1.3f', '1.0f'),
        'bst': (minimal, nope),
    },
    {
        'nam': "Effective cut-off radius sandard deviation and relative density standard deviation",
        'stm': 'std',
        'fun': deviations,
        'sym': (
            tfmtex2.replace("VALUE", fr"\hat{{STDDEV}} \left( {sym1} \right)"),
            tfmtex3.replace("VALUE", fr"\hat{{STDDEV}} \left( {sym2} \right)")+" (nm)",
            tfmtex3.replace("VALUE", fr"\hat{{STDDEV}} \left( {sym0} \right)"),
        ),
        'fmt': ('1.3f', '1.0f'),
        'bst': (minimal, nope),
    },
)

# number of harmonics displayed
n_j = 2

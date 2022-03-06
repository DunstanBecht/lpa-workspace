#!/usr/bin/env python
# coding: utf-8

"""
This script allows to compare the output for different values of PBC.
"""

from lpa.output import collect
import matplotlib.pyplot as plt

def plot(bunch, stm, ttl):
    plt.cla()
    plt.figure(figsize=(6.4, 3.8))
    xy = []
    for key in bunch:
        x, y = collect.load(['L', 'cos1'], bunch[key], impdir=impdir)
        plt.plot(x, y, label=key)
    plt.legend()
    plt.yscale('log')
    plt.xlabel("$ L $ (nm)")
    plt.ylabel("$ A(L) $")
    plt.title(ttl)
    plt.savefig(stm)

impdir = "../average_RRDD-E_test_PBC"

bunch1 = {
    'PBC0': 'RRDD-E_a3_1.50e00_nm_d_1.25e13_m-2_s_6.40e03_nm_PBC0_output.dat',
    'PBC1': 'RRDD-E_a3_1.50e00_nm_d_1.25e13_m-2_s_6.40e03_nm_PBC1_output.dat',
    'PBC2': 'RRDD-E_a3_1.50e00_nm_d_1.25e13_m-2_s_6.40e03_nm_PBC2_output.dat',
    'PBC3': 'RRDD-E_a3_1.50e00_nm_d_1.25e13_m-2_s_6.40e03_nm_PBC3_output.dat',
}

bunch2 = {
    'PBC0': 'RRDD-E_a3_1.50e00_nm_d_1.28e16_m-2_s_2.00e02_nm_PBC0_output.dat',
    'PBC1': 'RRDD-E_a3_1.50e00_nm_d_1.28e16_m-2_s_2.00e02_nm_PBC1_output.dat',
    'PBC2': 'RRDD-E_a3_1.50e00_nm_d_1.28e16_m-2_s_2.00e02_nm_PBC2_output.dat',
    'PBC3': 'RRDD-E_a3_1.50e00_nm_d_1.28e16_m-2_s_2.00e02_nm_PBC3_output.dat',
}

plot(
    bunch1,
    "RRDD-E_d_1.25e13_m-2.pdf",
    r"RRDD-E  $ \rho = 1.25 \times 10^{13} $ m$^{-2}$  ROI 6400 nm"
)

plot(
    bunch2,
    "RRDD-E_d_1.28e16_m-2.pdf",
    r"RRDD-E  $ \rho = 1.28 \times 10^{16} $ m$^{-2}$  ROI 6400 nm"
)

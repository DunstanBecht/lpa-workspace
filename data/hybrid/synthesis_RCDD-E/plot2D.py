#!/usr/bin/env python
# coding: utf-8

import csv
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np
from matplotlib import cm
import os

from lpa.input.notation import *

group = os.getcwd().split('synthesis_')[1].split('_')[0]

names = {
    2: "GUW",
    3: "KR",
    4: "W",
}

with open('avg_j1.csv', newline='') as f:
    reader = csv.reader(f, delimiter=';')
    data = list(reader)[1:]

def get_d_s_a3(stm):
    """Return d [m^-2], s [m] and a3 [m]."""
    d = stm.split('_d_')[1].split('_m-2_')[0].lstrip('0')
    s = stm.split('_s_')[1].split('_nm_')[0].lstrip('0')
    a3 = stm.split('_a3_')[1].split('_nm_')[0].lstrip('0')
    return eval(d), eval(s)*1e-9, eval(a3)*1e-9

d_latex = r" \rho "
M_latex = r" s \sqrt{\rho } "
B_latex = r" a_3 \sqrt{\rho } "

for model in names:
    d_list, M_list, e_list = [], [], []
    for i in range(len(data)):
        d, s, a3 = get_d_s_a3(data[i][0])
        M = s * np.sqrt(d)
        B = a3 * np.sqrt(d)

        try:
            e = eval(data[i][model])*100
            d_list.append(d)
            M_list.append(M)
            e_list.append(e)
        except Exception:
            print("/!\ missing data")

    d_order = np.sort(np.unique(d_list))
    T = np.array((d_list, M_list, e_list))
    order = np.argsort(T[1,:])
    T = T.T[order].T

    fig, ax_lin = plt.subplots(figsize=(7.5,5))
    fig.subplots_adjust(top=0.9, left=0.1, right=0.95, bottom=0.15)
    ax_lin.set_xlabel(fr"$ {M_latex} $")
    ax_lin.set_ylabel(r"error $ (\%)$")
    ax_lin.set_xscale('log')
    
    divider = make_axes_locatable(ax_lin)
    split_value = 5

    ax_log = divider.append_axes("top", size=2.0, pad=0, sharex=ax_lin)
    ax_log.xaxis.set_ticks_position('top')
    plt.setp(ax_log.get_xticklabels(), visible=False)
    
    ax_log.set_ylim((split_value, 115))
    ax_lin.set_ylim((0, split_value))

    for d in d_order:
        mask = T[0,:] == d
        _, x, y = T.T[mask].T
        label = equality(d_latex, number(d, c='ttl', w=7), c='ttl')+" m$^{-2}$"
        ax_log.plot(x, y, ".-", label=label)
        ax_lin.plot(x, y, ".-", label=label)

    prm = r"$ a_3 = \min\left(\max\left(0.1/\sqrt{\rho}, 1.5\right), 5.0\right) $ nm"
    plt.title(f"${names[model]}$ applied to {group} with {prm}")
    plt.legend()
    ax_log.grid(which='major', linestyle='-')
    ax_log.grid(which='minor', linestyle='--')
    ax_lin.grid(which='major', linestyle='-')
    ax_lin.grid(which='minor', linestyle='--')
    plt.savefig(f"plot2D_{names[model]}.pdf")
    #plt.show()

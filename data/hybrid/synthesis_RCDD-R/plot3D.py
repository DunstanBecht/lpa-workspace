#!/usr/bin/env python
# coding: utf-8

import csv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
import os

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
    X, Y, Z = [], [], []
    for i in range(len(data)):
        d, s, a3 = get_d_s_a3(data[i][0])
        M = s * np.sqrt(d)
        B = a3 * np.sqrt(d)

        x = np.log(M)
        y = np.log10(d)
        try:
            z = eval(data[i][model])*100
            X.append(x)
            Y.append(y)
            Z.append(z)
        except Exception as e:
            print("/!\ missing data")

    X = np.array(X)
    Y = np.array(Y)
    Z = np.array(Z)

    fig, ax = plt.subplots(figsize=(7.5,5), subplot_kw={"projection": "3d"})
    fig.subplots_adjust(top=0.9, left=0.0, right=1.0, bottom=0.1)
    ax.set_xlabel(fr"$ \ln \left( {M_latex} \right) $")
    ax.set_ylabel(fr"$ \log_{{10}} \left( {d_latex} \right) $")
    ax.set_zlabel(r"error $ (\%)$")
    ax.plot_trisurf(X, Y, Z, linewidth=0.2, cmap=cm.coolwarm)
    ax.view_init(20, 250)
    ax.set_zlim((0, 115))
    ax.dist = 8
    prm = r"$ a_3 = \min\left(\max\left(0.1/\sqrt{\rho}, 1.5\right), 5.0\right) $ nm"
    plt.title(f"${names[model]}$ applied to {group} with {prm}")
    plt.savefig(f"plot3D_{names[model]}.pdf")
    #plt.show()

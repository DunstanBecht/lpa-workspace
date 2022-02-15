#!/usr/bin/env python
# coding: utf-8

import numpy as np

# constants

deg_to_rad = np.pi/180 # [rad/deg]
wl = 0.154 # wavelength (Cu) [nm]
a = 0.4046 # cell parameter (Al FCC) [nm]
N = 9 # number of values in the table

# calculate Bragg angle

def bragg_angle(hkl, wl=wl, a=a, n=1):
    d_hkl = a/np.linalg.norm(hkl)
    return np.arcsin(n*wl/(2*d_hkl))

# calculate a3

def step(theta_2_rad, theta_0_rad):
    return wl/(4*(np.sin(theta_2_rad)-np.sin(theta_0_rad)))

# FCC form factor

def FCC(h, k, l):
    even = h%2==0 and k%2==0 and l%2==0
    odd = h%2==1 and k%2==1 and l%2==1
    return odd or even

# hkl list

hkl_list = []
for h in range(1, 4*N):
    for k in range(h+1):
        for l in range(k+1):
             if FCC(h, k, l):
                 hkl_list.append((h, k, l))
hkl_list = np.array(hkl_list)
norms = np.linalg.norm(hkl_list, axis=1)
hkl_list = hkl_list[np.argsort(norms)][:N+1]

# Bragg angles

theta_0_list = np.array([bragg_angle(hkl) for hkl in hkl_list])

# middle angles

middles = np.array([(theta_0_list[i]+theta_0_list[i+1])/2 for i in range(N)])

# maximum |t2-t0|
max_half_ranges = []
for i in range(N):
    bounds = [middles[i]]
    if i!=0:
        bounds.append(middles[i-1])
    max_half_range = min([np.absolute(b-theta_0_list[i]) for b in bounds])
    max_half_ranges.append(max_half_range)

# half ranges

max_half_ranges = np.array(max_half_ranges)
min_half_ranges = 0.5/180*np.pi

# theta_2

max_theta_2_list = theta_0_list[:N] + max_half_ranges
min_theta_2_list = theta_0_list[:N] + min_half_ranges

# a_3

min_a3_list = step(max_theta_2_list, theta_0_list[:N])
max_a3_list = step(min_theta_2_list, theta_0_list[:N])


with open('a3.tex', 'w') as f:

    print(f"Wavelength: {wl:1.7f} nm")
    print(f"Cell parameter: {a:1.7f} nm")
    print("")
    print(r"hkl |    t_0 | max t_2-t_0 | min a_3 | min t_2-t_0 | max a_3")
    f.write(r"\begin{tabularx}{\linewidth}{|X|X|X|X|X|X|}"+"\n")
    f.write(r"\hline"+"\n")
    f.write((r"hkl & \( \gls{brgang}_B \) & "
             r"\( \max \left( \Delta \theta / 2 \right) \) \(^{\circ}\) & \( \min \left( a_3 \right) \) nm & "
             r"\( \min \left( \Delta \theta / 2 \right) \) \(^{\circ}\) & \( \max \left( a_3 \right) \) nm \\"+"\n"))
    f.write(r"\hline"+"\n")
    for i in range(N):
        hkl = f"{hkl_list[i][0]}{hkl_list[i][1]}{hkl_list[i][2]}"
        t0 = theta_0_list[i]/deg_to_rad
        max_hr = max_half_ranges[i]/deg_to_rad
        min_hr = min_half_ranges/deg_to_rad
        max_a3 = max_a3_list[i]
        min_a3 = min_a3_list[i]
        print(fr"{hkl} | {t0:5.2f}° | {max_hr:10.2f}° | {min_a3:5.2f}nm | {min_hr:10.2f}° | {max_a3:5.2f}nm")
        f.write(fr"{hkl} & {t0:1.2f} & {max_hr:1.2f} & {min_a3:1.2f} & {min_hr:1.2f} & {max_a3:1.2f} \\"+"\n")
        f.write(r"\hline"+"\n")
    f.write(r"\end{tabularx}")

input('')

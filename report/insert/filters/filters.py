#!/usr/bin/env python
# coding: utf-8

from lpa.output import filters
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(6,3))

# f1
a = np.array([9, 8, 7, 6, 5, 4, 4, 5, 3, 4])
l = np.arange(len(a))
i1 = filters.f1(a)
plt.plot(l, a, "o-", label="all")
plt.plot(l[:i1], a[:i1], ".-", label="filtered")
plt.title("F1")
plt.legend()
plt.savefig('f1.pdf')
plt.clf()

# f2
y = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.2, 6.8, 8.6, 11.2])
x = np.arange(len(y))
i2 = filters.f2_xy(y, x)
plt.plot(x, y, "o-", label="all")
plt.plot(x[:i2], y[:i2], ".-", label="filtered")
plt.title("F2")
plt.legend()
plt.savefig('f2.pdf')
plt.clf()

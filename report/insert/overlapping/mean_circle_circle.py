import numpy as np
import matplotlib.pyplot as plt

from lpa.input import overlap

R = 10
r_ana = np.linspace(0.01, 2*R, 100)
r_sim = np.linspace(0.01, 2*R, 20)

plt.figure(figsize=(10,5))
plt.plot(
    r_ana,
    overlap.mean_circle_circle_analytic(r_ana, R),
    label=r"Closed-form expression",
)
plt.plot(
    r_sim,
    overlap.mean_circle_circle_simulation(r_sim, R),
    '.',
    label=r"Monte Carlo method",
)
plt.ylabel("Mean intersection area")
plt.xlabel("$r$")
plt.legend()
plt.grid()
plt.yticks(
    [
        0,
        np.pi*R**2/2,
        np.pi*R**2,
    ],
    [
        r"$0$",
        r"$\frac{1}{2}\pi R^2$",
        r"$\pi R^2$",
    ],
)
plt.xticks(
    [
        0,
        R,
        2*R,
    ],
    [
        r"$0$",
        r"$R$",
        r"$2R$",
    ],
)
plt.savefig("mean_circle_circle.pdf")

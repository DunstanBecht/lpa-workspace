import numpy as np
import matplotlib.pyplot as plt

from lpa.input import overlap

S = 10
r_ana = np.linspace(0, 2*S, 100)
r_sim = np.linspace(0, 2*S, 20)

plt.figure(figsize=(10,5))
plt.plot(
    r_ana,
    overlap.mean_circle_square_analytic(r_ana, S),
    label=r"Closed-form expression",
)
plt.plot(
    r_sim,
    overlap.mean_circle_square_simulation(r_sim, S),
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
        S**2/4,
        S**2/2,
        3*S**2/4,
        S**2,
    ],
    [
        r"$0$",
        r"$\frac{1}{4}S^2$",
        r"$\frac{1}{2}S^2$",
        r"$\frac{3}{4}S^2$", r"$S^2$",
    ],
)
plt.xticks(
    [
        0,
        S,
        S/2,
        2**(1/2)*S,
        2*S,
    ],
    [
        r"$0$",
        r"$S$",
        r"$\frac{1}{2}S$",
        r"$\sqrt{2}S$",
        r"$2S$",
    ],
)
plt.savefig("mean_circle_square.pdf")

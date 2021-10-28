import numpy as np
import matplotlib.pyplot as plt
from scipy import stats, special
from lpa.input import overlap

r0 = 1
R0 = 4*r0
RM = 1000
R = np.linspace(R0, RM, 20)
plt.plot(R, R, label=r"$R$")
u = 1

geo = {
    'circle': overlap.mean_circle_circle_analytic,
    'square': overlap.mean_circle_square_analytic,
}

hyp = (
    'HL',
    'H0',
    'H1',
    'H2',
    #'H3',
)

a = {
    'HL': lambda r: np.log(r/u),
    'H0': lambda r: 1/(2*np.pi)*np.ones(len(r)),
    'H1': lambda r: 1/(2*np.pi*r),
    'H2': lambda r: 1/(2*np.pi*r**2),
    'H3': lambda r: 1/(2*np.pi*r**3),
}

b = {
    'HL': lambda r: np.sqrt(
        np.e*u**2*np.exp(
            np.real(
                special.lambertw(
                    2/np.e/u**2*(2*F+r0**2*np.log(r0/np.sqrt(np.e)/u))
                )
            )
        )
    ),
    'H0': lambda F: np.sqrt(2*F+r0**2),
    'H1': lambda F: F+r0,
    'H2': lambda F: np.exp(F)*r0,
    'H3': lambda F: r0/(1-F*r0),
}

with open("regression.txt", "w") as f:

    for g in geo:
        for h in hyp:
            F = np.zeros(len(R))
            for i in range(len(R)):
                rM = R[i]
                r = np.linspace(r0, rM, round(rM/r0))
                Broi = geo[g](r, R[i])
                fun = a[h](r)
                F[i] = np.trapz(fun, Broi)
                Req = b[h](F)
            plt.plot(R, Req, label=r"$R^{"+h+r"}_{"+g+r"}$")
            linreg = stats.linregress(R, Req)
            f.write((g+" "+h+"\n" +
                "slope: "+format(linreg.slope, '1.15f')+"\n" +
                "intercept:"+format(linreg.intercept, '1.15f')+"\n" +
                "r value:"+format(linreg.rvalue, '1.15f')+"\n" +
                "p value:"+format(linreg.pvalue, '1.15e')+"\n" +
                "standard error:"+format(linreg.stderr, '1.15e')+"\n\n"))

plt.legend()
plt.grid()
plt.show()

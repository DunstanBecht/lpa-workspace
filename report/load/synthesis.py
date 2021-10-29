#!/usr/bin/env python
# coding: utf-8

"""
Generate LaTex files.
"""

from load import *
from lpa.input import notation

# fits data / [fit model] / [distribution model] / [densitiy]
datlstfit = [
                [
                    [
                        []
                    for i in range(len(readst))]
                for j in range(len(dismodord))]
              for e in range(len(fitmodord))
            ]

# fill datlstfit
for e in range(len(fitmodord)):
    for j in range(len(dismodord)):
        for i in range(len(readst)):
            for k in range(len(stmlstfit[j][i])):
                stmdis = stmlstfit[j][i][k]
                fitdat = f'fits_data_{fitmodord[e].upper()}.dat'
                datpth = os.path.join(impdirfit[i], stmdis, fitdat)
                with open(datpth, 'r') as f:
                    f.readline() # skip column names
                    datlstfit[e][j][i].append(np.loadtxt(f).T)
del e, j, i, k, stmdis, fitdat, datpth, f

# methods to find best values
def closer(lst, val):
    return list(lst==lst[np.argmin(np.abs(lst-val))])
def minimal(lst, *args):
    return list(lst==np.min(lst))
def nope(lst, *args):
    return [False]*len(lst)

# index in fits data
i_j = 0
i_L = 1
i_d = 3
i_r = 4
i_f = 5

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
tfmtex1 = r"\( \textstyle \left. \left|VALUE-\gls{dst}\right| \right/ \gls{dst} \)"
tfmtex2 = r"\( \textstyle \left. VALUE \right/ \gls{dst} \)"
tfmtex3 = r"\( \textstyle VALUE \)"
sym1 = r"\gls{dst}^{\mathrm{FIT}}"
sym2 = r"\gls{cutrad}^{\mathrm{FIT}}"
sym0 = r"\delta"
appmtdord = (
    {
        'nam': "Mean values",
        'fun': mean_values,
        'sym': (
            tfmtex1.replace("VALUE", fr"\gls{{expval}}\left({sym1}\right)"),
            tfmtex3.replace("VALUE", fr"\gls{{expval}}\left({sym2}\right)"),
            tfmtex3.replace("VALUE", fr"\gls{{expval}}\left({sym0}\right)"),
        ),
        'fmt': ('1.3f', '1.0f'),
        'bst': (minimal, nope),
    },
    {
        'nam': "Standard deviations",
        'fun': deviations,
        'sym': (
            tfmtex2.replace("VALUE", fr"\gls{{stddev}}\left({sym1}\right)"),
            tfmtex3.replace("VALUE", fr"\gls{{stddev}}\left({sym2}\right)"),
            tfmtex3.replace("VALUE", fr"\gls{{stddev}}\left({sym0}\right)"),
        ),
        'fmt': ('1.3f', '1.0f'),
        'bst': (minimal, nope),
    },
)

# number of harmonics displayed
n_j = 2

higlig = r"\cellcolor{Mines} \textcolor{white}{VALUE}"

# export synthesis.tex
with open('synthesis.tex', 'w') as f:
    for appmtd in appmtdord:
        f.write(r"\subsubsection{"+appmtd['nam']+r"}"+"\n")
        for h in range(1, 1+n_j):
            f.write(r"\begin{center}"+"\n")
            colfmt = r"|l|l|"
            colfmt += r">{\raggedleft\arraybackslash}X|" * len(fitmodord)*2
            f.write(r"\begin{tabularx}{\linewidth}{"+colfmt+r"} "+"\n")
            f.write(r"\hline"+"\n")
            f.write((r"\multirow{2}{*}{\centering{Distribution model}} "
                + r"& \multicolumn{1}{c|}{\centering{"+appmtd['sym'][2]+r"}} "
                + r"& \multicolumn{"+str(len(fitmodord))+r"}{c|}{ "
                + r""+appmtd['sym'][0]+r""
                + r"} "
                + r"& \multicolumn{"+str(len(fitmodord))+r"}{c|}{"
                + r""+ appmtd['sym'][1]+r""
                + r"} \\"+"\n"))
            f.write(r"\cline{2-"+str(2+2*len(fitmodord))+r"}"+"\n")
            f.write(r" &")
            f.write(r" \multicolumn{2}{c|}{\gls{"+fitmodord[0]+r"}}")
            for fitmod in fitmodord[1:]:
                f.write(r" & \multicolumn{1}{c|}{\gls{"+fitmod+r"}}")
            for fitmod in fitmodord:
                f.write(r" & \multicolumn{1}{c|}{\gls{"+fitmod+r"}}")
            f.write(r" \\"+"\n")
            f.write(r"\hline \hline "+"\n")
            for j in range(len(dismodord)):
                for i in range(len(readst)):
                    for k in range(len(stmlstfit[j][i])):
                        f.write((r"\hyperref["+lstnicnam[j][i][k]+r"]"
                            + r"{\texttt{\verb|"+lstnicnam[j][i][k]+r"|}}"))
                        col1, col2 = [], []
                        for e in range(len(fitmodord)):
                            datfit = datlstfit[e][j][i][k]
                            mashmc = datfit[i_j]==h
                            datfit = datfit.T[mashmc].T
                            val = appmtd['fun'](readst[i], datfit)
                            col1.append(val[0])
                            col2.append(val[1])
                            if len(val)==3:
                                col0 = val[2]
                        bstlst1 = appmtd['bst'][0](col1)
                        bstlst2 = appmtd['bst'][1](col2)
                        bstall = bstlst1 + bstlst2
                        vallst1 = [format(v, appmtd['fmt'][0]) if v<10 else r"\rightarrow \infty" for v in col1]
                        vallst2 = [format(v, appmtd['fmt'][1]) for v in col2]
                        vallst0 = [notation.number(col0, c='ttl', w=3).replace("$", "")]
                        valall = [r"\( "+v+r" \)" for v in vallst0+vallst1+vallst2]
                        for e in range(len(fitmodord)):
                            for c in range(2):
                                if bstall[2*e+c-1]:
                                    valall[2*e+c] = higlig.replace(
                                        'VALUE',
                                        valall[2*e+c],
                                    )
                        f.write(" & ")
                        f.write(" & ".join(valall))
                        f.write(r" \\"+"\n")
                f.write(r"\hline"+"\n")
            f.write(r"\end{tabularx}"+"\n\n")
            f.write(r"\end{center}"+"\n")
            f.write(r"\captionof{table}{"
                + appmtd['nam']+" for harmonic "+str(h)
                + r" in a square \gls{roi} of side 3200 nm}"+"\n\n")
            f.write(r"\medskip"+"\n\n")
del f, appmtd

input("OK")

#!/usr/bin/env python
# coding: utf-8

"""
Generate LaTex and text files.
"""

from synthesis import *

higlig = r"\cellcolor{Mines} \textcolor{white}{VALUE}"

# export synthesis.tex
for appmtd in appmtdord:
    with open(f"tex/{appmtd['stm']}-tables.tex", 'w') as f:
        for h in range(1, 1+n_j):
            f.write(r"\begin{center}"+"\n")
            colfmt = r"|l|l|"
            colfmt += r">{\raggedleft\arraybackslash}X|" * len(fitmodord)*2
            f.write(r"\begin{tabularx}{\linewidth}{"+colfmt+r"} "+"\n")
            f.write(r"\hline"+"\n")
            f.write((r"\multirow{2}{*}{\centering{Distribution}} "
                + r"& \multicolumn{1}{c|}{\centering{"+fmtrep(appmtd['sym'][2])+r"}} "
                + r"& \multicolumn{"+str(len(fitmodord))+r"}{c|}{ "
                + r""+fmtrep(appmtd['sym'][0])+r""
                + r"} "
                + r"& \multicolumn{"+str(len(fitmodord))+r"}{c|}{"
                + r""+fmtrep(appmtd['sym'][1])+r""
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
                        vallst1 = [format(v, appmtd['fmtrep'][0]) if v<10 else r"\rightarrow \infty" for v in col1]
                        vallst2 = [format(v, appmtd['fmtrep'][1]) for v in col2]
                        vallst0 = [format(col0, '1.3f')]
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
            f.write(r"\end{tabularx}"+"\n")
            f.write(r"\end{center}"+"\n\n")
            cap = (fr"\captionof{{table}}{{{appmtd['nam']} for harmonic \( j = {h} \) "
                   fr"of \gls{{guw1}}, \gls{{guw2}}, \gls{{w1}} and \gls{{w2}} models "
                   fr"fitted on the X-ray simulation output performed on distributions generated "
                   fr"in a square \gls{{roi}} of 3200 nm side length with \gls{{pbc}}1.}}")
            f.write(cap+"\n\n")
            f.write(r"\newpage"+"\n\n")
del higlig, f, appmtd

# export synthesis.csv
sep = '; '
for appmtd in appmtdord:
    for h in range(1, 1+n_j):
        syndir = f"{datpth}/synthesis"
        if not os.path.isdir(syndir):
            os.mkdir(syndir)
        hdr1 = ["", "fluctuation", *['density' for m in fitmodord], *['Re (nm)' for m in fitmodord]]
        hdr2 = ["distribution model", fitmodord[0].upper(), *2*[m.upper() for m in fitmodord]]
        dat = []
        for j in range(len(dismodord)):
            for i in range(len(readst)):
                for k in range(len(stmlstfit[j][i])):
                    line = [stmlstfit[j][i][k]]+[None]*(1+2*len(fitmodord))
                    for e in range(len(fitmodord)):
                        datfit = datlstfit[e][j][i][k]
                        mashmc = datfit[i_j]==h
                        datfit = datfit.T[mashmc].T
                        val = appmtd['fun'](readst[i], datfit)
                        line[2+e] = format(val[0], appmtd['fmtcsv'][0])
                        line[2+e+len(fitmodord)] = format(val[1], appmtd['fmtcsv'][0])
                        if len(val)==3:
                            line[1] = format(val[2], '1.9f')
                    dat.append(line)
        tab = [hdr1, hdr2] + dat
        for c in range(len(tab[0])):
            strlen = max([len(tab[l][c]) for l in range(len(tab))])
            for l in range(len(tab)):
                fmt = f"<{strlen}" if c==0 else f">{strlen}"
                tab[l][c] = format(tab[l][c], fmt)
        with open(os.path.join(syndir, f"{appmtd['stm']}_j{h}.csv"), 'w') as f:
            for line in tab:
                f.write(sep.join(line)+"\n")

del sep, f, appmtd

input("OK")

<div align="center">
  <img width="250" src="https://dunstan.becht.network/views/signatures/mines.svg" alt="Mines Saint-Etienne">
</div>

# Line Profile Analysis - Workspace

This project is related to the analysis of crystals containing dislocations by X-ray diffraction. It was developed and used for a study conducted during a research internship at the laboratory of material and structural sciences of the *École Nationale Supérieure des Mines de Saint-Étienne*. This repository contains the parameters and the scripts for the generation of the data used in the study. You can then easily replicate the results obtained or use it as inspiration to take the code in hand and conduct your own calculations.

The installation of the three following python packages is necessary for the scripts to work.
* [`lpa-input`](https://github.com/DunstanBecht/lpa-input) (line profile analysis input generator)
* [`lpa-xrd`](https://github.com/DunstanBecht/lpa-xrd) (line profile analysis x-ray diffraction simulation program)
* [`lpa-output`](https://github.com/DunstanBecht/lpa-output) (line profile analysis output analyzer)

These packages are released and can be installed with the following command.
```bash
pip install -U lpa-input lpa-xrd lpa-output
```

# Results reproducibility

The objective of this study was to calculate the error of the Wilkens model applied to dislocation distributions that do not meet the conditions of the RRDD model. The analyses were carried out for different dislocation densities, models and generation parameters of the distributions. This repository makes available the scripts and parameters used to obtain the published data in order to facilitate the reproducibility of the results.

Below is the description of the studied sample of distributions.
```
Density of 5e13nm-2:
square 3200nm edge PBCR1 RDD (d=5e-5nm-2)
square 3200nm edge PBCR1 RRDD-E (d=5e-5nm-2 s= 200nm)
square 3200nm edge PBCR1 RRDD-E (d=5e-5nm-2 s= 400nm)
square 3200nm edge PBCR1 RRDD-R (d=5e-5nm-2 s= 200nm)
square 3200nm edge PBCR1 RRDD-R (d=5e-5nm-2 s= 400nm)
square 2679nm edge PBCR1 RCDD-E (d=5e-5nm-2 s=1340nm t=141nm)
square 2679nm edge PBCR1 RCDD-R (d=5e-5nm-2 s=1340nm t=141nm)
square 3349nm edge PBCR1 RCDD-D (d=5e-5nm-2 s= 167nm t= 18nm l= 35nm)
square 3349nm edge PBCR1 RCDD-D (d=5e-5nm-2 s= 335nm t= 35nm l= 71nm)
square 3349nm edge PBCR1 RCDD-D (d=5e-5nm-2 s= 670nm t= 71nm l=141nm)
square 3349nm edge PBCR1 RCDD-D (d=5e-5nm-2 s=1674nm t=177nm l=354nm)
square 3349nm edge PBCR1 RCDD-D (d=5e-5nm-2 s=3349nm t=354nm l=707nm)

Density of 5e14nm-2:
square 3200nm edge PBCR1 RDD (d=5e-4nm-2)
square 3200nm edge PBCR1 RRDD-E (d=5e-4nm-2 s= 200nm)
square 3200nm edge PBCR1 RRDD-E (d=5e-4nm-2 s= 400nm)
square 3200nm edge PBCR1 RRDD-R (d=5e-4nm-2 s= 200nm)
square 3200nm edge PBCR1 RRDD-R (d=5e-4nm-2 s= 400nm)
square 3389nm edge PBCR1 RCDD-E (d=5e-4nm-2 s= 424nm t= 45nm)
square 3389nm edge PBCR1 RCDD-R (d=5e-4nm-2 s= 424nm t= 45nm)
square 3177nm edge PBCR1 RCDD-D (d=5e-4nm-2 s=  53nm t=  6nm l= 11nm)
square 3177nm edge PBCR1 RCDD-D (d=5e-4nm-2 s= 106nm t= 11nm l= 22nm)
square 3177nm edge PBCR1 RCDD-D (d=5e-4nm-2 s= 212nm t= 22nm l= 45nm)
square 3177nm edge PBCR1 RCDD-D (d=5e-4nm-2 s= 530nm t= 56nm l=112nm)
square 3177nm edge PBCR1 RCDD-D (d=5e-4nm-2 s=1059nm t=112nm l=224nm)

Density of 5e15nm-2:
square 3200nm edge PBCR1 RDD (d=5e-3nm-2)
square 3200nm edge PBCR1 RRDD-E (d=5e-3nm-2 s= 200nm)
square 3200nm edge PBCR1 RRDD-E (d=5e-3nm-2 s= 400nm)
square 3200nm edge PBCR1 RRDD-R (d=5e-3nm-2 s= 200nm)
square 3200nm edge PBCR1 RRDD-R (d=5e-3nm-2 s= 400nm)
square 3215nm edge PBCR1 RCDD-E (d=5e-3nm-2 s= 134nm t= 14nm)
square 3215nm edge PBCR1 RCDD-R (d=5e-3nm-2 s= 134nm t= 14nm)
square 3349nm edge PBCR1 RCDD-D (d=5e-3nm-2 s=  17nm t=  2nm l=  4nm)
square 3349nm edge PBCR1 RCDD-D (d=5e-3nm-2 s=  33nm t=  4nm l=  7nm)
square 3349nm edge PBCR1 RCDD-D (d=5e-3nm-2 s=  67nm t=  7nm l= 14nm)
square 3349nm edge PBCR1 RCDD-D (d=5e-3nm-2 s= 167nm t= 18nm l= 35nm)
square 3349nm edge PBCR1 RCDD-D (d=5e-3nm-2 s= 335nm t= 35nm l= 71nm)
```

# User guide

Here are the scripts to execute in order:
* `input_data_and_notations.py` to generate input data
* `xrd_run.py` to calculate line profile
* `output_fits.py` to fit the models on the output

These scripts can be executed at any time:
* `input_analyses_remote.py` to facilitate remote input analysis
* `input_maps.py` to generate dislocation maps

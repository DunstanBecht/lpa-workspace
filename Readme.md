<div align="center">
  <img width="250" src="https://dunstan.becht.network/views/signatures/mines.svg" alt="Mines Saint-Etienne">
</div>

# Line Profile Analysis - Workspace

This repository is related to the analysis of crystals containing dislocations by X-ray diffraction. It is part of a project conducted during a research internship at the laboratory of material and structural sciences of the *École Nationale Supérieure des Mines de Saint-Étienne*. Three python packages have been developed to conduct line profile analyses based on simulation results:
* [`lpa.input`](https://github.com/DunstanBecht/lpa-input) (line profile analysis input generator)
* [`lpa.xrd`](https://github.com/DunstanBecht/lpa-xrd) (line profile analysis x-ray diffraction simulation program)
* [`lpa.output`](https://github.com/DunstanBecht/lpa-output) (line profile analysis output analyzer)

# Results reproducibility

The objective of this study was to calculate the error of the Wilkens model applied to dislocation distributions that do not meet the conditions of the RRDD model. The analyses were carried out for different dislocation densities, models and generation parameters of the distributions. This repository makes available the scripts and parameters used to obtain the published data in order to facilitate the reproducibility of the results.

Below are the parameters for the generation of the studied sample distributions. 
```
Density of 5e13nm-2:
square 2000nm edge PBCR2 RDD (d=5e-5nm-2)
square 2000nm edge PBCR2 RRDD-E (d=5e-5nm-2 s= 200nm)
square 2000nm edge PBCR2 RRDD-E (d=5e-5nm-2 s= 400nm)
square 2000nm edge PBCR2 RRDD-R (d=5e-5nm-2 s= 200nm)
square 2000nm edge PBCR2 RRDD-R (d=5e-5nm-2 s= 400nm)
square 2679nm edge PBCR2 RCDD-E (d=5e-5nm-2 s=1340nm t=141nm)
square 2679nm edge PBCR2 RCDD-R (d=5e-5nm-2 s=1340nm t=141nm)
square 3349nm edge PBCR2 RCDD-D (d=5e-5nm-2 s= 167nm t= 18nm l= 35nm)
square 3349nm edge PBCR2 RCDD-D (d=5e-5nm-2 s= 335nm t= 35nm l= 71nm)
square 3349nm edge PBCR2 RCDD-D (d=5e-5nm-2 s= 670nm t= 71nm l=141nm)
square 3349nm edge PBCR2 RCDD-D (d=5e-5nm-2 s=1674nm t=177nm l=354nm)
square 3349nm edge PBCR2 RCDD-D (d=5e-5nm-2 s=3349nm t=354nm l=707nm)

Density of 5e14nm-2:
square 2000nm edge PBCR2 RDD (d=5e-4nm-2)
square 2000nm edge PBCR2 RRDD-E (d=5e-4nm-2 s= 200nm)
square 2000nm edge PBCR2 RRDD-E (d=5e-4nm-2 s= 400nm)
square 2000nm edge PBCR2 RRDD-R (d=5e-4nm-2 s= 200nm)
square 2000nm edge PBCR2 RRDD-R (d=5e-4nm-2 s= 400nm)
square 2118nm edge PBCR2 RCDD-E (d=5e-4nm-2 s= 424nm t= 45nm)
square 2118nm edge PBCR2 RCDD-R (d=5e-4nm-2 s= 424nm t= 45nm)
square 2012nm edge PBCR2 RCDD-D (d=5e-4nm-2 s=  53nm t=  6nm l= 11nm)
square 2012nm edge PBCR2 RCDD-D (d=5e-4nm-2 s= 106nm t= 11nm l= 22nm)
square 2118nm edge PBCR2 RCDD-D (d=5e-4nm-2 s= 212nm t= 22nm l= 45nm)
square 2118nm edge PBCR2 RCDD-D (d=5e-4nm-2 s= 530nm t= 56nm l=112nm)
square 2118nm edge PBCR2 RCDD-D (d=5e-4nm-2 s=1059nm t=112nm l=224nm)

Density of 5e15nm-2:
square 2000nm edge PBCR2 RDD (d=5e-3nm-2)
square 2000nm edge PBCR2 RRDD-E (d=5e-3nm-2 s= 200nm)
square 2000nm edge PBCR2 RRDD-E (d=5e-3nm-2 s= 400nm)
square 2000nm edge PBCR2 RRDD-R (d=5e-3nm-2 s= 200nm)
square 2000nm edge PBCR2 RRDD-R (d=5e-3nm-2 s= 400nm)
square 2009nm edge PBCR2 RCDD-E (d=5e-3nm-2 s= 134nm t= 14nm)
square 2009nm edge PBCR2 RCDD-R (d=5e-3nm-2 s= 134nm t= 14nm)
square 2009nm edge PBCR2 RCDD-D (d=5e-3nm-2 s=  17nm t=  2nm l=  4nm)
square 2009nm edge PBCR2 RCDD-D (d=5e-3nm-2 s=  33nm t=  4nm l=  7nm)
square 2009nm edge PBCR2 RCDD-D (d=5e-3nm-2 s=  67nm t=  7nm l= 14nm)
square 2009nm edge PBCR2 RCDD-D (d=5e-3nm-2 s= 167nm t= 18nm l= 35nm)
square 2009nm edge PBCR2 RCDD-D (d=5e-3nm-2 s= 335nm t= 35nm l= 71nm)
```

# User guide

Here are the scripts to execute in order:
* run input_data_and_notations.py
* run xrd_run.py on centaure (directly, not ssh-loged in the GPU)
* run output_average.py
* run output_fits.py

These scripts can be executed at any time:
* input_analyses_remote.py
* input_maps.py

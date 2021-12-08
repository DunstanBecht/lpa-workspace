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

Below is an overview of the parameters used for the generation of the studied models of distributions.
```
5e13m-2:
5.000e-05m-2 square 3200nm RDD (d=5e-5nm-2) S=0
5.000e-05m-2 square 3200nm RRDD-E (d=5e-5nm-2 s= 200nm) S=0
5.000e-05m-2 square 3200nm RRDD-E (d=5e-5nm-2 s= 400nm) S=0
5.000e-05m-2 square 3200nm RRDD-R (d=5e-5nm-2 s= 200nm) S=0
5.000e-05m-2 square 3200nm RRDD-R (d=5e-5nm-2 s= 400nm) S=0
5.000e-05m-2 square 3200nm RCDD-E (d=5e-5nm-2 s= 800nm t= 84nm) S=0
5.000e-05m-2 square 3200nm RCDD-R (d=5e-5nm-2 s= 800nm t= 84nm) S=0
5.000e-05m-2 square 3200nm RCDD-D (d=5e-5nm-2 s= 800nm t= 84nm l= 71nm) S=0
5.000e-05m-2 square 3200nm RCDD-D (d=5e-5nm-2 s= 800nm t= 84nm l=141nm) S=0
5.000e-05m-2 square 3200nm RCDD-D (d=5e-5nm-2 s= 800nm t= 84nm l=283nm) S=0

5e14m-2:
5.000e-04m-2 square 3200nm RDD (d=5e-4nm-2) S=0
5.000e-04m-2 square 3200nm RRDD-E (d=5e-4nm-2 s= 200nm) S=0
5.000e-04m-2 square 3200nm RRDD-E (d=5e-4nm-2 s= 400nm) S=0
5.000e-04m-2 square 3200nm RRDD-R (d=5e-4nm-2 s= 200nm) S=0
5.000e-04m-2 square 3200nm RRDD-R (d=5e-4nm-2 s= 400nm) S=0
5.000e-04m-2 square 3200nm RCDD-E (d=5e-4nm-2 s= 800nm t= 84nm) S=0
5.000e-04m-2 square 3200nm RCDD-R (d=5e-4nm-2 s= 800nm t= 84nm) S=0
5.000e-04m-2 square 3200nm RCDD-D (d=5e-4nm-2 s= 800nm t= 84nm l= 22nm) S=0
5.000e-04m-2 square 3200nm RCDD-D (d=5e-4nm-2 s= 800nm t= 84nm l= 45nm) S=0
5.000e-04m-2 square 3200nm RCDD-D (d=5e-4nm-2 s= 800nm t= 84nm l= 89nm) S=0

5e15m-2:
5.000e-03m-2 square 3200nm RDD (d=5e-3nm-2) S=0
5.000e-03m-2 square 3200nm RRDD-E (d=5e-3nm-2 s= 200nm) S=0
5.000e-03m-2 square 3200nm RRDD-E (d=5e-3nm-2 s= 400nm) S=0
5.000e-03m-2 square 3200nm RRDD-R (d=5e-3nm-2 s= 200nm) S=0
5.000e-03m-2 square 3200nm RRDD-R (d=5e-3nm-2 s= 400nm) S=0
5.000e-03m-2 square 3200nm RCDD-E (d=5e-3nm-2 s= 800nm t= 84nm) S=0
5.000e-03m-2 square 3200nm RCDD-R (d=5e-3nm-2 s= 800nm t= 84nm) S=0
5.000e-03m-2 square 3200nm RCDD-D (d=5e-3nm-2 s= 800nm t= 84nm l=  7nm) S=0
5.000e-03m-2 square 3200nm RCDD-D (d=5e-3nm-2 s= 800nm t= 84nm l= 14nm) S=0
5.000e-03m-2 square 3200nm RCDD-D (d=5e-3nm-2 s= 800nm t= 84nm l= 28nm) S=0
```

# User guide

## Project tree

The structure of the project is described below.
```
Workspace
├───data                (data for the study)
│   ├───maps_5eXXm-2        (distribution model maps for density 5eXXm-2)
│   ├───stats_5eXXm-2       (distribution model spatial analyses for density 5eXXm-2)
|   ├───notations_5eXXm-2   (LaTeX code for figure titles for density 5eXXm-2)
│   ├───inputs_5eXXm-2      (simulation input data for density 5eXXm-2)
│   ├───outputs_5eXXm-2     (simulation output data for density 5eXXm-2)
│   └───fits_5eXXm-2        (results of model fitting on output data for density 5eXXm-2)
├───launchers           (scripts for data generation)
│   ├───local               (scripts to run for local data generation)
│   │   ├───settings.py         (parameters for the generation of the distributions)
│   │   ├───maps.py             (distribution model maps generator)
│   │   ├───files.py            (notation and input data generator)
│   │   ├───stats.py            (script for input statistical analysis in parallel)
│   │   ├───stats.job           (script for submitting stats.py to SLURM)
│   │   ├───xrd.py              (automation of X-ray diffraction simulations)
│   │   └───fits.py             (script for model fitting on output data)
│   └───remote              (script for remote control of the supercomputer)
│       ├───link.py             (tools for communication and file exchange)
│       ├───stats.py            (remote controller for statistical analysis)
│       └───xrd.py              (remote controller for simulation)
├───report              (scripts and latex code for the presentation of results)
│   ├───include             (parts of the report)
│   ├───input               (header, macros and global data)
│   ├───insert              (illustrations and examples of use of the packages)
│   ├───load                (synthesis of the generated data)
│   └───report.tex          (latex code to be compiled)
└───commands.sh         (memo for regularly used commands)
```

## Cycles

In order to have the final data, it is necessary to generate the input, launch the calculations, process and synthesize the results. This process is called a cycle. An identifier can be assigned to each cycle in the form `YYYY-MM-HH-mmss` for traceability purposes.

Everything that is generated during a cycle is collected in a directory with the following structure. In a cycle one can classify the data by groups to synthesize the distributions in a partitioned way. These groups can be set up in the file `launchers/local/settings.py`.
```
data_YYYY-MM-HH-mmss
├───cycle-information.txt
├───benchmark.txt
├───inputs_<group-1-name>
├───inputs_<group-2-name>
├───notations_<group-1-name>
├───notations_<group-2-name>
├───maps_<group-1-name>
├───maps_<group-2-name>
├───stats_<group-1-name>
├───stats_<group-2-name>
├───stats_<group-1-name>
├───stats_<group-2-name>
├───outputs_<group-1-name>
├───outputs_<group-2-name>
├───fits_<group-1-name>
├───fits_<group-2-name>
├───synthesis_<group-1-name>
└───synthesis_<group-2-name>
```

For a complete cycle the following programs and tasks must be executed in order:
* Check the input parameters in `launchers/local/settings.py`
* Generate the input data and notations with `launchers/local/files.py`
* Generate the input maps with `launchers/local/maps.py`
* Launch the XRD simulations with `launchers/remote/xrd.py` (don't forger to transfer the input files to the GPU host)
* Perform a spatial analysis with `launchers/remote/stats.py`
* Retrieve simulation output data
* Fits the models on the output data with `launchers/local/fits.py`
* Synthetize the fits data with ...

The script `launchers/remote/xrd.py` and `launchers/remote/stats.py` are only aids to the automation of tasks. It allows you to transfer files to the host or cluster. If you want to run the programs locally you can use the `launchers/local/xrd.py` and `launchers/local/stats.py` scripts directly.

<div align="center"><br>
  <img width="250" src="https://dunstan.becht.network/permanent/mines.svg" alt="Mines Saint-Etienne">
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

# User guide

## Project tree

The structure of the project is described below.
```
Workspace
├───cycle_<YYYY-MM-DD-HHMMSS>  (generated data, see the section Cycles)
├───launchers                  (scripts for data generation)
│   ├───local                    (scripts to run for local data generation)
│   │   ├───average.py             (script to average simulation output data files)
│   │   ├───cycle                  (useful functions for data management)
│   │   ├───files.py               (script to generate input data and TEX denominations)
│   │   ├───filters.py             (script to evaluate the filter ranges)
│   │   ├───fits.py                (script to fit the models on output data)
│   │   ├───maps.py                (script to generate distribution model maps)
│   │   ├───settings.py            (parameters for the generation of the distributions)
│   │   ├───stats.job              (script to submit stats.py to SLURM)
│   │   ├───stats.py               (script to statistically analyze the distributions)
│   │   ├───synthesis.py           (script to make a synthesis of the results of the fits)
│   │   └───xrd.py                 (script to run X-ray diffraction simulations)
│   └───remote                   (scripts for remote control of the supercomputer)
│       ├───link.py                (tools for communication and file exchange)
│       ├───stats.py               (remote controller for statistical analysis)
│       └───xrd.py                 (remote controller for X-ray diffraction simulation)
├───report                     (scripts and latex code for the presentation of results)
│   ├───include                  (parts of the report)
│   ├───input                    (header, macros and global settings)
│   ├───insert                   (illustrations and examples of use of the packages)
│   ├───load                     (scripts to load the data into the report)
│   └───report.tex               (LaTeX main file to be compiled)
└───commands.sh                (memo for regularly used bash commands)
```

## Cycles

In order to have the final data, it is necessary to generate the input, launch the calculations, process and synthesize the results. This process is called a cycle. An identifier is assigned to each cycle in the form `YYYY-MM-DD-HHMMSS` for traceability purposes.

Everything that is generated during a cycle is collected in a directory with the following structure. In a cycle one can classify the data by groups to gather distributions of the same category. These groups can be set up in the file `launchers/local/settings.py`. The following example has two groups: `g1` and `g2`.
```
cycle_<YYYY-MM-DD-HHMMSS>
├───cycle-information.txt  (description of generated distributions)
├───benchmark.txt          (simulation run times)
├───inputs_<g1>            (simulation input data)
├───inputs_<g2>
├───notations_<g1>         (LaTeX code for figure titles)
├───notations_<g2>
├───maps_<g1>              (distribution model maps)
├───maps_<g2>
├───stats_<g1>             (distribution model spatial analyses)
├───stats_<g2>
├───outputs_<g1>           (raw simulation output data)
├───outputs_<g2>
├───average_<g1>           (averaged simulation output data)
├───average_<g2>
├───fits_<g1>              (results of model fitting on output data)
├───fits_<g2>
├───synthesis_<g1>         (synthesis of fits)
└───synthesis_<g2>
```

For a complete cycle the following programs and tasks must be executed in order:
* Check the input parameters in `launchers/local/settings.py`
* Generate the input data and notations with `launchers/local/files.py`
* Generate the input maps with `launchers/local/maps.py`
* Launch the XRD simulations with `launchers/remote/xrd.py` (don't forger to transfer the input files to the GPU host)
* Average the output files with `launchers/local/average.py` (don't forger to retrieve the output files from the GPU host)
* Perform a spatial analysis with `launchers/remote/stats.py`
* Retrieve simulation output data
* Fits the models on the output data with `launchers/local/fits.py`
* Synthetize the fits data with `launchers/local/synthesis.py`

The script `launchers/remote/xrd.py` and `launchers/remote/stats.py` are only aids to the automation of tasks. It allows you to transfer files to the host or cluster. If you want to run the programs locally you can use the `launchers/local/xrd.py` and `launchers/local/stats.py` scripts directly.

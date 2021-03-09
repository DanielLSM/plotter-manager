# plotter-manager
A plotting library based on matplotlib for a course on versioning, testing and refactoring

## Dependencies

This tutorial assumes an Ubuntu distribution (it was developed and tested on Ubuntu 20.04.1 LTS). 
In this readme file I will explain how to install all required dependencies for assigment, which are:
1. Anaconda :snake:

## Step-by-step installation

1. Install Anaconda (https://docs.anaconda.com/anaconda/install/linux/)
2. Git clone this repository (https://github.com/DanielLSM/plotter-manager)
```
$ cd ~
$ git clone https://github.com/DanielLSM/plotter-manager
```
3. Open your console in the root folder of the repository cloned.
```
$ cd plotter-manager
```
4. Create a new conda environment from the provided file
```
$ conda env create -f wasp-soft.yml
```
5. Activate said conda environment
```
$ conda activate wasp-soft
```
6. Hopefully everything went well!

## Running the tests

1. Open your console and activate the conda environment we created before:
```
$ conda activate wasp-soft
$ cd ~
$ cd plotter-manager/plotter-manager
```
2. Running the tests
```
$ pytest tests.py
```
3. Hopefully everything went well and there are no errors to the functionality!

## Running 2 demos (OPTIONAL)

1. Open your console and activate the conda environment we created before:
```
$ conda activate wasp-soft
$ cd ~
$ cd plotter-manager/plotter-manager
```
2. Running the demo
```
$ python demo.py
```

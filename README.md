# Getting Started With Python

## Install Anaconda or Miniconda 

Download from https://www.anaconda.com/download/success

## Creating a Python environment

### 1. Start the correct terminal

First, open your Anaconda terminal. In Windows, it is installed as *Anaconda Prompt* and it can be easily located in the Start Menu. 

### 2. Create an environment

To create an environment called *ex1* we use the following command ine:

```console
conda create -n ex1
```

### 3. Activating an environment

Once created, an environment must be activated before it can be used. For activation, use the following conda activate command:

```console
conda activate ex1
```

### 4. Installing packages

Let's install the following packages:
- numpy
- pandas
- matplotlib
- jupyter

To install a package, we use the *conda install* command. It installs packages in the current environment. To install the four packages below, for example, we use the command line is:

```console
conda install numpy pandas matplotlib jupyter
```

### 5. Installing our own packages

We can create our own packages, such as the *pkg1* package in this repo, to better organize our development in Python. Assuming the package is in the path *packages/pkg1*, one can install it using the following command:

```console
pip install -- editable packages/pkg1
```

### 6. Removing an environment

To erase the environment *ex1*, we can use:

```console
conda env remove -n ex1
```

### 7. Listing all environments

To list all environments. use:

```console
conda env list
```

## Jupyter Notebook

To start Jupyter Notebook, use:

```console
jupyter notebook
```

This repository contains an example notebook that creates a simple plot using Numpy and Matplotlib. 

## Visual Studio Code




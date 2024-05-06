# Python startup procedure


## Python environment creation

These commands will allow you to create an environment with conda.

```bash
conda install -y -c conda-forge mamba
mamba create -n tutorial
mamba activate tutorial
mamba install -c conda-forge -y python=3.10 scipy sympy pandas numpy matplotlib numba notebook jupyterlab=3 ipywidgets ipython

```


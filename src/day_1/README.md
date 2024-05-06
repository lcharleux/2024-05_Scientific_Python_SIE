# Python startup procedure


## Python environment creation

These commands will allow you to create an environment with conda.

```bash
conda install -y -c conda-forge mamba
```

```bash
mamba create -n tutorial
```

```bash
mamba activate tutorial
```

```bash
mamba install -c conda-forge -y python=3.10 scipy sympy pandas numpy matplotlib numba notebook jupyterlab=3 ipywidgets ipympl ipython
```

## Jupyter Lab

Start using:

```bash
jupyter lab
```

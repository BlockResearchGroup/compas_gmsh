# COMPAS GMSH

**THIS PROJECT IS WIP.**

**CONTRIBUTIONS TOWARDS CREATING A FIRST STABLE VERSION A VERY WELCOME :)...**

----

COMPAS friendly interface for Python-GMSH.

## Installation

```bash
conda create -n gmsh -c conda-forge python=3.8 python-gmsh compas compas_view2 --yes
conda activate gmsh
```

```bash
pip install -e .
```

To install COMPAS View2 for 3D visualisation outside of CAD environments

```bash
conda activate gmsh
conda install -n gmsh -c conda-forge compas_view2
```

## Getting Started

Have a look at some of the first [examples in the documentation](https://compas.dev/compas_gmsh/latest/examples.html).

## License

`compas_gmsh` provides a COMPAS friendly interface to `Python-Gmsh`.
`Gmsh` and `Python-Gmsh` are released under GPL-2.0-or-later.

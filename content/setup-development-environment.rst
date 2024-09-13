

I have been teaching scientific Python for about 15 years now and helping
students simply install everything correctly is still generally painful. I no
longer have to coach students through compiling NumPy and SciPy on Windows but
that pain has now been replaced with navigating them through the myriad of
package managers that all tout themselves to be *the* solution. A new option
seems to be released every week these days.

Back in 2008, I would ``apt install`` the Python scientific computing stack for
simple use on Linux (which still works nicely today!) and if I needed the
newest package version or was contributing to the packages I used, I would
compile NumPy & SciPy in a Python virtual environment and then install mostly
pure Python packages with ``easy_install`` from PyPi. But in 2012, Continuum
Analytics (now Anaconda) released the open source conda package manager and a
website host for conda packages with a goal to unify the bubbling packaging
mess with particular focus on equal status on all three major operating systems
and users never having to compile the scientific Python stack again (among
other things).  I started using conda immediately and have so since then (even
through the slow solver days). I've tried many of the subsequent solutions, but
they all seemed to miss at least detail that does not work with a scientific
computing oriented workflow. I still believe conda's approach is the best
solution, especially since Conda Forge came into being.

Setup Conda with Conda Forge
============================

Speaking of options, there are also various ways to install conda, but I
recommend to install miniforge due to its size being small and that it defaults
to installing packages only from Conda Forge. Miniforge installs a directory
that will house all of your installed software into a single directory that
does not need adminstrator priveleges. It also only installs packages from the
compatible set from Conda Forge.

https://conda-forge.org/download/

Get the latest `Miniforge3`. For Linux and Windows you likely need the x86_64
build and for MacOS you will need to choose the x86_64 for old Macs with Intel
chips and arm64 for new Macs with Arm chips. Follow the installation
instructions in the README here https://github.com/conda-forge/miniforge

Base Conda Environment
======================

conda has a "virtual environment" feature which allows you to install a set of
packages isolated from another set of packages. The "base" environment is the
default environment and I use this environment as my general calculator. I also
install all of the most common packages I use into the base environment. This
gives you something akin to Matlab where the latest version of everythign you
use is importable.

You interact with conda via the command line, so open a terminal on Linux or
Mac and open the miniforge command prompt on Windows.

Conda is installed if you type:

.. code-block:: bash

   conda --version

and it returns a version number like::

   conda 24.7.1

Now install any packages that you think you may use, e.g.:

.. code-block:: bash

   conda install numpy scipy matplotlib sympy ipython spyder

After that finishes you can use these packages:

.. code-block:: bash

   $ python -c "import numpy; print(numpy.ones(5))"
   [1. 1. 1. 1. 1.]

If you prefer working in an Integrated Development Environment (IDE) you can
try Spyder, for example:

.. code-block:: bash

   spyder

There are many choices in IDEs and most all of them work seemlessly with conda
and conda environments.

This setup may serve all of your needs and you can use the single set of
packages installed in the base environment. I would periodically run the
command:

.. code-block:: bash

   conda update --all

to keep your packages all at their latest compatible versions.

Project Conda Environments
==========================

At some point you may want a specific set of packages at possibly specific
versions for a project, paper, collaboration, etc. and these will likely be in
conflict with what you have installed in your base environment. For every
specific project I work on, I create a conda virtual environment with the small
set of packages I need for that project. I first create a directory/folder on
my computer for the project and then create a ``myproject-env.yml`` with
contents like this:

.. code-block:: yaml

   name: myproject
   channels:
     - conda-forge
   dependencies:
     - bicycleparameters
     - dynamicisttoolkit
     - ipython
     - matplotlib
     - numpy
     - opty
     - pip
     - pip
     - python ==3.10  # can specify specific versions
     - scipy
     - spyder-kernels  # will allow use of this environment in spyder isntalled in base
     - sympy
     - yeadon

All packages in the ``dependencies:`` list have to be https://conda-forge.org/packages/

This file can be used by you or others to reproduce a software installation for
your project.

https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

Once you save the file, you can create the environment with this command:

.. code-block:: bash

   conda env create -f myproject-env.yml

To use the environment, you have to activate it in the terminal/command prompt:

.. code-block:: bash

   conda activate myproject

Now you'll have access to that set of packages by default:

.. code-block:: bash
   $ python --version
   Python 3.10.9

We installed spyder in the base environment and spyder-kernels in the project's
environment. If we type ``spyder`` the spyder installed in base will open
(because we didn't install in the project environment). But when you open
spyder you can select this project environment to run the code.

python -c "import sys; print(sys.executable)"

Preferences -> Python interpreter -> Use the following Python interpreter and
paste in the path output from the above command.

https://medium.com/@apremgeorge/using-conda-python-environments-with-spyder-ide-and-jupyter-notebooks-in-windows-4e0a905aaac5

There is a similar approach for using this environment in Jupyter or other
IDEs.

If you are using version control, you should commit the environment yaml file
to the repository so others can reproduce your project environment.

People also build tools to do these kinds of things automatically, for example:
https://github.com/conda-incubator/conda-project

Package Not in Conda Forge
==========================

At some point you will want to use a package that is not available in Conda
Forge. There are different approaches to install the package in your
environment depending on what the package's primary programming language is,
but mostly commonly you may want a Python package that you can find on PyPi but
not in Conda Forge.

https://github.com/conda-forge/staged-recipes

Packages on PyPi are generally installed using the pip package manager
(although you will see many other recommendations on the web: pipx, hatchling,
poetry, pdm, uv, etc., pip is the main one). You can install packages from PyPi
into a Conda environment but this arrangement is delicate and you should never
install packages with pip into your base environment (your are just asking for
trouble then). The safest approach I have found over the years is to first
install everything the PyPi packages depends on using conda and then install
the PyPi package using pip's ``--no-depencencies`` flag.

SymPy is availabe on Conda Forge but we will pretend it isn't. SymPy's only
required dependencies are python and mpmath and both are available on conda
forge. So we create an environment file with pip so we can install from PyPi
and the two dependencies of SymPy:

.. code-block:: yaml

   name: myproject
   channels:
     - conda-forge
   dependencies:
     - pip
     - python
     - mpmath

.. code-block:: bash

   conda env create -f myproject-env.yml
   conda activate myproject

Now, you can run pip inside the conda environment:

.. code-block:: bash

   python -m pip install --no-deps sympy

If you now look at the list of installed packages you see that sympy is listed
as installed from pypi:

.. code-block:: bash

   $ conda list
   # packages in environment at /home/moorepants/miniforge/envs/myproject:
   #
   # Name                    Version                   Build  Channel
   _libgcc_mutex             0.1                 conda_forge    conda-forge
   _openmp_mutex             4.5                       2_gnu    conda-forge
   bzip2                     1.0.8                h4bc722e_7    conda-forge
   ca-certificates           2024.8.30            hbcca054_0    conda-forge
   ld_impl_linux-64          2.40                 hf3520f5_7    conda-forge
   libexpat                  2.6.3                h5888daf_0    conda-forge
   libffi                    3.4.2                h7f98852_5    conda-forge
   libgcc                    14.1.0               h77fa898_1    conda-forge
   libgcc-ng                 14.1.0               h69a702a_1    conda-forge
   libgomp                   14.1.0               h77fa898_1    conda-forge
   libnsl                    2.0.1                hd590300_0    conda-forge
   libsqlite                 3.46.1               hadc24fc_0    conda-forge
   libuuid                   2.38.1               h0b41bf4_0    conda-forge
   libxcrypt                 4.4.36               hd590300_1    conda-forge
   libzlib                   1.3.1                h4ab18f5_1    conda-forge
   mpmath                    1.3.0              pyhd8ed1ab_0    conda-forge
   ncurses                   6.5                  he02047a_1    conda-forge
   openssl                   3.3.2                hb9d3cd8_0    conda-forge
   pip                       24.2               pyh8b19718_1    conda-forge
   python                    3.12.5          h2ad013b_0_cpython    conda-forge
   readline                  8.2                  h8228510_1    conda-forge
   setuptools                73.0.1             pyhd8ed1ab_0    conda-forge
   sympy                     1.13.2                   pypi_0    pypi
   tk                        8.6.13          noxft_h4845f30_101    conda-forge
   tzdata                    2024a                h8827d51_1    conda-forge
   wheel                     0.44.0             pyhd8ed1ab_0    conda-forge
   xz                        5.2.6                h166bdaf_0    conda-forge

If you carefully install all dependencies from Conda Forge then you can safely
run ``conda update --all`` inside the conda environment and then follow that
with a ``python -m pip install -U sympy`` to upgrade the PyPi packages.

This method will generally work but it requires you to manually figure out and
install the dependencies. If you have many PyPi packages, then this may get out
of hand to manage but my experience is that you typically don't have many PyPi
packages you need that are not on Conda Forge.

Conda does also support specifying PyPi packages in the environment file like
so:

.. code-block:: yaml

   name: myproject
   channels:
     - conda-forge
   dependencies:
     - pip
     - python
     - mpmath
     - pip:
       - sympy

but the ``--no-deps`` flag isn't used and you may end of up with many pypi
packages in your conda env and then updating things becomes more difficult, or
even impossible. But you can always delete the environmetn and recreate it.

There are new developments to make this work more seemlessly, for example see
https://github.com/conda-incubator/conda-pypi. But the ideal solution is that
you contribute to Conda Forge and add the PyPi package you need via
https://github.com/conda-forge/staged-recipes. It is generally pretty straight
forward using `greyskull pypi package-name` to generate the recipe for a pull
request if the package is a pure python pacakge.

Developing a Package in Your Environment
========================================

   conda develop

===============
Guide: Software
===============

:date: 2025-12-20
:status: hidden

We write software in the lab and strive to make it open source to facilitate
reuse and collaboration. It is ideal if lab members 1) use the software we
write, 2) report bugs and issues, and 3) contribute back to the software. The
more we do all three points the more universally useful and easy to use the
software becomes for future use both by us and others outside the lab. This
page highlights the software that we have designed to be more easily reusable
and that we continuously maintain. It takes a collective effort from all lab
members to keep these tools useful to all of us.

BicycleParameters
=================

Generation and manipulation of bicycle physical parameters. If you measure the
geometry, mass, inertia of a bicycle and/or rider you can use this package to
process the measurements. It also has generic parameter sets and models that
can be used to do dynamics analysis of bicycles. Lastly, it has a web
application for exploring the linear Carvallo-Whipple model's properties.

| Languages: Python, HTML, CSS
| Repository: https://github.com/moorepants/BicycleParameters
| Documentation: https://bicycleparameters.readthedocs.io

opty
====

opty is our general toolbox for solving optimal control problems (trajectory
optimization & parameter identification) using the direct collocation +
nonlinear programming method.

| Languages: Python, Cython, C
| Repository: https://github.com/csu-hmc/opty
| Documentation: http://opty.readthedocs.io
| Examples of use in the lab:

- Sorgedrager, Simon, “Riding a Bicycle Without Hands: How To Do It and the
  Bicycle Dynamics Behind It,” 2025, MSc, Delft University of Technology.
  https://resolver.tudelft.nl/uuid:ee22c5d1-b27f-4542-8a49-71d92a9e2f55
- T. J. Stienstra, S. G. Brockie, and J. K. Moore, “BRiM: A modular
  bicycle-rider modeling framework,” presented at the Bicycle and Motorcycle
  Dynamics 2023, Delft, The Netherlands: TU Delft OPEN Publishing, Oct. 2023.
  https://doi.org/10.59490/660179a06bf1082286458109

yeadon
======

Takes geometrical measurements of a person and generates body segment
parameters (mass, inertia) following Fred Yeadon's model.

| Languages: Python
| Repository: https://github.com/chrisdembia/yeadon
| Documentation: https://yeadon.readthedocs.io

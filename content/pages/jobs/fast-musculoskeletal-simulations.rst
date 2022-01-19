=============================================================================================
Musculoskeletal Models Optimized For Speedy Forward Simulation Based on Analytic Descriptions
=============================================================================================

:date: 2020-09-21
:status: hidden
:slug: jobs/msc/fast-musculoskeletal-simulations
:template: msc-project

Increasingly, musculoskeletal models are being used with optimization tools to
answer a variety of research questions. When these optimization problems
require forward simulation of the models it is helpful if the simulations
execute as fast as possible to reduce the time to obtain results, because
optimization methods can require millions of distinct simulations and forward
simulations of musculoskeletal models may even still require real time
simulation times.

Many of the optimization methods used today wrap simulations based on generic
physics engines which solve for the equations of motion at each time step.
These physics engines are optimized for speedy forward simulation execution in
a variety of ways, but because of their generic-ness they are unlikely
optimized for the particular model. Many early prominent mutlibody dynamics
codes, and some modern ones, use computer algebra systems (CAS) to symbolically
derive long form analytic expressions for the equations of motion of the
system. This allows for very high level mathematical descriptors of the
equations of motion that can embody assumptions about the mathematical
variables and expressions. With this high level description of the math it is
possible to generate model and computer architecture specific low level codes
through tailored code generation and compilation. This process has the
potential to give significant speedups relative to the generic physics engines.

The hypothesis is that code generated from the symbolic forms can be
significantly faster than a numeric based system. There has been work over the
years in the SymPy and PyDy code generation tools that can be applied to
musculoskeletal models.

Possible goals related to this topic (there is enough for multiple MSc's
depending on the path):

- Improve SymPy's code generation facilities for arbitrary ordinary
  differential equations and differential algebraic equations that considers
  high level mathematical assumptions for optimizing the generated code.
- Create one or more benchmark models based on complex and typically
  slow-to-simulate biomechanics models using different software and compare
  execution times.
- Compare optimized forward simulations of different musculoskeletal simulation
  tools to tailored code generation from symbolic forms.
- Improve the Autolev to SymPy parser and get it working smoothly with complex
  Autolev models:
  https://docs.sympy.org/latest/modules/physics/mechanics/autolev_parser.html
- Implement the Featherstone, Jain, or similar equation of motion method in
  sympy.physics.mechanics, symbolically or as numeric code generation pattern.
- Implement code generation for typical models that slow simulations:
  stiffness, friction, switching, non-linearities, contact, muscle models, etc.
- Explore applicable parallelization techniques and apply to a complex muscle
  skeletal simulation.

Prior Art
=========

Mailing list and Github discussions in the SymPy and PyDy projects will be
useful.

Some symbolic multibody dynamics codes:

- Auto/Bike/Truck/CarSim (derived from Michael Sayer's work at University of Michigan), https://www.carsim.com/, http://www.umtri.umich.edu/our-results/publications/symbolic-computer-language-multibody-systems
- Autolev (https://link.springer.com/chapter/10.1007/978-3-642-50995-7_7)
- MotionGenesis (http://www.motiongenesis.com/)
- SD/Fast (https://support.ptc.com/support/sdfast/index.html)
- symy.physics.mechanics (https://docs.sympy.org/latest/modules/physics/mechanics/index.html)

Numeric mulitbody dynamics codes:

- `Bullet <https://github.com/bulletphysics/bullet3>`_
- `DART <https://github.com/dartsim/dart>`_
- `Open Dynamics Engine <https://bitbucket.org/odedevs/ode>`_
- `Rigid Body Dynamics Library <https://github.com/ORB-HD/rbdl-orb>`_
- `Simbody <https://github.com/simbody/simbody>`_

Papers that may be useful to this project in our Zotero group:
https://www.zotero.org/groups/966974/mechmotum/collections/GB9UR7YK

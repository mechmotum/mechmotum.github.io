=========================================================================
Experiments with Cyclist Social Forces for Microscopic Traffic Simulation
=========================================================================

:date: 2023-08-21
:status: hidden
:slug: jobs/msc/cyclist-social-force-experiments
:template: msc-project

.. list-table::
   :class: table

   * - |socialforcesim|
     - |sumosnapshot|
   * - The social force model in action.
     - SUMO Cyclists driven by social forces.

.. |socialforcesim| image:: https://objects-us-east-1.dream.io/mechmotum/sfm-intersection.png

.. |sumosnapshot| image:: https://objects-us-east-1.dream.io/mechmotum/sfm-intersection-sumo.png

Microscopic traffic simulation is an important tool that traffic engineers and
researchers use to assess the performances of existing and new transport
innovations. Historically being designed for car traffic, current simulation
frameworks (e.g. SUMO, VISSIM) still only provide rudimentary models for the
simulation of cyclists with strong limitations regarding the interaction of
cyclists and other road users.  At the bike lab, we are working on new models
for the microscopic simulation of cyclists. A new adaption of the social force
model introduces physics-based bicycle dynamics [Schmidt2023]_ to an
established microscopic model [Helbing1995]_, aiming to improve simulated
interactions. In this model, a cyclist's motivation to act is described by
imaginary forces. The summation of these forces becomes the input of a dynamic
bicycle model and drives the simulated movements. In this framework, we are
currently offering two options for Master’s projects.

Option 1: Modelling and Simulation:
===================================

With the fundamental framework set, many features have to be added to the model
to enable a full simulation of bicycle traffic. Think for example about the
transition between riding and stopping, path planning to execute complex riding
maneuvers, or taking and giving priority.  In a modeling and simulation
Master’s project, you may choose a relevant feature, identify the desired
cyclist behavior from the literature, develop a suitable model, implement the
model in Python, calibrate its parameters, and validate its performance.

Option 2: Validation Experiments:
=================================

Many aspects of our current model are derived heuristically and require
validation with real-world data.  So, how do cyclists actually interact? How do
they perform evasive maneuvers? How much space do they leave each other? How
closely do they overtake? In an experimental master’s project, you may run
experiments on cyclist interactions, measure interaction profiles in terms of
relative position, speed, acceleration, or orientation, and identify typical
behavioral patterns. This requires designing and setting up experiments,
selecting suitable performance measures, choosing and calibrating a sensor
setup, and post-processing the collected data. The post-processed data may then
be used to calibrate and validate parts of the cyclist social force model.

References
==========

.. [Helbing1995] Helbing, D., & Molnár, P. (1995). Social force model for
   pedestrian dynamics.  Physical Review E, 51(5), 4282–4286.
   https://doi.org/10.1103/PhysRevE.51.4282
.. [Schmidt2023] Schmidt, C., Dabiri, A., Schulte, F., Happee, R. & Moore, J.
   (2023). Essential Bicycle Dynamics for Microscopic Traffic Simulation: An
   Example Using the Social Force Model.  The Evolving Scholar - BMD 2023, 5th
   Edition. https://doi.org/10.59490/649d4037c2c818c6824899bd

Current implementation of the model: https://github.com/chrismo-schmidt/cyclistsocialforce

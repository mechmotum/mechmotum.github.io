:title: Research

The following details various research projects that are in progress.

Vehicle Dynamics, Control, and Handling
=======================================

Optimal Bicycle Design for Handling
-----------------------------------

| Current researchers: Roy Gilboa
| Collaborators: Mont Hubbard, Ronald Hess (UC Davis)

.. image:: https://objects-us-east-1.dream.io/mechmotum.github.io/optimal-handling-bicycle.png
   :align: center
   :width: 60%

We have developed an optimization algorithm that can discover bicycle designs
which maximize the lateral handling qualities of the vehicle [1]_. The
algorithm produces less-than-intuitive but physically feasible bicycle designs.
We are currently working to make the algorithm more robust and expand the
parameter search space. We are also constructing some of the discovered designs
for experimental validation and testing.

.. [1] Moore, Jason, Mont Hubbard, and Ronald A. Hess. "An Optimal Handling
   Bicycle." In Proceedings of the 2016 Bicycle and Motorcycle Dynamics
   Conference. Figshare, 2016. https://doi.org/10.6084/m9.figshare.c.3460590.v11.

Experimental Validation of Bicycle Handling Prediction
------------------------------------------------------

| Current researchers: Trevor Metz
| Collaborators: Mont Hubbard, Ronald Hess
| Past researchers: Scott Kresie

.. image:: https://objects-us-east-1.dream.io/mechmotum.github.io/handling-metric.png
   :align: center
   :width: 60%

We have proposed a theoretical lateral handling quality metric for any given
bicycle design based on a corpus of experimental data in aircraft handling
research [2]_. This project aims to validate this metric directly from
experimental evidence in bicycling maneuvers and tasks. We have developed a
variable stability instrumented bicycle and demonstrated preliminarily that
that there may be correlations between our theoretical metric and the rider's
subjective opinion of the bicycle's handling [3]_. Ongoing work includes,
improvements to the experimental apparatus and protocol for a larger scale
validation with arbitrary experimental subjects.

.. [2] Hess, Ronald, Jason K. Moore, and Mont Hubbard. “Modeling the Manually
   Controlled Bicycle.” IEEE Transactions on Systems, Man, and Cybernetics -
   Part A: Systems and Humans 42, no. 3 (May 2012): 545–57.
   https://doi.org/10.1109/TSMCA.2011.2164244.
.. [3] Kresie, Scott W., Jason K. Moore, Mont Hubbard, and Ronald A. Hess.
   "Experimental Validation of Bicycle Handling Prediction," September 13,
   2017. https://doi.org/10.6084/m9.figshare.5405233.v1.

Assistive Devices
=================

Control Identification of Human Standing
-----------------------------------------

| Current researchers: Erich Baur
| Collaborators: Ton van den Bogert (Cleveland State University)

Humans unconsciously utilize a control strategy while standing. Visual,
vestibular, and proprioceptive sensing inform the brain's control strategy
which reacts to internally and environmentally produced perturbations. This is
something humans are very good at but robots are bad at, thus if we can
understand how humans accomplish this we can potentially design robots with
biomimetic controllers. In laboratory settings we can accurately measure body
segment kinematics, muscle activation levels, and ground force reactions during
standing. Given all or subsets of this data collected during externally
perturbed standing, we are interested in developing optimal control theories
and methods of identifying the specific control strategy in use. We have
developed parameter identification methods using direct collocation to identify
the controllers used in simulated standing [4]_. The general optimal control
and parameter estimation methods used have been formalized in the software,
Opty [5]_. We are currently developing a small desktop "double pendulum on a
cart" robot to verify and improve the control identification methods. The robot
will allow us to measure the motion during perturbed balancing which is a
result of known programmed control strategies.

.. [4] Moore, Jason K., and Antonie J. van den Bogert. "Quiet Standing Control
   Parameter Identification with Direct Collocation." In XV International
   Symposium on Computer Simulation in Biomechanics. Edinburgh, UK, 2015.
.. [5] Jason K. Moore, and Antonie van den Bogert. "Opty: Software for
   Trajectory Optimization and Parameter Identification Using Direct
   Collocation." Journal of Open Source Software 3, no. 21 (2018): 300.
   https://doi.org/10.21105/joss.00300.

Design of a Quadrapeligic Friendly Tricycle
-------------------------------------------

| Current researchers: Aaron Shaw, Jake Parkhurst
| Collaborators: Greg Tanner (Disability Reports), Outrider USA
| Past researchers: Andy Wu, Felicia Fashanu, Haowei Li, Cynthia Devaughn, Vivian Ting, Thomas Poozhikala

.. image:: https://objects-us-east-1.dream.io/mechmotum.github.io/quad-friendly-trike.png
   :width: 60%

Students developed a adaptive input device to enable persons with ALS and
quadriplegia to control an electric tricycle.

Sports Engineering
==================

Smartphone-based Rowing Metric Estimation
-----------------------------------------

| Current researchers: Bryn Cloud, Ada Liu, Britt Tarien
| Collaborators: Paul Crawford (Hegemony Technologies), Mont Hubbard (UC Davis), Xinfan Lin (UC Davis)
| Past researchers: Thomas Shedd, Li Wang, Andrew Shoats

Real-time feedback of stroke-by-stroke rowing performance metrics can enable
data driven training and coaching. Instrumenting rowers during training and
competition with laboratory quality sensing is very difficult, but the ubiquity
of smartphones provides an avenue to collect fewer and less accurate kinematic
and kinetic measurements. This project aims to improve performance critical
biomechanic rowing metrics through dynamics informed estimation algorithms. We
have developed rower adaptive filtering methods to predict global boat
position, speed, stroke rate, and distance per stroke at high accuracy and with
experimental protocols for validating the estimations.

Ski Jumps Designed for a Specific Equivlanet Fall Height
--------------------------------------------------------

| Current researchers:
| Collaborators: Mont Hubbard (UC Davis), Jim McNeil (Colorado School of Mines)

Little engineering or science goes into the design and construction of ski and
snowboard jumps in terrain parks at publicly accessible ski resorts. A
relatively large number of injuries and even deaths occur during skiing and
snowboarding at these resorts. It is possible to design the landing surfaces of
jumps such that the normal impact velocity on landing is capped at a safer
value regardless of the jumper's takeoff speed and jump launch speed. These
jump designs can still provide large maximum heights and flight durations. We
have designed a web application that laymen can use to design ski jumps with a
specified equivalent fall height.

Engineering Education
=====================

Interactive Jupyter-Enabled LibreTexts Pages
--------------------------------------------

| Current researchers: Henry Agnew
| Collaborators: Delmar Larsen (UC Davis)

We are interested in providing an interactive computing environments in online
textbooks at a massive scale. LibreTexts is one of the largest and most visited
online compendium of textbooks used in collegiate academics. The website
currently serves mostly static and non-interactive content. We are working to
enable Jupyter-backed interactive computation cells that authors can use to
incorporate Python, R, Octave, and Sage generated media for pages. This will
enable arbitrary visualizations and allow students to learn through
computational oriented exercises.

.. _LibreTexts: http://www.libretexts.org

Development of a Beam Bending Package for SymPy
-----------------------------------------------

| Current researchers: Jashanpreet
| Collaborators: Ashirant and other SymPy Developers
| Past researchers: Sampad Saha

Mechanical and civil engineers utilize two- and three-dimensional theories of
stress and strain to determine if structural beams will fail. Simple
mathematical models can be used to make accurate predictions of failure due to
shear, bending, and torsion stresses and due to deflection. Solving beam
related problems typically involves integrating discontinuous functions and
solving for boundary conditions. The integral calculus and algebra details
often hide the trees for the woods. This project is centered around developing
a package for SymPy that can be used to model and solve analytical beam
problems, without getting bogged down in the mathematical details.

Learning Mechanical Vibrations Through Computational Thinking
-------------------------------------------------------------

| Current researchers:
| Past researchers: Kenneth Lyons

Appropriate Technology
======================

Design of a Mobile Bicycle Powered Irrigation Pump
--------------------------------------------------

| Current researchers: Aaron Shaw, Rayming Liang
| Collaborators: Andrew Hall (Buffalo Bikes)
| Past researchers: Abraham McKay

We have developed a inexpensive centrifugal pump that attaches to a simple PTO
on a Buffalo Bike.

:title: Research

The following details various research projects that are currently active.

Human-in-the-loop Augmented Automatic Control and Vehicle Design
================================================================

Optimal Bicycle Design for Handling
-----------------------------------

| Current researchers: Anastasia Kubicki, Anthony Toribio
| Collaborators: Mont Hubbard, Ronald Hess (UC Davis)
| Past researchers: Roy Gilboa

.. image:: https://objects-us-east-1.dream.io/mechmotum/optimal-handling-bicycle.png
   :align: center
   :width: 60%
   :alt: Image of a theorectical optimal bicycle.

We have developed an optimization algorithm that can discover bicycle designs
which maximize the lateral handling qualities of the vehicle [#]_. The
algorithm produces less-than-intuitive but physically feasible bicycle designs.
We are currently working to make the algorithm more robust and expanding the
parameter search space. We are also constructing some of the discovered designs
for experimental validation and testing. The first design, based on an optimal
design for 4 m/s is shown below:

.. image:: https://objects-us-east-1.dream.io/mechmotum/opt-bike-design.png
   :align: center
   :width: 60%
   :alt: Image of a realizable optimal bicycle.

.. [#] Moore, Jason, Mont Hubbard, and Ronald A. Hess. "An Optimal Handling
   Bicycle." In Proceedings of the 2016 Bicycle and Motorcycle Dynamics
   Conference. Figshare, 2016. https://doi.org/10.6084/m9.figshare.c.3460590.v11.

Experimental Validation of Bicycle Handling Prediction
------------------------------------------------------

| Current researchers: Trevor Metz
| Collaborators: Mont Hubbard, Ronald Hess
| Past researchers: Scott Kresie

.. image:: https://objects-us-east-1.dream.io/mechmotum/handling-metric.png
   :align: center
   :width: 60%
   :alt: Image showing handling quality metrics for a variety of bicycles.

We have proposed a theoretical lateral handling quality metric for any given
bicycle design based on a corpus of experimental data in aircraft handling
research [#]_. This project aims to validate this metric directly from
experimental evidence in bicycling maneuvers and tasks. We have developed a
variable stability instrumented bicycle and demonstrated preliminarily that
that there may be correlations between our theoretical metric and the rider's
subjective opinion of the bicycle's handling [#]_. Ongoing work includes,
improvements to the experimental apparatus and protocol for a larger scale
validation with arbitrary experimental subjects [#]_.

.. [#] Hess, Ronald, Jason K. Moore, and Mont Hubbard. "Modeling the Manually
   Controlled Bicycle." IEEE Transactions on Systems, Man, and Cybernetics -
   Part A: Systems and Humans 42, no. 3 (May 2012): 545–57.
   https://doi.org/10.1109/TSMCA.2011.2164244.
.. [#] Kresie, Scott W., Jason K. Moore, Mont Hubbard, and Ronald A. Hess.
   "Experimental Validation of Bicycle Handling Prediction," September 13,
   2017. https://doi.org/10.6084/m9.figshare.5405233.v1.
.. [#] Metz, Trevor. "Design of a PID Controller for Controlling The Speed of
   an Instrumented Ebike", Laboratorium of Marvelous Mechanical Motum Blog
   (December 15, 2018)
   https://mechmotum.github.io/blog/ebike-controller-design.html

Assistive Device Design for the Physically Impaired
===================================================

Control Identification of Human Standing
-----------------------------------------

| Current researchers:
| Collaborators: Ton van den Bogert (Cleveland State University)
| Past researchers: Dorian Crutcher, Jonathan Cubanski, Todd Sweeney, Greg McDonald, Jiahao Wei, Erich Baur, Kendall Lui, Stanley Tsang, Chenxiong Yi, Rouxi Peng

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
the controllers used in simulated standing [#]_. The general optimal control
and parameter estimation methods used have been formalized in the software,
Opty [#]_. We are currently developing a small desktop "double pendulum on a
cart" robot to verify and improve the control identification methods. The robot
will allow us to measure the motion during perturbed balancing which is a
result of known programmed control strategies.

.. [#] Moore, Jason K., and Antonie J. van den Bogert. "Quiet Standing Control
   Parameter Identification with Direct Collocation." In XV International
   Symposium on Computer Simulation in Biomechanics. Edinburgh, UK, 2015.
.. [#] Jason K. Moore, and Antonie van den Bogert. "Opty: Software for
   Trajectory Optimization and Parameter Identification Using Direct
   Collocation." Journal of Open Source Software 3, no. 21 (2018): 300.
   https://doi.org/10.21105/joss.00300.

Design of a Quadriplegic Friendly Tricycle
------------------------------------------

| Current researchers:
| Collaborators: Greg Tanner (Disability Reports), Tommy Ausherman (Outrider USA)
| Past researchers: Aaron Shaw, Jake Parkhurst, Andy Wu, Felicia Fashanu, Haowei Li, Cynthia Devaughn, Vivian Ting, Thomas Poozhikala

.. image:: https://objects-us-east-1.dream.io/mechmotum/quad-friendly-trike.png
   :width: 60%
   :align: center
   :alt: brochure image of the tricycle

Students developed a adaptive input device to enable persons with ALS or
quadriplegia to control an electric tricycle.

Enhancing Athlete Performance and Safety in Sports
==================================================

Smartphone-based Rowing Metric Estimation
-----------------------------------------

| Current researchers:
| Collaborators: Paul Crawford (Hegemony Technologies), Mont Hubbard (UC Davis), Xinfan Lin (UC Davis)
| Past researchers: Bryn Cloud, Ada Liu, Britt Tarien, Thomas Shedd, Li Wang, Andrew Shoats

Real-time feedback of stroke-by-stroke rowing performance metrics can enable
data driven training and coaching. Instrumenting rowers during training and
competition with laboratory quality sensing is very difficult, but the ubiquity
of smartphones provides an avenue to collect fewer and less accurate kinematic
and kinetic measurements. This project aims to improve performance critical
biomechanic rowing metrics through dynamics informed estimation algorithms. We
have developed rower adaptive filtering methods to predict global boat
position, speed, stroke rate, and distance per stroke at high accuracy and with
experimental protocols for validating the estimations [#]_.

.. [#] B. Cloud et al., "Adaptive smartphone-based sensor fusion for estimating
   competitive rowing kinematic metrics," 23-Dec-2018.
   https://doi.org/10.31224/osf.io/nykuh


Ski Jumps Designed for a Specific Equivalent Fall Height
--------------------------------------------------------

| Current researchers: Bryn Cloud
| Collaborators: Britt Tarien, Mont Hubbard (UC Davis), Jim McNeil (Colorado School of Mines)

.. image:: https://objects-us-east-1.dream.io/mechmotum/skijumpdesign-screenshot.jpg
   :width: 60%
   :align: center
   :target: http://www.skijumpdesign.info
   :alt: Screenshot of the ski jump design application.

Little engineering or science goes into the design and construction of ski and
snowboard jumps in terrain parks at publicly accessible ski resorts. A
relatively large number of injuries and even deaths occur during skiing and
snowboarding at these resorts. It is possible to design the landing surfaces of
jumps such that the normal impact velocity on landing is capped at a safer
value regardless of the jumper's takeoff speed and jump launch speed. These
jump designs can still provide large maximum heights and flight durations. We
have designed a web application that laymen can use to design ski jumps with a
specified equivalent fall height.

Sustainable Transportation
==========================

Inexpensive Open Source and Open Hardware Bicycle Data Logger
-------------------------------------------------------------

| Current researchers:
| Past researchers: Edward Jacobs
| Collaborators: Marco Dozza (Chalmers University), Christian-Nils Åkerberg Boda (Chalmers University)

Analysis of comprehensive dynamical data during bicycling trips and activities
has the potential to teach us much about travel behavior and safety of
bicyclists. We would like to develop a open collaborative project with the aim
of creating a modular, continually inexpensive, open source, and open hardware
bicycle data logger. This idea was pitched by Marco Dozza at ICSC 2017 [#]_ and
we are working with his team to bring this to fruition.

.. [#] Dozza, Marco; Rasch, A.; Boda, C. N. (2017): An Open-Source Data Logger
   for Field Cycling Collection: Design and Evaluation.
   https://doi.org/10.6084/m9.figshare.5404918.v1

Human Powered Appropriate Technology
====================================

Efficiency of Human Powered Irrigation Pumps
--------------------------------------------

| Current researchers:
| Collaborators: Andrew Hall (Buffalo Bikes)
| Past researchers: Aaron Shaw, Rayming Liang, Abraham McKay

We have developed a inexpensive centrifugal pump that attaches to a simple
power takeoff on a Buffalo Bike [#]_. Our hypothesis is that a less efficient
centrifugal pump paired with power generation from cycling will be overall more
efficient than a more efficient positive displacement pump paired with stepping
power generation. We have recently shown this to be true by accurately
measuring the input biomechanical power and output hydraulic power from both
systems to produce efficiency curves as a function of hydraulic load [#]_.

.. [#] Mckay, Abraham B., "The Water Buffalo: Design of a Portable Bicycle
   Powered Irrigation Pump for Small-Scale African Farmers", MSc Thesis,
   University of California, Davis, 2018.
   https://doi.org/10.6084/m9.figshare.6378401.v2
.. [#] Shaw, Aaron and Liang, Rayming. "Finding the Efficiency of the Xylem and
   Money Maker Treadle Pumps", Laboratorium of Marvelous Mechanical Motum Blog
   (December 27, 2018)
   https://mechmotum.github.io/blog/treadle-pump-experiment.html

Teaching and Learning Engineering Through Mobility Applications
===============================================================

Learning Mechanical Vibrations Through Computational Thinking
-------------------------------------------------------------

| Current researchers:
| Past researchers: Kenneth Lyons

"Computational thinking" is an alternative learning process for formulating and
solving engineering problems. A unique set of abstractions are available to the
learner in addition to those from mathematical and written language. We have
developed an interactive textbook and problem sets using the Jupyter system of
tools for 40 hours of in-class teaching and learning. These teaching materials
are backed by a custom software library for mechanical vibrations designed to
facilitate solving problems with computational thinking.

Interactive Jupyter-Enabled LibreTexts Pages
--------------------------------------------

| Current researchers: Celine Liang
| Collaborators: Delmar Larsen (UC Davis), Richard Feltstykket (UC Davis), Tom Neubarth (UC Davis)
| Past researchers: Xiaochen Zang, Xin Luigi Chen, Kevin Krausse, Henry Agnew

We are interested in providing an interactive computing environments in online
textbooks at a massive scale. LibreTexts_ is one of the largest and most
visited online compendium of textbooks used in collegiate academics. The
website currently serves mostly static and non-interactive content. We are
working to enable Jupyter-backed interactive computation cells that authors can
use to incorporate Python, R, Octave, and Sage generated media for pages. This
will enable arbitrary visualizations and allow students to learn through
computational oriented exercises.

.. _LibreTexts: http://www.libretexts.org

Development of a Beam Bending Package for SymPy
-----------------------------------------------

| Current researchers: Ishan Joshi (Netaji Subhas Institute of Technology, SymPy GSoC)
| Collaborators: SymPy Developers
| Past researchers: Jashanpreet Singh, Sampad Saha

Mechanical and civil engineers utilize two- and three-dimensional theories of
stress and strain to determine if structural beams will fail. Simple
mathematical models can be used to make accurate predictions of failure due to
shear, bending, and torsion stresses and due to deflection. Solving beam
related problems typically involves integrating discontinuous functions and
solving for boundary conditions. The integral calculus and algebra details
often hide the trees for the woods. This project is centered around developing
a package for SymPy that can be used to model and solve analytical beam
problems, without getting bogged down in the mathematical details.

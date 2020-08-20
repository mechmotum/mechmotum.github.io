:title: Research
:page-dir: research
:template: list-of-pages
:sortorder: 2

The following details various research projects that are currently active.

Human-in-the-loop Augmented Automatic Control and Vehicle Design
================================================================

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

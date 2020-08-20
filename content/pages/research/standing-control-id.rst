:title: Control Identification of Human Standing
:status: hidden
:date: 2019-02
:summary-sentence: Humans unconsciously utilize a control strategy while
                   standing. Visual, vestibular, and proprioceptive sensing
                   inform the brain's control strategy which reacts to
                   internally and environmentally produced perturbations. This
                   is something humans are very good at but robots are bad at,
                   thus if we can understand how humans accomplish this we can
                   potentially design robots with biomimetic controllers. In
                   laboratory settings we can accurately measure body segment
                   kinematics, muscle activation levels, and ground force
                   reactions during standing. Given all or subsets of this data
                   collected during externally perturbed standing, we are
                   interested in developing optimal control theories and
                   methods of identifying the specific control strategy in use.
:summary-image: https://objects-us-east-1.dream.io/mechmotum/project-image-standing-id.png

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

Associated Research Products
============================

Blog posts:

- `Double Pendulum Human Controller Robot: GUI Development <{filename}/double-pendulum-robot.rst>`_

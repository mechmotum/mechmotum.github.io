=========================================================
Optimization Based Bicycle Design For Equivalent Dynamics
=========================================================

:date: 2020-09-09
:status: hidden
:slug: jobs/msc/optimization-based-bicycle-design

.. figure:: https://upload.wikimedia.org/wikipedia/en/0/0c/Strida.JPG
   :align: center

   The Strida_ folding bicycle is an example of an unusual bicycle design in
   which it is desirable for it to handle as well as a more typical bicycle.

.. _Strida: https://en.wikipedia.org/wiki/Strida

Description
===========

When creating new bicycle styles, designers use little more than anecdotes and
intuition to guide them in design decisions that affect how the vehicle handles
during maneuvering [Kooijman2013]_. For example, if a designer has a very small
wheeled folding bicycle in mind, is it possible for that vehicle to handle and
feel the same or similar to a more typical bicycle design? If the wheels are
small, what is the best location for the center of mass? What should the angle
of the steer tube be?  What should the wheelbase be? The designer chooses
these, builds prototypes, tests the handling, and adjusts hopefully coming to a
favorable handling feeling.

The vehicle's uncontrolled dynamics affect both the perceived and objective
handling. We have one way fairly clear way to characterize a given bicycle's
dynamics: the eigenvalues of a linear model of the vehicle. For example, if the
Whipple-Carvallo model [Meijaard2007]_ is used to model the bicycle, there are
four complex numbers at any given travel speed that fully characterize the
uncontrolled dynamics. Existing good-handling bicycles have a set of
characteristic eigenvalues and a related characteristic equation [Moore2010]_.

One possible design approach would be to specify some aspects of a bicycle's
physical characteristics and then search for candidate physical characteristics
that ensure this new bicycle design has dynamics as similar as possible to a
bicycle that is subjectively judged to have good handling. This is what a
designer does in an ad-hoc way, but these characteristics could be chosen in an
optimal fashion. [Paudel2020]_ shows a manual method of this design process
that does utilize the vehicle's dynamics.

The goal of this project is to develop a constrained optimization problem which
ensures that an atypical bicycle design with some fully constrained
characteristics has uncontrolled dynamics as close as possible to a typical
bicycle. The optimization problem presented in [Moore2020]_ has similarities to
this problem and can be used for initial ideas. The success of the
methodology should be demonstrated with different atypical bicycles: bakfiets,
folding bicycles, recumbent bicycles, etc. and potentially constructing one of
the designs and testing it.

Required Skills
===============

- 3D multibody dynamics
- Constrained non-linear optimization techniques
- Proficiency in a scientific programming language
- Metal fabrication
- Experimental methods and dynamic measurements

References
==========

.. [Meijaard2007] J. P. Meijaard, J. M. Papadopoulos, A. Ruina, and A. L.
   Schwab, “Linearized dynamics equations for the balance and steer of a
   bicycle: A benchmark and review,” Proceedings of the Royal Society A:
   Mathematical, Physical and Engineering Sciences, vol. 463, no. 2084, pp.
   1955–1982, Aug.  2007.
.. [Moore2010] J. K. Moore, M. Hubbard, D. L. Peterson, A. L. Schwab, and J. D.
   G. Kooijman, “An Accurate Method of Measuring and Comparing a Bicycle’s
   Physical Parameters,” Delft, Netherlands, Oct. 2010.
.. [Kooijman2013] J. D. G. Kooijman and A. L. Schwab, “A review on bicycle and
   motorcycle rider control with a perspective on handling qualities,” Vehicle
   System Dynamics, vol. 0, no. 0, pp. 1–43, doi: 10.1080/00423114.2013.824990.
.. [Moore2020] J. K. Moore and M. Hubbard, “Expanded Optimization for
   Discovering Optimal Lateral Handling Bicycles,” Padua, Italy, 2019, p. 12,
   doi: 10.6084/m9.figshare.9942938.v1.
.. [Paudel2020] M. Paudel and F. F. Yap, “Development of an improved design
   methodology and front steering design guideline for small-wheel bicycles for
   better stability and performance,” Proceedings of the Institution of
   Mechanical Engineers, Part P: Journal of Sports Engineering and Technology,
   vol. 234, no.  3, pp. 227–244, Sep. 2020, doi: 10.1177/1754337120919608.

See Also
========

- `Lab research page on optimal handling bicycles <https://mechmotum.github.io/research/optimal-handling-bicycle.html>`_

How to Apply
============

Send an email to j.k.moore@tudelft.nl with the title of the project in the
subject line. Include an approximately half-page motivation letter explaining
why you want to work in the Bicycle Lab on this project along with your current
resume or C.V.

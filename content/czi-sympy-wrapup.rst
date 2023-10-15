=================================================
SymPy CZI Code Generation & Biomechanics Outcomes
=================================================

:date: 2023-09-28 00:00:00
:tags: sympy, czi, biomechanics
:category: news
:slug: sympy-czi-outcomes
:authors: Jason K. Moore, Sam Brockie
:summary: TODO

We were awarded a two year grant from CZI to improve SymPy_. There were three
themes associated with each of the three co-principal investigators:

- Improve SymPy's Documentation (Meuer)
- Improve SymPy's Performance (Benjamin)
- Improve SymPy's Code Generation for Biomechanical Modeling (Moore)

We were in charge of the last one.

Our overarching goal is to use SymPy to generate symbolic dynamical models of
biomechanical systems, i.e. multibody systems actuated by muscles. This
involves formulating the Newton-Euler equations of motion, possibly with
additional kinematical constraints, and the differential equations that
describe the relationship between neurological activation and generated muscles
forces.

We selected a complex human-machine system as a benchmark problem: the bicycle
and its rider. The nonlinear and linear equations of motion of a riderless
bicycle are traditionally a very challenging system to derive correctly in full
symbolic form ( [BasuMandal2007]_, [Meijaard2007]_). Including a model of a
human rider with muscle activation increases its complexity even further. This
model is made up of hundreds of thousands of arithmetic and transcendental
operations, making it a challenging system to differentiate and evaluate. We
want SymPy to be able to handle models of this and more complexity with ease.
To test SymPy's ability to correctly derive, differentiate, and evaluate the
bicycle-rider's governing equations we choose to formulate and solve an optimal
control problem via direct collocation. The bicycle-rider optimal control
problem would test SymPy's limits.

To do this, we worked on numerous areas in SymPy and downstream packages to
reach this goal. The work herein was primarily done by Timo Steinstra, Jan
Heinen, Sam Brockie, and Jason Moore.

.. _SymPy: https://www.sympy.org

.. [BasuMandal2007] TODO
.. [Meijaard2007] TODO

General Improvements to SymPy Mechanics
=======================================

Joints Package
--------------

Timo Steinstra began with the project through a 2022 Google Summer of Code
internship where he improved the SymPy Mechanics Joints package with
documentation improvements, by reworking the fundamental definition of a joint,
and adding cylindrical, planar, and spherical joints. These were key early
updates to enable the joints package's use in constructing a bicycle-rider
model. See the details of Timo's work in his `GSoC Report`_. This project lead
Timo to do a TU Delft Biomechanical Design MSc project on bicycle-rider
modeling using SymPy. Sam was the primary supervisor of Timo.

.. _GSoC Report: https://github.com/sympy/sympy/wiki/GSoC-2022-Report-Timo-Stienstra-:-Enhancing-the-Joints-Framework

TODO: Maybe add a figure showing one of Timo's nice joints figures from the
SymPy docs. SVG scaling with "width" seems to crop not scale.

.. list-table::
   :class: borderless
   :align: center
   :width: 100%
   :widths: 50 50

   * - |joint1|
     - |joint2|
   * - |joint3|
     - |joint4|
   * - |joint5|
     - |joint6|

.. |joint1| image:: https://docs.sympy.org/dev/_images/PinJoint.svg
   :width: 300px

.. |joint2| image:: https://docs.sympy.org/dev/_images/PrismaticJoint.svg
   :width: 300px

.. |joint3| image:: https://docs.sympy.org/dev/_images/CylindricalJoint.svg
   :width: 300px

.. |joint4| image:: https://docs.sympy.org/dev/_images/PlanarJoint.svg
   :width: 300px

.. |joint5| image:: https://docs.sympy.org/dev/_images/SphericalJoint.svg
   :width: 300px

.. |joint6| image:: https://docs.sympy.org/dev/_images/WeldJoint.svg
   :width: 300px

Symbolic Solutions to Linear Equations
--------------------------------------

Kane's Method relies on solving three sets of linear equations:

1. putting the kinematical differential equations in explicit form
   :math:`\dot{\mathbf{q}} = \mathbf{M}_k^{-1}\mathbf{u}`
2. putting the dynamical differential equations in explicit form
   :math:`\dot{\mathbf{u}} = \mathbf{M}_d^{-1}\mathbf{f}(\mathbf{u}, \mathbf{q}, t)`
3. solving the dependent generalized speeds in terms of the independent
   generalised speeds
   :math:`\mathbf{u}_s = \mathbf{A}^{-1}\mathbf{u}_r`

If these equations are symbolic, it is impossible to determine a zero-pivot in
Gaussian elimination and the solutions are suseptible to divide-by-zero
operations for ranges of numerical values for the variables involved.

There are three ways to deal with this:

1. select the generalized coordinates, generalized speeds, and constants such
   that divide-by-zero cannot occur for the numerical values of interest
2. select Gaussian elimination algorithm that does not put the solutions in a
   form that have divide-by-zero for the numerical values of interest
3. use a zero-division free Gaussian elimination algorithm
4. do the Gaussian elimination numerically for any specific set of numerical
   values

Alternative Symbolic Solvers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In 2014, we switched to using ``LUsolve()`` for all of the linear solves in
Mechanics in `PR 7581`_, which resulted in divide-by-zero issues for complex
problems. That change broke a test that solved the linear Carvallo-Whipple
bicycle model to a machine precision match against published benchmarks as well
as the corresponding `documentation page
<https://docs.sympy.org/latest/modules/physics/mechanics/examples/bicycle_example.html>`_.
This bug has hounded us for 9 years (see https://github.com/pydy/pydy/pull/122,
https://github.com/sympy/sympy/issues/9641).

.. _PR 7581: https://github.com/sympy/sympy/pull/7581

Timo discovered the fundamental divide-by-zero issue after `much sleuthing and
discussion`_. He then introduced a new linear solver that uses `Cramer's
rule`_, which can eliminate divide-by-zero operations in many cases. We then
added support to ``KanesMethod`` and ``Linearizer`` for using linear solvers
other than ``LUSolve()`` including the new Cramer's rule-based solver. With
this we closed the `9 year old bug`_ and allowed out base bicycle model to
build both in non-linear and linear forms.

.. _much sleuthing and discussion: https://github.com/sympy/sympy/issues/24780
.. _Cramer's rule: https://en.wikipedia.org/wiki/Cramer%27s_rule
.. _new linear solver: https://github.com/sympy/sympy/pull/25179
.. _9 year old bug: https://github.com/sympy/sympy/issues/9641

Delayed Numerical Solves
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   A = MatrixSymbol('A', 2, 2)
   b = MatrixSymbol('b', 2, 1)
   x = Inverse(A) @ b
   result = x[0, 0] + x[1, 0]
   eval_x = lambdify((A, b), result)

The above works but the linear solve is handled symbolically::

   Signature: f(A, b)
   Docstring:
   Created with lambdify. Signature:

   func(A, b)

   Expression:

   A[0, 0]*b[1, 0]/(A[0, 0]*A[1, 1] - A[0, 1]*A[1, 0]) - A[0, 1]*b[1, 0]/(A[0,...

   Source code:

   def _lambdifygenerated(A, b):
       return A[0, 0]*b[1, 0]/(A[0, 0]*A[1, 1] - A[0, 1]*A[1, 0]) - A[0, 1]*b[1, 0]/(A[0, 0]*A[1, 1] - A[0, 1]*A[1, 0]) - A[1, 0]*b[0, 0]/(A[0, 0]*A[1, 1] - A[0, 1]*A[1, 0]) + A[1, 1]*b[0, 0]/(A[0, 0]*A[1, 1] - A[0, 1]*A[1, 0])


   Imported modules:

We'd like lambdify to generate code that looks like:

.. code-block:: python

   def eval_x(A, b):
      x = numpy.linalg.solve(A, b)
      return x[0, 0] + x[1, 0]

which allows NumPy (or actually lapack) to use the best algorithm given the
numerical values used for A and b. The expression `Inverse(A) @ b` would need
to remain unevaluated for that to work.

Inertia, Loads, Actuators
-------------------------

We introduced three helper classes:

- ``Inertia()``
- ``Force``, ``Torque``

The inertia object lets you associate a dyadic with a point, to completely
define an inertia. Force and Torque are named tuples that associate a vector
and point and a vector and a frame, respectively.

An Actuator describes the equal and opposite pair of forces or torques.

System
------

Introduction of SymPy Biomechanics
==================================

SymPy Code Generation
=====================

lambdify should handle large expressions

- code gen
  - lambdify docstring speed up
  - MatrixSolve
- dagify
- cse jacobian

BRiM
====

- BMD paper & Timo's thesis

Optimal Skateboard Ollie
========================

- Jan's work: thesis & paper
- pycollo documentation

Optimal Bicycle-Rider Trajectories
==================================

- opty improvements
- muscle driven bicycle model

Lessons Learned
===============

- 6 months to negotiate a contract
- 6 months to hire someone

People
======

Timo, Sam, Jan, Jason

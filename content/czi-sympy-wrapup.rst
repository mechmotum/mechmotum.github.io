=================================================
SymPy CZI Code Generation & Biomechanics Outcomes
=================================================

:date: 2023-09-28 00:00:00
:tags: sympy, czi, biomechanics
:category: news
:slug: sympy-czi-outcomes
:authors: Jason K. Moore, Sam Brockie
:summary: TODO

We were awarded a two year grant from CZI to improve SymPy. There were three
themes associated with each of the three co-principal investigators:

- Improve SymPy's documentation (Meuer)
- Improve SymPy's Performance (Benjamin)
- Improve SymPy's Code Generation to Support Biomechanical Modeling (Moore)

We were in charge of the last one.

An overarching goal is to make SymPy usuable to generate symbolic models of
biomechanical systems, i.e. multibody systems actuated by muscles. Our target
system is the bicycle and its rider. The nonlinear and linear equations of
motion of a bicycle are traditionally a challenging system to derive correctly
full symbolic form. Including a model of a human rider increases its complexity
further. This model is made up of many thousands of arthemtic and transcendtal
operations, making it a challenging system to differentiate and evaluate. We
want SymPy to be able to handle models of this and more complexity with ease.
Formulating and solving optimal control problems with the bicyle-rider system
currently tests the limits of SymPy's abilities.

We worked on numerous areas in SymPy and downstream packages to reach the goal
of solving a bicycle-rider biomechanical optimal control problem.

General Improvements to SymPy Mechanics
=======================================

Symbolic Solutions to Linear Equations
--------------------------------------

Kane's Method relies on solving three sets of linear equations:

1. putting the kinematical differential equations in explicit form
2. putting the dynamical differential equations in explicit form
3. solving the dependent generalized speeds in terms of the indepdent
  generalised speeds

If these equations are symbolic, it is impossible to determine a zero-pivot in
Gaussian elimination and the solutions can easily aquire divide-by-zero
operattions for ranges of numerical values for the variables involved.

There are two ways to deal with this 1) only do these solves numerically and 2)
ensure there are no zero-divisions with careful choice of algorthm or variable
choice. 1. is easy to manage if you set q' = u.

In ?2014?, we switched to using ``LUsolve()`` for all of these linear solves,
which resulted in divide-by-zero issues for complex problems. We introduced a
new solver that uses Cramer's method, which can eliinate divide-by-zero
operations in many situations. ``KanesMethod`` and ``Linearizer`` now support
selecting the linear solver, including the new Cramer solver. This allowed us
to fix a test that had been failing for almost 10 years.

.. code-block:: python

   A = MatrixSymbol('A', 4, 4)
   b = MatrixSymbol('b', 4, 2)
   x = Inverse(A) @ b
   result = x[0, 0] + x[1, 0] + x[2, 0] + x[3, 0]
   eval_x = lambdify((A, b), result)

We'd like lambdify to generate code that looks like:

.. code-block:: python

   def eval_x(A, b):
      x = numpy.linalg.solve(A, b)
      return x[0, 0] + x[1, 0] + x[2, 0] + x[3, 0]

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

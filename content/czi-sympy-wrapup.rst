=================================================
SymPy CZI Code Generation & Biomechanics Outcomes
=================================================

:date: 2023-09-28 00:00:00
:tags: sympy, czi, biomechanics
:category: news
:slug: sympy-czi-outcomes
:authors: Jason K. Moore, Sam Brockie
:summary: TODO

.. list-table::
   :class: borderless
   :width: 60%
   :align: center

   * - |czi-logo|
     - |sympy-logo|

.. |sympy-logo| image:: https://objects-us-east-1.dream.io/mechmotum/sympy-logo.png

.. |czi-logo| image:: https://objects-us-east-1.dream.io/mechmotum/czi-logo.png

.. contents::
   :local:
   :class: floatcon

Introduction
============

We were awarded a `two year grant`_ from CZI to improve SymPy_. There were
three themes associated with each of the three co-principal investigators:

- Improve SymPy's Documentation (Aaron Meuer, Quantsight)
- Improve SymPy's Performance (Oscar Benjamin, University of Bristol)
- Improve SymPy's Code Generation for Biomechanical Modeling (Jason K. Moore,
  Delft University of Technology)

.. _two year grant: https://doi.org/10.6084/m9.figshare.16590053.v1

We were in charge of the last one and hired Dr. Sam Brockie to work on the
project as a postdoctoral researcher. Jan Heinen and Timo Stienstra worked on
the project through their TU Delft MSc projects under the supervision of Sam
and Jason.

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
operations, making it a challenging system to differentiate and evaluate
efficiently. We want SymPy to be able to handle models of this and more
complexity with ease.  To test SymPy's ability to correctly derive,
differentiate, and evaluate the bicycle-rider's governing equations we choose
to formulate and solve an optimal control problem via direct collocation. We
beleived that the bicycle-rider optimal control problem would test SymPy's
limits, forcing us to make significant improvements to SymPy. To do this, we
worked on numerous areas in SymPy and downstream packages to reach this goal.

.. _SymPy: https://www.sympy.org

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
   :height: 200px

.. |joint2| image:: https://docs.sympy.org/dev/_images/PrismaticJoint.svg
   :height: 200px

.. |joint3| image:: https://docs.sympy.org/dev/_images/CylindricalJoint.svg
   :height: 200px

.. |joint4| image:: https://docs.sympy.org/dev/_images/PlanarJoint.svg
   :height: 200px

.. |joint5| image:: https://docs.sympy.org/dev/_images/SphericalJoint.svg
   :height: 200px

.. |joint6| image:: https://docs.sympy.org/dev/_images/WeldJoint.svg
   :height: 200px

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

- Cramer Solve: https://github.com/sympy/sympy/pull/25179

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

Pathways

An Actuator describes the equal and opposite pair of forces or torques.

System
------

SymPy Biomechanics
==================

We've developed a new sub-package sympy.physics.biomechanics_ that enables
including musculotendon force actuators in multibody dynamics models created
with ``sympy.physics.mechanics``. ``biomechanics`` contains these primary
modules:

- ``curve.py``: contains classes that represent mathmathical functional
  relationships between muscle-tendon length, velocity, and force.
- ``activation.py``: TODO
- ``musculotendon.py``: contains classes that represent complete musculatendon
  models with one example implementation

A full explanation of this package and the modules can be found in the new
`Introduction to Biomechanical Modeling
<https://docs.sympy.org/dev/tutorials/biomechanics/biomechanics.html>`_
tutorial. We demonstrate the package on a non-trivial system in the new
`Biomechanical Model Example
<https://docs.sympy.org/dev/tutorials/biomechanics/biomechanical-model-example.html>`_
tutorial.

.. figure:: https://docs.sympy.org/dev/_images/biomechanics-steerer.svg
   :align: center
   :width: 80%

   Muscle driven arm pushing and pulling a lever taken from the new tutorial.

.. _sympy.physics.biomechanics: https://docs.sympy.org/dev/modules/physics/biomechanics/index.html

Code Generation
===============

``lambdify()`` is the primary interface for converting SymPy expressions into
NumPy-backed Python functions for numerical evaluation. ``lamdify()`` has not
been able to code generate large mechanics' models in the past. We proposed
adding common subexpression elmination support to help with that. ``cse()``
support was added to ``lambdify()`` before we started the CZI work in
https://github.com/sympy/sympy/pull/21546. ``lambdify()`` was still quite slow
for our benchmark problems and Sam sped up lambdify's code generation by
disabling the docstring generation for large expressions in
https://github.com/sympy/sympy/pull/24754.

It is commonly needed to evaluate both a function and its Jacobian. SymPy is
capable of taking the analytical derivatives but it can be prohibitly slow for
large expressions. If common subexpressions are extracted from a SymPy
expression, all operations are represented as a directed acyclic graph. Taking
the derivative of a directed acyclic graph instead of a tree graph, as SymPy
stores expressions, can provide exponential speedups to differentiation. If the
code generation for the function and its Jacobian uses common subexpression
elinimation, then it makes sense to call ``cse()`` on the function, then take
the partial derivatives, and the Jacobian will be in a DAG form for easy code
generation. Sam has introduced a major code generation speed up for
lambdifying large SymPy expressions if you desire the Jacobian.

- forward_jacobian: https://github.com/sympy/sympy/pull/25801
- https://github.com/sympy/sympy/pull/24649
- https://github.com/sympy/sympy/pull/25797

Demonstration
=============

As explained in the introduction, our goal is to make SymPy capbale of deriving
very efficient neuromusular multibody models. A use case for these models is
solving `optimal control`_ problems, which benefit greatly from the fastest
numerical evaluation of the equations of motion and its higher order partial
derivatives. In particluar, forming a `nonlinear programming`_ problem using
direct collocation transcription from very large symbolic equations of motion
was already known to push SymPy's past its limits. In the past, we have
developed two software packages that transcribe and solve optimal control
problems based on SymPy expressions: opty_ and pycollo_.

.. _optimal control: https://en.wikipedia.org/wiki/Optimal_control
.. _nonlinear programming: https://en.wikipedia.org/wiki/Nonlinear_programming
.. _opty: https://github.com/csu-hmc/opty
.. _pycollo: https://github.com/brocksam/pycollo

Optimal Skateboard Ollie
-------------------------

As a first demonstration that SymPy can be used to solve research grade complex
optimal control problems, TU Delft MSc student Jan Heinen began working on
developing a model of a skateboarder performing an ollie, the fundamental
jumping trick in the sport. Jan used SymPy to formulate the equations of motion
of this biomechanical human-machine system and used pycollo to solve the
multi-phase trajectory optimization and parameter identification optimal
control problem.  Jan succeeded and produced an MSc thesis and a preprint that
is currently udner review at Sports Engineering:

- TU Delft MSc thesis: `Optimal Skateboard Geometry for Maximizing Ollie Height
  <http://resolver.tudelft.nl/uuid:61f4e969-8bd1-4687-9942-b70024b216dc>`_
- engrXiv preprint: `Maximizing Ollie Height by Optimizing Control Strategy and
  Skateboard Geometry Using Direct Collocation
  <https://doi.org/10.31224/3171>`_

This video shows the simulations of the problem solutions:

.. raw:: html

   <center>
   <iframe width="560" height="315"
   src="https://www.youtube.com/embed/jw5DmNnvD7c" title="YouTube video player"
   frameborder="0" allow="accelerometer; autoplay; clipboard-write;
   encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
   </center>

Following his MSc project, Jan contributed Sphinx documentation to the pycollo
project with the following pull requests:

- https://github.com/brocksam/pycollo/pull/80
- https://github.com/brocksam/pycollo/pull/82
- https://github.com/brocksam/pycollo/pull/84
- https://github.com/brocksam/pycollo/pull/85
- https://github.com/brocksam/pycollo/pull/87
- https://github.com/brocksam/pycollo/pull/88

BRiM
----

All of our prior bicycle-rider human-machine system models were one-off
derivations that were repurposed for each new model variation. These had
varying accessiblity for easy use by other users. Timo came up with the idea to
develop a software package that allows you to build bicycle-rider models from
modular elements, yet still retain a minimial coorindate derivation of the
equations of motion. His MSc thesis, "`BRiM: A Modular Bicycle-Rider Modeling
Framework
<http://resolver.tudelft.nl/uuid:a2b132e9-8d38-4553-8587-0c9e3341b202>`__",
details the design, implementation, and use of BRiM. We also wrote a paper,
"`BRiM: A Modular Bicycle-Rider Modeling Framework
<https://doi.org/10.59490/6504c5a765e8118fc7b106c3>`__", for the Bicycle and
Motorcycle Dynamics 2023 conference that gives a more concise overview of the
package as well as demonstrating easily swapping models for optimal control
results.

.. figure:: https://tjstienstra.github.io/brim/_images/lane_change.gif
   :align: center
   :width: 80%

   Lane change simulation created with BRiM showing without and without a rider

- BRiM source code: https://github.com/TJStienstra/brim/
- BRiM documentation: https://tjstienstra.github.io/brim/

Optimal Bicycle-Rider Trajectories
----------------------------------

With all of the above work, we were able to solve a muscle-driven optimal
control problem of the bicycle and rider. This is the problem we posed:

   Given a multibody model of the Carvallo-Whipple bicycle model extended with
   a rider that has muscle acutated movable arms and given a desired path on
   the ground, can we find muscle activations that cause the bicycle-rder to
   follow the path as closely as possible while minimizing the effort from the
   the representative bicep and tricep muscles?

The objective of this optimal control problem takes the form:

.. math::

   J = (1 - w)\int_{t_0}^{t_f} (x_s(t) - x_d(t))^2 dt + w\int_{t_0}^{t_f} e(t)^2 dt

where :math:`x_s` are a subset of the model's state trajectories and
:math:`x_d` are some desired trajectories and :math:`e` are the muscle
excittions.

Forming the constraints that represent the equations of motion (set of
differential algebraic equations) involves computing a very large sparse
Jacobian. When we first attempted this differentiation of the discretized
bicycle-rider model, SymPy bogged down on the Jacobian calculation. We let the
computation run for **over 3 hours** and killed the execution before the
Jacobian completed. SymPy's differentation is untenable for large equations of
motion.  Since we already cse the functions before code generation in opty, Sam
implemented a forward Jacobian on the cse'd expressions in:

https://github.com/csu-hmc/opty/pull/102

This allowed the equations to be differentiated and the differentiation occurs
in less that a few minutes, showing the drastic improvements such an approach
can have. With that improvement, we were able to solve the muscle driven
bicycle-rider path tracking problem with opty. Once this fix was applied we
could solve the trajectory optimization problem with opty_.

Other
=====

pytest pr

Lessons Learned
===============

- 6 months to negotiate a contract
- 6 months to hire someone

Conclusion
==========

We completed almost all of the goals set out in the original proposal along
with as many more unplanned outcomes. Primarliy we have improved SymPy such
that it can be used to solve non-trivial biomechanical optimal control
problems.

References
==========

.. [Meijaard2007] J. P. Meijaard, J. M. Papadopoulos, A. Ruina, and A. L.
   Schwab, “Linearized dynamics equations for the balance and steer of a
   bicycle: A benchmark and review,” Proceedings of the Royal Society A:
   Mathematical, Physical and Engineering Sciences, vol. 463, no. 2084, pp.
   1955–1982, Aug. 2007.
.. [BasuMandal2007] P. Basu-Mandal, A. Chatterjee, and J. M. Papadopoulos,
   "Hands-free circular motions of a benchmark bicycle," Proceedings of the
   Royal Society A: Mathematical, Physical and Engineering Sciences, vol. 463,
   no. 2084, pp. 1983–2003, Aug. 2007.

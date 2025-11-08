=======================================================
Biomechanical Optimization with SymPy 1.13 and Opty 1.3
=======================================================

:date: 2024-08-05 00:00:00
:tags: sympy, czi, biomechanics, multibody dynamics, open source software,
       muscles, optimal control, bicycle, code generation
:category: research
:authors: Jason K. Moore
:summary: SymPy 1.13 and Opty 1.3 can now be used for optimal control solutions
          of muscle-driven biomechanical simulation. This blog post shows of a
          solution to a muscle driven cycling time trial.
:thumbnail: https://objects-us-east-1.dream.io/mechmotum/one-legged-80m-power.png

`SymPy 1.13`_ was released on July 8, 2024. This release includes `all of the
work we did under the CZI Open Source Software for Science Cycle 4 grant
<{filename}/czi-sympy-wrapup.rst>`_. For example, SymPy now includes new features
for modeling biomechanical multibody systems. The new features include model
construction from joints via a system manager and force actuator classes
including a musculo-tendon model. At the close of the grant period, we
demonstrated how these features can be used in the solution of biomechanical
trajectory optimization and parameter estimation optimal control problems, but
only from development branches of the various intertwined software packages.
Today, we released `Opty 1.3`_ which can now be used alongside SymPy 1.13 to solve
biomechanical optimal control problems. Opty can now handle symbolic equations
of motion that have many millions of mathematical operations and tens of
thousands of constraints and optimization variables. To help grow adoption,
we've built out a new example gallery that demonstrates how Opty can be used to
solve a variety of problems:

.. figure:: https://objects-us-east-1.dream.io/mechmotum/opty-1.3-examples.png
   :align: center
   :target: https://opty.readthedocs.io/stable/examples/index.html

   Opty 1.3's new example gallery.

.. _SymPy 1.13: https://github.com/sympy/sympy/releases/tag/1.13.0
.. _Opty 1.3: https://github.com/csu-hmc/opty/releases/tag/v1.3.0

One example in the gallery, the "`One-Legged Cycling Time Trial
<https://opty.readthedocs.io/stable/examples/plot_one_legged_time_trial.html>`_",
shows how to find an optimal control solution of a musculo-tendon driven model
that makes use of SymPy 1.13's new biomechanics features. We developed this
example for an activity in TU Delft's 2024 Sports Engineering course to show
the students how models can be used to study how muscles play a role in optimal
performance. The example solves a minimum time cycling race using a model of a
single leg and simplified muscles that drive the leg motion to propel the
bicycle. The example in the gallery is set up with a short race distance but if
you bump the distance up to 80 meters the cyclist starts approaching terminal
velocity. Opty can find an optimal solution for the 17,000 variables in this
problem in about 10 minutes on an AMD Ryzen 5 2600X 12 core machine.

This produces a reasonably realistic overall motion which can be seen in the
cadence, resulting speed, and the power to accelerate and overcome rolling and
air resistance:

.. image:: https://objects-us-east-1.dream.io/mechmotum/one-legged-80m-power.png
   :align: center

There is no limit on the fatigue of the muscles so the optimizer finds a
bang-bang style coordination of the muscle excitations to power the leg and
push the muscles to their maximum force production:

.. figure:: https://objects-us-east-1.dream.io/mechmotum/one-legged-80m-muscle.png
   :align: center

   The four muscle forces, muscle lengths, and muscle excitations versus time
   during the 80 meter time trial with the minimum race time shown at the top.

This solution results in this overall pedaling motion:

.. raw:: html

   <center>
     <video controls>
       <source src="https://objects-us-east-1.dream.io/mechmotum/one-legged-80m.mp4" type="video/mp4">
     </video>
   </center>

Our next step is to incorporate muscles in our 3D nonlinear bicycle-rider
models to enable deeper understanding of how bicycles are balanced and
controlled. Opty can quickly find optimal trajectories of the joint torque
driven model, as shown in our `BRiM paper`_:

.. figure:: https://objects-us-east-1.dream.io/mechmotum/brim-paper-opty-example.png
   :align: center

   Torque driven Opty optimal control solution for the non-linear
   Carvallo-Whipple bicycle model.

.. _BRiM paper: https://doi.org/10.59490/660179a06bf1082286458109

Thanks to Timo, Sam, Peter, and all the SymPy developers for the contributions
that helped pull all this together! We hope that others can make use of these
models and tools for their own work.

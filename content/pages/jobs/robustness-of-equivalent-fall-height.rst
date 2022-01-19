==================================================================================
How Robust is Equivalent Fall Height for Predicting Injury Severity in Snow Jumps?
==================================================================================

:date: 2020-09-09
:status: hidden
:slug: jobs/msc/robustness-of-equivalent-fall-height
:template: msc-project

.. figure:: https://objects-us-east-1.dream.io/mechmotum/ski-figure-01.png
   :width: 600px
   :align: center

   Example snow jump with a constant equivalent fall height landing surface.

Description
===========

*Equivalent fall height* has been proposed as an important measure to minimize
in the design of safer ski and snowboard jumps [Hubbard2009]_. The equivalent
fall height is a proxy measure for the impact velocity of a human against a
surface. It provides better context for a layperson to perceive the associated
danger, i.e. people have a strong experiential sense of the danger associated
with falling from a given height. Jumps can be designed with a specified
equivalent fall height by simulating a particle model of a jumper [Levy2015]_.
These models seem simplistic but they are a useful because both the equivalent
fall height is such a dominant corollary to injury and it's predictive power is
robust to many other factors that can cause injury in a jump landing
[Hubbard2012]_. Nevertheless, there are naysayers to the idea that jumps should
be designed with a small equivalent fall height. One objection is that the
particle models do not capture enough of reality to be useful, see
[Shealy2010]_ & [Scher2015]_. The goal of this project would be to extend the
particle model to one or more rigid bodies which can have angular rotation and
tangential forces due to friction on the landing surface are considered.  Here
are some questions that could possibly be answered:

- Is equivalent fall height a robust measure of injury severity with respect to
  a rotating jumper? Or is a different measure necessary?
- How dangerous is the force to the skier in terms of the tangential and normal
  components?
- For what angular rotation and surface friction conditions is or isn't
  equivalent fall height a dominant cause of impact forces?
- How much curvature can safely be permitted in the takeoff ramp shape to
  prevent large tangential impact forces?
- Are there simple measures or criteria like the equivalent fall height for the
  particle model that can be used for jump design that considers the rotational
  affects of the jumper?
- Are there any reasons that equivalent fall height should not be lowered in
  jump designs with respect to rotating impacts?

Possible Approach
=================

- Literature review on foundational topics: human body collisions, ski jumping,
  measures of injury severity in falls & collisions, etc.
- Develop a simple rigid body model and show that it simulates reasonable
  free-rotating ski jump flight. See [Hubbard1989]_ for one such model.
- Exercise the simulation to find impact velocities and/or forces for differing
  initial conditions and landing surfaces.
- Expand the skijumpdesign library and web application [Moore2018]_ with any
  validated findings.

Required Skills
===============

- 2D rigid body dynamics and impact
- Simulation of rigid body dynamics
- Visualisation with Python based tools
- Web application (basic HTML/CSS and Dash)

References
==========

.. [Hubbard1989] M. Hubbard, R. L. Hibbard, M. R. Yeadon, and A. Komor, "A
   Multisegment Dynamic Model of Ski Jumping," Journal of Applied Biomechanics,
   vol. 5, no. 2, pp. 258–274, May 1989, doi: 10.1123/ijsb.5.2.258.
.. [Hubbard2009] M. Hubbard, "Safer Ski Jump Landing Surface Design Limits
   Normal Impact Velocity," Journal of ASTM International, vol. 6, no. 1, p.
   10, 2009, doi: 10.1520/STP47480S.
.. [Shealy2010] J. Shealy, I. Scher, L. Stepan, and E. Harley, "Jumper
   Kinematics on Terrain Park Jumps: Relationship between Takeoff Speed and
   Distance Traveled," Journal of ASTM International, vol. 7, no. 10, p. 10,
   Nov.  2010, doi: 10.1520/JAI102885.
.. [Hubbard2012] M. Hubbard and A. D. Swedberg, "Design of Terrain Park Jump Landing
   Surfaces for Constant Equivalent Fall Height Is Robust to ‘Uncontrollable’
   Factors," in Skiing Trauma and Safety: 19th Volume, R. J. Johnson, J. E.
   Shealy, R. M. Greenwald, and I. S. Scher, Eds. 100 Barr Harbor Drive, PO Box
   C700, West Conshohocken, PA 19428-2959: ASTM International, 2012, pp. 75–94.
.. [Levy2015] D. Levy, M. Hubbard, J. A. McNeil, and A. Swedberg, "A design
   rationale for safer terrain park jumps that limit equivalent fall height,"
   Sports Engineering, vol. 18, no. 4, pp. 227–239, Dec. 2015, doi:
   10.1007/s12283-015-0182-6.
.. [Scher2015] I. Scher, J. Shealy, L. Stepan, R. Thomas, and R. Hoover,
   "Terrain Park Jump Design: Would Limiting Equivalent Fall Height Reduce
   Spine Injuries?," in Skiing Trauma and Safety: 20th Volume, R. J. Johnson,
   J. E.  Shealy, and R. M. Greenwald, Eds. 100 Barr Harbor Drive, PO Box C700,
   West Conshohocken, PA 19428-2959: ASTM International, 2015, pp. 72–90.
.. [Moore2018] J. K. Moore and M. Hubbard, “skijumpdesign: A Ski Jump Design
   Tool for Specified Equivalent Fall Height,” The Journal of Open Source
   Software, vol. 3, no. 28, p. 818, Aug. 2018, doi: 10.21105/joss.00818.

See Also
========

- `Lab research page on ski jumps <https://mechmotum.github.io/research/ski-jump-safety.html>`_
- skijumpdesign web application: http://www.skijumpdesign.info

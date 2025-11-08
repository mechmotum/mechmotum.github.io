=======================================================
Validation of Ski & Snowboarding Low Impact Jump Design
=======================================================

:date: 2022-01-12
:status: hidden
:slug: jobs/msc/ski-jump-impact-model-validation
:template: msc-project

Description
===========

.. figure:: https://objects-us-east-1.dream.io/mechmotum/ski-figure-01.png
   :width: 600px
   :align: center

   Example snow jump with a constant equivalent fall height landing surface.

*Equivalent fall height* has been proposed as an important measure to minimize
for the design of safer ski and snowboard jumps [Hubbard2009]_. The equivalent
fall height is a proxy measure for the impact energy of a human against a
surface. It provides better context for a layperson to perceive the associated
danger, i.e. people have a strong experiential sense of the danger associated
with falling from a given height. Snow terrain park jump landing shapes can be
designed with a specified equivalent fall height by using a simulation of a
particle model of a jumper [Levy2015]_ and this model has been used to develop
jump design tools that minimize equivalent fall height [Moore2018]_.

Prinoth_ develops snow groomers that are used to build public use and
professional level terrain parks. They have computer aided design and
construction tools that allow jumps to be built at centimeter level precision.
The landing area of the jumps (the sweet spot) are designed to minimize impact
forces. The following video demonstrates the approach and capabilities:

.. raw:: html

   <center>
   <iframe width="560" height="315"
   src="https://www.youtube.com/embed/RH2xSkMs3JY" title="YouTube video player"
   frameborder="0" allow="accelerometer; autoplay; clipboard-write;
   encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
   </center>

The goal of this project will be to measure impact on a variety of terrain park
jumps using mobile sensor technologies and a selection of skiers and
snowboarders to validate the effectiveness of the low impact jump designs and
then transfer those findings into the simulation system.

This project will start as an internship where you will work with Prinoth
employees in Sterzing, Italy to collect impact data in real jumps and learn
about their design methodologies. You will be advised by Drs. Jason K. Moore
(TU Delft) and Mont Hubbard (UC Davis). This will be followed by an MSc
graduation project that focuses on impact data analysis and interpretation,
jumper model validation, and model improvement incorporation into the `ski jump
design web application <https://www.skijumpdesign.info>`_ and Prinoth's
simulation system.

The X camp terrain park is available to test on between August and October,
thus the internship will need to start in at least by July to prepare for data
collection in August.

More information on past research in on this topic can be found on the `ski
jump research page <{filename}/pages/research/ski-jump-safety.rst>`_.

.. _Prinoth: https://www.prinoth.com

References
==========

.. [Hubbard2009] M. Hubbard, "Safer Ski Jump Landing Surface Design Limits
   Normal Impact Velocity," Journal of ASTM International, vol. 6, no. 1, p.
   10, 2009, doi: 10.1520/STP47480S.
.. [Levy2015] D. Levy, M. Hubbard, J. A. McNeil, and A. Swedberg, "A design
   rationale for safer terrain park jumps that limit equivalent fall height,"
   Sports Engineering, vol. 18, no. 4, pp. 227–239, Dec. 2015, doi:
   10.1007/s12283-015-0182-6.
.. [Moore2018] J. K. Moore and M. Hubbard, “skijumpdesign: A Ski Jump Design
   Tool for Specified Equivalent Fall Height,” The Journal of Open Source
   Software, vol. 3, no. 28, p. 818, Aug. 2018, doi: 10.21105/joss.00818.

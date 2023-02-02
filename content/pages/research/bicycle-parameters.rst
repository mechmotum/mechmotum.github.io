===================================================================
Measurement and Estimation of Bicycle and Rider Physical Parameters
===================================================================

:status: hidden
:date: 2020-08
:collaborators: Mont Hubbard, Ronald Hess, Chris Dembia, Arend Schwab, Jodi
                Kooijman
:current_researchers: Julie van Vlerken
:past_researchers: Noah Sanders, Chris Dembia
:research_theme: Bicycle Engineering
:template: project
:slug: research/bicycle-rider-parameters
:summary-sentence: The purpose of this research is to establish methods for
                   measuring and estimating the physical parameters of bicycles
                   and bicycle riders necessary for simulating models of the
                   bicycle-rider system.
:summary-image: https://objects-us-east-1.dream.io/mechmotum/project-image-bicycle-rider-parameters.png

In [Moore2008]_ we developed and used a method for estimating the inertial
properties of the bicycle and rider given simple geometric measurements. The
rider method in [Moore2008]_ was formalized in [Moore2009]_ and combined with
more accurate measures and estimates of the bicycle's physical parameters based
on the methods used in [Kooijman2006]_. We presented estimates of the physical
parameters of several different styles of bicycles in [Moore2010]_ and compared
their resulting dynamics. Then in [Moore2012]_ the prior work was further
refined and included measurements of additional bicycles and a new method for
estimating the rider's inertial parameters. The generalized human inertia
estimation method used in [Moore2012]_ was published in [Dembia2015]_.  The
software [Moore2011]_ used for the computations has been developed over the
years and basic functionality is now available in a freely accessible web
application:

.. figure:: https://objects-us-east-1.dream.io/mechmotum/bicycle-dynamics-app.png
   :width: 800px
   :align: center
   :target: https://bicycle-dynamics.onrender.com

   Screenshot of the bicycle dynamics web app. Click the image to go to the app
   at https://bicycle-dynamics.onrender.com.

Funding
=======

This material is partially based upon work supported by the National Science
Foundation under `Grant No. 0928339
<http://www.nsf.gov/awardsearch/showAward?AWD_ID=0928339>`_. Any opinions,
findings, and conclusions or recommendations expressed in this material are
those of the authors and do not necessarily reflect the views of the National
Science Foundation.

References
==========

.. [Kooijman2006] J. D. G. Kooijman. Experimental validation of a model for the
   motion of an uncontrolled bicycle. Master’s thesis, Delft University of
   Technology, 2006.
.. [Moore2008] J. Moore and M. Hubbard, "Parametric Study of Bicycle
   Stability," in The Engineering of Sport 7, 2008, vol. 2,
   https://dx.doi.org/10.1007/978-2-287-99056-4_39.
.. [Moore2009] J. K. Moore, J. D. G. Kooijman, M. Hubbard, and A. L. Schwab, "A
   Method for Estimating Physical Properties of a Combined Bicycle and Rider,"
   presented at the ASME 2009 International Design Engineering Technical
   Conferences & Computers and Information in Engineering Conference, IDETC/CIE
   2009, San Diego, CA, USA, Aug. 2009, https://dx.doi.org/10.1115/DETC2009-86947.
.. [Moore2010] Jason K. Moore et al. An Accurate Method of Measuring and Comparing a
   Bicycle's Physical Parameters". In: Proceedings of Bicycle and Motorcycle
   Dynamics: Symposium on the Dynamics and Control of Single Track Vehicles.
   Delft, Netherlands, Oct. 2010.
.. [Moore2011] J. K. Moore, C. Dembia, O. Lee and N. Sanders,
   BicycleParameters: A Python library for bicycle parameter estimation and
   analysis. 2011. https://github.com/moorepants/BicycleParameters
.. [Moore2012] Jason K. Moore. Human Control of a Bicycle". PhD thesis. Davis,
   CA: University of California, Davis, Aug. 2012.
   http://moorepants.github.io/dissertation
.. [Dembia2015] C. Dembia, J. K. Moore, and M. Hubbard, "An object oriented
   implementation of the Yeadon human inertia model," F1000Research, vol. 3,
   no. 233, Apr. 2015, https://dx.doi.org/10.12688/f1000research.5292.2.

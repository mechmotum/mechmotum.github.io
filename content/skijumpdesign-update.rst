Ski Jump Design Software to Analyze User Inputted Jumps
=======================================================

:date: 2019-03-23 00:00:00
:tags: ski, sports, engineering, safety
:category: research
:slug: skijumpdesign-analysis
:authors: Bryn Cloud
:summary: Blog post on adding page to skijumpdesign app to analyze user inputted
          ski jumps for equivalent fall height.

Introduction
------------

The goal of this work is to add a new page to the `Ski Jump Design Tool`_
that allows users to input a measured jump profile and get a depiction of
the equivalent fall height (EFH) for their jump.Figure 1 illustrates the
components of a terrain park using common terminology.

.. figure:: https://objects-us-east-1.dream.io/mechmotum/bike-speed-control-01.jpg
   :width: 80%
   :align: center
   :alt: Ski Jump Terminology.

   *Figure 1. Components of standard terrain park jump.*

The software is designed for users with little to no technical background,
and guides the users through correct implementation.

Calculating Equivalent Fall Height
----------------------------------

The theory of equivalent fall height calculations has been discussed by [Levy]_.
EFH can be expressed as follows:

.. math::

    h = \frac{v_j^2sin^2(\theta_J - \theta_L)}{2g}

where :math:`$v_j$` is the jumper's landing speed, :math:`$\theta_J$` is the jumper's
landing angle, :math:`$\theta_L$` is the slope angle and :math:`$g$` is gravity.
This calculation was added to the skijumpdesign software to evaluate the EFH of any surface.
A takeoff angle, skier instance, and a takeoff point relative to the surface are
user inputs to the function. Then, the function uses these inputs to find the skier
impact velocity at each point along the surface and extracts the skier's landing speed
and landing angle. The slope angle is calculated using the slope along the surface.

Measuring A Jump's Profile
--------------------------

A jump has been measured using the three following methods.

1. Use a tape measure and level to find the surface distance and angle at defined points
   along the jump. Then, input the values into the J. A. McNeil Excel Jump Tool.
#. Mount a high precision differential GPS to a snowboard and slowly walk the snowboard
   along the jump.
#. Mount a differential GPS on a helmet and have a skier ski along the jump as slowly as
   possible.

We spent time this quarter testing the latter at Sierra at Tahoe ski resort. The skier
went down four different jumps while the recorder was with the base station left at the
bottom of the resort. We found that the differential GPS can accurately measure at a range
of over 1000 meters. This data showed promise for this jump profiling method. Figure 2
shows me (the skier) with the differential GPS ski helmet.

.. figure:: https://objects-us-east-1.dream.io/mechmotum/bike-speed-control-01.jpg
   :width: 50%
   :align: center
   :alt: Differential GPS Skier Helmet.

   *Figure 2. A differential GPS mounted to a helmet for testing at Sierra at Tahoe.*

Ski Jump Application Update
---------------------------

The new version of the ski jump web application has not launched yet, but a lot of progress
was made. A home page was added to keep it user friendly. This is shown below.

.. figure:: https://objects-us-east-1.dream.io/mechmotum/bike-speed-control-01.jpg
   :width: 50%
   :align: center
   :alt: Differential GPS Skier Helmet.

   *Figure 3. New Ski Jump Web Application (Work in Progress) - Home Page.*

The buttons centered in the middle of this page will direct users to the ski jump design
or the new analysis page shown in Figure 4.

.. figure:: https://objects-us-east-1.dream.io/mechmotum/bike-speed-control-01.jpg
   :width: 50%
   :align: center
   :alt: Differential GPS Skier Helmet.

   *Figure 4. New Ski Jump Web Application (Work in Progress) - Analysis Page.*

Here the user can upload their csv or excel file with the distance and height coordinates
of their jump. Then the user specifies the takeoff point and takeoff angle of the jump. An
example of a jump built using a jump designed with a takeoff angle of 25 degrees and
maximum equivalent fall height of 0.5 m was input into the app and is shown in Figure 5 below.

.. figure:: https://objects-us-east-1.dream.io/mechmotum/bike-speed-control-01.jpg
   :width: 50%
   :align: center
   :alt: Differential GPS Skier Helmet.

   *Figure 5. Analysis Page with a 0.5 m Constant Equivalent Fall Height.*

The user can see the jump profile, EFH value, and maximum and recommended EFH values.
The calculation shows a constant EFH value of 0.5 m until it reaches the landing transition
surface. At this point, the ski jump design app limits the acceleration felt by the skier instead,
and is the reason for the spike in EFH.

This version is not deployed yet as there is work to be done to speed up the EFH calculation,
limit user error, and make the web application stable.

If you'd like to check out the deployed version of the web app, click the image below:

.. image:: https://objects-us-east-1.dream.io/mechmotum.github.io/skijumpdesign-screenshot.jpg
   :width: 50%
   :align: center
   :target: http://www.skijumpdesign.info
   :alt: Screenshot of the application.

Conclusion
----------

A function was added to the skijumpdesign software to calculate the equivalent fall height of a
surface. A differential GPS mounted on a skier's helmet is a promising way to measure a jump profile
becuase it is portable and efficient. The ski jump web application has expanded to showcase three
pages: a home page, design page, and analysis page. Further work is needed to speed up the
calculations, determine the best methods for users to measure a jump, and make the new web app user
friendly.

Other related information:

- Web application: http://www.skijumpdesign.info
- Software repository: https://gitlab.com/moorepants/skijumpdesign
- Software documentation: http://skijumpdesign.readthedocs.io

.. _Ski Jump Design Tool: http://www.skijumpdesign.info


References
----------

.. [Levy] Levy, D., Hubbard, M., McNeil, J.A. et al. Sports Eng (2015) 18: 227.
   https://doi.org/10.1007/s12283-015-0182-6

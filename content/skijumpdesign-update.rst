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
software that allows users to input a measured jump profile and get a
depiction of the equivalent fall height (EFH) for their jump.

Figure 1 illustrates the components of a terrain park using common
terminology.

.. figure:: https://objects-us-east-1.dream.io/mechmotum/bike-speed-control-01.jpg
   :width: 80%
   :align: center
   :alt: Ski Jump Terminology.

   *Figure 1. Components of standard terrain park jump.*

The software is designed for users with little to no technical background,
and guides the users through correct implementation.

Calculating Equivalent Fall Height
----------------------------------

The theory of equivalent fall height calculations has been discussed by [Moore]_.
EFH can be expressed as follows:

.. math::

    h = \frac{v_j^2sin^2(\theta_J - \theta_L)}{2g}

where v_j is the jumper's landing speed, theta_j is the jumper's landing
angle, theta_l is the landing surface and g is gravity.


If you'd like to check out the web app, click the image below:

.. image:: https://objects-us-east-1.dream.io/mechmotum.github.io/skijumpdesign-screenshot.jpg
   :width: 50%
   :align: center
   :target: http://www.skijumpdesign.info
   :alt: Screenshot of the application.

Other related information:

- Web application: http://www.skijumpdesign.info
- Software repository: https://gitlab.com/moorepants/skijumpdesign
- Software documentation: http://skijumpdesign.readthedocs.io

.. _Ski Jump Design Tool: http://www.skijumpdesign.info


References
----------

.. [Moore] Moore, J. (2012). Human Control of a Bicycle.
   Available at: http://moorepants.github.io/dissertation/davisbicycle.html
   [Accessed 12 Dec. 2018].
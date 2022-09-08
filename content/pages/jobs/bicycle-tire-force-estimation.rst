====================================================================
Estimation of Bicycle Tire Contact Patch Forces Using Simple Sensors
====================================================================

:date: 2022-09-08
:status: hidden
:slug: jobs/msc/bicycle-tire-force-estimation
:template: msc-project

.. figure:: https://upload.wikimedia.org/wikipedia/commons/f/fa/Tire_coordinate_system.png
   :align: center

   Free body diagram of bicycle tire forces. AndrewDressel, `CC BY-SA 4.0
   <https://creativecommons.org/licenses/by-sa/4.0>`_, via Wikimedia Commons

The force between a bicycle tire and the road is difficult to measure and
predict. If we were able to accurately estimate these force in real-time from
simple inexpensive sensors, such as inertial measurement units, we could use
these force estimates to drastically improve traction control systems for
robotically augmented bicycles, scooters, and motorcycles. The challenge of
this project is to develop a computational method that accurately estimates the
tire forces (magnitude and direction) at each wheels' contact patch using a
minimal set of inexpensive and unobtrusive sensors. A solution is likely to
involve an inverse dynamics model of a bicycle, signal processing, filtering
and estimation, experimental validation, and/or (physics informed) machine
learning.

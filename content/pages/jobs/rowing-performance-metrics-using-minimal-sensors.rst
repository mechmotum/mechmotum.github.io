=======================================================================================================
Maximizing Quantity and Quality of Rowing Performance Metrics From a Minimal Number of Inertial Sensors
=======================================================================================================

:date: 2020-09-09
:status: hidden
:slug: jobs/msc/rowing-performance-metrics-using-minimal-sensors
:template: msc-project

.. figure:: https://mechmotum.s3.us-east-005.dream.io/experimental-boat.jpg
   :width: 600px
   :align: center

   US Olympic rower Seth Weil rowing an instrumented single scull.

Most everyone carries a smartphone each of which have an evolving array of
sensors capable of measuring aspects of the phone's dynamic state. The GPS,
accelerometer, rate gyroscopes, and magnetometer sensors are particularly
useful for predicting the orientation and position of the phone. Smartphones
are being used in innovative ways across sports to monitor and assess the
performance of athletes. In competitive rowing smartphones can possibly be used
to provide more useful performance metrics than the currently used speed
measurement devices. We have shown that smartphone data can be used to improve
speed and distance per stroke estimates [Cloud2019]_ but much more may be able
to be gleaned by 1) collecting data from smartphones attached to the oars,
rower, and seat, 2) collecting data using multiple smartphones simultaneously,
and 3) using more advanced filtering algorithms. We have preliminary data
available that can be used to further improve the quality and quantity of
performance metrics that are important to rowers.

The goals of this project will be tied to answering at least some or more of
the following questions:

- What rowing performance metrics can possibly be estimated from limited
  numbers of smartphones placed on the boat, seat, rower, and/or oars?
- What are the minimal number of smartphones and optimal mounting locations to
  reasonably estimate specific metrics?
- How accurate can the estimated performance metrics be given limited data (few
  phones, poor data) and carefully designed filtering algorithms?
- What sensor fusion algorithms are best suited for the available data?
- How can the kinematics and dynamics of the rower-boat system be used to
  improve the filter estimates?
- How can you minimize the need for calibration and end user complications in
  mounting the smartphones?

Skills
======

- 3D multibody kinematics and dynamics
- Data analytics of inertial sensor and GIS time series
- Software engineering (existing tools are written in Python)

References
==========

.. [Cloud2019] Cloud B, Tarien B, Liu A, Shedd T, Lin X, Hubbard M, et al.
   (2019) Adaptive smartphone-based sensor fusion for estimating competitive
   rowing kinematic metrics. PLoS ONE 14(12): e0225690.
   https://doi.org/10.1371/journal.pone.0225690

See Also
========

- `Lab web page on rowing <https://mechmotum.github.io/research/rowing-performance.html>`_

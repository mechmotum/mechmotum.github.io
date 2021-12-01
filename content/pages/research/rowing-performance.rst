====================================================
Estimation of Rower Kinematics in Competitive Rowing
====================================================

:collaborators: Mont Hubbard, Paul Crawford, Xinfan Lin, Seth Weil
:current_researchers:
:date: 2019-12-05
:past_researchers: Bryn Cloud, Britt Tarien, Thomas Shedd, Ada Liu, Li Wang
:research_theme: Sports Engineering
:status: hidden
:template: project
:summary-sentence: Real-time feedback of stroke-by-stroke rowing performance
                   metrics can enable data driven training and coaching.
                   Instrumenting rowers during training and competition with
                   laboratory quality sensing is very difficult, but the
                   ubiquity of smartphones provides an avenue to collect fewer
                   and less accurate kinematic and kinetic measurements. This
                   project aims to improve performance critical biomechanic
                   rowing metrics through dynamics informed estimation
                   algorithms. We have developed rower adaptive filtering
                   methods to predict global boat position, speed, stroke rate,
                   and distance per stroke at high accuracy and with
                   experimental protocols for validating the estimations.
:summary-image: https://objects-us-east-1.dream.io/mechmotum/project-image-row.png
:slug: research/rowing-performance

Description
===========

The purpose of this project was to develop methods to estimate important rowing
performance metrics using data collected from sensors in a smartphone: rate
gyros, accelerometers, magnetometer, and GPS. We simultaneously collected data
during typical single scull rowing from smartphones attached to the boat and a
differential GPS antennae. We showed that "distance per stroke" estimates could
be improved with the use of either a complementary filter or Kalman filter with
mean errors dropping to around 0.5 meter or less using the filters. The
accuracy and frequency of the GPS measurements from the smartphone is the
primary factor preventing these estimates from being closer to 5 centimeters; a
threshold to make the estimates useful for analyzing performance on a
stroke-by-stroke basis. More advanced filters might improve the estimates, but
improvements in smartphone sensors and the associated GPS network might be the
best way to obtain desirable estimates. `The results were published in PLoS One
in 2019 <https://doi.org/10.1371/journal.pone.0225690>`_. The abstract reads:

   Competitive rowing highly values boat position and velocity data for
   real-time feedback during training, racing and post-training analysis. The
   ubiquity of smartphones with embedded position (GPS) and motion
   (accelerometer) sensors motivates their possible use in these tasks. In this
   paper, we investigate the use of two real-time digital filters to achieve
   highly accurate yet reasonably priced measurements of boat speed and
   distance traveled. Both filters combine acceleration and location data to
   estimate boat distance and speed; the first using a complementary frequency
   response-based filter technique, the second with a Kalman filter formalism
   that includes adaptive, real-time estimates of effective accelerometer bias.
   The estimates of distance and speed from both filters were validated and
   compared with accurate reference data from a differential GPS system with
   better than 1 cm precision and a 5 Hz update rate, in experiments using two
   subjects (an experienced club-level rower and an elite rower) in two
   different boats on a 300 m course. Compared with single channel (smartphone
   GPS only) measures of distance and speed, the complementary filter improved
   the accuracy and precision of boat speed, boat distance traveled, and
   distance per stroke by 44%, 42%, and 73%, respectively, while the Kalman
   filter improved the accuracy and precision of boat speed, boat distance
   traveled, and distance per stroke by 48%, 22%, and 82%, respectively. Both
   filters demonstrate promise as general purpose methods to substantially
   improve estimates of important rowing performance metrics.

Associated Research Products
============================

- Journal article: Cloud B, Tarien B, Liu A, Shedd T, Lin X, Hubbard M, et al.
  (2019) Adaptive smartphone-based sensor fusion for estimating competitive
  rowing kinematic metrics. PLoS ONE 14(12): e0225690.
  https://doi.org/10.1371/journal.pone.0225690
- Preprint article: https://engrxiv.org/nykuh/
- Software repository: https://gitlab.com/mechmotum/row_filter
- Software archive: http://doi.org/10.5281/zenodo.3378965
- Data: https://doi.org/10.6084/m9.figshare.7963643.v2
- Blog posts:

  - `Estimating Competition Rowing Metrics <{filename}/estimating-rowing-metrics.rst>`_
  - `Rowing Performance Estimation Paper Published <{filename}/rowing-estimation-paper-published.rst>`_
  - `Laboratorium Represented at the UC Davis Undergraduate Research Conference <urc-2019.rst>`_

Media
=====

.. figure:: https://objects-us-east-1.dream.io/mechmotum/experimental-boat.jpg
   :width: 80%
   :alt: Experimental setup of the scull.
   :align: center

   Seth Weil during his trials with annotations indicating the equipment on the
   boat.

.. raw:: html

   <iframe width="560" height="315"
   src="https://www.youtube.com/embed/yL8U_8ALjHc" frameborder="0"
   allow="accelerometer; autoplay; encrypted-media; gyroscope;
   picture-in-picture" allowfullscreen></iframe>

A video of the club-level rower during the data collection:

.. figure:: https://objects-us-east-1.dream.io/mechmotum/dist-per-stroke-summary.png
   :width: 80%
   :alt: Final results plot for the distance per stroke estimates.
   :align: center

   Final results showing the improvements in the distance per stroke estimates
   for the complementary filter (CF) and Kalman filter (KF) as compared to the
   estimates from the raw smartphone data (SP).

.. figure:: https://objects-us-east-1.dream.io/mechmotum/row-research-team.png
   :width: 80%
   :alt: Rowing performance estimation project team.
   :align: center

   Research team members Li Wang, Ada Liu, Thomas Shedd, Paul Crawford, Britt
   Tarien, and Bryn Cloud

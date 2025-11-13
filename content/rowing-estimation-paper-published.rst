Rowing Performance Estimation Paper Published
=============================================

:date: 2019-12-30 21:00:00
:tags: rowing, sports, engineering, estimation, kalman filter
:category: papers
:slug: rowing-estimation-paper-published
:authors: Jason K. Moore
:summary: Our 2019 rowing performance estimation paper is now published in Plos
          One.
:thumbnail: https://mechmotum.s3.us-east-005.dream.io/row-plos-screenshot.png

We've been working on this project and paper for two years and it was finally
published in Plos One on December 5, 2019. The citation is:

   Cloud B, Tarien B, Liu A, Shedd T, Lin X, Hubbard M, et al. (2019) Adaptive
   smartphone-based sensor fusion for estimating competitive rowing kinematic
   metrics. PLoS ONE 14(12): e0225690. https://doi.org/10.1371/journal.pone.0225690

.. image:: https://mechmotum.s3.us-east-005.dream.io/row-plos-screenshot.png
   :width: 80%
   :alt: Screenshot of the Plos One paper.
   :align: center
   :target: https://doi.org/10.1371/journal.pone.0225690

The abstract reads:

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

Congratulations to everyone involved in making this happen! We hope this work
helps others progress in sports performance estimation and other related
topics.

.. figure:: https://mechmotum.s3.us-east-005.dream.io/row-research-team.png
   :width: 80%
   :alt: Rowing performance estimation project team.
   :align: center

   Research team members Li Wang, Ada Liu, Thomas Shedd, Paul Crawford, Britt
   Tarien, and Bryn Cloud

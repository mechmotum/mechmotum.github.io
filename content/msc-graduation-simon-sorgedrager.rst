=====================================================
Simon Sorgedrager Successfully Defends His MSc Thesis
=====================================================

:date: 2025-05-29 10:17:00
:tags: bicycle, optimization, rider, countersteer
:category: news
:authors: Jason K. Moore
:thumbnail: https://mechmotum.s3.us-east-005.dream.io/thesis-cover-sorgedrager.png

.. list-table::
   :class: borderless
   :width: 60%
   :align: center

   * - |headshot|
     - |cover|

.. |headshot| image:: https://mechmotum.s3.us-east-005.dream.io/headshot-sorgedrager-simon.jpg
   :height: 400px

.. |cover| image:: https://mechmotum.s3.us-east-005.dream.io/thesis-cover-sorgedrager-w400.png
   :height: 400px
   :target: https://resolver.tudelft.nl/uuid:092f3b70-2d97-436e-b193-139a593e09c7

Simon Sorgedgrager successfully defended his MSc thesis titled `Riding a
Bicycle Without Hands: How To Do It and the Bicycle Dynamics Behind It
<https://resolver.tudelft.nl/uuid:ee22c5d1-b27f-4542-8a49-71d92a9e2f55>`_ on
April 25, 2025. Simon created variations of bicycle rider upper-body models for
use in the study of controlling the non-linear Carvallo-Whipple bicycle model.
In particular, he developed a model of the rider's seat-butt connection that
imposes a configuration constraint that better mimics the motion we have
observed in no-hands riding. He also developed a triple pendulum model that
includes motion of the head. He then solved optimal path tracking problems to
find solutions for making lane changes, 90 degree turns, and staying on a
straight path when subject to wind. He discovered several new and interesting
things through these optimal control solutions:

- The rider uses less control energy to make a lane change with the new seat
  joint than typical pin joint pendulum models. This implies that the strategy
  of shifting the seat laterally under your butt is a more effective way to
  manipulate the roll angle of the bicycle.
- When subjected to lateral wind forces, the rider leans into the wind to
  maintain a straight path.
- A rider can make a turn **without countersteering** with carefully
  coordinated upper body contortions.

Simon developed all of the models with `SymBRiM
<https://github.com/mechmotum/symbrim>`_ and solved the optimal control
problems with `opty <https://github.com/csu-hmc/opty>`_. Simon's code is found
at https://github.com/mechmotum/no-hands-riding.

The following animations show the rider model variations performing a lane
change:

.. |single| image:: https://mechmotum.s3.us-east-005.dream.io/simon-single-pendulum-lange-change.gif
   :width: 300px

.. |sliding| image:: https://mechmotum.s3.us-east-005.dream.io/simon-single-pendulum-with-sliding-lane-change.gif
   :width: 300px

.. |triple| image:: https://mechmotum.s3.us-east-005.dream.io/simon-triple-pendulum-lane-change.gif
   :width: 300px

.. list-table::
   :class: borderless
   :align: center
   :width: 100%

   * - |single|
       Classic single pendulum upper body rider model performing a lane change.
     - |sliding|
       New single pendulum with laterally sliding seat-butt model performing a lane change.
     - |triple|
       New triple pendulum with laterally sliding seat-butt model performing a
       lane change.

|
|

The following videos show the comparison of turning with and without
countersteering:

.. |countersteering| image:: https://mechmotum.s3.us-east-005.dream.io/simon-countersteering.gif

.. |no-countersteering| image:: https://mechmotum.s3.us-east-005.dream.io/simon-no-countersteering.gif

.. list-table::
   :class: borderless
   :align: center
   :width: 100%

   * - |countersteering|
       Triple pendulum model performing a turn with countersteering.
     - |no-countersteering|
       Triple pendulum model performing a turn **without countersteering**.

Simon was co-supervised by Jason K. Moore and José Farías. Everyone at the
bicycle lab is very proud of Simon and wishes him the best in his next
adventures.

==============================================
Yuke Huang Successfully Defends Her MSc Thesis
==============================================

:date: 2026-03-19 14:39:00
:tags: cycling, behavior, overtake, mpc, optimal control
:category: news
:authors: Jason K. Moore
:thumbnail: https://mechmotum.s3.us-east-005.dream.io/thesis-cover-huang.png

.. list-table::
   :class: borderless
   :width: 60%
   :align: center

   * - |headshot|
     - |cover|

.. |cover| image:: https://mechmotum.s3.us-east-005.dream.io/thesis-cover-huang.png
   :height: 400px
   :target: https://resolver.tudelft.nl/uuid:7fcb3081-32e6-42a6-8fed-219bc6398e9b

.. |headshot| image:: https://mechmotum.s3.us-east-005.dream.io/headshot-huang-yuke.png
   :height: 400px

Yuke Huang successfully defended her MSc Thesis titled `Adaptive-Horizon Model
Predictive Control for Modeling Anticipative Behavior in Cyclist Interaction
<https://resolver.tudelft.nl/uuid:7fcb3081-32e6-42a6-8fed-219bc6398e9b>`_ on
March 18, 2026.

Yuke developed a cyclist navigation controller representing the cyclist's
heading control loop using adaptive-horizon model predictive control. This
adaptive-horizon element was introduced to capture a hypothesized change in
reactive behavior when closer or further to another cyclist. She extracted
pairwise cyclist overtaking data from a public dataset of cyclists in a German
city and formulated an optimal control cost function that took into account
following a desired path, maintaining speed, avoiding collision with the other
cyclist, and minimizing large motions and control inputs. She calibrated the
model on the data with Bayesian optimization first assuming a constant MPC
horizon and then showing that more realistic simulated motion occurs if the
horizon is variable throughout the overtaking maneuver, supporting the
hypothesis that we shorten our internal planning horizon when closer to
obstacles. She showed that we have a minimum horizon and that we use that
minimum when closest to the other cyclist.

.. figure:: https://mechmotum.s3.us-east-005.dream.io/huang-example-figure.png
   :width: 800px
   :align: center

   Example result of simulating an overtaking maneuver with a constant horizon
   and adaptive horizon MPC controller, showing the adaptive controller better
   simualtes the cyclist's behavior.

Yuke was supervised by Christoph Konrad, Azita Dabiri, and Jason K. Moore with
help from Riender Happee. Everyone at the bicycle lab is very proud of Yuke and
wishes her the best with her upcoming PhD position in Eindhoven.

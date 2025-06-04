===================================================
Sara Youngblood Successfully Defends Her MSc Thesis
===================================================

:date: 2025-06-04 10:55:00
:tags: bicycle, control, slip, tire, ice
:category: news
:authors: Jason K. Moore
:thumbnail: https://objects-us-east-1.dream.io/mechmotum/thesis-cover-youngblood-w240.png

.. |headshot| image:: https://objects-us-east-1.dream.io/mechmotum/headshot-youngblood-sara.png
   :height: 400px

.. |cover| image:: https://objects-us-east-1.dream.io/mechmotum/thesis-cover-youngblood.png
   :height: 400px
   :target: https://resolver.tudelft.nl/uuid:2109f294-ddba-4849-934b-9ce5cef15ec3

.. list-table::
   :class: borderless
   :width: 60%
   :align: center

   *  - |cover|
      - |headshot|

Sara Youngblood successfully defended her MSc thesis titled `Engineering
Bicycle Stability: A Study of Control Strategies for Crash Prevention on Icy
and Normal Terrain
<https://resolver.tudelft.nl/uuid:2109f294-ddba-4849-934b-9ce5cef15ec3>`_.

Sara developed a pair of non-linear bicycle models, one without lateral tire
slip and another with tire slip. In the tire slip model, she generated the tire
forces using a relationship that was linear in the +/- 6 degree slip angle
range and saturated outside of that range. She setup both models to simulate
steady turns at various speeds with PD control and introduced an abrupt change
in the tire friction characteristics to simulate hitting an ice patch in the
slip model. To mitigate the ice patch, she introduced an LQR controller using
roll motion feedback that engaged only when large slip angles were detected.
The controller was able to keep the bicycle in a stable state for steady turns
with roll angles of up to 10 degrees. Her work demonstrates the possibility of
active bicycle traction control in mitigating falls caused by reduced friction
between the tire and the ground.

The following animations show the controller in action:

.. |slip-no-slip| image:: https://objects-us-east-1.dream.io/mechmotum/bicycle-ice-vs-normal.gif
   :width: 300px

.. |ice| image::
   https://objects-us-east-1.dream.io/mechmotum/bicycle-ice-both-wheels-highlighted.gif
   :width: 300px

.. |lqr-pd| image:: https://objects-us-east-1.dream.io/mechmotum/bicycle-lqr-vs-pd-with-path-highlight.gif
   :width: 300px

.. list-table::
   :class: borderless
   :align: center
   :width: 100%

   * - |slip-no-slip|
       Comparison of the no-slip bicycle motion to that of the model with tire
       slip on ice.
     - |ice|
       Simulation of the tire slip model falling on ice.
     - |lqr-pd|
       Simulations of the tire slip model controlled by roll motion feedback
       with manually selected gains and LQR generated gains.

Sara was co-supervised by Jason K. Moore and Benjamin González. Everyone at the
bicycle lab is very proud of Sara and wishes her the best in her next
adventures.

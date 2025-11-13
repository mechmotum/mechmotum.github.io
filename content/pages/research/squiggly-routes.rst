=======================
Squiggly Bicycle Routes
=======================

:status: hidden
:date: 2024-10-16
:collaborators: Ted Beuhler, Mont Hubbard
:current_researchers:
:past_researchers: Sietse Soethout
:research_theme: Bicycle Engineering
:template: project
:summary-sentence: We have developed a simulation model that predicts travel
                   time and energy costs for a bicyclist traveling over an
                   arbitrary route accounting for elevation changes, bicycle
                   type, rider physiology, traffic signals, and yielding.
:summary-image: https://mechmotum.s3.us-east-005.dream.io/squiggly-400x400.png
:slug: research/squiggly-routes

.. figure:: https://mechmotum.s3.us-east-005.dream.io/direct-vs-squiggly.png
   :width: 600px
   :align: center

   Direct and squiggly routes have time and energy costs for bicyclists.

Description
===========

Bicyclists choose routes at least partially based on the travel time and the
energy required to traverse the route [Winters2010]_. Grade changes, wind, stop
signs, traffic signal timing, rough pavement, undulations, etc. all contribute
to the time and energy costs [Broach2012]_. Urban planners and civil engineers
design infrastructure and routes for bicyclists that have specific time and
energy costs associated with them. In fact, automobile routes and
infrastructure often have more preferable time and energy costs than the
parallel bicycle routes and infrastructure. These bicycle routes are quite
squiggly and are not optimizing the convenience of the bicyclists over the
automobile drive. Using simple physics-based simulations, existing and future
routes and infrastructure designs can be evaluated for time and energy costs.
This puts a clear quantitative numbers to important aspects of the convenience
of bicycling.

Products
========

Theses

- S. S. Soethout, "A dynamic utility cycling model for energy and time
  expenditure calculation of a population of cyclists," Delft University of
  Technology, Delft, The Netherlands, 2024.
  https://resolver.tudelft.nl/uuid:ae45c43e-8eb1-4256-b7c2-e290f1260def

Presentations

- `2019 Squiggly Routes COSMOS Workshop Slides <https://tinyurl.com/squiggly-cosmos2019>`_
- `2012 Velocity Presentation Slides
  <https://docs.google.com/presentation/d/e/2PACX-1vQtgEHSrHu0HobIaReFllvckTnCiYCkpZS-kqQx5jhJXQu3nz907JDoO3UGckoiT5_1nAFsW6K0fEtq/pub?start=false&loop=false&delayms=3000>`_

Software

- Software from the 2012 work: https://github.com/moorepants/EfficientRoutes

Media
=====

The following video shows a single simulation along a route in The Hague, The
Netherlands:

.. raw:: html

   <center>
   <video width="800px" controls>
     <source src="https://mechmotum.s3.us-east-005.dream.io/hs_noi_tunnel_single.mp4" type="video/mp4">
     Your browser does not support the video tag.
   </video>
   </center>

The next video shows a population of cyclists riding the route:

.. raw:: html

   <center>
   <video width="800px" controls>
     <source src="https://mechmotum.s3.us-east-005.dream.io/all_animation_hs_noi_normal_all_fast.mp4" type="video/mp4">
     Your browser does not support the video tag.
   </video>
   </center>

References
==========

.. [Winters2010] M. Winters, K. Teschke, M. Grant, E. M. Setton, and M. Brauer,
   "How Far Out of the Way Will We Travel?: Built Environment Influences on
   Route Selection for Bicycle and Car Travel," Transportation Research Record:
   Journal of the Transportation Research Board, vol. 2190, no. 1, pp. 1–10,
   Jan. 2010, doi: 10.3141/2190-01.
.. [Broach2012] J. Broach, J. Dill, and J. Gliebe, "Where do cyclists ride? A
   route choice model developed with revealed preference GPS data,"
   Transportation Research Part A: Policy and Practice, vol. 46, no. 10, pp.
   1730–1740, Dec. 2012, doi: 10.1016/j.tra.2012.07.005.

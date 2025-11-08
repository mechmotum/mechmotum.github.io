=======================
Squiggly Bicycle Routes
=======================

:date: 2020-09-10
:status: hidden
:slug: jobs/msc/squiggly-routes
:template: msc-project

.. figure:: https://objects-us-east-1.dream.io/mechmotum/direct-vs-squiggly.png
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

The goal of this project is to 1) develop a realistic yet simple simulation of
a bicyclist traversing a route that considers all major influences to time and
energy costs of the rider, 2) evaluate several case studies using the
simulation and demonstrate how route designs can be improved with minor changes
to designed elements, 3) propose simple guidelines for planners, and 4) develop
an open source web application that allows planners to evaluate routes with
respect to time and energy costs.

Proposed Approach
=================

- Review the transportation literature for related research (time costs, energy
  costs, bicyclist convenience, route & infrastructure design, standards & codes)
- Develop a 2D mathematical and computational simulation model that can
  realistically traverse routes.
- Find or collect route data based on existing routes, automobile routes, and
  design plans.
- Evaluate the routes and interpret the results.
- Propose simple design guidelines based on the results that will generally
  help lower time and energy costs.
- Develop a web application that accepts route information, simulates the
  route, and presents the resulting time and energy costs.

Required Skills
===============

- Modeling 2D dynamics
- GIS for transportation
- Simulation of vehicle dynamics
- Web application development

References
==========

.. [Fajans2001] J. Fajans and M. E. Curry, "Why Bicyclists Hate Stop Signs,"
   no. 18, p. 2, 2001.
.. [Winters2010] M. Winters, K. Teschke, M. Grant, E. M. Setton, and M. Brauer,
   "How Far Out of the Way Will We Travel?: Built Environment Influences on
   Route Selection for Bicycle and Car Travel," Transportation Research Record:
   Journal of the Transportation Research Board, vol. 2190, no. 1, pp. 1–10,
   Jan. 2010, doi: 10.3141/2190-01.
.. [Broach2012] J. Broach, J. Dill, and J. Gliebe, "Where do cyclists ride? A
   route choice model developed with revealed preference GPS data,"
   Transportation Research Part A: Policy and Practice, vol. 46, no. 10, pp.
   1730–1740, Dec. 2012, doi: 10.1016/j.tra.2012.07.005.

Zotero collection: https://www.zotero.org/groups/966974/mechmotum/collections/DPLMTBEG

See Also
========

Some preliminary work from the lab has been done that should be built upon:

- `2012 Velocity Presentation Slides <https://docs.google.com/presentation/d/e/2PACX-1vQtgEHSrHu0HobIaReFllvckTnCiYCkpZS-kqQx5jhJXQu3nz907JDoO3UGckoiT5_1nAFsW6K0fEtq/pub?start=false&loop=false&delayms=3000>`_
- Software from the 2012 work: https://github.com/moorepants/EfficientRoutes
- `2019 Squiggly Routes COSMOS Workshop Slides <https://tinyurl.com/squiggly-cosmos2019>`_

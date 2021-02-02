:title: Optimal Handling Bicycles
:collaborators: Mont Hubbard, Ronald Hess
:current_researchers:
:date: 2019-09
:past_researchers: Roy Gilboa, Stasia Kubicki, Molly Moritzburke, Anthony Toribio, Shizhao Yang
:research_theme: Bicycle Engineering
:status: hidden
:template: project
:summary-image: https://objects-us-east-1.dream.io/mechmotum/project-image-optimal-handling-bicycle.png
:summary-sentence: Our goal with this project is to develop metrics that
                   quantify the handling, i.e. ease of control, of a bicycle or
                   other single track vehicle and using these metrics develop
                   methods for designing bicycles with specified handling
                   characteristics. We have developed an optimization algorithm
                   that can discover bicycle designs which maximize the lateral
                   handling qualities of the vehicle. The algorithm currently
                   produces less-than-intuitive but physically feasible bicycle
                   designs. These methods can likely be extended to any
                   human-machine system design.
:slug: research/optimal-handling-bicycle

In [Hess2012]_, we proposed a handling quality metric that can be derived from
a bicycle design and its associated human-like controller. Bicycles that have
an associated low handling quality metric should be easier to maneuver and
control. The handling quality metric can be analytically computed for almost
any bicycle design and provides a single value for comparing handling among
different designs. In [Moore2012]_ (Chapter 8: Control), a robust computational
method of designing the human-like controller was introduced. These ideas
allowed us to frame an optimization problem in which we search for bicycle
designs that minimize the handling quality metric. In [Moore2016]_, we
discovered optimal handling designs for various travel speeds by optimizing
over four geometric parameters. This created some non-intuitive designs, but
they were difficult to realize due to the geometry mismatching with the fixed
inertial parameters. We solved this issue in [Moore2019]_ by developing a
constrained optimization problem which enforces consistency and realism in the
geometric and inertial parameters. This method produced bicycle designs that
can be constructed and tested. We constructed one such bicycle in [Gilboa2019]_
and showed that the vehicle is realizable and rideable. For this work, we have
developed companion open source software [Moore2011]_ that can create
human-like controllers for a broad set of bicycle designs, calculate the
handling quality metric, and solve the optimal design problems.

Associated Research Products
============================

- Journal articles:

   - [Hess2012]_

- Conference papers:

   - [Gilboa2019]_
   - [Moore2019]_
   - [Moore2016]_

- Conference presentations:

   - "`An Optimal Handling Bicycle <https://www.moorepants.info/presentations/2016/BMD2016>`_", BMD 2016
   - "`Expanded Optimization for Discovering Optimal Lateral Handling Bicycles <https://docs.google.com/presentation/d/e/2PACX-1vSs1mO_r0up-V_J-rHGOawPF-BAi8EtSdnGBUzNsRp1g5C4IAJeDx56b7y0mMmKzDPlAqTau6pMnmN6/pub?start=false&loop=false&delayms=3000#slide=id.p>`_", BMD 2019
   - "`Practical Realization of a Theoretical Optimal-Handling Bicycle <https://docs.google.com/presentation/d/e/2PACX-1vSEw9wiGY9DfPvp76Q6AorG1_Yf2I90ZaTrCrJzLXcVTwXXNM1aY90lROchV84E0Y1Rx9aFkPQBJtOo/pub?start=false&loop=false&delayms=3000>`_",  BMD 2019

- Reports:

  - "Optimal Handling Bicycle: Final Design" https://doi.org/10.6084/m9.figshare.12833933.v1

- Software:

   - [Moore2011]_

- Blog posts:

   - `Practical Realization of a Theoretical Optimal-Handling Bicycle Results <{filename}/practical-realization-of-a-theoretical-optimal-handling-bicycle-results.rst>`_

Media
=====

.. figure:: https://objects-us-east-1.dream.io/mechmotum/handling-metric.png
   :align: center
   :width: 60%
   :alt: Example handle quality metric plot.

   Figure taken from [Hess2012]_ showing the handling quality metrics for an
   assortment of bicycles.

.. figure:: https://objects-us-east-1.dream.io/mechmotum/optimal-handling-bicycle.png
   :align: center
   :width: 60%
   :alt: Image of a theorectical optimal bicycle.

   Figure taken from [Moore2016]_ showing an optimal handling bicycle design
   for a 5 m/s travel speed compared to the benchmark bicycle from
   [Meijaard2007]_.

.. figure:: https://objects-us-east-1.dream.io/mechmotum/opt-bike-design.png
   :align: center
   :width: 60%
   :alt: Image of a realizable optimal bicycle.

   Image of an early realizable potentiall optimal bicycle. This bicycle design was based
   on some incorrect analisys and was not constructed.

.. figure:: https://objects-us-east-1.dream.io/mechmotum/3ms-fabricated-rider.jpg
   :width: 50%
   :align: center
   :alt: 3ms Fabricated Rider.

   Fabricated model of optimal bicycle for 3 m/s with rider.


.. raw:: html

   <iframe width="560" height="315"
   src="https://www.youtube.com/embed/videoseries?list=PLK0jeQYhBx8OKwawxvqduBsUDNv8WVHG1"
   frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope;
   picture-in-picture" allowfullscreen></iframe>
   <br>
   Playlist of videos of some of the bicycles we have constructed.

References
==========

.. [Gilboa2019] R. Gilboa, A. Kubicki, A. Toribio, M. Hubbard, and J. K. Moore,
   "Practical Realization of a Theoretical Optimal-Handling Bicycle," 2019, p.
   11, https://doi.org/10.6084/m9.figshare.9883328.v1.
.. [Moore2019] J. K. Moore and M. Hubbard, "Expanded Optimization for
   Discovering Optimal Lateral Handling Bicycles," Padua, Italy, 2019, p. 12,
   https://doi.org/10.6084/m9.figshare.9942938.v1.
.. [Moore2016] Moore, Jason, Mont Hubbard, and Ronald A. Hess. "An Optimal
   Handling Bicycle." In Proceedings of the 2016 Bicycle and Motorcycle
   Dynamics Conference. Figshare, 2016.
   https://doi.org/10.6084/m9.figshare.c.3460590.v11.
.. [Moore2012] J. K. Moore, "Human Control of a Bicycle," Doctor of Philosophy,
   University of California, Davis, CA, 2012. https://moorepants.github.io/dissertation
.. [Hess2012] R. Hess, J. K. Moore, and M. Hubbard, "Modeling the Manually
   Controlled Bicycle," IEEE Transactions on Systems, Man, and Cybernetics -
   Part A: Systems and Humans, vol. 42, no. 3, pp. 545–557, Feb. 2012, doi:
   10.1109/TSMCA.2011.2164244.
.. [Moore2011] J. K. Moore, HumanControl: Human control of a bicycle.
   University of California, Davis, 2011. Github:
   https://github.com/moorepants/HumanControl.
.. [Meijaard2007] J. P. Meijaard, J. M. Papadopoulos, A. Ruina, and A. L.
   Schwab, "Linearized dynamics equations for the balance and steer of a bicycle:
   A benchmark and review," Proceedings of the Royal Society A: Mathematical,
   Physical and Engineering Sciences, vol. 463, no. 2084, pp. 1955–1982, Aug.
   2007.

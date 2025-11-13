Practical Realization of a Theoretical Optimal-Handling Bicycle Results
=======================================================================

:date: 2019-10-03 00:00:00
:tags: bicycle, design, handling qualities, control, optimization, fabrication
:category: research
:authors: Anthony Toribio, Stasia Kubicki
:summary: Blog post on the design and fabrication of a theoretically optimal
          handling bicycle
:thumbnail: https://mechmotum.s3.us-east-005.dream.io/3ms-fabricated.jpg

The goal of this research is to design and fabricate a theoretically optimal
lateral handling bicycle based on a dynamics based algorithm written by
Professor Moore. Lateral handling is quantified using the Handling Quality
Metric (HQM) where lower peak values indicate better handling. This
optimization algorithm takes into account physical bicycle properties including
geometry, mass, moments of inertia and speed. In particular, the geometry
defining the bicycle's trail, wheelbase, steer axis tilt, and front wheel
radius are optimized for the target speed.

Our measure of lateral handling difficulty is the theoretical handling quality
metric (HQM). HQM is a function of frequency and quantifies the human control
effort needed to stabilize and direct a given bicycle based on quantifying the
rider's roll rate sensing activity. We then followed an iterative design
process to develop physically realizable wheels, frame, and fork that will
produce parameter values as close as possible to the target optimal parameter
values. We then fabricated and test rode the resulting bicycle.

A theoretical target bicycle design has been found using the algorithm at a
speed of 3m/s with an HQM of 1.2 as compared to a standard bicycle's HQM of 7.8
at the same speed. Once a realizable model was created in CAD, the HQM was seen
to rise from 1.2 to 2.45. This value far surpasses the standard bicycle.
However, the fabrication of the design proved to be rather challenging. Issues
were encountered with tolerances and therefore error propagation as well as
issues with deflection under loading. These issues in combination created a
fabricated bicycle dissimilar to the original model. The fabricated bicycle
yielded an HQM with close-loop instability meaning that the handling could not
be evaluated using the algorithm.

The bicycle was test ridden by Stasia and determined to have characteristics
described as "stable and effortless to ride when the intent is not to steer in
a particular direction". Riding the bicycle felt "stable, as if you are sitting
in a cart". Even though the bicycle is unstable in the algorithm, a real rider
can control it. For more information on the current status of this research,
please see the attached paper and media below. Future work on this research
will be to evaluate the handling of the bicycle both subjectively and
objectively.

Paper: https://doi.org/10.6084/m9.figshare.9883328.v1

.. figure:: https://mechmotum.s3.us-east-005.dream.io/3ms-fabricated.jpg
   :width: 50%
   :align: center
   :alt: 3ms Fabricated.

   *Figure 1. Fabricated model of optimal bicycle for 3 m/s.*

.. figure:: https://mechmotum.s3.us-east-005.dream.io/3ms-fabricated-rider.jpg
   :width: 50%
   :align: center
   :alt: 3ms Fabricated Rider.

   *Figure 2. Fabricated model of optimal bicycle for 3 m/s with rider.*

.. raw:: html

   <iframe width="560" height="315"
   src="https://www.youtube.com/embed/oDPssZu9Uso" frameborder="0"
   allow="accelerometer; autoplay; encrypted-media; gyroscope;
   picture-in-picture" allowfullscreen></iframe>

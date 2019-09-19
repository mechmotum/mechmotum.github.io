Practical Realization of a Theoretical Optimal-Handling Bicycle
=====================================================================================

:date: 2019-09-19 00:00:00
:tags: bicycle, design, handling qualities, control, optimization, fabrication
:category: research
:slug: 
:authors: Anthony Toribio, Stasia Kubicki
:summary: Blog post on the design and fabrication of a theoretically optimal handling bicycle

.. contents::

Summary
^^^^^^^^^^^^^^^^

The goal of this research is to design and fabricate a theoretically optimal lateral handling bicycle based on a dynamics based algorithm written by Professor Moore. Lateral handling is quantified using the Handling Quality Metric (HQM) where lower peak values indicate better handling. This optimization algorithm takes into account physical bicycle properties including geometry, mass, moments of inertia and speed. In particular, the geometry defining the bicycle’s trail, wheelbase, steer axis tilt, and front wheel radius are optimized for the target speed.

Our measure of lateral handling difficulty is the theoretical handling quality metric (HQM). HQM is a function of frequency and quantifies the human control effort needed to stabilize and direct a given bicycle based on quantifying the rider’s roll rate sensing activity. We then followed an iterative design process to develop physically realizable wheels, frame, and fork that will produce parameter values as close as possible to the target optimal parameter values. We then fabricated and test rode the resulting bicycle.

A theoretical target bicycle design has been found using the algorithm at a speed of 4m/s with an HQM of 1.2 as compared to a standard bicycle’s HQM of 7.8 at the same speed. Once a realizable model was created in CAD, the HQM was seen to rise from 1.2 to 2.45. This value far surpasses the standard bicycle. However, the fabrication of the design proved to be rather challenging. Issues were encountered with tolerances and therefore error propagation as well as issues with deflection under loading. These issues in combination created a fabricated bicycle dissimilar to the original model. The fabricated bicycle yielded an HQM with close-loop instability meaning that the handling could not be evaluated using the algorithm. 
The bicycle was test ridden by Stasia and determined to have characteristics described as “stable and effortless to ride when the intent is not to steer in a particular direction”. Riding the bicycle felt “stable, as if you are sitting in a cart”. Even though the bicycle is unstable in the algorithm, a real rider can control it. For more information on the current status of this research, please see the attached paper. Future work on this research will be to evaluate the handling of the bicycle both subjectively and objectively.

Paper: https://documentcloud.adobe.com/link/track?uri=urn%3Aaaid%3Ascds%3AUS%3Ad79d016f-477c-4a7f-9672-ce2e5862e3ec 

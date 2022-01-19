=======================================================
Determining Dynamics Perception Thresholds of Bicycles
=======================================================

:date: 2021-01-04
:status: hidden
:slug: jobs/msc/determining-dynamics-perception-thresholds-of-bicycles
:template: msc-project

The "handling qualities", or ease of control, of human controlled vehicles are
difficult to objectively characterize. The subjective nature of human
perception to changes in vehicle dynamics confounds the certainty in
hypothesized relationships between plant dynamics and the handling qualities.
For example, humans can even be tricked into incorrect judgements when there is
nuance in varied vehicles dynamics. Additionally, perception can be affected
differently for different tasks and for equivalent order plants with large
differences in the dynamics. A first step to reaching relationships between
plant dynamics, task type, and perception of handling is to understand what the
threshold precision of subjectively reported perception of a human subject
under controlled situations. This has been explored for laboratory tasks, such
as tracking a single degree of freedom motion on a screen with a joystick
[Wei2020]_ and aircraft stall [Smets2019]_, but not yet in more complex
experimental scenarios.

The bicycle-rider system is well suited to attempt perception threshold
identification due to the ability of constraining the plant as a SIMO system
and that it is a "lab scaled" and a low cost experimental platform. The bicycle
provides unique plant dynamics that can be exploited, such as variable
stability, non-minimum phase behavior, and non-trivial system order. Some prior
work with a bicycle has been performed in [Kresie2017]_. There are two primary
options for varying the dynamics of the vehicle: 1) manually change specific
physical aspects of the vehicle or 2) to make use of the Bicycle Lab's
steer-by-wire bicycle in which the open loop dynamics between the handlebars
and fork can be implemented in software. Both have been done in the lab before
and there are merits to each. A method of setting precise and repeatable plant
dynamics will be required.

The primary goal of the project will be to develop experimentally derived
measures of the perception thresholds to changes in vehicle dynamics, i.e.
what's the smallest change in a physical characteristics that riders can
successfully detect.

Experiments will have to be carefully designed such that the rider does not
make perception judgements based on preconceived ideas about how physical
characteristics relate to handling and appropriate control tasks (maneuvers)
will have to be chosen that maximize the ability to make objective measures of
control success. The dynamics will have to be able to varied precisely for
repeatability and also in a way that both randomizes the order of changes and
hones in on threshold limits in with a minimal number of trials. Multiple
riders will need to be evaluated to increase certainty in the perception
measures. Riders will need to be coaxed into utilizing similar passive
biomechanics or these differences will need to be measured. Lastly, careful
design of extracting the subjective assessment from the subject for a given
trial will need to be implemented.

We will collaborate with Rene van Paassen in Human Machine Systems in Aerospace
Engineering.

References
==========

.. [Wei2020] Fu, Wei, M. M. van Paassen, and Max Mulder. "Human Threshold Model for
   Perceiving Changes in System Dynamics." IEEE Transactions on Human-Machine
   Systems 50, no. 5 (October 2020): 444–53. https://doi.org/10.1109/THMS.2020.2989383.
.. [Smets2019] Smets, Stephan C., Coen C. de Visser, and Daan M. Pool. "Subjective
   Noticeability of Variations in Quasi-Steady Aerodynamic Stall Dynamics." In
   AIAA Scitech 2019 Forum. AIAA SciTech Forum. American Institute of
   Aeronautics and Astronautics, 2019. https://doi.org/10.2514/6.2019-1485.
.. [Kresie2017] Kresie, Scott W., Jason K. Moore, Mont Hubbard, and Ronald A.
   Hess.  "Experimental Validation of Bicycle Handling Prediction," September
   13, 2017. https://doi.org/10.6084/m9.figshare.5405233.v1

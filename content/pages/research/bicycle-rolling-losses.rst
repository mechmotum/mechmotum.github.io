=======================================
Energy Loss in Bicycling Due to Rolling
=======================================

:status: hidden
:date: 2026-11-21
:collaborators:
:current_researchers: Stijn Wolters
:past_researchers: Kirsten Dijkman, Andrew Dressel, Eloy Vázquez Fernández,
                   Quinten Bongers, Daniel Body
:research_theme: Bicycle Engineering
:template: project
:summary-sentence: Gravity, air, and rolling can all contribute to slowing a
                   cyclist, but the energy loss due to rolling is not as simple
                   as a traditional rolling resistance view makes it seem. The
                   roads a cyclist traverses have varying degrees of roughness.
                   When the loaded tire rolls over these rough surfaces it
                   deforms and loses energy due to hysteresis, but the
                   roughness also causes the entire bicycle-rider system to
                   vibrate. These vibrations are partially absorbed by the
                   tire, the bicycle materials, suspension systems, and the
                   rider themselves. Each of these cause energy loss which
                   translates to slowing the forward motion of the cyclist.
                   When riding on high roughness road surfaces, the majority of
                   energy loss can be from the vibration. This project is
                   focused on developing the science behind this vibrational
                   energy loss mechanism and seeking ways to reduce it.
:summary-image: https://mechmotum.s3.us-east-005.dream.io/de-veeger-trailer.png

Findings
========

Dijkman 2024
------------

MSc Kirsten Dijkman first developed "De Veeger", our rolling loss measurement
trailer which allows us to collect on-road data without air resistance and can
be pulled over varied road surfaces. See it in action below:

.. raw:: html

   <center>
   <iframe width="560" height="315"
   src="https://www.youtube.com/embed/685I6pjQcfw?si=-uKNN13BkDehnaQ6"
   title="YouTube video player" frameborder="0" allow="accelerometer; autoplay;
   clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
   allowfullscreen></iframe>
   </center>

In her thesis, she showed that you can find differences in tires but those
difference are small for ~1 bar change or 2 mm tire carcass diameter. The
uncertainty in our measurements needs to be reduced significantly to have
reliable comparisons among such similar tires. She showed that paver bricks
have higher losses than asphalt, as expected.

.. figure:: https://mechmotum.s3.us-east-005.dream.io/kirsten-results.png
   :width: 80%
   :align: center

   Rolling resistance coefficient derived from total rolling losses (rolling +
   vibrational) for two tire sizes, three pressures, and two target speeds.

Vázquez 2025
------------

MSc student Eloy Vázquez Fernández created a simulated cobblestone surface
based on equivalent bicycle roughness index (BRI) and extracted vibrational
losses using accurate speed measurements finding vibrational losses being
dominant at higher speeds and accounting for 150-350 watts loss when seated in
an aero-position on the bicycle.

.. figure:: https://mechmotum.s3.us-east-005.dream.io/eloy-plot-power-30kph.png
   :width: 80%
   :align: center

   Power loss due to vibration, rolling, and aerodynamic drag at 30 km/h seated
   over cobblestones for varying tire pressure.

He also found that vibrational losses do not behave linearly with respect to
speed and tire pressure over this surface, showing that losses can be reduced
by adjusting tire pressure depending on the speed.

.. figure:: https://mechmotum.s3.us-east-005.dream.io/eloy-vibration-power-loss-seated.png
   :width: 80%
   :align: center

   Nonlinear surface of power loss due to vibration at different speeds and
   tire pressures while seated.

Bongers 2026
------------

MSc student Quinten Bongers developed our variable surface treadmill and power
loss measurement technique based on accurately measured towing force.

.. raw:: html

   <center>
   <video width="80%" controls>
     <source src=" https://mechmotum.s3.us-east-005.dream.io/vibration-treadmill-first-day-960x540-no-sound.mp4" type="video/mp4">
     Your browser does not support the video tag.
   </video>
   </center>

His measurements over a 3D printed paver brick surface with ~2 cm gaps aligned
with Eloy's findings, in that the vibrational power loss is high (150 watts at
30 km/h) but Quinten found the speed, pressure, power loss relationship to be
more linear for this surface.

.. figure:: https://mechmotum.s3.us-east-005.dream.io/bongers-figure.png
   :align: center

Products
========

- Dijkman, K. (2024). Impact of bicycle tire parameter on the total rolling
  losses [Master of Science, Delft University of Technology].
  https://repository.tudelft.nl/islandora/object/uuid%3A7d45c36f-5df4-46bf-a526-b3f28a4a9fab
- Vázquez Fernández, E. (2025). Vibration Impact on Cycling Performance [Master
  of Science, Delft University of Technology].
  https://repository.tudelft.nl/record/uuid:c33246b4-b42e-49cb-b042-c0b7ee4a0ac0
- Vázquez Fernández, E. (2026, June). Vibrational Energy Losses in Road Cycling
  [Poster]. International Sports Engineering Association Student Competition.
- Bongers, Q. (2026). The Influence of Roadsurface on Powerloss [Master of
  Science, Delft University of Technology].
  https://repository.tudelft.nl/record/uuid:b43d8df3-a89a-4c0e-8f67-8cdc8623f89c
- Body, D. (2026). Measuring the vibrations of a bicycle on a treadmill to
  evaluate comfort [Technical]. Delft University of Technology.
  https://doi.org/10.6084/m9.figshare.33886375
- Vázquez Fernández, E., Dell’Orto, G., & Moore, J. K. (2026).
  Vibration-Induced Power Loss in Cycling: Experimental Quantification on a
  Simulated Cobblestone Surface [Submitted].

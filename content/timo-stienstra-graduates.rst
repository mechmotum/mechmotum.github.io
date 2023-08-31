==================================================
Timo Stienstra Successfully Defends His MSc Thesis
==================================================

:date: 2023-08-30 16:58:00
:tags: bicycle, modeling, software, engineering, sympy
:category: news
:slug: timo-stienstra-graduates
:authors: Jason K. Moore

.. image:: https://objects-us-east-1.dream.io/mechmotum/thesis-cover-stienstra.png
   :align: center
   :height: 400px

Timo Stienstra successfully defended "`BRiM: A Modular Bicycle-Rider Modeling
Framework
<http://resolver.tudelft.nl/uuid:a2b132e9-8d38-4553-8587-0c9e3341b202>`_". Timo
developed a multibody dynamics modeling tool that makes it much easier to build
and change bicycle-rider models. It nicely allows you to modularly construct
these models from components yet still have a minimal coordinate formulation of
the dynamics that precisely evaluates the equations of motion of the system. We
plan to use Timo's work as a basis for our bicycle-rider models, which we use
in most of the lab's projects. Timo also made significant contributions to
SymPy_ during his Google Summer of Code internship and during his thesis
project. He improved the joints module by making important corrections, adding
new joint types, and including high quality figures in the documentation. You
can read about the GSoC work on `his blog`_ and you can see how the joints are
used to model a four-bar linkage `in the SymPy documentation`_. Timo also
developed new load components and new system object and demystified a long
standing bug associated with solving linear systems symbolically. Timo created
a matplotlib-based 3D plotting and animation tool for SymPy mechanics objects
called symmeplot_ that simplifies visualizing your models. With all of these
tools he brought his bicycle-rider simulations to life with BRiM_. Here are
some example animations of his simulations:

.. _SymPy: https://sympy.org
.. _his blog: https://tjstienstra.github.io/gsoc/2022/2022/10/03/final-overview.html
.. _in the SymPy documentation: https://docs.sympy.org/dev/modules/physics/mechanics/examples/four_bar_linkage_example.html
.. _symmeplot: https://github.com/TJStienstra/symmeplot
.. _BRiM: https://github.com/TJStienstra/brim/

.. list-table::
   :class: borderless
   :width: 100%
   :align: center

   *  - |bike-circle|
      - |bike-large-turns|
   *  - |bike-rider|
      - |one-bike|
   *  - |two-bikes|
      - |rolling-disc|

.. |bike-circle| image:: https://objects-us-east-1.dream.io/mechmotum/timo-bike-circle.gif
   :height: 400px

.. |bike-large-turns| image:: https://objects-us-east-1.dream.io/mechmotum/timo-bike-large-turns.gif
   :height: 400px

.. |bike-rider| image:: https://objects-us-east-1.dream.io/mechmotum/timo-bike-rider.gif
   :height: 400px

.. |one-bike| image:: https://objects-us-east-1.dream.io/mechmotum/timo-one-bike.gif
   :height: 400px

.. |two-bikes| image:: https://objects-us-east-1.dream.io/mechmotum/timo-two-bikes.gif
   :height: 400px

.. |rolling-disc| image:: https://objects-us-east-1.dream.io/mechmotum/timo-rolling-disc.gif
   :height: 400px

Timo was co-supervised by Sam Brockie (TU Delft) and Jason K. Moore (TU Delft).
Everyone at the bicycle lab is very proud of Jan and wishes him the best in his
next adventures.

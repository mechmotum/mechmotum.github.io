====================================================
First measurement data from the instrumented bicycle
====================================================

:date: 2005-03-11
:authors: Arend L. Schwab

First measurement data from the instrumented bicycle. This work is done by my
Delft MSc student Jodi Kooijman. This is the bike:

|image28|

.. raw:: html

   <iframe width="560" height="315"
   src="https://www.youtube.com/embed/7V1QWY1STi8" frameborder="0"
   allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope;
   picture-in-picture" allowfullscreen></iframe>

Note the laptop on the rear rack, the manual launcher is Jodi. The bike is
instrumented with two rate gyros, one for the lean rate and one for the yaw
rate. The steering angle is measured by a potentiometer. The speed is measured
(temporarily) by a dynamo (originally meant for the head and tail light). Data
is collected via a USB data collecting box driven by LabVIEW and stored on the
laptop. Here is an `video file(2.8Mb)
<http://bicycle.tudelft.nl/schwab/Bicycle/CIMG0650.AVI>`__ of the first test
run, and here is the `graph(23Kb)
<http://bicycle.tudelft.nl/schwab/Bicycle/Bike1Graph.gif>`__ with the first
measured data.

The final goal is to create a *Robot Bicycle* by adding a steering torque
controller, to stabilize the bike, and a small elector motor to maintain
forward speed.

.. |image28| image:: http://bicycle.tudelft.nl/schwab/Bicycle/Bike1Still.jpg
   :width: 320px
   :height: 240px

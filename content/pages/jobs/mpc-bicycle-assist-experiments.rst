================================================================
Using Model Predictive Control to Assist in Bicycle Lane Changes
================================================================

:date: 2023-10-27
:status: hidden
:slug: jobs/msc/mpc-bicycle-assist-experiments.rst
:template: msc-project

.. image:: https://objects-us-east-1.dream.io/mechmotum/
   :align: center

Prior research has shown that tracking performance can be improved in a
human-in-the-loop control task by inserting a robot in between the human and
the environment and utilizing Model Predictive Control (MPC) with a short
horizon to assist control. The goal of this project is to extend this idea to
the more complex task of making lane changes on a bicycle.

In a prior MSc project, the student implemented a real-time MPC controller on
our steer-by-wire bicycle that was synced with a virtual lane change task. We
tested the ability of the controller to help improve the performance of the
riders, but did not find a positive result. This is most likely due to a number
of shortcomings in the hardware and experimental design. The goal of this
project would be to alleviate those shortcomings and to perform a larger scale
experiment to test the capabilities of the MPC based steering assist.

See our paper on the topic for a description of the work you will build upon:

   Model Predictive Control-based haptic steering assistance to enhance motor
   learning of a bicycling task: A pilot study, https://doi.org/10.31224/2811

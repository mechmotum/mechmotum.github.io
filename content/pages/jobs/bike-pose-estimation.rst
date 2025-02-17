============================================
Bicycle pose estimation from monocular video
============================================

:date: 2025-02-13
:status: hidden
:slug: jobs/msc/bike-pose-estimation
:template: msc-project

.. list-table::
   :class: table

   * - |openposegif|
     - |dygertvideo|
   * - Pose estimation example using OpenPose.
     - Example bicycle crash

.. |openposegif| image:: https://raw.githubusercontent.com/CMU-Perceptual-Computing-Lab/openpose/master/.github/media/dance_foot.gif
   :width: 400px


..
.. |dygertvideo| raw:: html

   <div style="text-align: center;">
   <iframe
     width="400"
     height="225"
     src="https://www.youtube.com/embed/rEzFIQmDJYU"
     frameborder="0"
     allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
     allowfullscreen>
   </iframe>
   </div>



Traditional methods to analyse the motion of bodies, such as humans or
vehicles, rely on Motion Capture systems or plenty of sensors. These methods
offer great precision and reliability, however, they are only available in
specialised laboratories or instrumented vehicles, which limits the analysis of
'in-the-wild' data. For this reason, during the last years, and supported by
the constant performance increase of computer vision techniques, the scientific
community have been developing tools to extract motion data from normal videos.
This method is called 'Pose estimation' and has received great attention in the
last ten years, mainly focused on human motion. However, there is no publicly
available implementationof this methodology for estimating the motion of a
bicycle. Therefore, we propose a project to implement similar methodologies
into bicycle motion analysis, which will allow researchers to analyse bicycles
in-the-wild and enhance their understanding.


**Objective:** Extract bicycle's kinematic data from monocular videos and
compare the performance of different training approaches.

Suggested approach
==================

To carry this project, the suggested approach consists in a three-stage
pipeline, based on KinePose_:

#. Use computer vision algorithms to detect keypoints on the bicycle.
#. Convert 2D keypoints into 3D point cloud with different methodologies.
#. Compare the performance of the different methodologies.

Known methodologies
-------------------

From MotionBert_, it is known that three different methodologies to go from 2D
keypoints to 3D cloud of points are:

* Heatmap from depth estimation.
* Train the algorithm with motion capture data.
* Train the algorithm with synthetic data.


**PDF version**: Proposal_

Don't hesitate to reach out at b.gonzaleztoledo@tudelft.nl if you have more
questions.


.. _OpenPose: https://github.com/CMU-Perceptual-Computing-Lab/openpose
.. _DeepLabCut:  http://www.mousemotorlab.org/deeplabcut
.. _Anipose: https://anipose.readthedocs.io
.. _KinePose: https://kevgildea.github.io/KinePose/
.. _MotionBert: https://motionbert.github.io/
.. _Proposal: https://github.com/Eimolgon/Drafts/blob/main/MSc_Proposal_BGonzalez.pdf

=========================================================================
Describing and predicting cyclists' workload in natural urban conditions
=========================================================================

:status: hidden
:date: 2025-11-19
:collaborators: Jason K. Moore, Holger Caesar
:current_researchers:
:past_researchers: Jules Ronné
:research_theme: Bicycle Engineering
:template: project
:summary-sentence: This project's goal is to connect the subjective cognitive workload of 
                   cyclists with gaze, head kinematics and vehicule kinematics metrics. 
                   This reseach investigate the possibiliy to predict the subjective workload based
                   on objective metrics using machine learning methods. 
:summary-image: https://mechmotum.s3.us-east-005.dream.io/child-dummy-in-bakfiets-400x400.jpg
:slug: research/urban-cycling-workload

..
   python bin/rest_bib.py 425053 user GRUNPYYH

Products
========

Preprints

1. `Jules Ronné`, `Jason K. Moore`, and `Holger Caesar` "Describing and predicting cyclists’ workload in natural urban conditions through gaze, head and bicycle kinematics"

Articles In Preparation or Under Review

1. `Jules Ronné`, `Jason K. Moore`, and `Holger Caesar` "Describing and predicting cyclists’ workload in natural urban conditions through gaze, head and bicycle kinematics" <https://engrxiv.org/preprint/...>`__", 2025-09-22, Under Review at Transportation Research Part F: Traffic Psychology and Behaviour

Description
===========

**Motivations**

This research is part of an effort to improve the safety of cyclists in their daily mobility in urban environments. It focuses on the cognitive load of cyclists when navigating a complex environment that requires constant interaction between the infrastructure and other road users. With limited information processing and control capabilities for handling a vehicle, cognitive overload is known to be a factor that compromises safety (associated with poorer decision-making and potential loss of control). For this reason, studying the cognitive load of cyclists is relevant to their safety.

**Data collection**

This experimental study consisted of measuring the cognitive load of cyclists while riding their bikes in natural urban traffic conditions in the city of Delft (Netherlands). The collection of this information was accompanied by position measurement (using GPS), head movement measurement (using IMU), eye movement measurement (using eye tracking glasses), and video measurement from a first-person perspective. This data collection is unique in that it combines a subjective measurement of cognitive load in real time with objective measurements in an uncontrolled environment over several days with multiple participants.

**Analysis**

The data analysis consisted of two phases. First, we studied cognitive load indicators derived from eye movements, which are well known in the literature in more controlled measurement environments. The objective was to see whether these indicators were also sensitive to cognitive load in uncontrolled environments. The same approach was taken with new indicators based on head and bicycle kinematics.
The second phase of the data analysis was to build machine learning models capable of predicting a cyclist's cognitive load at any given moment based on a few objective measurements. This type of algorithm could be very useful for monitoring the cognitive load of cyclists on a large scale in order to assess traffic conditions or the quality of infrastructure. This tool would be useful for infrastructure research. 

**Main results**

The results indicate that cognitive load indicators based on eye movement are mostly sensitive to workload in uncontrolled environments, but their variations are not very specific, making their predictive capabilities weak.
Combining indicators from different measurement modalities has therefore proven to be a powerful way to improve the predictive capabilities of machine learning algorithms. These algorithms have shown remarkable generalization capabilities, even if their predictive performance remains limited. The main result of this analysis is that bicycle kinematics is a resilient source of information for predicting cyclists' workload. This is based in particular on the fact that cyclists exhibit task difficulty homeostasis behavior, in which they modulate their speed to control their workload.

**Code and data**

The code and dataset for this project will be published very soon in open access.
https://github.com/jrPhD/NaturalCyclingWorkload

The data was collected as part of the final bachelor's degree project of:

- Jur Nelissen (Investigation, Methodology)

- Tim Janssen (Investigation, Methodology)

- Alex Mampuya (Investigation, Methodology)

- Vince Opsteeg (Investigation, Methodology)

These four students produced a robust and substantial piece of work that will directly benefit research into cyclist safety.

**Future research**

This 12-month project deserves to be continued in order to consolidate the cognitive load prediction models. So far, we have demonstrated the concept and shown what type of method could be used to develop a monitoring tool that can be used to map urban spaces. It would be particularly interesting to continue using metrics based on vehicle cinematics, which are easy to measure and highly predictive.




Funding
=======

This 12 months postdoc project was funded by a cohesion grant of TU Delft between the Inteligent vehicule group (Cognitive Robotics departement) and the Bicycle Lab (BioMechanical Engineering departement).

Media
=====

#TODO Insert here the giff


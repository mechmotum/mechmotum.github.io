=========================================================================
Learning to balance a bicycle: How do cyclists adapt to a new bicycle?
=========================================================================

:status: hidden
:date: 2025-11-19
:collaborators: Jason K. Moore, Holger Caesar
:current_researchers:
:past_researchers: Jules Ronné
:research_theme: Bicycle Engineering
:template: project
:summary-sentence: This project aims to characterize how cyclists adapt balance control and visual behavior while learning to balance a highly unstable bicycle. It investigates the relationship between subjective workload, head roll angular rate, and visual metrics (pupil diameter, saccade rate, fixation rate) to quantify learning progression and predict task success using logistic regression.
:summary-image: https://mechmotum.s3.us-east-005.dream.io/image-400x400-learning.png
:slug: research/learning-balance

..
   python bin/rest_bib.py 425053 user GRUNPYYH

Products
========

Poster presentation

1. `Jules Ronné`, `Jason K. Moore`, and `Holger Caesar` (2025, November 4-6) "Learning to balance a bicycle: How do cyclists adapt to a new bicycle?", 13th Internationnal Cycling Safety Conference (ICSC), Oslo, Norway

Description
===========

**Motivations**

This research investigates how cyclists adapt to balance control when learning to ride a new (highly unstable) bicycle. The ability to maintain balance is a fundamental level of expertise, yet the underlying control adaptations remain largely unknown. Understanding these adaptations can inform the design of training protocols or assistive systems for novice or aging cyclists.

**Data collection**

The study involved 5 participants riding a very unstable bicycle along a 35 m corridor. Measurements included:

- Visual behavior: saccades, fixations, and pupil diameter, recorded using Tobii Pro Lab’s eye-tracking glasses.

- Head kinematics: roll angular rate, measured via IMU.

- Subjective workload: assessed using the NASA-TLX questionnaire after each trial.

- Task performance: defined as successfully crossing the corridor without stopping or falling, or failing.

Participants performed repeated trials until achieving multiple successes in a row, with workload assessed after each trial.

**Analysis**

Three aspects were analyzed:

- Balance control adaptation: quantified by deriving the rate at which the variability of head roll rate changes over trials. A logistic regression model was fitted to predict the probability of task success based on this stability metric.

- Visual behavior adaptations: monitored through changes in pupil diameter, saccade rate, and fixation rate across trials.

- Workload evolution: reconstructed using the relative variations of workload.


**Main results**

Participants exhibited consistent patterns of balance control adaptation: reducing instability over trials, with stabilization head rolling motion.
Visual behavior adapted: pupil size decreased, saccade rate decreased, and fixation rate decreased — suggesting reduced workload.
Workload, as assessed via NASA-TLX, showed a decreasing trend over trials, with local increases following failures.
The logistic regression model achieved 100% correct prediction of success, with head roll angular rate variability identified as a strong predictor of loss of balance.
Recovery capacity increased with experience, indicating improved ability to recover from perturbations.

In summary, learning to balance a new bicycle involves measurable adaptations in both balance control and visual behavior, which can be objectively monitored to track the learning process.

Funding
=======

This 12 months postdoc project was funded by a cohesion grant of TU Delft between the Inteligent vehicule group (Cognitive Robotics departement) and the Bicycle Lab (BioMechanical Engineering departement).




======================
Guide: Experimentation
======================

:date: 2022-12-23
:status: hidden

If your project involves doing physical experiments, you will need to develop a
plan, assemble the resources and equipment needed, recruit assistants, possibly
recruit human subjects, and execute your experiment. It is of utmost importance
to plan your experiments in meticulous detail and practice it before executing.
Doing experiments have a higher resource cost (money, people's time, loaned
equipment, etc.) than theoretical and simulation studies and you want to
minimize the chances that those resources are wasted in any way. You absolutely
do not want to have to redo a human subjects experiment. A well designed and
written plan will make it easy for others to help you succeed.

This is general process we recommend following to ensure a successful
experiment:

Develop the theoretical foundation
   This often occurs during a literature study phase and kickoff phase of your
   project. You should develop a research question and/or hypotheses that can
   be answered via, in some part, experimentation.
Develop measurement specifications
   Based on the mathematical theory you've developed, you will need to measure
   different physical quantities. It is important to identify which quantities
   can be measured directly (e.g. temperature sensor for temperature) and those
   that need to be estimated (e.g. altitude from barometric pressure). You
   should create minimum specifications for your measurement needs that include
   accuracy, precision, range, sampling rate, streaming data, time
   synchronization, etc.
Look for measurement solutions
   Once you know precisely your minimum specifications for the desired
   measurements, you have to find sensors and tools to collect these
   measurements. You should source these from the bike lab's existing
   equipment, the 3mE MeetShop, borrow from other labs at the University, build
   the sensors yourself, or buy new sensors (in that order). To understand the
   possibilities, chat with existing lab members and refer to the many
   textbooks on engineering and scientific measurements (e.g.  [Morris2001]_.
   Developing your measurement specifications and looking for measurement
   solutions is an iterative process. You will need to adjust your
   specifications once you learn what resources are realistically available.
Design your experiments
   You now need to work out what your experiment will be and how you will do
   it. Here you answer questions like: how many subjects do I need? how many
   repetitions are necessary? what variables are changed and which are fixed?
   where will the experiments occur? who will perform them? There is a
   scientific field called `Design of Experiments`_ dedicated to designing
   experiments that can be evaluated in a statistically sound way and provides
   methods on deciding variables, number of trials, repetitions, etc. Books
   like [Anderson2018]_ give an introduction to the ideas. Many of the other
   things to figure out at this stage are specific to the nature of the
   experiment and involve attending to various logistics.
Write a experimental plan
   Once you know what you want to do (in a precise scientific and engineering
   sense), you should draft an experimental plan document. The purpose of this
   document is two-fold: 1) to organize your ideas and plans for yourself and
   2) to communicate your plans to others. The document should include an
   objective for the experiments and introduction, description of the
   experimental methods, resources you will use and/or need, a budget, time
   planning, location information, safety concerns and how you can address
   them, and a protocol_ for the experiment (step-by-step recipe of the
   experiment). See `this document
   <https://depts.washington.edu/wildfire/resources/protckl.pdf>`_ for ideas
   about what can be in a protocol. Share this document with your advisors to
   get feedback and to initiate their support in obtaining resources for your
   experiment.
Minimal viable measurement setup
   Once you have a plan you need to try out elements of your methods to make
   sure they actually work as you think they will. This usually involves a
   series of mini-tests and mini-experiments to get all of your measurements
   working. It may also involve creating new sensors and measurement
   techniques. Try to make use of existing equipment to validate you ability to
   measure what you want before purchasing or creating new equipment.
Pilot experiment
   Once you have your measurement system working you will need to pilot your
   protocol. If your experiment involves human subjects this typically involves
   testing the experiment on yourself. You should execute your protocol
   completely as if it were the real experiment and collect a pilot set of data
   to analyze. Make sure to review all safety aspects of your protocol with
   your advisor(s) before performing the experiment. Take copious notes on what
   does and doesn't work in your protocol, so that you adjust for the real
   experiments.
Analyze pilot data
   It is critical that you analyze your pilot data to ensure your measurements
   provide sufficient information to guaranteed that your study's overall data
   analysis can succeed. Much of the time this means ensuring that you can
   calculate all summary statistics reliably and accurately. You don't want to
   find out after doing the final experiments that you have missed a critical
   measurement or that a measurement is too noisy to be useful. Once again, the
   experiment piloting process is iterative. You have to iterative until you
   know your experiment functions and provides adequate data.
Finalize the protocol
   Once you know your experiment is sound, write up the finalized protocol.
   Make sure it has all details necessary for another person to execute the
   experiment.
Human subjects ethics
   If your study involves human subjects you need to have your experiment
   reviewed by the `TU Delft Human Research Ethics Committee`_. Follow the
   procedures outlined by the committee. We have past examples in the lab
   Google Drive. You may be able to submit this before the protocol is
   finalized, as long as nothing would be different with respect to ethical
   concerns.
Prepare for the real experiments
   Finalize all of your preparations, including recruiting human subjects,
   recruiting assistants, planning with partners, and organize all the final
   logistics.
Execute your experiments
   If all of the above is in order, then the real experiments should go like
   clockwork.

.. _Design of Experiments: https://en.wikipedia.org/wiki/Design_of_experiments
.. _protocol: https://en.wikipedia.org/wiki/Protocol_(science)
.. _TU Delft Human Research Ethics Committee: https://www.tudelft.nl/en/about-tu-delft/strategy/integrity-policy/human-research-ethics

References
==========

.. [Morris2001] Morris, A. S. (2001). Measurement and instrumentation
   principles.
.. [Anderson2018] Anderson, V. L., & McLean, R. A. (2018). Design of
   experiments: a realistic approach. CRC Press.

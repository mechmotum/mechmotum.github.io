=================================
What Caused Chloe Dygert's Crash?
=================================

:date: 2020-9-29 00:00:00
:tags: bicycle, wobble, shimmy, sports, engineering
:category: outreach
:slug: dygert-crash
:authors: Jason K. Moore
:summary: Back of the napkin analysis and commentary on Chloe Dygert's 2020 UCI
          Road World Championships crash.

Chloe Dygert had a race ending crash on September 24th, 2020 in the UCI Road
World Championships. The crash was caught quite clearly on video. The bicycle
starts oscillating during a right turn decent and she loses directional control
of the bicycle. She ultimately collided with a guard rail and had major
injuries. You can watch for yourself in the video below:

.. raw:: html

   <div style="text-align: center;">
   <iframe
     width="560"
     height="315"
     src="https://www.youtube.com/embed/rEzFIQmDJYU"
     frameborder="0"
     allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
     allowfullscreen>
   </iframe>
   </div>

The video has made its round on the internet with various commentary. As is
common with videos showing oscillation of this nature, the words "wobble"
and "shimmy" are often brought up.

What is "wobble" and "shimmy" of a bicycle?
===========================================

The words (speed) wobble and shimmy are both interchangeably used in both
academic and popular literature to describe a higher frequency oscillations
that single track vehicles (bicycles, motorcycles, and similar vehicles)
sometimes exhibit. Although, there does not seem to be a definitive unique
definition of the two words. "Higher frequencies" refers to being higher than
the vehicle's weave frequency. Weave is the fundamental steer and roll
oscillation that occurs in the 0 to 4 Hz bandwidth for bicycles traveling at
speeds below 20 m/s (72 km/h, 45 mph). In addition to the frequency
differences, at higher speeds this wobble/shimmy oscillation can grow in
magnitude (unstable) whereas weave oscillations become more damped (stable) as
the speed increases.

Wobble/shimmy oscillations are attributed to the effective flexibility of the
bicycle frame between the contact patches of the two tires. This flexibility is
primarily a combination of the flex in the tire carcass, structural stiffness
of the frame and wheels. Weave oscillations are present even if the bicycle and
tires are infinitely stiff.

Dynamics models of bicycles and motorcycles are able to predict the
wobble/shimmmy oscillation ([Plöchl2012]_, [Klinger2014]_) and, at least in
these papers, wobble/shimmy is specifically defined. These models show that:

- at speed > 45 km/h the frequency of oscillation is between 8 and 10 Hz
- the dominant motion is oscillation of the handle bar and fork about the
  steering axis; it being 3-5X the magnitude of roll oscillations
- there is a speed threshold at which the oscillation will tend to grow
  unstably; above this threshold damping this oscillation is the responsibility
  of the rider
- slowing down will reduce the oscillations

This video shows a steer dominant high frequency oscillation that qualitatively
matches the wobble/shimmy model predictions:

.. raw:: html

   <div style="text-align: center;">
   <iframe
     width="560"
     height="315"
     src="https://www.youtube.com/embed/vSNjpQPdrX4?start=27"
     frameborder="0"
     allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
     allowfullscreen>
   </iframe>
   </div>

Did Chloe Dygert experience wobble/shimmy?
==========================================

After watching Dygert's crash frame by frame, we make some observations:

- She's likely traveling at a speed between 9 m/s (32 km/h, 20 mph) and 13 m/s
  (47 km/h, 29 mph)
- She is initially bounced from her seat and the oscillation builds with her
  disconnecting more and more from the seat. This left her fully connected to
  the bike only at the time trial bars and at the pedals. She also isn't
  pedaling.
- The magnitudes of the steer and roll angles during oscillation are of similar
  magnitude.
- The frequency of oscillation is approximately 4.2 Hz.

The last two points would seem to indicate that this isn't wobble/shimmy; at
least not the definition espoused by the academic literature. The frequency is
half what it should be and it isn't steer dominant. The video of Dygert shows
clearly different oscillations than that shown in the "Bicycle Shimmy" video.
We aren't likely seeing wobble/shimmy in Dygert's crash.

Here is a video that has similarities to Dygert's oscillation. In this video,
the rider's pelvis seems fairly firmly connected to the seat. The oscillations
are similar in magnitude for steer and roll and a frame-by-frame analysis
estimate gives a 2 Hz oscillation frequency.

.. raw:: html

   <div style="text-align: center;">
   <iframe
     width="560"
     height="315"
     src="https://www.youtube.com/embed/VfngbsIUSj8?start=27"
     frameborder="0"
     allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
     allowfullscreen>
   </iframe>
   </div>

Wrap up
=======

One important assumption in the wobble/shimmy academic literature is that the
rider's pelvis is firmly connected to the seat in the models. With Dygert's
pelvis disconnected from the seat, the bicycle rider system is thus different
than these models. The interactions of the rider's flexible body with the
bicycle in Dygert's riding position may very well destabilize the weave mode.
For example, [Moore2012]_ shows that simply adding the inertial effects of the
riders arms onto the handlebars can have a destabilizing effect. Developing a
predictive model of the rider being loosely coupled to the bicycle could help
answer whether there are aspects of the bicycle's design which could minimize
the chance of this happening. In addition, a rider control model could help
determine whether there is something the rider can do to stop this (besides
slowing down).

Notes
=====

- Women time trialers average about 45 km/h (12.5 m/s), so she should have been
  going faster than this going down hill (but she isn't pedaling).
- [Plöchl2012]_ shows wobble frequencies between 6 and 9 Hz for 0 to 20 m/s in
  Figure 4. Same figure shows the wobble mode unstable from about 4 to 20 m/s.
  This is for a model with rider lean and the but attached to the seat.
- [Klinger2014]_ shows wobble between 8 and 12 Hz for 0 to 20 m/s for leaned
  over hands on handlebars (no rider lean DOF).
- Figure 6.10 in [Moore2012]_ shows that the weave frequency for a bicycle
  without a rider can get higher 10 rad/s (1.6 Hz) at 7 m/s, maybe it would be
  close to 4 Hz at 13 m/s?? But weave should be damped and stable at these
  speeds.

Dygert Crash Video
------------------

- Going downhill
- Rightward curve
- Large lean angle to the right
- The magnitude of roll is dominant. The steer and roll magnitudes are similar,
  more like weave that a steering dominated wobble/shimmy.
- Riding a Felt bicycle
- She kept cycling holding on to the time trial bars. Can you can damp
  oscillations as good in that position?
- Can the geometry of the time trial bike and the different mass distribution
  due to the different rider position have influence on the wobble frequency (a
  time trial bike is definitely different in geometry than a normal racing bike
  which Klungel might have used in his experiments)?
- Here is a map of the course by Imola:
  https://www.cyclingweekly.com/news/racing/uci-road-world-championships-465806
- 4:09 to 4:10 the seat of the bike bounces upward, maybe a bump in the road?
- 4:10 to 4:19 She bounces once on the seat and then a second time with her
  butt disconnecting from the seat. The bicycle leans further rightward during
  this process.
- 4:19 to 4:23 bounces back down on the seat
- 4:23 to 4:27 bounces back up off the seat, bike is even further leaned hard
  to the right
- 4:27 to 5:02 connects back down to the seat (much harder it seems), bike
  leans back to the left just before connecting (but still at hard right roll
  angle)

The follow csv file, ``dygert-oscillation-data.csv`` gives the second and frame
number for the peak left/right motions of the seat.

.. code::

   second,frame,side
   4,27,right
   5,01,left
   5,06,right
   5,10,left
   5,13,right
   5,16,left
   5,19,right
   5,23,left
   5,26,right
   5,29,left
   6,03,right
   6,06,left
   6,09,right
   6,13,left
   6,16,right
   6,20,left
   6,24,right

Some code to calculate frequency:

.. sourcecode:: python

   import pandas as pd
   df = pd.read_csv('dygert-oscillation-data.csv')
   fps = 30
   df['time'] = df['second'] + (df['frame'] - 1)/fps
   period = 2*df['time'].diff().mean()
   frequency_hz = 1/period
   frequency_hz

Wintergreen Cycling Camp Video
------------------------------

- guy's butt is connected to the seat the whole time (much more than Dygert)
- downhill in dropbar position
- got 2.18 Hz from this video, which is half that of Dygert and also much
  lowered that the expected wobble mode.

``wintergreen.csv``::

   second,frame,side
   31,29,left
   32,06,right
   32,13,left
   32,20,right
   32,26,left
   33,03,right
   33,08,left
   33,15,right
   33,24,left

References
==========

.. [Plöchl2012] Plöchl, Manfred, Johannes Edelmann, Bernhard Angrosch, and
   Christoph Ott. “On the Wobble Mode of a Bicycle.” Vehicle System Dynamics
   50, no. 3 (March 1, 2012): 415–29. https://doi.org/10.1080/00423114.2011.594164.
.. [Klinger2014] Klinger, Florian, Julia Nusime, Johannes Edelmann, and Manfred
   Plöchl. “Wobble of a Racing Bicycle with a Rider Hands on and Hands off the
   Handlebar.” Vehicle System Dynamics 52, no. sup1 (May 30, 2014): 51–68.
   https://doi.org/10.1080/00423114.2013.877592.
.. [Moore2012] http://moorepants.github.io/dissertation/extensions.html#rider-arms


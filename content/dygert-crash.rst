==================
Chloe Dygert Crash
==================

:date: 2020-9-25 00:00:00
:tags: bicycle, engineering
:category: research
:slug:
:authors: Jason K. Moore
:summary:

Chloe Dygert had a race ending crash on September 24th. It was caught clearly
on video. It seems the bicycle began to oscillate and she ultimately lost
directional control bicycle and collided with a guard rail.

.. raw:: html

   <iframe
     width="560"
     height="315"
     src="https://www.youtube.com/embed/rEzFIQmDJYU"
     frameborder="0"
     allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
     allowfullscreen>
   </iframe>

The video is making its round on the internet with various commentary. The most
common words that pop up regarding this uncontrollable oscillation are "speed
wobble" and "shimmy".

What is wobble and shimmy?
==========================

The words wobble and shimmy are both interchangeably used to describe a higher
frequency oscillations that single track vehicles (bicycles, motorcyles, and
things inbetween) sometimes exhibit. There isn't a definitive unique definition
of the two words. The key thing is that this oscillation is not the
fundatmenatl steer and roll oscillation, called weave, that occurs in the 0 to
2 Hz bandwidth.At higher speeds this oscillation can grow and be difficult to
control and even cause a crash.  Wobble/shimmy are attributed to the effective
flexibility of the bicycle frame between the contact patches of the two tires.
This flexibility is primarily a a combination of the flex in the tire carcas,
structural stiffness of the frame and wheels.

These things are true about wobble:

- there is a speed threshold at which the oscillation will tend to grow
  unstably, above this threshold damping this ossiclation is up to the rider
- the dominant motoin is osciallation about the steering axis (3-5X magnitude
  of roll oscillations)
- the frequency of oscillation is going to be between 8 and 10 Hz [Klinger2014]
- slowing down is likely the most effective way to reduce the oscillations

Notes
=====

- Going downhill
- Rightward curve
- Large lean angle to the right
- The magnitude of roll is dominant. The steer and roll magnitudes are similar,
  more like weave that a steering dominated wobble/shimmy.
- Riding a Felt bicycle
- She kept cycling holding on to the time trial bars. I am curious whether you
  can damp oscillations as good in that position
- And whether the geometry of the time trial bike and the different mass
  distribution due to the different rider position has influence on the wobble
  frequency (a time trial bike is definitely different in geometry than a
  normal racing bike which Klungel might have used in his experiments)
- Here is a map of the course by Imola: https://www.cyclingweekly.com/news/racing/uci-road-world-championships-465806
- Women time trialers average about 45 km/h (12.5 m/s), so she must have been
  going faster than this going down hill (but she isn't pedaling).
- Ploch2012 shows wobble frequencies between 6 and 9 Hz for 0 to 20 m/s in
  Figure 4. Same figure shows the wobble mode unstable from about 4 to 20 m/s.
  This is for a model with rider lean and the but attached to the seat.
- Klinger2014 shows wobble between 8 and 12 Hz for 0 to 20 m/s for leaned over
  hands on handlebars (no rider lean DOF).
- Figure 6.10 in my dissertation shows that the weave frequency for a bicycle
  without a rider can get higher 10 rad/s (1.6 Hz) at 7 m/s, maybe it would be
  close to 4 Hz at 13 m/s?? But weave should be damped and stable at these
  speeds.

Video Analysis
==============

4:09 to 4:10 The seat of the bike bounces up, seemingly a bump in the road
4:10 to 4:19 She bounces once on the seat and then a second time with her butt
disconnecting from the seat. The bicycle leans further rightward during this
process.
4:19 to 4:23 bounces back down on the seat
4:23 to 4:27 bounces back up off the seat, bike is even further leaned hard to
the right
4:27 to 5:02 connects back down to the seat (much harder it seems), bike leans
back to the left just before connecting (but still at hard right roll angle)

4:27,right
5:01,left
5:06,right
5:10,left
5:13,right
5:16,left
5:19,right
5:23,left
5:26,right
5:29,left
6:03,right
6:06,left
6:09,right
6:13,left
6:16,right
6:20,left
6:24,right
hard to detect next left max because the collision with the rail is occurring

Some code to calculate frequency::

   import pandas as pd
   df = pd.read_csv('dygert-oscillation-data.csv')
   fps = 30
   df['time'] = df['second'] + (df['frame'] - 1)/fps
   df['time'].diff()
   df['time'].diff().mean()
   period = 2*df['time'].diff().mean()
   frequency_hz = 1/period
   frequency_hz

Wintergreen Cycling Camp Video Analysis
=======================================

- butt is connected to the seat the whole time (much more than dygert)
- downhill in dropbar position

.. raw:: html

   <iframe
     width="560"
     height="315"
     src="https://www.youtube.com/embed/VfngbsIUSj8?start=27"
     frameborder="0"
     allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
     allowfullscreen>
   </iframe>

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

I got 2.18 Hz from this video, which is half that of Dygert and also much
lowered that the expected wobble mode.

Bicycle Shimmy Video
====================

This video shows a steer dominant high frequency oscillation.

.. raw:: html

   <iframe
     width="560"
     height="315"
     src="https://www.youtube.com/embed/vSNjpQPdrX4?start=27"
     frameborder="0"
     allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
     allowfullscreen>
   </iframe>

TODO
====

- Get the grade and curvature of the curve from Google maps or some other
  similar thing?
- What speed was she going? We may be able to use the railing pilons she passes
  to calculate speed. Just need to know the distance between the pilons.
- Check frequency in this video: https://youtu.be/VfngbsIUSj8

References
==========

.. [Plöchl2012] Plöchl, Manfred, Johannes Edelmann, Bernhard Angrosch, and
   Christoph Ott. “On the Wobble Mode of a Bicycle.” Vehicle System Dynamics
   50, no. 3 (March 1, 2012): 415–29.
   https://doi.org/10.1080/00423114.2011.594164.
.. [Klinger2014] Klinger, Florian, Julia Nusime, Johannes Edelmann, and Manfred
   Plöchl. “Wobble of a Racing Bicycle with a Rider Hands on and Hands off the
   Handlebar.” Vehicle System Dynamics 52, no. sup1 (May 30, 2014): 51–68.
   https://doi.org/10.1080/00423114.2013.877592.
.. https://www.sheldonbrown.com/brandt/shimmy.html

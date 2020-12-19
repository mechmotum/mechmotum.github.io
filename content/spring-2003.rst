=============
(Spring 2003)
=============

:authors: Arend L. Schwab
:category: research
:date: 2003-04
:slug: spring-2003
:tags: bicycle, spacar, dynamics

**Results:** Here are some of my preliminary results on the analysis of the
dynamic behavior of a bicycle. For the analysis we used our software system
SPACAR.  This software has been developed at Delft University of Technology and
is capable of doing dynamic analysis of flexible multibody systems. The method
is based upon the Finite Element Method where the expressions for the
generalized strains can be used as constraint equations to model partly rigid
systems. Pure rolling is be modeled by zero generalized slips. The equations of
motion are expressed in terms of independent generalized coordinates this to
facilitate the numerical integration of the equations of motion.

The model of the bicycle is an ordinary Dutch city bike, like this one:

.. image:: http://bicycle.tudelft.nl/schwab/Bicycle/fiets2small.jpg
   :align: center

This is a sketch of the SPACAR model, with all the element and node numbers:

.. image:: http://bicycle.tudelft.nl/schwab/Bicycle/bike2small.jpg
   :align: center

Finally the input file, which contains the complete definition of the bike,
looks like this:

.. code-block:: none

   * bike3
   pinbody  1  1 2 3
   pinbody  2  1 2 4
   pinbody  3  1 2 5
   hinge    4  2 6      1 0 0
   pinbody  5  5 6 7
   hinge    6  2 8      0.36 0 0.9
   pinbody  7  3 8 9
   pinbody  8  3 8 10
   hinge    9  8 11     0 -1 0
   wheel   10  10 11 12 0 -1 0
   hinge   11   2 13    0 -1 0
   wheel   12   4 13 14 0 -1 0
   hinge   13  2 15     0 1  0
   hinge   14  15 16   -1 0  0
   hinge   15  16 18    0 0 -1
   pinbody 16  17 18 14
   x  1  0.50 0 -0.60
   x  3  0.90 0 -0.90
   x  4  0    0 -0.35
   x  5  0.25 0 -1.00
   x  7  0.30 0 -1.20
   x  9  1.00 0 -0.70
   x 10  1.20 0 -0.35
   x 12  1.20 0  0
   x 14  0    0  0
   x 17  0    0  0
   fix 17  1 2 3
   fix 18  1 2 3 4
   line 6 1
   rlse 9 1
   enhc 10 4  9 1
   enhc 10 5 15 1
   inpute 11 1
   enhc 12 4 16 1
   enhc 12 5 16 2
   rlse 13 1
   line 14 1
   rlse 15 1
   rlse 16 1 2 3
   mass  1 16
   mass  2  2 0 0 8 0 2
   mass  4  2
   * mass  6 10 0 0 10 0 2
   mass  6 6 0 -4 10 0 6
   mass  7 80
   mass  9  1
   mass 10  2
   mass 11  0.12 0 0 0.24 0 0.12
   mass 13  0.12 0 0 0.24 0 0.12
   * dependent should be calculated from m*g
   * take g=10
   force  1  0 0 160
   force  4  0 0  20
   force  7  0 0 800
   force  9  0 0  10
   force 10  0 0  20
   ed 11 1 30
   epskin 1e-3
   epsint 1e-3
   epsind 1e-3
   timestep 1 0.001
   hmax 0.01
   end
   eof

In a first analysis we look at the steady motion of the upright bicycle with a
rigid rider, hands free, and pure rolling. These are the root-loci from the
linearized equations of motion with the forward speed v as a parameter.

.. image:: http://bicycle.tudelft.nl/schwab/Bicycle/Bike3xrl.jpg
   :align: center

You can take a closer look at the original Figure `Bike3xrl.pdf
<http://bicycle.tudelft.nl/schwab/Bicycle/Bike3xrl.pdf>`_.

In order to get an idea about the stability of this upright motion look at the
bottom-left figure, the forward speed v versus the Real part of the eigenvalues
l. Now its customary to have the parameter, here the forward speed v, on the
abscissa and the Real part of the eigenvalue  l on the ordinate. The stability
diagram then looks like this:

.. image:: http://bicycle.tudelft.nl/schwab/Bicycle/Bike3xRev.jpg
   :align: center

You can take a closer look at the original Figure `Bike3xRev.pdf
<http://bicycle.tudelft.nl/schwab/Bicycle/Bike3xRev.pdf>`_, the dots are
horizontally equidistant at 0.1 m/s.

We see that at a forward speed v of less then 0.9 m/s the bike simple falls
over, 4 real eigenvalues l with 2 positive ones. We call this the capsize mode.
At a speed of 0.9 m/s two real eigenvalues become identical and start forming a
conjugated pair after which we have an unstable oscillatory motion, the
so-called weave motion. This weave motion is an oscillatory motion in which the
bicycle sways about the headed direction. At about 4.1 m/s this weave becomes
stable. But then at about 5.7 m/s the previously stable capsize becomes
marginally unstable. So at high speed, v>5.7 m/s, we have an unstable capsize
mode but the timescale is so long, l=0.2 1/s or t=5 s, that in practice you can
easily correct this mode. Now look at the bottom-right part of the previous
figure, the 3D depiction of the root loci as a function of the forward speed,
and identify the different modes at increasing speed v.

In a second full nonlinear analysis we look at the motion of the bike by means
of a forward dynamic analysis of the perturbed upright motion. The perturbation
is a small lateral velocity of 0.1 m/s for the whole bike to start the unstable
motion, if present. The results are visualized by a number of VRML (Virtual
Reality Modeling Language) files at different initial forward speeds. You can
view these VRML files in internet browsers like Firefox, Opera or Internet
Explorer with the plugin Freeware from `Cosmo
<http://cic.nist.gov/vrml/cosmoplayer.html#AUTOMATIC>`_. For the bike to start
moving you must click on the red frame of the bike. If you want to see the path
of the rear and front wheel, then you can click on one of the wheels. You can
change your viewpoint: look in the Viewpoint List located below left. A very
nice one is the one called 'Camera', which is a moving camera with stable
horizon (as if you were riding along on the rear passenger seat).

Ok, so now for the VRML movies:

| `bike3v000.wrl <http://bicycle.tudelft.nl/schwab/Bicycle/bike3v000.wrl>`_ at v=0 m/s, unstable capsize.
| `bike3v175.wrl <http://bicycle.tudelft.nl/schwab/Bicycle/bike3v175.wrl>`_ at v=1.75 m/s, unstable weave.
| `bike3v350.wrl <http://bicycle.tudelft.nl/schwab/Bicycle/bike3v350.wrl>`_ at v=3.50 m/s, unstable weave.
| `bike3v368.wrl <http://bicycle.tudelft.nl/schwab/Bicycle/bike3v368.wrl>`_ at v=3.68 m/s, stable weave in a curve! (a nice nonlinear result)
| `bike3v490.wrl <http://bicycle.tudelft.nl/schwab/Bicycle/bike3v490.wrl>`_ at v=4.90 m/s, a stable weave.
| `bike3v630.wrl <http://bicycle.tudelft.nl/schwab/Bicycle/bike3v630.wrl>`_ at v=6.30 m/s, an unstable capsize.
|

Note that obtaining a speed of 36 km/h and above is no problem in Ithaca,
although I myself do not dare to go that fast.

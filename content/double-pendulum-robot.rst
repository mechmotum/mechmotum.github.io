Double Pendulum Human Controller Robot: GUI Development
=================================================================

:date: 2019-02-11 00:00:00
:tags: controller, double pendulum, gui
:category: research
:slug: double-pendulum-robot
:authors: Jonathan Blaze Cubanski, Dorian Crutcher
:summary: Blog post on creating a new interface to test different controller
          designs for the Double Pendulum Robot.

Introduction and background
---------------------------

The Double Pendulum Biomimetic Project has the overarching goal of developing a
desktop-controlled inverted double pendulum with actuators in each joint to
serve as a model for a human balancing on a moving platform (i.e. a
skateboard), where the degrees of freedom is limited to the human’s waist and
ankle joints. This model is illustrated in Figure 1 below.

.. figure:: https://objects-us-east-1.dream.io/mechmotum/pendulum-fbd.png
   :width: 80%
   :alt: Image depicting visual model showing the dynamics of the double pendulum robot
   :align: center

   *Figure 1: Double Pendulum Reference (Photo created by Erich Baur, Todd Sweeney, Jiahao Wei, Greg McDonald)*

There are two key applications for such a device. Firstly, it can assist in
controller identification, helping bridge the gap between the simulation of
human movements and real-world data collection. Secondly, the project is done
in collaboration with the Dr. Zhaodan Kong and the Cyber Human Physical Systems
Lab— Dr. Kong intends to use the device to demonstrate the fundamentals of
control theory to school students.

The pendulum hardware was developed previously by EME 185 students, as well as
some preliminary Arduino code to enable robot movement. The primary objectives
were now to bring this hardware to life with UI software with an interactive
GUI for the robot, and improve upon the embedded Arduino code. Additional
objectives included restoring and improving the electromechanical hardware as
needed, and allow data collection from the onboard encoders.

Software Development
--------------------

The following presents a high-level overview of the software solutions that
were implemented. To make the code modular and user-friendly, 4 custom
libraries were developed to encapsulate all needed functionality. General
system operation functions and interrupts governing writing PWM signals,
tracking encoder positions, enforcing position limits, and computing system
states were isolated in a general functionality library. A separate library for
controllers allows the user to add or modify controllers for all actuators. In
order to send position and angle commands as a function of time, the user can
directly write mathematical functions into a dedicated position library in
inches, degrees, and seconds. It was determined that the educational value of
the system and the overall functionality would greatly benefit from real-time
gain updates and user control. To facilitate this, a serial processing library
was established and using the IDE Processing, a GUI was created. The GUI, as
shown below, has a startup and swing-up buttons which enable the user to safely
start system operation when ready. The user can select the desired motor
controller and update the gains in real time.

.. figure:: https://objects-us-east-1.dream.io/mechmotum/pendulum-gui.png
   :width: 50%
   :align: center
   :alt: Operating GUI.

   *Figure 2. Operating GUI for Double Pendulum Operation*

Results and Discussion
----------------------

The system currently is operating with PID controllers for each actuator and
the aforementioned functionality. The custom designed GUI successfully augments
the controller values and output response of the double pendulum robot. In the
video below, the robot is set to remain positioned perpendicular to the ground
as different external inputs are enacted onto the robot. The different PID
gains inputted into the GUI clearly affect its ability to return to that
position after being offset by external forces. Here is a link to a video that
showcases its performance.

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/nCciGgxlK24" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Further Work
------------------

The current limiting factors of this system primarily relate to the state of
the hardware and certain design decisions. Testing of serial communication
indicates that there may be a systematic shielding issue, and the
microprocessor should be moved away from high voltage lines. It is also unclear
if the code is operating fast enough to achieve optimal performance. Thorough
testing of performance while increasing the delay between each loop is needed
to understand the effects of this. Including a feature to allow enter custom
controller algorithms to save, access and port these into the microcontroller
was also difficult to achieve within the time constraints allotted.

Data collection using a serial monitoring application is currently possible by
printing encoder data to the terminal, however, this slows down the code since
serial writing is relatively slow. Without a clear understanding of the effects
of changing loop time, it is not possible to draw clear conclusions about the
implications of this. A viable solution would be to have a second Arduino
running in parallel which only prints serial data and does not command the
robot. More testing is needed.

Here is the link to our GitHub Repository where you can find the Arduino .ino
code, the custom libraries to operate the robot, and the Processing IDE code
for the GUI controller.

https://github.com/mechmotum/DoublePendulumCode

Thank you
----------

.. figure:: https://objects-us-east-1.dream.io/mechmotum/dorian-blaze.jpg
   :width: 80%
   :alt: This image displays the two students that worked on this project over the Fall 2018 Quarter, Dorian Crutcher and Jonathan Blaze Cubanski
   :align: center

   *Figure 3: Left: Dorian Crutcher   Right: Jonathan Blaze Cubanski*

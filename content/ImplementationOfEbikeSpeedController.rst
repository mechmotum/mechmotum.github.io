Implementation of a PID Controller for Controlling The Speed of an Instrumented Ebike 
===================================================================================== 

:date: 2019-03-31 00:00:00
:tags: bikes, engineering, controller implementation, arduino
:category: research
:slug: ebike-controller-implementation
:authors: Trevor Metz
:summary: Blog post on the implementation of a PID controller on an instrumented ebike 

.. contents:: 

1.0 Introduction
^^^^^^^^^^^^^^^^

The overall goal of this project is to design and implement a control system for an instrumented ebike 
used in bicycle handling experimentation. A previous blog post found `here`_

.. _here:: ebike-controller-design

outlines the design and analysis of a PID controller that meets the steady state error goal of +/- 0.1m/s. This blog post 
tells the story of how the designed PID controller was implemented on the instrumented ebike using an Arduino Nano.  

2.0 System Operation & Functionality 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The implementation of the PID controller on the electric bike was fundamentally informed by the interactions
that the user would have with the system. A typical user interaction with the system is outlined in Figure 1 below. 

.. figure:: 
   :width: 80%
   :align: center
   :alt: User Interaction. 
   
   *Figure 1. A typical user interaction with the system.* 
     
This user interaction flowchart was used to help better understand the problem and sculpt the concept
for the hardware and software design of the speed control system.  

3.0 System Architecture 
^^^^^^^^^^^^^^^^^^^^^^^

3.1 Control Architecture
------------------------

The control architecture is a simple feedback design that computes the error between a user defined setpoint and compares it 
to the speed of the ebike as measured via a DC generator wheel speed sensor (more on this in section 5.2). Figure 2, shows how 
this error is inputted to the control algorithm encoded in the Arduino Nano resulting in an output variable used to 
control the speed of the ebike. 

.. figure:: 
   :width: 80%
   :align: center
   :alt: Control Architecture. 

   *Figure 2. Control architecture.*

3.2 Physical Architecture
-------------------------

At the heart of the control system’s physical architecture is its integration into the existing instrumented ebike platform. 
Figure 3, below, shows this integration by highlighting the input/output and geometric relationships between 
existing components of the ebike and the additional control system components. 

.. figure:: 
   :width: 80%
   :align: center
   :alt: System Architecture. 

*Figure 3. Geometric layout of the system components showing relative size, location, information flow, and type of each component. 
Components called out with a triangle are existing components on the ebike. Components called out with a circle are components that are 
introduced to the ebike system to implement the controller.*  

The fundamental interaction between the control system and the existing ebike powertrain system occurs at the interface between the 
Arduino nano and the ebike motor controller. While the cruise control is engaged, the function of the Arduino is to take control of the 
throttle signal away from the user and pass it through the control algorithm before sending it to the motor controller. When the cruise 
control is disengaged, the Arduino simply reads the user commanded throttle position and passes it directly to the motor controller. 
Figure 4, below, graphically shows this interaction. 

.. figure:: 
   :width: 80%
   :align: center
   :alt: Arduino's Main Function. 

*Figure 4. Schematic showing the Arduino’s function as a throttle emulator.* 

4.0 Software 
^^^^^^^^^^^^

The control system software was written in C using the Arduino IDE. Based on user inputs from two momentary pushbuttons, the software 
decides whether or not to pass the throttle signal as an output or compute a throttle output based on the PID controller. The software 
also updates the user on the current status of the system via an LCD and logs diagnostic information to an SD card. 

Figure 5, below, shows the logic flow of the code. 

.. figure:: 
   :width: 80%
   :align: center
   :alt: Code Logic Flowchart. 

*Figure 5. Code logic flowchart.* 

The software, and more details about it, can be found on the Laboratorium’s Github repository `found here 
<https://github.com/mechmotum/eBikeSpdController>`_. 

4.1 Code Libraries 
------------------

The continuous time PID controller derived in part one of this blog post series was digitized on the Arduino Nano using Brett Beauregard’s 
PID_v1 library `(found here) <https://github.com/br3ttb/Arduino-PID-Library>`_. This library was developed by Brett to implement PID 
controllers on an Arduino microcontroller.

Brett’s library was chosen to implement the PID controller because of its many robust features such as Derivative Kick and Initialization. 
Additionally, this library contains fantastic documentation which can be `found here <http://brettbeauregard.com/blog/2011/04/improving-
the-beginners-pid-introduction/>`_.  
  
To avoid slowing the code’s main loop, interrupts were used to manage the change in setpoint brought on by a press of the speed increment 
decrement buttons. Using interrupts free’s up the Arduino’s processor from having to check whether or not there’s been a button press on 
every loop iteration. Instead, the processor reacts to pin changes and interrupts the execution of the main code to perform the function 
tied to the interrupt pin. However, the Arduino Nano only has a limited number of pins that can be used as interrupts. A library, written 
by GreyGnome `(found here) <https://github.com/GreyGnome/PinChangeInt>`_, enables the use of interrupts on any pin of the Arduino Nano. 
This library was used to free up pin real estate for the many components that are wired up to the Arduino. 

5.0 Hardware Hook Up and Design 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

5.1 Instrumented Ebike Platform
-------------------------------

Jason Moore, the lab’s PI, originally began constructing the instrumented ebike platform in 2008 from a large Surly single speed off road 
steel frame bicycle converted to an ebike with a conversion kit sold by Amped Bikes. The Amped Bikes kit consists of a brushless direct 
drive hub motor driven by a motor controller and a 36V Li ion battery. More information on the build and the bike’s instrumentation system 
can be found in Jason’s dissertation `found here <http://moorepants.github.io/dissertation/davisbicycle.html>`_.  

.. figure:: 
   :width: 80%
   :align: center
   :alt: Instrumented Ebike. 

*Figure 6. The instrumented ebike today.*

5.2 Electrical Hook Up  
----------------------

The electrical components of the control system revolve around an Arduino Nano which is used to process inputs and outputs to human 
interface hardware, actuators, and logging hardware. Table 1, below, shows a complete list of the hardware used in this build. 

.. csv-table:: *Table 1. Table of components used in the control system. Prices and sources for each component can be found in the Bill of Materials in section 6.0.*
   :header: "Component Name", "Details", "Function"
   :widths: 20, 20, 10

    "Arduino Nano", "ATmega328P Processor", "Main   Processor"
    "Wheel Speed Sensor", "DC generator in contact with rear tire `(Click here for more information) <http://moorepants.github.io/dissertation/davisbicycle.html>`_",  "Control Loop Input"
    "Voltage Divider", "Used to step down wheel speed sensor voltage to a range measurable by the Arduino", "Wheel Speed Sensor Signal Conditioning"
    "Pushbuttons", "Momentary pushbuttons to get user input", "User Input"
    "Battery", "7.2V NiCd", "System Power"
    "LCD", "16x2 character LCD", "User Feedback"
    "Motor Controller", "Amped Bikes motor controller", "Control Loop Output"
    "SD Card Module", "SPI SD card module for Arduino", "Data Logging"

Figure 7, below, shows a Fritzing diagram of the electrical system.

.. figure:: 
   :width: 80%
   :align: center
   :alt: Electrical Hookup. 

*Figure 7. Fritzing diagram of control system electronics. Note that the motor controller is represented by a DC motor and the 7.2V NiCd 
battery is represented by a 1S LiPo battery.*  

The Arduino Nano and the voltage divider circuits were soldered to a small 3” x 1.1” piece of stripboard. Wires, braided 22AWG, were 
soldered to the stripboard to connect the external components to the Nano. Figure 8, below, shows the completed Arduino board. 

.. figure:: 
   :width: 80%
   :align: center
   :alt: Arduino Board. 

*Figure 8. The Arduino board with wires attached.*

With many of the components located on the handlebars, a majority of these wires were routed together along the top tube, up the head tube 
and stretched across to the handlebars. This task was facilitated using spiral wound cable housings, zip ties, and a 15 pin Molex 
connector. Once on the handlebars, wires were connected to header pins on the LCD and pushbuttons with Dupont connectors. 

Rearward of the Arduino, T-tap wire splices were used to cleanly splice power signals from the NiCd battery above the Arduino near the top 
tube and from the wheel speed sensor near the bottom bracket.  

5.3 Electronics Housings 
------------------------

Housings for the Arduino Nano, pushbuttons and LCD were designed and 3D printed to enclose the electrical components and mount them to the 
ebike. Figure 9, below, shows the CAD model design of the Arduino housing. The housing’s design includes pins for press fitting the 
Arduino stripboard to the mount. Slots on the sides and top of the housing allow for wires to exit towards their destinations on the 
ebike. Threaded inserts on the base are used to secure the top cover using M3 screws.

.. figure:: 
   :width: 80%
   :align: center
   :alt: Arduino Housing. 

*Figure 9.  Arduino housing design.* 

This housing is clamped to the downtube of the ebike by a socket head screw as shown in Figure 10.   

.. figure:: 
   :width: 80%
   :align: center
   :alt: Arduino Mounting. 

*Figure 10. Arduino housing mounting point.*  

Both the LCD and button housings were 3D printed and designed to mount to the handlebars using a clamshell style mount used for securing 
GoPro cameras to bikes. Each mount had a pair of “bunny ears” designed to interface with the GoPro style mount. The LCD housing, shown in 
Figure 11 below, is a simple rectangular two-piece enclosure joined by button head screws. 

.. figure:: 
   :width: 80%
   :align: center
   :alt: LCD Housing. 

*Figure 11. LCD housing design.* 

Similar to the LCD housing, the button housing is a two-piece, enclosure joined by screws. Inside the housing is a small piece of 
stripboard that the pushbuttons are soldered to. To make pressing the mini momentary pushbuttons more convenient for the user, larger 
button parts were 3D printed and offset from each mini momentary pushbutton using a compression spring as shown in Figure 12 below. 

.. figure:: 
   :width: 80%
   :align: center
   :alt: Button Housing. 

*Figure 12. Button housing design.*

As shown in Figure 13, the button housing is mounted on right side of the handlebars near the throttle and brake lever for convenient 
access.  

.. figure:: 
   :width: 80%
   :align: center
   :alt: Button Housing Mount. 

*Figure 13. Button housing position on the handlebars.*

6.0 Bill of Materials 
^^^^^^^^^^^^^^^^^^^^^

*Table 2. Bill of materials (BOM) showing each part of project, where it was purchased, what quantity was purchased and its cost.*

.. figure:: 
   :width: 80%
   :align: center
   :alt: Bill of Materials. 

7.0 Lessons Learned and Suggested Improvements  
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Throughout the process of implementing this controller, I learned some helpful practices to follow when designing 3D printed electronics 
housings and doing electrical hookups.  

When designing electronics housings I found it very necessary to account for the minimum bend radius of each wire as not taking this into 
account will not leave enough room for routing wires without excessive strain. Additionally,  it is important to follow `best practices 
<https://www.lulzbot.com/learn/tutorials/heat-set-inserts-tips-and-tricks>`_ when designing for heat set threaded inserts.  Most 
importantly, when it comes to physically realizing these designs using a fused deposition modeling 3D printer, there is a lot of trial and 
error and patience required to dial in the print settings that will achieve the intent of the design.  

An improvement to the electronics housings can come in the form of reducing the complexity of the button housing. Using larger momentary 
pushbuttons would eliminate the need for a more complex button assembly, improving the usability and assembly of the mount. 

While hooking up the electronics I learned it’s important to plan out wire lengths, routes and connections well ahead of time to avoid 
spending time correcting mistakes. Furthermore, I found it very useful to try new connectors and tricky connections on scrap wire first in 
order to both practice the assembly and prove the connection before commiting to the real thing. As being one person with only two hands, 
I found it extremely helpful to jig up fixtures on the bike to help with assembly in awkward positions.  

On looking back at this project, I’ve realized that a lot of the electronics used in this build can be replaced with cleaner, simpler 
components that would reduce the total assembly time and improve the robustness of the system. The LCD on the bike required a whopping 
nine wires to function, causing a big mess of wires on the bike. This can be replaced by using a display module with an SPI communication 
protocol requiring only four wires to function. Additionally, the stripboard Arduino circuit can be replaced by a custom PCB with screw 
terminal connectors making the wiring of the Arduino much simpler and robust.    
  
8.0 Acknowledgements 
^^^^^^^^^^^^^^^^^^^^

I would like to thank `Nicholas Chan <https://github.com/ngchan>`_ for writing the camera gimbal software that my speed control software 
is based off of. I’d also like to thank `Brett Beuaregard <https://github.com/br3ttb>`_ for writing the PID library and it’s excellent 
documentation that is the heart of the speed control software. Finally, I’d like to thank Jason Moore for his support and mentorship 
throughout this project.  

Stay tuned for part three of this series: Testing and Validation  

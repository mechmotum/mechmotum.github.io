================================================
A Web Application for Analyzing Bicycle Dynamics
================================================

:date: 2020-07-03 00:00:00
:tags: bicycle, web application
:category: research
:slug: bicycle-dynamics-web-application
:authors: Lyla Sanders
:summary: Blog post on creating a web application to serve as a GUI for bicycle
          dynamics.
:thumbnail: https://mechmotum.s3.us-east-005.dream.io/bicycle-dynamics-app.png

.. figure:: https://mechmotum.s3.us-east-005.dream.io/bicycle-dynamics-app.png
   :width: 800px
   :align: center
   :target: https://bicycle-dynamics.onrender.com

   Screenshot of the bicycle dynamics web app. Click the image to go to the app
   at https://bicycle-dynamics.onrender.com.

Background
----------

The BicycleParameters_ Python program provides a way for users to interact with
the 27 parameters laid out by the Whipple-Carvallo bicycle model. However, its
accessibility is limited to the programming experience of the user, and it can
be unweildy to manually work with.  To make the program more accessible, the
Bicycle Dynamics Web App was created to supply a graphical user interface for
the program as well as to enable a broader range of users to access it via the
web. The web app takes heavy inspiration from JBike6_, but aims to remove the
accessibility barriers inherent to MATLAB.

.. _BicycleParameters: https://github.com/moorepants/BicycleParameters
.. _JBike6: http://ruina.tam.cornell.edu/research/topics/bicycle_mechanics/JBike6_web_folder/index.htm

Building the App
----------------

Given that BicycleParameters was to be used as the backend for the website, it
made sense to use another Python based program to build the frontend. Dash_
from Plotly serves this purpose perfectly, providing us with a full set of html
components in addition to many custom made Javascript elements such as
datatables and value sliders.  Finally, the app is styled with `Dash Bootstrap
Components`_, so that only a very minimal amount of custom CSS had to be
written.

.. _Dash: https://dash.plotly.com
.. _Dash Bootstrap Components: https://dash-bootstrap-components.opensource.faculty.ai

Functionality
-------------

The Bicycle Dynamics Web App provides a graphical interface with 10 different
default parameter sets, a set of editable tables where users may adjust the
parameter values as they see fit, and two plots which are generated behind the
scenes from the datatable values. The geometry plot displays the essential
schematic and centers of mass of the bicycle, while the eigenvalue plot reveals
the self-stability of the bicycle as a function of its speed. Users may toggle
the centers of mass and intertia ellipsoid on the geometry plot, and they may
adjust the speed range for the eigenvalue plot.

Conclusion
----------

The Bicycle Dynamics Web App is currently deployed at
https://bicycle-dynamics.onrender.com and its github repository is located at
https://github.com/moorepants/BicycleParameters. Feel free to play around with
the app and provide suggestions or feedback!

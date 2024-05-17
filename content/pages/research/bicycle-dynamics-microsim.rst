===================================================
Bicycle Dynamics for Microscopic Traffic Simulation
===================================================

:status: hidden
:date: 2024-05-15
:collaborators: Jason Moore, Azita Dabiri, Frederik Schulte, Riender Happee 
:current_researchers: Christoph Schmidt, Anna Marbus
:research_theme: Cycling Safety
:template: project
:summary-sentence: We are investigating the influence of bicycle dynamics on the traffic conflict process to improve traffic simulation models towards predictive safety assessment of infrastructure improvements, smart cycling assistance systems, connectivity, and automated driving. 
:summary-image: https://objects-us-east-1.dream.io/mechmotum/social-force-example.png
:slug: research/bicycle-dynamics-microsim


Description
===========

Simulated safety assessment is a valuable prospective tool to understand the impact of 
new traffic infrastructure and novel innovations in the traffic sector 
like automated vehicles, cycling assistance systems, and intelligent connectivity. 
However, current traffic simulations are designed to model traffic flow and do 
not automatically enable reliable safety assessment, especially for cyclists. 

In this project, we investigate the influence of bicycle dynamics on the traffic 
conflict process. This aims to improve simulation models towards better representing
cyclist behavior and to add one potentially crucial factor on the way to capturing
conflict causality in simulation. Understanding the role of vehicle dynamics in 
conflicts may also contribute to developing safer vehicles, safer infrastructure, and
future assistance systems. 

For our analysis, we add explicit mechanical models of bicycle dynamics to existing 
traffic simulation frameworks. We collect data on cyclist conflict behavior in
controlled experimental conditions and natural traffic, calibrate the improved 
models to the observations, and evaluate the model performance in comparison to existing 
models without bicycle dynamics. 

Cyclist Social Forces
=====================

.. raw:: html

   <center>
   <video width="522" height = "347" controls>
	 <source src="https://objects-us-east-1.dream.io/mechmotum/socialforce_scenario_crossing_BMD2023.mp4" type="video/mp4">
   Your browser does not support the video tag.
   </video> 
   <p>Animation of an interaction simulationed by our cyclist social force model.</p>
   </center>
   
	
At the heart of our project lies the development of an interaction model for cyclists.  
We adapted the social force concept introduced by Helbing and Molnár [1]_ to accommodate 
models of bicycle dynamics and rider control. Our first conference paper from this 
project details the approach [2]_. It enables us to test different 
bicycle dynamic models with varying controllers in simulated conflict scenarios. The model 
is compatible with DLR's established open-source traffic simulation SUMO_ [3].

`A Python implementation of our current progress is available on GitHub.`__

.. _SUMO: https://eclipse.dev/sumo/
.. _cyclistsocialforce: https://github.com/chrismo-schmidt/cyclistsocialforce

__ cyclistsocialforce_

Ongoing Work
============

- **Rider control parameters for desired yaw inputs:**  Extracting the rider control parameters 
  from responses to desired yaw angle input collected in controlled riding experiments to calibrate 
  the bicycle dynamics.

- **Cyclist interaction behavior (Master's Graduation Project Anna Marbus):** Conducting a controlled 
  riding experiment and recording highly accurate dynamic data from on-bike sensors to understand the 
  behavior of cyclists in different traffic conflict scenarios. 

- **Native Cyclist Social Forces for SUMO:** Adding a new C++ implementation of our cyclist 
  social force model to the codebase of DLR's open-source simulator SUMO_ to make the model 
  generally available for use in traffic simulation.   
  


Research Output
===============

:Journal Articles:

	Schmidt, C. M., Dabiri, A., Schulte, F., Moore, J. K. & Happee, R. (2024). Cycling Safety Assessment in Microscopic Traffic Simulation: A Review and Methodological Framework [Manuscript submitted to Transportation Research Interdisciplinary Perspectives].

:Conference Papers:

	Schmidt, C. M., Dabiri, A., Schulte, F., Happee, R., & Moore, J. K. (2024). Essential Bicycle Dynamics for Microscopic Traffic Simulation: An Example Using the Social Force Model [Conference paper, accepted/in press]. In *The Evolving Scholar: BMD 2023 , 5th Edition*. TU Delft OPEN. https://doi.org/10.59490/65a5124da90ad4aecf0ab147

		Supplementary Material
			Schmidt, C. M., Dabiri, A.; Schulte, F., Happee, R.; Moore, J. K. (2024): Supplementary Material of "Essential Bicycle Dynamics for Microscopic Simulation" - Experiments & Plots [Software].  4TU.ResearchData. https://doi.org/10.4121/574cd504-ad56-4234-8d48-c10931d13204
			
			`Also available on GitHub.`__
			
:Conference Abstracts and Posters:

	Schmidt, C. M., Dabiri, A., Schulte, F., Happee, R., & Moore, J. K. (2023). Essential Bicycle Dynamics for Microscopic Traffic Simulation: An Example Using the Social Force Model [Extented abstract]. In *The Evolving Scholar: BMD 2023 , 5th Edition*. TU Delft OPEN. https://doi.org/10.59490/649d4037c2c818c6824899bd

	Schmidt, C. M., Moore, J. K., Dabiri, A., Happee, R., & Schulte, F. (2023). Connected Traffic of Vulnerable Bicyclists and Automated Vehicles: Deep Learning Trajectory Generation for Realistic Simulated Bicycle Intersection Crossings. Poster session presented at SUMO User Conference 2023, Berlin, Germany. http://resolver.tudelft.nl/uuid:77d1435a-f7dc-4ad3-a12e-3bbc2ba60038

:Conference Presentations:

	Schmidt, C. M. (2023, October 18).	Essential Bicycle Dynamics for Microscopic Traffic Simulation: An Example Using the Social Force Model [Conference presentation]. Symposium on the Dynamics and Control of Single Track Vehicles (BMD 2023), Delft, The Netherlands.
	
.. _bmd2023suppl: : https://github.com/chrismo-schmidt/bmd2023-supplements-bike-dynamics-microsim/

__ bmd2023suppl_

Contact
=======

If you want to learn more about the project, are interested in collaboration, or are looking for Master's and Bachelor's Thesis project opportunities, please **reach out!**  

| **Christoph M. Schmidt (Dipl.-Ing.)** - he | him
| *PhD Candidate, TU Delft*
| ---
| Biomechatronics & Human-Machine Control
| Department of Biomechanical Engineering (BmE)
| Faculty of Mechanical Engineering (ME)
| Delft University of Technology
| Mekelweg 2, 2628CD, Delft, The Netherlands
| ---
| Email_ | LinkedIn_ | ResearchGate_ | GitHub_ | `TU Delft`__

.. _Email: mailto:c.m.schmidt@tudelft.nl  
.. _LinkedIn: https://www.linkedin.com/in/chm-schmidt/
.. _ResearchGate: https://www.researchgate.net/profile/Christoph-Schmidt-30
.. _Github: https://github.com/chrismo-schmidt 
.. _TUD: https://www.tudelft.nl/en/staff/c.m.schmidt/

__ TUD_

References
==========

.. [1]  Helbing, D., & Molnár, P. (1995). Social force model for pedestrian dynamics. Physical Review E, 51(5), 4282–4286. https://doi.org/10.1103/PhysRevE.51.4282

.. [2]  Schmidt, C. M., Dabiri, A., Schulte, F., Happee, R., & Moore, J. K. (2024). Essential Bicycle Dynamics for Microscopic Traffic Simulation: An Example Using the Social Force Model (Conference paper, accepted/in press). In *The Evolving Scholar: BMD 2023 , 5th Edition*. TU Delft OPEN. https://doi.org/10.59490/65a5124da90ad4aecf0ab147

.. [3]  Lopez, P. A., Behrisch, M., Bieker-Walz, L., Erdmann, J., Flötteröd, Y.-P., Hilbrich, R., Lücken, L., Rummel, J., Wagner, P., & Wiessner, E. (2018). Microscopic Traffic Simulation using SUMO. 2018 21st International Conference on Intelligent Transportation Systems (ITSC), 2575–2582. https://doi.org/10.1109/ITSC.2018.8569938

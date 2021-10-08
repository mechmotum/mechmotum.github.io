=====================================
LibreTexts Jupyter Integration Wrapup
=====================================

:date: 2021-10-08
:authors: Jason K. Moore
:category: education
:tags: jupyter,libretexts,computation,education,oer,textbooks

.. figure:: https://objects-us-east-1.dream.io/mechmotum/libretexts-plus-jupyter.png
   :align: center

As of September 30th we have wrapped up our work integrating Jupyter based
computing tools into the LibreTexts_ platform. This work was part of a three
year $5M grant from the U.S. Department of Education (DoE) to enhance open
access textbooks called `Open Textbooks Pilot Program`_ (CFDA No. 84.116T).

.. _LibreTexts: https://www.libretexts.org
.. _Open Textbooks Pilot Program: https://www.ed.gov/news/press-releases/us-department-education-awards-49-million-grant-university-california-davis-develop-free-open-textbooks-program

This blog post serves as a report on the outcomes from the portion of the grant
I was responsible for as a co-principal investigator. Overall, I think we were
quite successful. LibreTexts users are creating textbooks with interactive
computational elements (10+ textbooks), we've served hundreds of students with
our JupyterHub, and we've trained 12 undergraduate students in full stack
development, system administration, and site reliability engineering with many
of them now in professional positions making use of those skills.

Project Goals
=============

The overall goals of the DoE grant were multifold and we contributed to one
small chunk. Our project was part of *"Thrust 3: Next Generation Technology -
Interactive Visualizations, Automated Assessment, Annotations, Database
Integration, & Technological Synergy"*. Here is what I proposed we would do in
the grant proposal:

   3C: Interactive Figure Editor (Jason K. Moore).

   While the CalcPlot3D application provides powerful, simple-to-use,
   specialized 3D visualizations, many LibreTexts authors also desire arbitrary
   interactive visualizations illustrating concepts in any scientific domain.
   It is known that quality figures enhance learning when adjunct to text
   regardless if the figures are static, dynamic, or interactive,[18,40] but
   research demonstrating whether interactivity improves learning is nascent.
   In computer science education, there is evidence that interactive
   visualizations of computer algorithms improve learning when they are self
   paced and of high quality[41–43] but may hamper learning if poorly
   designed.[44,45] There is recent evidence that interactivity is especially
   beneficial for lower performing students.[46] Cutting edge interactive
   visualizations demonstrate how concepts are learned through exploration [47]
   and modern publishing platforms are adopting interactive figures for high
   level scientific communication (Authorea)[48] as well as for the public
   (e.g.  New York Times). This will enable LibreText to become a platform for
   research into the benefits of interactive figures in addition to providing
   authors with infinite interactive visualization possibilities to convey
   concepts (see Figure 4 for examples). To do so, we will implement general
   functionality for authors to easily include any type of interactive figure
   through a new "interactive figure editor" that relies on the Jupyter
   interactive widget system, ipywidgets.[49]

   Jupyter is a popular open source web application that allows users to create
   and share interactive documents that contain equations, visualizations,
   narrative text, and the execution of code.[50] LibreTexts authors will be
   able to write high level code in the Python programming language in the
   LibreTexts editing interface to generate figures. On page save, the Python
   code will be sent to an external server where it will be executed in a
   secure container using Jupyter to generate an entry in an open access
   database of versioned interactive Javascript figures.

By the time the grant period started, the specific goals solidified into three
primary aims and two ancillary aims:

**Primary**

1. Allow textbook authors and readers to execute code that produces passive and
   interactive figures
2. Allow any reader of a LibreTexts textbook page to execute code interactively
3. Add Jupyter enabled textbooks and portions of textbooks to LibreTexts

**Ancillary**

1. Provide a JupyterHub for LibreTexts and UC Davis users
2. Train students in full stack development, system administration, and site
   reliability engineering

Below, each section describes the various things we produced to meet these
goals. Developing a system like this from scratch is an enormous task, so it is
important to note that we built everything off of the strong open source
foundation of the greater Jupyter community and various other connected
projects.

UC Davis Kubernetes Cluster
===========================

We decided to build and run our own `bare metal`_ Kubernetes_ computing
cluster.  We chose to do this instead of using cloud services because the 5-10
year cost projection seemed to be more favorable. We also had the expertise and
existing hardware available to pilot the system. After two build and test
iterations, we now have a 19 node cluster that runs JupyterHub and BinderHub on
top of Kubernetes for UC Davis and LibreTexts users. The cluster has several
notable features:

- Puppet based deployment that allows us to  tear down and rebuild the cluster
  with one command
- Monitoring and alerts via Prometheus and Grafana
- Large redundant ZFS data storage node
- High availability entry point server pair
- Custom user abuse sensors and process killers

.. figure:: https://objects-us-east-1.dream.io/mechmotum/ucd-kube-cluster.png
   :align: center

   The cluster humming away in the server room.

.. _bare metal: https://en.wikipedia.org/wiki/Bare-metal_server
.. _Kubernetes: https://kubernetes.io/

JupyterHub
==========

We run JupyterHub on the cluster that defaults to the latest JupyterLab
interface for interacting with the available programming languages. The
JupyterHub is accessible at both https://jupyter.libretexts.org and
https://jupyterhub.ucdavis.edu. Anyone with a UC Davis email address can log in
and make use of the hub. We've served over 400 users over the last couple of
years, most from various UC Davis and LibreTexts courses. We developed a FAQ_
that provides instructions for more advanced use. We also created a section in
the LibreTexts `construction guide`_ that provides guidance specifically for
LibreTexts users and authors.

.. figure:: https://objects-us-east-1.dream.io/mechmotum/libretexts-jupyterhub-login-page.png
   :align: center

   LibreTexts UC Davis JupyterHub Login Screen

.. figure:: https://objects-us-east-1.dream.io/mechmotum/libretexts-jupyter-guide.png
   :align: center

   Author construction guide section about Jupyter integration

.. _FAQ: https://jupyterhub.ucdavis.edu/hub/faq
.. _construction guide: https://chem.libretexts.org/Courses/Remixer_University/LibreTexts_Construction_Guide/05%3A_Interactive_Elements

Custom Docker Image
===================

The default repo2docker_ based docker image for our our hub includes a large
set of software. We manage the software dependencies using APT and Mamba_, with
most packages installed via Mamba from the conda-forge_ channel. Managing an
image with a large set of software packages in a single environment has been
rather difficult due to hard-to-solve version compatibilities, relying on
packages that languish in maintenance, user desire for different versions of
some packages, packages not being available in conda-forge, slow build times,
and large docker image sizes. We've wrestled with these issues for three years,
but things are reasonably smooth at this point. New images are immediately
cached on all of our cluster nodes so that user load times are snappy and the
vast majority of needed software is pre-installed.

Our repo2docker build specs for the image can be found here:

https://github.com/LibreTexts/default-env

This image is a nice starting image for many scientific computing situations as
it includes Python, R, Julia, Octave, C++, and Sage in the console and
notebooks as well as RStudio server access to R.

.. figure:: https://objects-us-east-1.dream.io/mechmotum/libretexts-jupyterhub-jupyterlab-launch.png
   :align: center

   JupyterLab Interface

.. figure:: https://objects-us-east-1.dream.io/mechmotum/libretexts-rstudio.png
   :align: center

   RStudio Interface

.. _repo2docker: https://github.com/jupyterhub/repo2docker
.. _Mamba: https://github.com/mamba-org/mamba
.. _conda-forge: https://conda-forge.org/

CKEditor Thebe Plugin
=====================

Thebe_ is a JavaScript application that enables live Jupyter code cells to be
integrated into an arbitrary HTML page. Viewers of the HTML page can interact
with the cells by editing and executing them. Once executed the output can be
simple text output or advanced Javascript based interactive visualizations.
Thebe was originally developed as part of Europe's OpenDreamKit_ project and
ties into the Jupyter ecosystem. There are some alternatives to Thebe, but they
offered essentially the same features. Because of this we more-or-less flipped
a coin and chose to make use of Thebe in LibreTexts. LibreTexts uses the
CKEditor for WYSIWYG editing of textbook pages. Once we settled on using Thebe
for LibreTexts pages, we developed a plugin for CKEditor_ that allows page
authors to edit and execute code cells. The plugin can be found here:

https://github.com/LibreTexts/ckeditor-binder-plugin

The plugin allows authors to:

- Insert code cells and run them from CKEditor to check their execution.
- Embed the code cell with or without the output of the cell.
- Embed the code cell with or without the code of the cell displayed to
  readers.
- Set the cells to uneditable by the LibreTexts readers.

.. raw:: html

   <center>
   <iframe width="560" height="315"
   src="https://www.youtube.com/embed/dIwZ-QQ8xSs" title="YouTube video player"
   frameborder="0" allow="accelerometer; autoplay; clipboard-write;
   encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
   <p>Video showing how to use the plugin on LibreTexts</p>
   </center>

LibreTexts page authors can get started with the above video and the
instructions_ in the guide.

.. _instructions: https://chem.libretexts.org/Courses/Remixer_University/LibreTexts_Construction_Guide/05%3A_Interactive_Elements/5.02%3A_Jupyter_Notebooks_(Executable_Programming_Code_and_Figures)

.. _Thebe: https://github.com/executablebooks/thebe
.. _OpenDreamKit: https://opendreamkit.org/
.. _CKEditor: https://ckeditor.com/

Thebe Improvements
==================

After selecting Thebe and developing the CKEditor plugin we discovered that
ipywidgets_ did not fully function with Thebe. We had planned to use ipywidgets
to offer LibreTexts readers interaction with figures and visualization using
GUI widgets (sliders, buttons, input boxes, etc.). We set out to remedy this
and began contributing to Thebe. In the fall of 2020, we organized a sprint_
for Thebe during JupyterCon which helped breathe some life into the project.
With the help of the original Thebe developer, `Executable Book Project`_
members, Curvenote_ project members, and JupyterCon sprint attendees we knocked
out a number of outstanding issues (see the `Github project`_ for details).
Since the sprint, there have been regular contributions to the repository and
we've made three releases of Thebe that have added a number of import new
features and bug fixes. Most importantly we recently merged the fix to fully
enable ipywidgets support. Here are some of the major improvements made during
and since the sprint:

- Improved the documentation, including examples of more advanced cell outputs
- Thebe now uses JupyterLab 3.0 APIs
- Added a configuration for read-only cells
- Improved unit testing infrastructure
- Thebe now persists binder sessions across pages on the same domain
- A "Restart & Run All" button is now available on each cell
- Each cell has a "busy indicator" to give the user feedback from the server
- Enabled general ipywidgets functionality

.. figure:: https://objects-us-east-1.dream.io/mechmotum/thebe-ipywidgets.gif
   :height: 600px
   :align: center

   Example of an ipywidget controlling a matplotlib figure in Thebe.

You can see examples many of the rich Jupyter outputs on this LibreTexts page:

https://query.libretexts.org/Sandboxes/jupyterteam_at_ucdavis.edu

.. _ipywidgets: https://github.com/jupyter-widgets/ipywidgets
.. _sprint: https://jupytercon.com/sprint/
.. _Executable Book Project: https://executablebooks.org
.. _Curvenote: https://curvenote.com/
.. _Github project: https://github.com/executablebooks/thebe/projects/1

Supporting Classes
==================

We piloted the JupyterHub and LibreTexts in several courses over the last three
years:

- GEL 56: Introduction to Geophysics, GEL 161: Geophysical Field Methods (Prof.
  Magali Billen, UC Davis)
- GEL 160: Geological Data Analysis (Prof. Max Rudolph, UC Davis)
- GEL 298 (Profs. Sarah Stewart & Max Rudolph, UC Davis)
- STS 101: Introduction to Data Studies (Prof. Lindsay Nicole Poirier)
- ENG 122: Introduction to Mechanical Vibrations, MAE 223: Multibody Dynamics
  (Prof. Jason K. Moore, UC Davis)
- Cheminformatics OLCC (Prof. Robert Belford et al., University of Arkansas at
  Little Rock)

The cheminformatics course was a collaboration among several universities and
partners. This published paper details more about that effort:

   Kim et al. (2020), Teaching Cheminformatics through a Collaborative
   Intercollegiate Online Chemistry Course (OLCC), Journal of Chemical
   Education, https://doi.org/10.1021/acs.jchemed.0c01035

.. figure:: https://objects-us-east-1.dream.io/mechmotum/libretexts-cheminformatics-poster.png
   :align: center

   Conference poster about the cheminformatics project.

ngshare
=======

During our efforts to get professors to adopt the hub at UC Davis, we found out
that many wanted to use nbgrader_ for auto-grading of Jupyter notebooks. But
nbgrader was only built for servers that had a standard shared user space
storage with a UNIX permission model. Thus, nbgrader could not function in a
JupyterHub running on a distributed system like Kubernetes. Computer science
professor, Christopher Nitta, and I proposed a computer science capstone BSc
project and attracted a talented group of students. This group invented
**ngshare**, which solves the problem by running a data exchange database on a
Kubernetes pod that can be swapped out for nbgrader's traditional shared disk
space. This resulted in three code repositories with the software required to
run the service:

`ngshare <https://github.com/LibreTexts/ngshare>`_
   Primary repository containing the ngshare application.
`ngshare-helm-repo <https://github.com/LibreTexts/ngshare-helm-repo>`_
   A ready made Helm chart for deploying to kubernetes.
`ngshare_exchange <https://github.com/LibreTexts/ngshare_exchange>`_
   Exchange used to run ngshare on single user space systems (non distributed
   systems).

.. raw:: html

   <center>
   <iframe width="560" height="315"
   src="https://www.youtube.com/embed/SEJCaqD7xXQ" title="YouTube video player"
   frameborder="0" allow="accelerometer; autoplay; clipboard-write;
   encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
   <p>Demo video of ngshare</p>
   </center>

.. _nbgrader: https://github.com/jupyter/nbgrader

LibreTexts Textbooks Using Jupyter Integration
==============================================

There are at least 10 textbooks now on LibreTexts that make use of the Jupyter
integration for a variety of different programming languages.

Python

- `Introduction to Geophysics <https://geo.libretexts.org/Courses/University_of_California_Davis/GEL_056:_Introduction_to_Geophysics>`_ (Magali Billen, University of California, Davis)
- `Introduction to Programming Concepts - Python <https://eng.libretexts.org/Courses/Delta_College/Introduction_to_Programming_Concepts_-_Python>`_ (Chuck Severance, University of Michigan)
- `Matrix Algebra with Computational Applications <https://math.libretexts.org/Bookshelves/Linear_Algebra/Matrix_Algebra_with_Computational_Applications_(Colbry)>`_ (Dirk Colbry, Michigan State University)
- `Introduction to Engineering for Engineers and Scientists <https://eng.libretexts.org/Bookshelves/Introduction_to_Engineering/EGR_1010:_Introduction_to_Engineering_for_Engineers_and_Scientists>`_
- `Python for Everybody <https://eng.libretexts.org/Bookshelves/Computer_Science/Programming_Languages/Book%3A_Python_for_Everybody_(Severance)>`_ (Chuck Severance, University of Michigan)
- `Chemistry Interactive Applications <https://chem.libretexts.org/Ancillary_Materials/Interactive_Applications/Jupyter_Notebooks>`_

.. figure:: https://objects-us-east-1.dream.io/mechmotum/libretexts-robot-sim.png
   :align: center

   Example interactive robot arm simulator from Matrix Algebra with
   Computational Applications (Colbry)

R

- `Cheminformatics <https://chem.libretexts.org/Courses/Intercollegiate_Courses/Cheminformatics_OLCC_(2019)>`_
- `Visual Statistics Use R <https://stats.libretexts.org/Bookshelves/Introductory_Statistics/Book:_Visual_Statistics_Use_R_(Shipunov)>`_ (Alexey Shipunov, Minot State University)
- `Answering Questions with Data - Introductory Statistics for Psychology Students <https://stats.libretexts.org/Bookshelves/Applied_Statistics/Book:_Answering_Questions_with_Data_-__Introductory_Statistics_for_Psychology_Students_(Crump)>`_ (Matthew J. C. Crump, Brooklyn College of CUNY)

Julia

- `Scientific Computing <https://math.libretexts.org/Bookshelves/Scientific_Computing_Simulations_and_Modeling/Book:_Scientific_Computing_(Staab)>`_ (Peter Staab, Fitchburg State University)

Octave

- `Introduction to Control Systems <https://eng.libretexts.org/Bookshelves/Industrial_and_Systems_Engineering/Book:_Introduction_to_Control_Systems_(Iqbal)>`_ (Karmran Iqbal, University of Arkansas at Little Rock)

Shell, Python, R

- `Internet of Science Things <https://chem.libretexts.org/Courses/Intercollegiate_Courses/Internet_of_Science_Things_(2020)>`_ (Robert Belford, University of Arkansas at Little Rock)

.. raw:: html

   <center>
   <iframe width="560" height="315"
   src="https://www.youtube.com/embed/gA9s0NQRVzY" title="YouTube video player"
   frameborder="0" allow="accelerometer; autoplay; clipboard-write;
   encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
   <p>Three of the book authors (Belford, Billen, Iqbal) present their use of
   Jupyter in LibreTexts.</p>
   </center>

Outreach
========

We did a number of outreach talks. This was important for disseminating what we
had done, but also in helping the students develop their presenting skills and
connecting them to the communities of practice. We presented at Jupyter Open
Studio (2019), SacPy (2020), OpenEd Week (2020), Women in Data (2020), and the
National Workshop on Data Education (2020).

.. figure:: https://objects-us-east-1.dream.io/mechmotum/celine-sacpy.jpg
   :align: center
   :width: 600px

   Hao, Tannavee, and Celine presenting at the SacPy meetup in 2019.

.. raw:: html

   <center>
   <iframe width="560" height="315"
   src="https://www.youtube.com/embed/l-OVteC4PpA" title="YouTube video player"
   frameborder="0" allow="accelerometer; autoplay; clipboard-write;
   encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
   <p>OpenEd Week Webinar</p>
   </center>

The Team
========

It is important to point out that all of the work to bring Jupyter to
LibreTexts was done by a group of amazing undergraduate students over the last
three years. Richard Feltstykket and I mentored them and couldn't have asked
for a better group. Overall, we had 12 students work from 2 quarters to a whole
year on the project. They developed their teamwork process and onboarded new
students every other quarter. Many of the the students particpated during the
height of the COVID 19 pandemic. I have been thoroughly impressed with them and
their work. They came to the project with minimal to no knowledge about the
assortment of tools and skills that they needed to solve the presented
problems. The skillset needed for them to succeed was very broad, from building
servers all the way up the stack to frontend Javascript app development. The
students vacuumed up the knowledge, learned the skills, and it wasn't before
long that they all knew way more than their two mentors (which is the agenda of
all good mentors). As far as I can tell, this has paid off for many of them.
Some have taken positions doing very similar work to what they did in this
project. And outside of the work, the students led us through an assortment of
online games during our quarterly social breaks. I'll have nightmares about
Jackbox Trivia Murder Party for some time to come :). Without further ado, here
is it the team that made all of this magic happen:

.. list-table::
   :class: table
   :width: 48%
   :align: center

   * - .. image:: https://objects-us-east-1.dream.io/mechmotum/libretexts-headshot-celine.png
     - .. image:: https://objects-us-east-1.dream.io/mechmotum/libretexts-headshot-hao.jpg
     - .. image:: https://objects-us-east-1.dream.io/mechmotum/libretexts-headshot-henry.jpg
   * - Celine Liang (now @ Facebook)
     - Hao Huang (now @ Zillow)
     - Henry Agnew (now @ UC San Diego)
   * - .. image:: https://objects-us-east-1.dream.io/mechmotum/libretexts-headshot-kevin-k.png
     - .. image:: https://objects-us-east-1.dream.io/mechmotum/libretexts-headshot-kevin-r.png
     - .. image:: https://objects-us-east-1.dream.io/mechmotum/libretexts-headshot-mandeepika.jpg
   * - Kevin Krausse (now @ Ekata)
     - Kevin Rong (now @ Zoox)
     - Mandeepika Sani (UC Davis)
   * - .. image:: https://objects-us-east-1.dream.io/mechmotum/libretexts-headshot-noah.png
     - .. image:: https://objects-us-east-1.dream.io/mechmotum/libretexts-headshot-patrick.jpg
     - .. image:: https://objects-us-east-1.dream.io/mechmotum/libretexts-headshot-tannavee.png
   * - Noah Sanders (UC Davis)
     - Patrick Mackle (now @ DocuSign)
     - Tannavee Kumar (now @ Tempus Labs)
   * - .. image:: https://objects-us-east-1.dream.io/mechmotum/libretexts-headshot-tim.png
     - .. image:: https://objects-us-east-1.dream.io/mechmotum/libretexts-headshot-xiaochen.png
     - .. image:: https://objects-us-east-1.dream.io/mechmotum/libretexts-headshot-luigi.png
   * - Tim Stewart (UC Davis)
     - Xiaochen Zeng (now @ Tencent)
     - Xin Luigi Chen (now @ VMware)

|
|

Additionally, students Kevin Rong, Lawrence Lee, Eric Li, Abigail Almanza
co-developed ngshare.

Congratulations on a job well done!

We also had tons of help and support from a number of folks. Special thanks
goes out to: Bob Belford & team, Chris Holdgraf, Christopher Nitta, Delmar
Larsen, Hongfei Wang, Lindsay Nicole Poirier, Max Rudolph, Michael Casper
Lewis, Magali Billen, Min Ragan-Kelley, Paul Ivanov, Sarah Stewart, Steve
Purves, Tim Head, Tom Neubarth, Yuvi Panda, and likely others that I am
forgetting.

And I give the most special thanks to Richard Feltstykket for being an amazing
partner in this project. We couldn't have pulled it off without his extensive
knowledge and resources regarding the cluster development and system
administration. Richard had some major things to deal with outside of work
during these three years but he never showed any slowing down or loss of
enthusiasm. He has my full admiration. I'll miss working with you Richard,
hopefully we can start up something new in the future! The project is in great
hands.

.. figure:: https://objects-us-east-1.dream.io/mechmotum/lab-pizza-outing.png
   :align: center

   Pre-pandemic pizza social with the team. From the left around the table:
   Celine, Michael, Trevor, Henry, Jason, Hao, Luigi, Tannavee.

The Future
==========

The future for the system and tools we've developed as a part of this grant
look good. Richard Feltstykket is taking the project forward with LibreText's
support. The cluster, JupyterHub, and LibreTexts page integration will continue
to support a variety of instructors, courses, and students. The next big step
is to scale up use for courses at UC Davis and LibreTexts participating
universities. I certainly hope to see things grow now that it is all running
smoothly.

Resources
=========

`Lab project page <{filename}/pages/research/libretexts-jupyter.rst>`_

Code repositories
-----------------

`ckeditor-binder-plugin <https://github.com/LibreTexts/ckeditor-binder-plugin>`_
   CKEditor plugin that adds a button to add Jupyter code cells via Thebe.
`ckeditor-query-plugin <https://github.com/LibreTexts/ckeditor-query-plugin>`_
   CKEditor plugin to add buttons for LibreTexts' Query and Adapt systems.
`default-env <https://github.com/LibreTexts/default-env>`_
   Our custom JupyterHub repo2docker spec.
`galaxy-vagrant <https://github.com/LibreTexts/galaxy-vagrant>`_
   Vagrant setup for testing our galaxy cluster
`jupyterhub-templates <https://github.com/LibreTexts/jupyterhub-templates>`_
   JupyterHub HTML templates that add the About and FAQ pages.
`jupyterteam_widget <https://github.com/LibreTexts/jupyterteam_widget>`_
   Example Jupyter widget used for learning how Jupyter widgets work.
`labextension-libretexts-faq <https://github.com/LibreTexts/labextension-libretexts-faq>`_
   JupyterLab extension that adds an FAQ link in the menu bar.
`metalc <https://github.com/LibreTexts/metalc/>`_
   Primary documentation and issue tracker for the project.
`ngshare <https://github.com/LibreTexts/ngshare>`_
   Primary repository containing the ngshare application.
`ngshare_exchange <https://github.com/LibreTexts/ngshare_exchange>`_
   Exchange used to run ngshare on single user space systems (non distributed
`ngshare-helm-repo <https://github.com/LibreTexts/ngshare-helm-repo>`_
   A ready made Helm chart for deploying to kubernetes.
`protogalaxy <https://github.com/LibreTexts/protogalaxy>`_
   Puppet module bootstrapping highly available Kubernetes cluster using
   kubeadm, keepalived and HAProxy
`widget-testing <https://github.com/LibreTexts/widget-testing>`_
   Extensive tests for various advanced Jupyter cell outputs in Thebe and
   LibreTexts.

Prior blog posts
----------------

The students wrote (almost-)quarterly blog posts throughout the project
duration. These have more details on the various topics discussed above. Here
are all of the prior posts:

- `Grant Award Announcement <{filename}/libretexts-grant.rst>`_
- `Winter 2019 Update <{filename}/jupyter-winter-2019.rst>`_
- `Summer 2019 Update <{filename}/jupyter-summer-2019.rst>`_
- `SacPy Talk <{filename}/sacpy-slidedeck-2019.rst>`_
- `Spring 2020 Update <{filename}/libretexts-jupyter-plugin.rst>`_
- `Summer 2020 Update <{filename}/jupyter-summer-2020.rst>`_
- `Fall 2020 Update <{filename}/jupyter-fall-2020.rst>`_
- `Summer 2021 Update <{filename}/jupyter-summer-2021.rst>`_

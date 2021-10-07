=====================================
Libretexts Jupyter Integration Wrapup
=====================================

:date: 2021-10-01
:authors: Jason K. Moore
:category: education
:tags: jupyter,libretexts

As of September 30th, we have wrapped up our work intergrating Jupyter based
computing tools into the Libretexts website. This work was part of a three year
$5M grant from the U.S. Department of Education (DoE) to enhance open access
textbooks called `Open Textbooks Pilot Program`_ (CFDA No. 84.116T).

.. _Open Textbooks Pilot Program: https://www.ed.gov/news/press-releases/us-department-education-awards-49-million-grant-university-california-davis-develop-free-open-textbooks-program

This blog post serves as a report on the outcomes from the portion of the grant
I was responsible for as a Co-Principal Investigator. Overall, I think we were
quite successful. Libretexts users are creating textbooks with interactive
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
   visualizations demonstrate how concepts are learned through exploration47
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

By the time we received the money and the grant period started the specific
goals solidified into three primary aims and two ancillary aims:

**Primary**

1. Allow any reader of a libretexts textbook page to execute code interactively
2. Allow textbook authors and readers to execute code that produces passive and
   interactive figures
3. Add Jupyter enabled textbooks and portions of textbooks to LibreTexts

**Ancillary**

1. Provide a JupyterHub for LibreTexts and UC Davis users
2. Train students in full stack development, system administration, and site
   reliability engineering

Below each section describes the various things we produced to meet these
goals. Developing a system like this from scratch is an enormous task, so it is
important to note that we built everything off of the inc rebel open source
foundation of greater Jupyter community and various other essential projects.

UC Davis Kubernetes Cluster
===========================

We decided to build and run our own `bare metal`_ Kubernetes computing cluster.
We chose to do this instead of using cloud services because the 5-10 year costs
projection seemed to be more favorable. We also had the expertise and existing
hardware available to pilot the system. After two build and test iterations, we
now have a 19 node cluster that runs JupyterHub and BinderHub for UC Davis and
LibreTexts users. The cluster has several notable features:

- Puppet based deployment (we can tear down and rebuild the cluster with one
  command)
- Monitoring and alerts via Promethesu and Grafana
- ZFS data storage node
- High availability entry point server pair
- Custom user abuse sensors and process killers

.. _bare metal: https://en.wikipedia.org/wiki/Bare-metal_server

Custom Docker Image
===================

The default repo2docker_ based docker image for our our hub includes a large
set of software. We manage the software dependencies using APT and Mamba_, with
most packages installed via Mamba from the conda-forge_ channel. Managing an
image with a large set of software packages in a single environment has been
rather difficult due to hard to solve version compatibilities, packages that
aren't kept up-to-date, user desire for different versions of some packages,
packages not being available in conda-forge, slow build times, and large docker
image sizes. We've wrestled with these issues for three years, but things are
reasonably smooth at this point. New images are immediately cached on all of
our cluster nodes so that user load times are snappy and the vast majority of
needed software is pre-installed. We'd like hard pins to work better with Conda
so that software updates are more easily managed.

Our build specs for the image can be found here:

https://github.com/LibreTexts/default-env

It should be a nice starting image for many scientific computing situations as
it includes Python, R, Julia, Octave, C++, and Sage in the console and
notebooks as well as Rstudio server access to R.

.. _repo2docker: https://github.com/jupyterhub/repo2docker
.. _Mamba: https://github.com/mamba-org/mamba
.. _conda-forge: https://conda-forge.org/

JupyterHub
==========

The JupyterHub is accessible at https://jupyter.libretexts.org and
https://jupyterhub.ucdavis.edu.

JupyterHub & Rstudio Server Class Support

CKEditor Thebe Plugin
=====================

Thebe is a javascript application that enables live Jupyter code cells to be
integrated into an arbitrary HTML page. Viewers of the HTML page can interact
with the cells by editing and  executing them. Once executed the output can be
simple text output or advanced javascript based itneractive visualizations.
Thebe was orginally developed as part of Europe's OpenDreamKit project and ties
into the Jupyter ecosystem. There are soem alternatives to Thebe, but those did
not seem to offer anything more than Thebe. Once we settled on using Thebe for
LIbretexts pages, we developed a plugin for the CKEditor that allows page
authors to eidt and check code cells. LibreTexts uses the CKEditor for WYSIWYG
editing of textbook pages.

The plugin allows authors to:

- Insert code cells and run them from CKEditor to check their execution.
- Embed the code cell with or without the output of the cell.
- Embed the code cell with or without the code of the cell displayed to
  readers.
- Set the cells to uneditable by the LIbretexts readers.

https://opendreamkit.org/

https://github.com/LibreTexts/ckeditor-binder-plugin

https://ckeditor.com/

Thebe Improvements
==================

After selecting Thebe and developing the CKEditor plugin we discovered that
ipywidgets did not fully function with Thebe. We had planned to use ipywidgets
to offer Libretexts readers interaction with figures and visualization using
GUI widgets (sliders, buttons, input boxes, etc.). We set out to rememdy this
and began contributing to THebe. In the fall of 2020 we organized a sprint for
Thebe during Jupytercon which helped breathe some life into the project, along
with Executable Books and Curenote project members. We've made three releasese
of Tehbe since then that have added a number of import new features and bug
fixes, cinluding fully enabling ipytwidget support.

- Improved the documetnation, cinlding examples of advacned cell outputs
- Added a configuration for read-only cells
- Use JupyterLab 3.0 APIs
- Improved unit testing infrastrcuture
- Persist binder sessions across pages
- Restart & Run all
- Busy indicator
- Fixed ipywidget interaction

You can see many of the rich Jupyter outputs on this page:

https://query.libretexts.org/Sandboxes/jupyterteam_at_ucdavis.edu

Supporting Classes
==================

ngshare
-------

During our efforts to get professors to adopt the hub at UC Davis, we found out
that many wanted to use nbgrader_ for auto-grading of Jupyter notebooks. But
nbgrader was only built for servers that had a standard shared user space
storarge with a UNIX permission model. Thus nbgrader could not function in a
kubernetes backed JupyterHub. Chris X and I proposed a computer science
capstone BSC project and attracted a group of students for the project. This
group evented ngshare, which solves the problem by running a data excahnge
database on a kubernetes pod that can be swapped out for nbgrader's traditoinal
shared disk space.

.. _nbgrader: https://github.com/jupyter/nbgrader

https://github.com/LibreTexts/ngshare
https://github.com/LibreTexts/ngshare_exchange
https://github.com/LibreTexts/ngshare-helm-repo

LibreTexts Textbooks Using Jupyter Integration
==============================================

Introduction to Geophysics


R:

- `https://chem.libretexts.org/Courses/Intercollegiate_Courses/Cheminformatics_OLCC_(2019)`
- `https://stats.libretexts.org/Bookshelves/Introductory_Statistics/Book:_Visual_Statistics_Use_R_(Shipunov)`
- `https://stats.libretexts.org/Bookshelves/Applied_Statistics/Book:_Answering_Questions_with_Data_-__Introductory_Statistics_for_Psychology_Students_(Crump)`

Julia

- `https://math.libretexts.org/Bookshelves/Scientific_Computing_Simulations_and_Modeling/Book:_Scientific_Computing_(Staab)`

Python

- `https://eng.libretexts.org/Courses/Delta_College/Introduction_to_Programming_Concepts_-_Python`
- `https://geo.libretexts.org/Courses/University_of_California_Davis/GEL_056:_Introduction_to_Geophysics`
- `https://math.libretexts.org/Bookshelves/Linear_Algebra/Matrix_Algebra_with_Computational_Applications_(Colbry)`
- `https://eng.libretexts.org/Bookshelves/Introduction_to_Engineering/EGR_1010:_Introduction_to_Engineering_for_Engineers_and_Scientists`
- `https://eng.libretexts.org/Bookshelves/Computer_Science/Programming_Languages/Book%3A_Python_for_Everybody_(Severance)`

Shell, Ptyon, R:

- `https://chem.libretexts.org/Courses/Intercollegiate_Courses/Internet_of_Science_Things_(2020)`

Octave

- `https://eng.libretexts.org/Bookshelves/Industrial_and_Systems_Engineering/Book:_Introduction_to_Control_Systems_(Iqbal)`

Other:

- `https://query.libretexts.org/Sandboxes/hdagnew@ucdavis.edu/Jupyter_Widgets`
- `https://chem.libretexts.org/Ancillary_Materials/Interactive_Applications`


Students presenting
===================

SacPy
Women in Tech

The Future
==========

- Hub will continue to run for LIbreTexts and UC Davis

Students getting jobs & grad school
===================================

Thanks to students and partners

Resources
=========

metalc https://github.com/LibreTexts/metalc/
   Primary documentation and issue tracker for the project.

https://github.com/LibreTexts/labextension-libretexts-faq
https://github.com/LibreTexts/ckeditor-query-plugin
https://github.com/LibreTexts/labextension-libretexts-faq
https://github.com/LibreTexts/jupyterhub-templates
https://github.com/LibreTexts/protogalaxy
https://github.com/LibreTexts/jupyterteam_widget
https://github.com/LibreTexts/widget-testing

Prior blog posts
================

=====================================
Libretexts Jupyter Integration Wrapup
=====================================

:date: 2021-10-01
:authors: Jason K. Moore
:category: education
:tags: jupyter,libretexts

As of September 30th, we have wrapped up our work intergrating Jupyter tools
into the Libretexts platform. This work was part of a 3 year $5M grant from the
U.S. Department of Education to enhance open access textbooks.

Funded by the Open Textbooks Pilot Program (CFDA No. 84.116T) from

https://www.ed.gov/news/press-releases/us-department-education-awards-49-million-grant-university-california-davis-develop-free-open-textbooks-program

Project Goals
=============

The overall goals of the grant were multifold and we contributed one small
chunk. We were part of Thrust 3: "Next Generation Technology - Interactive
Visualizations, Automated Assessment, Annotations, Database Integration, &
Technological Synergy". Here is the text from the grant proposal for our
portion of Thrust 3:

   3C: Interactive Figure Editor (Jason K. Moore).

   While the CalcPlot3D application provides powerful, simple-to-use,
   specialized 3D visualizations, many LibreTexts authors also desire arbitrary
   interactive visualizations illustrating concepts in any scientific domain.
   It is known that quality figures enhance learning when adjunct to text
   regardless if the figures are static, dynamic, or interactive,18,40 but
   research demonstrating whether interactivity improves learning is nascent.
   In computer science education, there is evidence that interactive
   visualizations of computer algorithms improve learning when they are self
   paced and of high quality41–43 but may hamper learning if poorly
   designed.44,45 There is recent evidence that interactivity is especially
   beneficial for lower performing students.46 Cutting edge interactive
   visualizations demonstrate how concepts are learned through exploration47
   and modern publishing platforms are adopting interactive figures for high
   level scientific communication (Authorea)48 as well as for the public (e.g.
   New York Times). This will enable LibreText to become a platform for
   research into the benefits of interactive figures in addition to providing
   authors with infinite interactive visualization possibilities to convey
   concepts (see Figure 4 for examples). To do so, we will implement general
   functionality for authors to easily include any type of interactive figure
   through a new "interactive figure editor" that relies on the Jupyter
   interactive widget system, ipywidgets.49

   Jupyter is a popular open source web application that allows users to create
   and share interactive documents that contain equations, visualizations,
   narrative text, and the execution of code.50 LibreTexts authors will be able
   to write high level code in the Python programming language in the
   LibreTexts editing interface to generate figures. On page save, the Python
   code will be sent to an external server where it will be executed in a
   secure container using Jupyter to generate an entry in an open access
   database of versioned interactive Javascript figures.

By the time we recieved the money and the grant period started the goals
solidied into:

Primary goals

1. Allow any reader of a libretexts textbook page to execute code interactively
2. Allow textbook authors and readers to execute code that produces passive and
   interactive figures
3. Add Jupyter enabled textbooks and portions of textbooks to LibreTexts

Anscillary goals

1. Provide a JupyterHub for LibreTexts and UC Davis users
2. Train students in full stack development and system administration

We based all of this on the hard work and shared resources of the greater
Juyter community.

Kubernetes Bare Metal Cluster
=============================

We decided to build and run our own Kubernetes computing cluster. We chose to
do this instead of using cloud services because the 5-10 year costs outlook
seemed to be more favorable. We also had the experise and existing hardware
available to pilot the system. After two build and test iterations, we now have
a 19 node cluster that runs JupyterHub and BinderHub for LibreTexts and UC
Davis users. The cluster has several notable features:

- Puppet based deployment (we can tear down and rebuild the cluster with one
  command)
- Montioring and alerts via Promethesu and Grafana
- ZFS data storage node

Custom repo2docker image
========================

The default docker image for our our hubs include a large set of software. We
manage the sofware dependencies using APT and Conda/Mamba, with most packages
installed via Mamba from the conda-forge channel. Managing an image with a
large set of software packages in a single environment has been rather
difficult due to hard to solve version compatibilities, packages that arent'
kept up-to-date, desire for different versions of some packages, packages not
being available in conda-forge, slow build times, and large docker image sizes.
We've wreslted with these issues for three years, but things are resaonably
smooth at this point. New images are immediately cached on all of our cluster
nodes so that user load times are snappy and the vast majority of needed
software is pre-installed.

https://github.com/LibreTexts/default-env

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

https://github.com/LibreTexts/ngshare


LibreTexts Textbooks Using Jupyter Integration
==============================================

- `https://geo.libretexts.org/Courses/University_of_California_Davis/GEL_056:_Introduction_to_Geophysics`
- `https://math.libretexts.org/Bookshelves/Linear_Algebra/Matrix_Algebra_with_Computational_Applications_(Colbry)`

R:

- `https://stats.libretexts.org/Bookshelves/Introductory_Statistics/Book:_Visual_Statistics_Use_R_(Shipunov)`
- `https://chem.libretexts.org/Courses/Intercollegiate_Courses/Cheminformatics_OLCC_(2019)`
- `https://stats.libretexts.org/Bookshelves/Applied_Statistics/Book:_Answering_Questions_with_Data_-__Introductory_Statistics_for_Psychology_Students_(Crump)`

Julia

- `https://math.libretexts.org/Bookshelves/Scientific_Computing_Simulations_and_Modeling/Book:_Scientific_Computing_(Staab)`

Python

- `https://eng.libretexts.org/Courses/Delta_College/Introduction_to_Programming_Concepts_-_Python`
- `https://eng.libretexts.org/Bookshelves/Introduction_to_Engineering/EGR_1010:_Introduction_to_Engineering_for_Engineers_and_Scientists`
- `https://eng.libretexts.org/Bookshelves/Computer_Science/Programming_Languages/Book%3A_Python_for_Everybody_(Severance)`

Shell, Ptyon, R:

- `https://chem.libretexts.org/Courses/Intercollegiate_Courses/Internet_of_Science_Things_(2020)`

Octave

- `https://eng.libretexts.org/Bookshelves/Industrial_and_Systems_Engineering/Book:_Introduction_to_Control_Systems_(Iqbal)`

Other:

- `https://query.libretexts.org/Sandboxes/hdagnew@ucdavis.edu/Jupyter_Widgets`
- `https://chem.libretexts.org/Ancillary_Materials/Interactive_Applications`


STudents presenting


Students getting jobs & grad school

Thanks to students and partners

Resources

metalc

https://github.com/LibreTexts/labextension-libretexts-faq


Prior blog posts

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

The overall goals of the grant were multifold and we only worked on one small
chunk: adding interactive features to Libretexts.

Primary goals

1. Allow any reader of a libretexts textbook page to execute code interactively
2. Allow textbook authors and readers to execute code that produces passive and
   interactive figures
3. Add Jupyter enabled textbooks and portions of textbooks to LibreTexts

Anscillary goals

1. Provide a JupyterHub for LibreTexts and UC Davis users
2. Train students in full stack development and system administration

Kubernetes Bare Metal Cluster
=============================

We decided early on to build and run our own kubernetes cluster. We did this
instead of using cloud services because the 5-10 year costs seemed to be more
favorable. We also had the experise and existing hardware available to 

We built an onsite "bare metal" kubernetes based computing cluster at UC Davis
to run the UCD-Libretexts a JupyterHub and BinderHub. It took two iterations of
the cluster to get it in stable production shape.


JupyterHub & Rstudio Server Class Support

default-env

Thebe Improvements

https://query.libretexts.org/Sandboxes/jupyterteam_at_ucdavis.edu

Cke Editor Plugins

ngshare

Textbooks on libretexts

- `test <https://geo.libretexts.org/Courses/University_of_California_Davis/GEL_056:_Introduction_to_Geophysics>`_
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

Students getting jobs & grad school

STudents presenting


Thanks to students and partners


Resources

metalc

https://github.com/LibreTexts/labextension-libretexts-faq

https://github.com/LibreTexts/ngshare

Prior blog posts

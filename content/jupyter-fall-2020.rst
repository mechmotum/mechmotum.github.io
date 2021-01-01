JupyterTeam Progress Fall 2020
==============================

:date: 2020-12-31 00:00:00
:tags: oer, education, jupyter, textbooks, engineering, libretexts
:category: education
:slug: jupyter-fall-2020
:authors: Noah Sanders, Kevin Rong, Hao Huang, Celine Liang
:summary: Blog post on the progress made by JupyterTeam over the fall of 2020

Summary
-------
During the fall quarter of 2020, the Jupyter Team made improvements to

JupyterCon 2020
---------------
Jupyter Team attended a JupyterCon sprint to improve 
`Thebe <https://github.com/executablebooks/thebe/>`__, an open source project
which we use to insert executable code blocks into LibreTexts textbook pages.

Additions to Thebe made by the team include:

* Documenting how to display various `ipywidgets <https://github.com/jupyter-widgets/ipywidgets/>`__ in Thebe code blocks. Without including scripts such as `RequireJS <https://requirejs.org/>`__ and `Font Awesome 4 <https://fontawesome.com/v4.7.0/>`__, many ipywidgets would not display properly. Some example pages for widgets created include `bqplot <https://thebe.readthedocs.io/en/latest/examples/bqplot_example.html>`__, `ipyleaflet <https://thebe.readthedocs.io/en/latest/examples/ipyleaflet_example.html>`__, and `plotly <https://thebe.readthedocs.io/en/latest/examples/plotly-example.html>`__.
* `Adding a read-only option to code blocks <https://github.com/executablebooks/thebe/pull/274>`__, allowing users to disable editing on rendered code blocks. 
* `Persisting Binder sessions across pages <https://github.com/executablebooks/thebe/pull/266>`__, which decreases the time to connect to a Binder pod if a user has already requested a previous session.
* `Simplifying Jest tests <https://github.com/executablebooks/thebe/pull/297>`__ 

CKEditor Query Plugin
---------------------
The `CKEditor Query Plugin <https://repo2docker.readthedocs.io/en/latest/>`__ 
is a plugin added to the text editor, CKEditor, allowing textbook authors to
add interactive problems to the HTML pages. It does so by embedding 
HTML and Javascript into the page.

Cluster Migration
-----------------
During the winter break, the Jupyter team migrated the previous Flock cluster 
to the new Galaxy cluster. This involved various changes in networking,
hardware, and Jupyterhub.



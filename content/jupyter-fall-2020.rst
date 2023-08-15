==============================
JupyterTeam Progress Fall 2020
==============================

:date: 2021-01-14 00:00:00
:tags: oer, education, jupyter, textbooks, libretexts
:category: education
:slug: jupyter-fall-2020
:authors: Lyla Sanders, Kevin Rong, Hao Huang, Celine Liang
:summary: Blog post on the progress made by JupyterTeam over the fall of 2020

Summary
-------

During the fall quarter of 2020 the JupyterTeam attended JupyterCon and was
able to make improvements to Thebe which our `CKEditor Binder Plugin
<https://github.com/LibreTexts/ckeditor-binder-plugin>`__ depends on.
Furthermore, we expanded LibreTexts's CKEditor with a new Query Plugin to
enable authors to embed interactive problems into their textbook pages for
readers to solve. Finally, we went through most of the process of migrating the
Flock kubernetes cluster to Galaxy, which contains many improvements.

JupyterCon 2020
---------------

Jupyter Team attended a JupyterCon sprint to improve `Thebe
<https://github.com/executablebooks/thebe/>`__, an open source project which we
use to insert executable code blocks into LibreTexts textbook pages.

Additions to Thebe made by the team include:

* Documenting how to display various `ipywidgets
  <https://github.com/jupyter-widgets/ipywidgets/>`__ in Thebe code blocks.
  Without including scripts such as `RequireJS <https://requirejs.org/>`__ and
  `Font Awesome 4 <https://fontawesome.com/v4.7.0/>`__, many ipywidgets would
  not display properly. Some example pages for widgets created include `bqplot
  <https://thebe.readthedocs.io/en/latest/examples/bqplot_example.html>`__,
  `ipyleaflet
  <https://thebe.readthedocs.io/en/latest/examples/ipyleaflet_example.html>`__,
  and `plotly
  <https://thebe.readthedocs.io/en/latest/examples/plotly-example.html>`__.
* `Adding a read-only option to code blocks
  <https://github.com/executablebooks/thebe/pull/274>`__, allowing users to
  disable editing on rendered code blocks.
* `Persisting Binder sessions across pages
  <https://github.com/executablebooks/thebe/pull/266>`__, which decreases the
  time to connect to a Binder pod if a user has already requested a previous
  session.
* `Simplifying Jest tests
  <https://github.com/executablebooks/thebe/pull/297>`__

We plan to continue working with Thebe in order to improve how it inserts and
displays interactive JupyterLab widgets.

CKEditor Query Plugin
---------------------

The `CKEditor Query Plugin
<https://github.com/LibreTexts/ckeditor-query-plugin>`__ is a plugin added to
the LibreTexts text editor, CKEditor. The plugin allows textbook authors to
embed interactive problems into HTML pages. Just like with our CKEditor Binder
Plugin, the Query Plugin adds a small icon to CKEditor so that authors may add
answerable problems into their textbooks.  The plugin works by simply embedding
a LibreTexts Javascript template into the HTML code which constitutes the
webpage. This plugin is completely operational and deployed on libretexts.org.

Cluster Migration
-----------------

During the winter break, the Jupyter team migrated the previous Flock cluster
to the new Galaxy cluster. This involved various changes in networking,
hardware, and Jupyterhub.

The first step was to make sure that all of the physical computers were
properly wired to each other. At the end of it all, we were able to
reconsolidate our Flock and protogalaxy clusters to where we now have 17 nodes
online. These new Galaxy nodes are running high availability programs like
metallb and HAproxy to preserve the availability of our Libretexts services and
Kubernetes control-planes which is a great improvement over the previous Flock
cluster.

We improved cluster management by setting up Ubuntu cloudinit to boot the nodes
and install a Puppet agent from which we are able to configure and install all
the processes we need using a Puppet server. This creates consistency across
our nodes and makes it easier to refresh the state of the cluster if something
goes massively wrong. Both of these features were lacking in the Flock cluster
and using them now makes it much easier to remotely manage these nodes.

Looking Foward
--------------

While there are still a few `remaining objectives
<https://github.com/LibreTexts/metalc/issues/14#issuecomment-753696732>`__ to
complete the setup of the Galaxy cluster, our services such as JupyterHub and
BinderHub are all online and available to the public.  In fact, all UC Davis
students and faculty have now been authorized to access jupyter.libretexts.org
without needing manual permission from us to do so. We intend to continue to
expand the availability of these Jupyter services, with our next target being a
JupyterHub for high preformance computing.

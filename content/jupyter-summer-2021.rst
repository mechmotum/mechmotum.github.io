==============================
JupyterTeam Progress Summer 2021
==============================

:date: 2021-09-07 00:00:00
:tags: oer, education, jupyter, textbooks, libretexts
:category: education
:slug: jupyter-summer-2020
:authors: Noah Sanders, Tim Stewart
:summary: Blog post on the progress made by JupyterTeam since winter 2020 through summer 2021

Improvements and Progress
-------------------------

Since winter quarter of 2020, the JupyterTeam has fixed a long standing issue where Thebe,
the Javascript package that we use to display and run code on libretexts.org, would not properly
work with the entire interactive Jupyter widget ecosystem. By migrating from the 
Jupyter HTML manager package to the Lab manager, we are now able to run all 
ipywidget interactive widgets, which greatly expands the possibilities for textbook authors.

In terms of cluster reliability, we have added a second router/gateway to be highly 
available with the already existing one; if the master router fails for any reason,
then the backup one will take its place until the master comes back online. Furthermore,
we configured the routers to act as TFPT servers so that they we may use Ubuntu netboot
to load Ubuntu on all nodes from scratch. As compared to the previous method, this
way is more effective and utilizes existing infastructure better.

We completed the migration of our default-env computing environment
to JupyterLab 3.0, which includes new features which are great for widgets
and their Javascript extensions. Additionally, we added a new Adapt plugin
to supplement our already existing Query plugin on libretexts.org.

Finally, after many bitcoining mining attempts on libretexts.org through our binder.libretexts.org,
we have implemented successful automated measures in order to deal with these cryptominers
and prevent them from mining on the cluster. Since then, there have been no major instances
of bitcoin miners running on the cluster, and we have further ideas if more
anti-mining measures need to be added in the future.

In the Works
------------

For the future, we are planning to develop a Ceph cluster to replace our NFS-client-provisioner 
as the storage solution for users on the JupyterHub. We also intend to extend the cluster
with GPU nodes, and provide more specialized computing enviornments. Feel free to use our Binder plugin on libretexts.org, and checkout jupyterhub.ucdavis.edu if you are a UC Davis member!

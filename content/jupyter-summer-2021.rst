==============================
JupyterTeam Progress Summer 2021
==============================

:date: 2021-09-08 00:00:00
:tags: oer, education, jupyter, textbooks, libretexts
:category: education
:slug: jupyter-summer-2021
:authors: Noah Sanders, Tim Stewart
:summary: Blog post on the progress made by JupyterTeam since winter 2020 through summer 2021

Improvements and Progress
-------------------------

Since winter quarter of 2020, the JupyterTeam has fixed a long standing issue where Thebe,
the JavaScript package that we use to display and run code on libretexts.org, would not properly
work with the entire interactive Jupyter widget ecosystem. By migrating from the 
Jupyter HTML Manager package to the Lab Manager, we are now able to run all 
ipywidget interactive widgets, which greatly expands the possibilities for textbook authors.

.. |thebe-working| image:: https://cdn.discordapp.com/attachments/840776718930411561/885315459560374323/BdXwA3V0Pl.gif
   :height: 200px
   :align: center

In terms of cluster reliability, we have added a second router to be highly 
available with the already existing one; If the master router fails for any reason,
then the backup one will take its place until the master comes back online. Furthermore,
we configured the routers to act as TFTP servers so that they we may use Ubuntu netboot
to load Ubuntu on all nodes from scratch. As compared to the previous method, this
way is more effective and utilizes existing infastructure better.

We completed the migration of our default-env computing environment
to JupyterLab 3.0, which includes new features which are great for widgets
and their JavaScript extensions. Additionally, we added a new Adapt plugin
to supplement our already existing Query plugin on libretexts.org.

Finally, after many bitcoining mining attempts on libretexts.org,
we have successfully implemented measures to mitigate these abuses.

In the Works
------------

For the future, we are planning to develop a Ceph cluster to replace our NFS-client-provisioner 
as the storage solution for users on the JupyterHub. We also intend to extend the cluster
with GPU nodes and provide more specialized computing enviornments. 
Feel free to use our Binder plugin on `libretexts.org <https://libretexts.org/>`__, and 
check out our `JupyterHub <https://jupyterhub.ucdavis.edu>`__ if you are a UC Davis member!

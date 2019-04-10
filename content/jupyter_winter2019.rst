Creating Linux Servers for JupyterHub
=====================================

:date: 2019-04-08 00:00:00
:tags: oer, education, jupyter, textbooks, engineering, libretexts
:category:
:slug: jupyter_winter2019
:authors: Celine Liang, Kevin Krausse, Xin Luigi Chen, Xiaochen Zeng
:summary: Blog post on setting up JupyterHub for a future computing cluster

.. contents::

1.0 Background
^^^^^^^^^^^^^^

As part of the `$5M grant`_ awarded to the LibreTexts project last year,
our team was created with two goals: to integrate Jupyter into the LibreTexts
website and to create a computing cluster running JupyterHub to serve UC Davis.
This quarter, we focused on researching how to create the cluster through
building test servers.

.. _$5M grant: https://mechmotum.github.io/blog/libretexts-grant.html

2.0 Virtual Machines
^^^^^^^^^^^^^^^^^^^^

The first step in our journey to building a cluster was to familiarize ourselves
with how to setup a single server. It was crucial for us to really understand all
the details on how to setup a single server, as we would need the knowledge to setup
each and every single node in the cluster. We decided to use VirtualBox as our
starting playground so we had easily disposable environments to learn.

3.0 

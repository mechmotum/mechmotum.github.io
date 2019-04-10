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

2.0 Virtual Machine Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The first step in our journey to building a cluster was to familiarize ourselves
with how to setup a single server. It was crucial for us to really understand all
the details on how to setup a single server, as we would need the knowledge to setup
each and every single node in the cluster. We decided to use VirtualBox as our
starting playground so we had an easily disposable environments to learn from.

3.0 RAID1 and LVM
^^^^^^^^^^^^^^^^^

After we succeeded in installing Ubuntu 18 in our VirtualBox machines, we started
adding more features to the installations that we would eventually use in our cluster
configuration. We started by adding a software RAID1 to our installations to familiarize
ourselves with the process.

Redundant Array of Independent Disks, also known as RAID, provides multiple ways of orchestrating
and synchronizing multiple hard drives in a computer network to establish reliable data storage
within the network. We decided to use RAID1, which consists of an exact copy of a set of data on
two or more disks. We chose RAID1 because it allows us to switch a drive while the server is live,
in case a drive fails.

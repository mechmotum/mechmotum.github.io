Creating Linux Servers for JupyterHub
=====================================

:date: 2019-04-08 00:00:00
:tags: oer, education, jupyter, textbooks, engineering, libretexts
:category: education
:slug: jupyter-winter-2019
:authors: Celine Liang, Kevin Krausse, Xin Luigi Chen, Xiaochen Zeng
:summary: Blog post on setting up JupyterHub for a future computing cluster


Background
^^^^^^^^^^

As part of the `$5M grant <libretexts-grant.rst>`_ awarded to the LibreTexts project last year,
our team had two goals: to integrate Jupyter into the LibreTexts
website and to create a computing cluster running JupyterHub to serve LibreTexts
and UC Davis users. This quarter, we focused on researching how to create the
cluster through building test servers.

Virtual Machine Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The first step in our journey to building a cluster was to familiarize ourselves
with how to setup a single server. It was crucial for us to really understand all
the details on how to setup a single server, as we would need the knowledge to setup
each and every single node in the cluster. We decided to use VirtualBox as our
starting playground so we had an easily disposable environments to learn from.

RAID1 and LVM
^^^^^^^^^^^^^

We started adding more features to the installations that we would eventually use in our cluster
configuration. We started by adding a software RAID1 to our installations to familiarize
ourselves with the process, and then we moved on to adding LVM too.

Redundant Array of Independent Disks, also known as RAID, provides multiple ways
of orchestrating and synchronizing multiple hard drives in a computer network to
establish reliable data storage within the network. We decided to use RAID1, which
consists of an exact copy of a set of data on two or more disks. We chose RAID1
because it allows us to switch a drive while the server is live, in case a
drive fails.

Logical Volume Manager, also known as LVM, is a device mapper target that provides
logical volume management for the Linux kernel. The benefits of using LVM is the
ability to use and manage "dynamic partitions". When using LVM "partitions",
known just as logical volumes, we can manage them very easily through the command
line if we wanted to either create additional partitions, or resize/delete any
existing partitions.

While installing Ubuntu Live Server 18.04 with RAID1, we ran into an issue where
the server failed to start. After some researching, we learned that `a bug
<https://bugs.launchpad.net/subiquity/+bug/1785332>`__ from the Ubuntu Live Server image
caused the installer to fail to mount the boot partition. We instead used a 
non-live server image to successfully install Ubuntu Server 18.04 with RAID1 on the 
virtual machines.

When installing Ubuntu Server with RAID1 and LVM on our virtual machines, we did not allot
enough space on our hard disks for the operating system and JupyterHub combined. We determined
that in total, the operating system and JupyterHub required about 15 GB of storage. To be safe,
we now recommend to create two 20 GB virtual hard disks for setting up JupyterHub.

Our individual setups varied between each test server. In one successful setup, each hard disk 
contained two partitions. One partition contained 2.0 GB and was mounted on ``/boot`` as the
boot partition. The other partition contained 19.5 GB, serving as primary storage.

A stack of Ubuntu 18, RAID1, and LVM will be our standard setup for each node in
the cluster.

JupyterHub Bare-Metal
^^^^^^^^^^^^^^^^^^^^^

Our next step was trying to setup a bare-metal verion of JupyterHub in our virtual machines. 
We followed the instructions provided in the repository, `jupyterhub-deploy-teaching
<https://github.com/mechmotum/jupyterhub-deploy-teaching>`__, to install JupyterHub on 
our virtual machines and connect to it through the browser.

We ran into a few issues during the installation process.
The Ansible script in the repository did not install all of the packages required by JupyterHub.
This included `python3-distutils` and the conda submodules. 

After succeeding in setting up JupyterHub on our virtual machines, we incorporated the changes
into the configuration files and wrote a bash script to automate the installation process, testing it
to make sure that it worked.

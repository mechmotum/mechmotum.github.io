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
the server failed to start. According to the `Ubuntu 18.04.02 Release Notes 
<https://wiki.ubuntu.com/BionicBeaver/ReleaseNotes#Server_installer>`__: 

  The next generation Subiquity server installer, brings the comfortable live session 
  and speedy install of Ubuntu Desktop to server users at last.

  N.B., If you require multipath, full-disk encryption, or the ability to re-using 
  existing partitions, you will want to continue to use the alternate installer 
  which can be downloaded from http://cdimage.ubuntu.com/releases/18.04/release/ 
  
  As of 18.04.1, the Subiquity server installer now supports LVM, RAID, vlans, and bonds. 

After some researching, we learned however that `a bug <https://bugs.launchpad.net/subiquity/+bug/1785332>`__ 
from the Ubuntu Live Server image caused the installer to fail to mount the boot partition, 
preventing the installation of Ubuntu on RAID1. We instead used this 
`alternate installer (non-live server image file) <http://cdimage.ubuntu.com/releases/18.04.2/release/ubuntu-18.04.2-server-amd64.iso>`__ 
to successfully install Ubuntu Server 18.04 with RAID1 on the virtual machines. 

When installing Ubuntu Server with RAID1 and LVM on our virtual machines, we did not allot
enough space on our hard disks for the operating system and JupyterHub combined. We determined
that in total, the operating system and JupyterHub required about 15 GB of storage. To be safe,
we now recommend to create two 20 GB virtual hard disks for setting up JupyterHub.

Our individual setups varied between each test server. In one successful setup, each hard disk 
contained two partitions. One partition contained 2.0 GB and was mounted on ``/boot`` as the
boot partition. The other partition contained 19.5 GB, serving as primary storage.

We plan to have a stack of Ubuntu 18, RAID1, and LVM as our standard setup for each node in
the cluster.

JupyterHub Bare-Metal
^^^^^^^^^^^^^^^^^^^^^

Our next step was trying to setup a bare-metal verion of JupyterHub in our virtual machines. 
We followed the instructions provided in the repository, `jupyterhub-deploy-teaching
<https://github.com/mechmotum/jupyterhub-deploy-teaching>`__, to install JupyterHub on 
our virtual machines and connect to it through the browser. The repository is a "light fork" 
from the JupyterHub's `original jupyterhub-deploy-teaching <https://github.com/jupyterhub/jupyterhub-deploy-teaching>`__
repository, intended for UC Davis uses.

We ran into a few issues during the installation process.
The Ansible script in the repository was missing some required installations.
The package `python3-distutils` is required by JupyterHub but was not installed. We suspect that the 
package may have been part of Ubuntu 16.04, so it is possible that the Ansible script did not need to
specify installing `python3-disutils` previously. This was fixed in the Ansible Playbook via 
`this commit <https://github.com/mechmotum/jupyterhub-deploy-teaching/commit/51b070a9ae3223d1919ec56323411ef455d642e5>`__.

We also encountered Conda errors while installing JupyterHub. We suspect that this is 
due to the conda submodules, which are fixed by running their updates in our automatic configuration 
and deploying script, `setup.sh`.

After succeeding in setting up JupyterHub on our virtual machines, we incorporated the changes
into the configuration files and completed `setup.sh` to automate the installation process, testing it
to make sure that it worked.

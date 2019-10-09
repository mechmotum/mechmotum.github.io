Creating a Kubernetes Bare-Metal Cluster for JupyterHub
=======================================================

:date: 2019-10-04 00:00:00
:tags: oer, education, jupyter, textbooks, engineering, libretexts
:category: education
:slug: jupyter-winter-2019
:authors: Xin Luigi Chen, Celine Liang
:summary: Blog post on setting up JupyterHub on a Kubernetes bare-metal cluster

Background
^^^^^^^^^^

During the spring quarter and summer sessions, we focused on creating a Kubernetes
bare-metal cluster to deploy JupyterHub, BinderHub, and other services.


Virtual Machine Cluster
^^^^^^^^^^^^^^^^^^^^^^^
During spring quarter, Kevin and Celine worked on creating the bare metal
Kubernetes cluster. We first created a cluster of virtual machines (VMs)
A Linux test server served as the master node and host machine, 
while virtual machines served as the child nodes. We used Vagrant
to create these child nodes and Ansible to provision them.

`This folder in our main repository 
<https://github.com/LibreTexts/metalc/tree/master/dev-env>`__ contains 
instructions for setting up this development environment.

Bare-Metal Cluster
^^^^^^^^^^^^^^^^^^
Our original bare-metal cluster consists of one master node named chick0 and 
11 children named chick1 through chick10 sequentially. It also contains a 
management node called rooster, which acts as a proxy between the Internet
and the cluster. The cluster is under a private network, so the only way
to access the cluster is by connecting through rooster.

The following diagram describes our networking setup.

.. image:: kubediagram.png
   :width: 300
   :alt: Kubernetes diagram of cluster

The private network is under the ``10.0.0.0/8``. Kubernetes uses this network 
for its resources to communicate.  Rooster has a public IP address of 
``128.120.136.26``, which serves multiple services based on the domain name
entered by the user.

All servers are connected to a smart switch. The ZFS server is also connected
to the switch and provides persistent storage of JupyterHub users' files.

`PXEBoot <https://wiki.debian.org/PXEBootInstall#Preface>`__ used a preseed 
file and a DHCP server to install Ubuntu Server 18.04 on 
the servers more efficiently. Each new server pulls the preseed and
installation files via a TFTP server set up on rooster. 

As done in the development environment, the nodes were provisioned using 
`Ansible scripts 
<https://github.com/LibreTexts/metalc/tree/master/ansible/playbooks>`__.
Unlike the development environment, the bare-metal cluster `uses Calico
instead of Flannel 
<https://medium.com/@jain.sm/flannel-vs-calico-a-battle-of-l2-vs-l3-based-networking-5a30cd0a3ebd>`__ for 
pod networking. This was chosen because Calico doesn't require software 
bridges or IP tunneling like Flannel does. When communicating
from pod to pod, Flannel requires the pod's IP to be "packaged" in another IP
(IP tunneling) to send to the other pod. Calico, on the other
hand, uses BGP protocol and conserves the original pod IP.

Additionally, we originally had an NFS server on rooster itself, 
so each node had a mount to a folder on rooster. We later built a ZFS 
server to save users' files.

Later, we added more chicks and upgraded the RAM of almost all chicks.

Our 
`documentation <https://github.com/LibreTexts/metalc/blob/master/docs/Bare-Metal/baremetal.md>`__ details
our setup further and describes the actions taken to build the cluster from
scratch.

Customizing JupyterHub
^^^^^^^^^^^^^^^^^^^^^^
We made many modifications to JupyterHub, including redesigning the website,
adding new default environments, and more.

JupyterHub pages is customizable using the `Jinja2 templating system
<https://jinja.palletsprojects.com/en/2.10.x/templates/>`__ .
There are two ways to add custom HTML files to JupyterHub
(as described in 
`this Discourse post <https://discourse.jupyter.org/t/customizing-jupyterhub-on-kubernetes/1769>`__):

* Through `InitContainers <https://kubernetes.io/docs/concepts/workloads/pods/init-containers/>`__ that pull repositories of template files before the hub starts, 
* Or through mounting `ConfigMaps <https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/>`__ to the template file directory.

We chose the former option and have repositories for 
`custom HTML files <https://github.com/LibreTexts/jupyterhub-templates>`__ 
and `additional
images <https://github.com/LibreTexts/jupyterhub-images>`__.

This is a screenshot of how the login page looks now.

.. image:: jupyterhubscreenshot.png
   :width: 300
   :alt: Screenshot of the redesigned JupyterHub login page

Additionally, more spawner options are included. We modified the default environment
to include many packages requested by professors and students. RStudio is also
available in addition to JupyterLab.

.. image:: jupyterhubspawner.png
   :width: 300
   :alt: Screenshot of the redesigned JupyterHub spawner page

Future
^^^^^^
In the future, we plan to create another cluster including, but not limited,
to the following:

* Creating multiple master nodes to avoid single points of failure
* Assigning GPU's to different users
* Assigning different networks based on organization

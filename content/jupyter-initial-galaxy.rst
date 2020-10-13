JupyterTeam Progress Summer 2020
================================

:date: 2020-10-13 00:00:00
:tags: oer, education, jupyter, textbooks, engineering, libretexts
:category: education
:slug: jupyter-summer-2020
:authors: Noah Sanders, Kevin Rong
:summary: Blog post on the progress made by JupyterTeam over the summer of 2020

Summary
-------

Over the summer sessions of 2020, the JupyterTeam was able to
restructure the default-env image used by our `JupyterHub
deployment <https://jupyter.libretexts.org/hub/login>`__ so that it is
built by
`repo2docker <https://repo2docker.readthedocs.io/en/latest/>`__,
allowing us to finally make use of our own `Binder
deployment <https://binder.libretexts.org/>`__ as the backend for the
`CKEditor Binder
plugin <https://github.com/LibreTexts/ckeditor-binder-plugin>`__ on
`Libretexts.org <https://libretexts.org/>`__. This resolves the
remaining issues mentioned in the JupyterTeam's `previous blog
post <https://mechmotum.github.io/blog/libretexts-jupyter-plugin.html#future>`__.

Additionally, we began bare-metal development on the new Galaxy
Kubernetes cluster building off of experiences with the first `flock
cluster <https://mechmotum.github.io/blog/jupyter-summer-2019.html>`__
and improving on it. We also made numerous miscallaneous improvements
including a new Grafana alert setup, a more detailed FAQ page for our
JupyterHub as well as completing some much needed cluster upgrades.

default-env 2.0
---------------

A long standing complication with our previous `rich default
default-env <https://github.com/LibreTexts/default-env/tree/1.13/rich-default>`__
image was that it was built using only a single, cluttered Dockerfile
and environment.yml. This led to the files being `quite
long <https://github.com/LibreTexts/metalc/issues/121>`__ and `difficult
to maintain <https://github.com/LibreTexts/metalc/issues/130>`__. One of
the advantages of moving to a `repo2docker compatible
environment <https://github.com/LibreTexts/default-env/tree/2.0.1>`__ is
that it separates our image building files into more `logical
parts <https://repo2docker.readthedocs.io/en/latest/config_files.html>`__.
Using repo2docker, we no longer have to include a Dockerfile and our
current environment is able to automate away much of what we previously
had to do using docker commands.

Additionally, the new `default-env
2.0 <https://github.com/LibreTexts/default-env>`__ is properly equipped
to handle `custom conda
environments <https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html>`__.
Not only does this enable users to install their own persistent packages
on the Hub, but it also permitted us to `reduce the conda
channels <https://github.com/LibreTexts/metalc/issues/151>`__ necessary
to build the image down to just conda-forge/defaults and those provided
by repo2docker. Additionally, repo2docker now uses an alternative
dependency solver named `mamba <https://github.com/mamba-org/mamba>`__
which reduces our conda environment build times (one part of the image
building process) down to only a few seconds. We further sought to
improve the maintainability of default-env 2.0 by including only the top
level dependencies for all of our desired packages to avoid listing
redundancies.

Finally, we've fully overhauled the `LibreTexts FAQ page for
JupyterHub <https://jupyter.libretexts.org/hub/faq>`__ to explain these
default env changes, provide information on creating conda environments,
and more. A small
`extension <https://github.com/LibreTexts/labextension-libretexts-faq>`__
was added to the JupyterLab interface so that users can directly access
the FAQ through the 'help' tab or in the Jupyter Launcher. To do this,
we consolidated the
`jupyter-templates <https://github.com/LibreTexts/jupyterhub-templates>`__
and `jupyter-images <https://github.com/LibreTexts/jupyterhub-images>`__
repositories into just jupyter-templates, and *all* html pages are now
jinja templates. You can read more about the specifics from the
jupyter-templates `README.md
file <https://github.com/LibreTexts/jupyterhub-templates/blob/master/README.md>`__.

CKEditor Binder plugin and our Kubernetes BinderHub deployment
--------------------------------------------------------------

The `CKEditor Binder
plugin <https://github.com/LibreTexts/ckeditor-binder-plugin>`__ helps
provide kernels to executable code cells on Libretexts.org using
`BinderHub <https://github.com/jupyterhub/binderhub>`__ as a backend.
While the plugin has been working for a while now and it does enable
JupyterLab-esque features on LibreTexts, the code cells would `often
take many minutes to load and
execute <https://github.com/LibreTexts/metalc/issues/83>`__, if they
ever did at all. Furthermore, Binder uses repo2docker to build images
which meant that we could not use our own default-env repository as the
programming environment. As a result, we had to point CKEditor towards
external repositories where we had no control over the exact packages in
the environment. Two changes were made to fix this; we created
default-env 2.0 as outlined above, and we also brought our BinderHub
Kubernetes deployment into operation.

The improvements of using our own default-env 2.0 and BinderHub in
CKEditor Binder plugin represent a huge benefit for LibreTexts. Now that
we can adjust the packages and kernels provided on LibreTexts with our
default-env 2.0, we can include additional `interactive
widgets <https://chem.libretexts.org/Courses/Remixer_University/LibreTexts_Construction_Guide/05%3A_Interactive_Elements>`__
and exercise greater version control over the programming environment.
Switching to a locally maintained BinderHub allows us to cache the
images which are built by Binder on that node, dramatically increasing
loading speeds when executing code cells on LibreTexts. Pressing "run"
will now take no more than 20 seconds to connect to a Binder provided
kernel whereas before it often took minutes or longer due to the
inconsistent availability of mybinder.org. This drastic decrease in load
times makes the plugin much more accessible for both authors and
readers.

Galaxy Cluster
--------------

The primary objectives for the new Galaxy cluster are high availability
and maintainability. Part of how we achieve high availability is by
using `Keepalived and
HAproxy <https://github.com/kubernetes/kubeadm/blob/master/docs/ha-considerations.md#options-for-software-load-balancing>`__.

Keepalived runs as a static Kubernetes pod on each control-plane node
and it manages a virtual IP for the kube-apiserver that all of the
Kubernetes worker nodes communicate with. If the control-plane node
currently holding this Keepalived virtual IP goes down, Keepalived will
pass the virtual IP on to one of our remaining control-plane nodes so
that the rest of the Kubernetes cluster can still communicate with the
kube-apiserver.

After Keepalived receives a kube-apiserver request, HAproxy (also
running as a static pod on each control-plane node) will load-balance
the request onto whichever control-plane node is chosen according to a
`round robin
algorithm <https://avinetworks.com/glossary/round-robin-load-balancing/>`__.
If we did not use HAproxy, any kube-apiserver request received through
the Keepalived virtual IP would automatically be routed to that same
control-plane node, leaving the other control-plane nodes to just sit
there and do nothing. Load-balancing with HAproxy takes better advantage
of our available hardware and lowers the kube-apiserver load on any
given node.

To improve the maintainability of this cluster, we use
`Puppet <https://puppet.com/docs/puppet/6.18/puppet_index.html>`__ to
setup Kubernetes and administrate our entire bare-metal cluster.
Although there already exists a `Puppet module for bootstrapping
Kubernetes <https://github.com/puppetlabs/puppetlabs-kubernetes>`__, our
high availability setup has specific demands which required a `new
Puppet module <https://github.com/LibreTexts/protogalaxy>`__ to be
written. The Protogalaxy Puppet module bootstraps all of the necessary
components for Kubernetes using kubeadm like kubelet, kubelctl, and also
configures Keepalived and HAproxy as static pods. You can read more
about the module on its
`README <https://github.com/LibreTexts/protogalaxy/blob/master/README.md>`__
page.

Finally, we have a `Puppet
control-repo <https://github.com/LibreTexts/metalc/blob/master/docs/Galaxy-Control-Repo.md>`__
which employs the ProtoGalaxy module and configures all the
non-Kubernetes components of our Galaxy cluster. Our goal is to use this
control-repo to completely reset the cluster state to a working version
in the case that something massively breaks. This would greatly improve
the maintainability of Galaxy cluster.

As of now, we currently only have a development Galaxy cluster with no
public availability. We repurposed chicks11-18 from the Flock cluster
with brand new SSDs and then booted them up using IPMI. We also used
IPMI to install Ubuntu on all of these nodes because we do not have
physical access to the cluster in the midst of Covid-19.

Flock Cluster Upgrades/Improvements
-----------------------------------

At the beginning of summer, the original flock cluster went totally down
because our `kubeadm
certificates <https://v1-18.docs.kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/>`__
expired. The reason for this was that our cluster was very behind on
Ubuntu and Kubernetes upgrades; the kube-apiserver and kubelet were on
v1.12 while the latest release was v1.18 at the time. One of the first
things we did was to upgrade the flock cluster across all the nodes, and
they now sit at a neat v1.19 for kubelet/kube-apiserver and v18.04.5 for
Ubuntu. Furthermore, we established a policy of upgrading the cluster
every 4 months so that the certificates do not meet their yearly
expiration date as they did before.

Other improvements were made as well. Kubernetes
`cert-manager <https://cert-manager.io/docs/installation/kubernetes/>`__
has been upgraded to v1, and `helm <https://v3.helm.sh/>`__ has also
been migrated over to v3. Our Grafana alerts setup has been recrafted so
that we no longer have to manually reinput our dashboards if the pod
goes down. We also enabled IPMI interfaces on all the nodes, affording
us remote adminstration tools in light of Covid-19.

Future Plans
------------

Our top priorities moving forward are to enhance the executable code
cell features of LibreTextsand continue development on the Galaxy
cluster. We would like to fix the current issues with ipywidgets and
other interactive plotting features currently exhibited by our CKEditor
Binder plugin. To complement this, we must bring cell-to-cell
communcation to the plugin so that adjusting the output of one cell
(such as a slider) can redraw the output of a previous cell just as it
would in JupyterLab.

For the Galaxy cluster, we need to find a way to read the authentication
process of Hub users so that we can tag their pod and send them to the
high performance computing setup as needed. We will also need to
construct the physical computer setup for Galaxy, just as was done for
Flock cluster over a year ago. Stay tuned for more updates!

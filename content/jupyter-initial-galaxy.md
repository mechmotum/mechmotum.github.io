# JupyterTeam Progress Summer 2020

dunno how to translate these to markdown, they come from the rst file and we'll probably want them later

:date: 2020-10-01 00:00:00
:tags: oer, education, jupyter, textbooks, engineering, libretexts
:category: education
:slug: libretexts-jupyter-plugin
:authors: Noah Sanders, Kevin Rong
:summary: Blog post on the progress made by JupyterTeam over the summer of 2020

## Summary

Over the summer sessions of 2020, the JupyterTeam was able to restructure the default-env image used by our JupyterHub deployment to be built by [repo2docker](https://repo2docker.readthedocs.io/en/latest/), allowing us to finally make use of our own binder deployment as the backend for the CKEditor Binder plugin on Libretexts.org. This resolves the remaining issues mentioned in the JupyterTeam's [previous blog post](https://mechmotum.github.io/blog/libretexts-jupyter-plugin.html#future).

Additionally, we began bare-metal development on the new Galaxy kubernetes cluster building off of experiences with the first [flock cluster](https://mechmotum.github.io/blog/jupyter-summer-2019.html) and improving on it. We also made numerous miscallaneous improvements including a new alert setup, a more detailed FAQ page for our JupyterHub as well as completing some much needed cluster upgrades.

## default-env 2.0

A long standing complication with our previous [rich default default-env](https://github.com/LibreTexts/default-env/tree/1.13/rich-default) image was that it was built using only a single, cluttered, Dockerfile and environment.yml. This led to the files being [quite long](https://github.com/LibreTexts/metalc/issues/121) and [difficult to maintain](https://github.com/LibreTexts/metalc/issues/130). One of the advantages of moving to a [repo2docker compatible environment](https://github.com/LibreTexts/default-env/tree/2.0.1) is that it seperates our image building files into more [logical parts](https://repo2docker.readthedocs.io/en/latest/config_files.html). Using repo2docker, we no longer have to include a dockerfile and our current environment is able to automate away much of what we previously had to do using docker commands.

Additionally, the new [default-env 2.0](https://github.com/LibreTexts/default-env) is properly equipped to handle [custom conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html). Not only does this enable users to install their own persistent packages on the Hub, but it also permitted us to [reduce the conda channels](https://github.com/LibreTexts/metalc/issues/151) necessary to build the image down to just conda-forge/defaults and those provided by repo2docker. Additionally, repo2docker now uses an alternative dependency solver named [mamba](https://github.com/mamba-org/mamba) which reduces our conda environment build times (one part of the image building process) down to only a few seconds. We further sought to improve the maintainability of default-env 2.0 by including only the top level dependencies for all of our desired packages to avoid listing redundancies.

Finally, we've fully overhauled the [LibreTexts FAQ page for JupyterHub](https://jupyter.libretexts.org/hub/faq) to explain these default env changes, provide information on creating conda environments, and more. A small [extension](https://github.com/LibreTexts/labextension-libretexts-faq) was added to the JupyterLab interface so that users can directly access the FAQ through the 'help' tab or in the Jupyter Launcher. To do this, we consolidated the [jupyter-templates](https://github.com/LibreTexts/jupyterhub-templates) and [jupyter-images](https://github.com/LibreTexts/jupyterhub-images) repositories into just jupyter-templates, and *all* html pages are now jinja templates. You can read more about the specifics from the jupyter-templates [READEME.md file](https://github.com/LibreTexts/jupyterhub-templates/blob/master/README.md).

## CKEditor Binder plugin and our Kubernetes BinderHub deployment

The [CKEditor Binder plugin](https://github.com/LibreTexts/ckeditor-binder-plugin) helps provide kernels to executable code cells on Libretexts.org using [BinderHub](https://github.com/jupyterhub/binderhub) as a backend. While the plugin has been working for a while now and it does enable JupyterLab-esque features on LibreTexts, the code cells would [often take many minutes to load and execute](https://github.com/LibreTexts/metalc/issues/83), if they ever did at all. Furthermore, Binder uses repo2docker to build images which meant that we could not use our own default-env repository as the programming environment. As a result, we had to point CKEditor towards external repositories where we had no control over the exact packages in the environment. Two changes were made to fix this; we created default-env 2.0 as outlined above, and we also brought our BinderHub kubernetes deployment back into operation.

### Fixing our Binder Deployment (todo)

- for stuff about why we couldn't use our binder before and what had to be changed to fix it

### The Rewards

The improvements of using our own default-env 2.0 and BinderHub in CKEditor Binder plugin represent a huge benefit for LibreTexts. Now that we can adjust the packages and kernels provided on LibreTexts with our default-env 2.0, we can include additional [interactive widgets](https://chem.libretexts.org/Courses/Remixer_University/LibreTexts_Construction_Guide/05%3A_Interactive_Elements) and exercise greater version control over the programming environment. Switching to a locally maintained BinderHub allows us to cache the images which are built by Binder on that node, dramatically increasing loading speeds when executing code cells on LibreTexts. Pressing "run" will now take no more than 20 seconds to connect to a Binder provided kernel whereas before it often took minutes or longer due to the inconsistent availability of mybinder.org. This drastic decrease in load times makes the plugin much more accessible for both authors and readers.

## Galaxy Cluster

The primary objectives for the new Galaxy cluster are high availability and maintainability. Part of how we achieve high avialability is by using [Keepalived and HAproxy](https://github.com/kubernetes/kubeadm/blob/master/docs/ha-considerations.md#options-for-software-load-balancing).

Keepalived runs as a static kubernetes pod on each control-plane node and it manages a virtual IP for the kube-apiserver that all of the kubernetes worker nodes communicate with. If the control-plane node currently holding this Keepalived virtual IP goes down, Keepalived will pass the virtual IP on to one of our remaining control-plane nodes so that the rest of the kubernetes cluster can still communicate with the kube-apiserver.

After Keepalived recieves a kube-apiserver request, HAproxy (also running as a static pod on each control-plane node) will load-balance the request onto whichever control-plane node is chosen according to a [round robin algorithm](https://avinetworks.com/glossary/round-robin-load-balancing/). If we did not use HAproxy, any kube-apiserver request recieved through the Keepalived virtual IP would automatically be routed to that same control-plane node, leaving the other control-plane nodes to just sit there and do nothing. Load-balancing with HAproxy takes better advantage of our available hardware and lowers the kube-apiserver load on any given node.

To improve the maintainability of this cluster, we use [puppet](https://puppet.com/docs/puppet/6.18/puppet_index.html) to setup kubernetes and administrate our entire bare-metal cluster. Althought there already exists a [puppet module for boostrapping kubernetes](https://github.com/puppetlabs/puppetlabs-kubernetes), our high availability setup has specific demands which required a [new puppet module](https://github.com/LibreTexts/protogalaxy) to be written. The ProtoGalaxy puppet module boostraps all of the necessary components for kubernetes using kubeadm like kubelet, kubelctl, and also configures Keepalived and HAproxy as static pods.

Finally, we have a (private) puppet control-repo which employs the ProtoGalaxy module and configures all the non-kubernetes components of our Galaxy cluster. Our goal is to use this control-repo to completely reset the cluster state to a working version in the case that something massively breaks. This would greatly improve the maintainability of Galaxy cluster.

## Flock Cluster Upgrades/Improvements

At the beginning of summer, the original flock cluster went totally down because our [kubeadm certificates](https://v1-18.docs.kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/) expired. The reason for this was that our cluster was very behind on Ubuntu and kubernetes upgrades; the kube-apiserver and kubelet were on v1.12 while the latest release was v1.18 at the time. One of the first things we did was to upgrade the flock cluster across all the nodes, and they now sit at a neat v1.19 for kubelet/kube-apiserver and v18.04.5 for Ubuntu. Furthermore, we established a policy of upgrading the cluster every 4 months so that the certificates do not meet their yearly expiration date as they did before.

Other improvements were made as well. Kubernetes [cert-manager](https://cert-manager.io/docs/installation/kubernetes/) has been upgraded to v1, and [helm](https://v3.helm.sh/) has also been migrated over to v3. Our grafana alerts setup has been recrafted so that we no longer have to manually reinput our dashboards if the pod goes down. We also enabled IPMI interfaces on all the nodes, affording us remote adminstration tools in light of Covid-19.

## Future Plans

Our top priorities moving forward are to enhance the executable code cell features of LibreText and continue development on the Galaxy cluster. We would like to fix the current issues with ipywidgets and other interactive plotting features currently exhibited by our CKEditor Binder plugin. To compliment this, we must bring cell-to-cell communcation to the plugin so that adjusting the output of one cell (such as a slider) can redraw the output of a previous cell just as it would in JupyterLab.

For the Galaxy cluster, we need to find a way to read the authentication process of Hub users so that we can tag their pod and send them to the high performance computing setup as needed. We will also need to construct the physical computer setup for Galaxy, just as was done for Flock cluster over a year ago. Stay tuned for more updates!

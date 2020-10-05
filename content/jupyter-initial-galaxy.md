# JupyterTeam Progress Summer 2020

dunno how to translate these to markdown, they come from the rst file and we'll probably want them later

:date: 2020-10-01 00:00:00
:tags: oer, education, jupyter, textbooks, engineering, libretexts
:category: education
:slug: libretexts-jupyter-plugin
:authors: Noah Sanders, Kevin Rong
:summary: Blog post on the progress made by JupyterTeam over the summer of 2020

## Summary

Over the summer sessions of 2020, the JupyterTeam was able to make some major accomplishments despite Covid-19 complications. One such success was to restructure the default-env image used by our JupyterHub deployment to be built by [repo2docker](https://repo2docker.readthedocs.io/en/latest/), allowing us to finally make use of our own binder deployment as the backend for the CKEditor Binder plugin on Libretexts.org. We were also able to begin bare-metal development on the new Galaxy kubernetes cluster building off of experiences with the first [flock cluster](https://mechmotum.github.io/blog/jupyter-summer-2019.html) and improving on it. We also made numerous miscallaneous improvements including a new alert setup, a more detailed FAQ page for our JupyterHub as well as completing some much needed cluster upgrades.

## default-env 2.0

A long standing complication with our previous [rich default default-env image](https://github.com/LibreTexts/default-env/tree/1.13/rich-default) was that it was built using only a single, cluttered Dockerfile and environment.yml. This led to the files being [quite long](https://github.com/LibreTexts/metalc/issues/121) and [difficult to maintain](https://github.com/LibreTexts/metalc/issues/130). One of the advantages of moving to a [repo2docker compatible environment](https://github.com/LibreTexts/default-env/tree/2.0.1) is that it seperates our image building files into more [logical parts](https://repo2docker.readthedocs.io/en/latest/config_files.html). Using repo2docker, we no longer have to include a dockerfile and our current environment is able to automate away much of what we previously had to do using docker commands.

Additionally, the new default-env 2.0 is properly equipped to handle [custom conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) so  we were able to [reduce the conda channels](https://github.com/LibreTexts/metalc/issues/151) necessary to build the image down to just conda-forge/defaults and those provided by default by repo2docker. Additionally, repo2docker now uses an alternative dependency solver named [mamba](https://github.com/mamba-org/mamba) which reduces our conda environment build times (one part of the image building process) to only a few seconds. We further sought to improve the maintainability of default-env 2.0 by including only the top level dependencies for all of our desired packages to avoid listing redundancies.

Finally, we've fully overhauled the [LibreTexts FAQ page for JupyterHub](https://jupyter.libretexts.org/hub/faq) to explain these default env changes, provide information on creating conda environment, and much more. A small extension was added to the JupyterLab interface so that users can directly access the FAQ through the 'help' tab or in the Jupyter Launcher. 

- any other important or interesting changes? can nbgrader/ngshare be mentioned here?

## CKEditor Binder plugin and our Kubernetes BinderHub deployment

The [CKEditor Binder plugin](https://github.com/LibreTexts/ckeditor-binder-plugin) provides kernels to executable code cells on Libretexts.org using [BinderHub](https://github.com/jupyterhub/binderhub) as a backend. While the plugin has been working for a while now and it does enable JupyterLab-esque features on LibreTexts, the code cells would [often take many minutes to load and execute](https://github.com/LibreTexts/metalc/issues/83), if they ever did at all. Furthermore, Binder uses repo2docker to build images which meant that we could not use our own default-env repository as the programming environment. As a result, we had to point CKEditor towards external repositories where we had no control over the exact packages in the environment. Two changes were made to fix this; we created default-env 2.0 as outlined above, and we also brought our BinderHub kubernetes deployment back into operation.

### Fixing our Binder Deployment

- for stuff about why we couldn't use our binder before and what had to be changed to fix it

### The Rewards

The improvements of using our own default-env 2.0 and BinderHub in CKEditor Binder plugin represent a huge benefit for LibreTexts. Now that we can adjust the packages and kernels provided on LibreTexts with our default-env 2.0, we can include additional [interactive widgets](https://chem.libretexts.org/Courses/Remixer_University/LibreTexts_Construction_Guide/05%3A_Interactive_Elements) and exercise greater version control over the programming environment. Switching to a locally maintained BinderHub allows us to cache the images which are built by Binder on that node, dramatically increasing loading speeds when executing code cells on LibreTexts. Pressing "run" will now take no more than 20 seconds to connect to a Binder provided kernel whereas before it often took minutes or longer due to the inconsistent availability of mybinder.org. This drastic decrease in load times makes the plugin much more accessible for both authors and readers.

- switched to binder.libretexts.org with new image (huge improvement in binder plugin run times!)
- widget testing
- construction guide additions

## Galaxy cluster

- new high availability setup
- possibly talk about new metallb networking and multus
- puppet module stuff/control-repo
- ipmi added to boot stuff up

## miscellaneous

- cluster ubuntu/k8s upgrades as well as new 4 month policy
- jupyter-images merged into jupyter-templates
- ngshare
- helm value extensions/`extraConfig` things


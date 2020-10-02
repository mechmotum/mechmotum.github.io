# JupyterTeam Progress Summer 2020

dunno how to translate these to markdown, they come from the rst file and we'll probably want them later

:date: 2020-10-01 00:00:00
:tags: oer, education, jupyter, textbooks, engineering, libretexts
:category: education
:slug: libretexts-jupyter-plugin
:authors: Noah Sanders, Kevin Rong
:summary: Blog post on the progress made by JupyterTeam over the summer of 2020

## Summary

Over the summer sessions of  2020, the JupyterTeam was able to make some major accomplishments despite Covid-19 complications. One such success was to restructure the default-env image used by our JupyterHub deployment to be built by [repo2docker](https://repo2docker.readthedocs.io/en/latest/), allowing us to finally make use of our own binder deployment as the backend for the CKEditor Binder plugin on Libretexts.org. We were also able to begin bare-metal development on the new Galaxy kubernetes cluster building off of experiences with the first [flock cluster](https://mechmotum.github.io/blog/jupyter-summer-2019.html) and improving on it. We also made numerous miscallaneous improvements including a new alert setup, a more detailed FAQ page for our JupyterHub as well as completing some much needed cluster upgrades.

## default-env 2.0

- new repo2docker image for jupyterhub/binderhub
- mamba included, reduced channels for our conda environment, improved build times and made it neater
- image is built with repo2docker and therefore compatible with binder

## Libretexts things

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


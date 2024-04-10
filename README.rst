Source files for the TU Delft Bicycle Laboratorium's website.

Editing Guide
=============

- The website is built using Pelican. Review the `Pelican documentation`_ to
  get familiar with how to create pages and articles.
- The source files are in the git branch called ``source``. This is the default
  branch of the repository. The HTML files are generated in a Github Action and
  pushed to the ``master`` branch, which is automatically served to
  http://mechmotum.github.io. Don't manually edit files in the ``master``
  branch (except if a special need arises).
- All articles, pages, and similar content should be written in
  reStructuredText_. See the `Sphinx reStructuredText primer`_ to learn the
  syntax.
- All changes, in general, should be submitted as Github pull requests. Don't
  commit directly to the ``source`` branch. Doing so will ensure that the
  website is at least built with no errors on the CI service.
- Binary Assets such as images, videos, etc should be served from an external
  hosting site. The information for pushing binary objects to the Dreamhost
  DreamObject bucket is in the Fietslab Commons Google Drive. Do not commit
  binary assets to this Github repository. Images should be all lower case
  unique filenames with a ``-`` to separate words, for example:
  ``my-image-for-this-blog-post.png``. All assets are store in the same
  directory on the object store and should have unique file names.

.. _Pelican documentation: http://docs.getpelican.com/en/stable/
.. _reStructuredText: https://en.wikipedia.org/wiki/ReStructuredText
.. _Sphinx reStructuredText primer: http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html

Building Locally
================

It is good practice to build the documentation locally so that you can review
change before submitting a pull request.

First, clone the Pelican plugin repository::

   $ git clone git@github.com:getpelican/pelican-plugins.git

Note the path to the plugin repository, e.g.::

   /home/my_username/.../pelican-plugins

Clone the theme repository (you want the mechmotum branch to be active because
we have custom edits on the theme)::

   $ git clone -b mechmotum git@github.com:mechmotum/pelican-alchemy.git

Note the path to the theme, e.g.::

   /home/my_username/.../pelican-alchemy

Clone your fork of this repository and change into the new directory::

   $ git clone git@github.com:<your github username>/mechmotum.github.io.git
   $ cd mechmotum.github.io/

Create a configuration file called ``config.yml`` and add the full path to
where you installed the plugins and theme (note the added /alchemy subfolder in
THEME_PATH)::

   $ echo "THEME_PATH: /home/my_username/.../pelican-alchemy/alchemy" > config.yml
   $ echo "PLUGIN_PATHS: /home/my_username/.../pelican-plugins" >> config.yml

Create a conda environment with pelican and the other needed dependencies::

   $ conda env create -f env.yml
   $ conda activate bikelab-website

Now you can build and serve the documentation with::

   (bikelab-website)$ make devserver

If this succeeds you can open the website in your web browser at
http://localhost:8000.

While the server is running you can change the website source files and they
will be build automatically. Refresh your web browser to view the changes. Use
``<Ctrl>+C`` to kill the webserver.

Update Process
==============

The first step is to create a new branch that will hold the commits for your
changes::

   $ git checkout -b my-branch-name

Now edit existing files, create new files and add with ``git add
my-new-file.rst``, or move or remove things as needed. Once you are happy with
your changes (use ``make devsever`` as explained above to check), the commit
your changes::

   $ git commit -am "My edits to the website."

Now push your branch to your fork on Github::

   $ git push origin my-branch-name

You should see a message in the response with a URL for opening a pull request
on the primary repository. Click that and then open the pull request on Github.
As you get feedback on the pull request, add new commits to this branch and
push those to your fork. The pull request will update automatically with your
changes.

::

   $ git commit -am "My fixes based on feedback in the PR."
   $ git push origin my-branch-name

LICENSE
=======

This repository is licensed under the CC-BY 4.0 license.

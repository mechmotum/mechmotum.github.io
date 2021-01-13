Source files for the TU Delft Bicycle Laboratorium's website.

Editing Guide
=============

- The website is built using Pelican. Review the `Pelican documentation`_ to
  get familiar with how to create pages and articles.
- The source files are in the git branch called ``source``. This is the default
  branch of the repository. The HTML files are generated via doctr_ and pushed
  to the ``master`` branch, which is automatically served to
  http://mechmotum.github.io. Don't manually edit files in the ``master``
  branch (except if a special need arises).
- All articles, pages, and similar content should be written in
  reStructuredText. See the `Sphinx reStructuredText primer`_ to learn the
  syntax.
- All changes, in general, should be submitted as Github pull requests. Don't
  commit directly to the ``source`` branch. Doing so will ensure that the
  website is at least built with no errors on the CI service.
- Binary Assets such as images, videos, etc should be served from an external
  hosting site. Ask Jason about using his Dreamhost DreamObject bucket. He'll
  set it up for multi-user access when needed. Do not commit binary assets to
  this repository. Images should be all lower case unique filenames with a
  ``-`` to separate words, for example: ``my-image-for-this-blog-post.png``.
  All assets are store in the same directory on the object store and should
  have unique file names.

.. _Pelican documentation: http://docs.getpelican.com/en/stable/
.. _doctr: https://github.com/drdoctr/doctr
.. _Sphinx reStructuredText primer: http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html

Building Locally
================

It is good practice to build the documentation locally so that you can review
change before submitting a pull request.

Install pelican with conda (or pip if you prefer)::

   $ conda install pelican beautifulsoup4

Clone the plugin repository::

   $ git clone git@github.com:getpelican/pelican-plugins.git

Note the path to the plugin repository, e.g.::

   /home/my_username/.../pelican-plugins

Clone the theme repository (you want the mechmotum branch to be active)::

   $ git clone -b mechmotum git@github.com:mechmotum/pelican-alchemy.git

Note the path to the theme, e.g.::

   /home/my_username/.../pelican-alchemy

Clone this repository and change into the new directory::

   $ git clone git@github.com:mechmotum/mechmotum.github.io.git
   $ cd mechmotum.github.io/

Create a configuration file called ``config.yml`` and add the full path to
where you installed the plugins and theme::

   $ echo "THEME_PATH: /home/my_username/.../pelican-alchemy" > config.yml
   $ echo "PLUGIN_PATHS: /home/my_username/.../pelican-plugins" >> config.yml

Now you can build and serve the documentation with::

   $ make devserver

If this succeeds you can open the website in your web browser at
http://localhost:8000.

While the server is running you can change the website source files and they
will be build automatically. Refresh your web browser to view the changes.

To stop the web server type::

   $ make stopserver

LICENSE
=======

This repository is licensed under the CC-BY 4.0 license.

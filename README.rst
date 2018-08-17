Source files for the Laboratorium of Marvelous Mechanical Motum's website.

Editing Guide
=============

- The website is built using Pelican. Review the `Pelican documentation`_ to
  get familar with how to create pages and articles.
- The source files are in the git branch called ``source``. This is the default
  branch of the repository. The HTML files are generated via doctr and pushed
  to the ``master`` branch, which is automatically seved to
  http://mechmotum.github.io. Don't manually edit files in the ``master``
  branch.
- All articles, pages, and similar content should be written in
  reStructuredText. See the `Sphinx reStructuredText primer`_ to learn the syntax.
- All changes, in general, should be submitted as Github pull requests. Don't
  commit directly to the ``source`` branch.

.. _Pelican documentation: http://docs.getpelican.com/en/stable/
.. _Sphinx reStructuredText primer: http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html

Building Locally
================

It is good practice to build the documentation locally so that you can review
change before submitting a pull request.

Install pelican with conda (or pip if you prefer)::

   $ conda install pelican

Clone the theme repository::

   $ git clone git@github.com:gfidente/pelican-svbhack.git

Note the path to the theme, e.g.::

   $ /home/my_username/pelican-svbhack

Clone this repository and change into the new directory::

   $ git clone git@github.com:mechmotum/mechmotum.github.io.git
   $ cd mechmotum.github.io/

Create a configuration file called ``config.yml`` and add the full path to
where you installed the theme::

   $ echo "THEME_PATH: /home/my_username/pelican-svbhack" > config.yml

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

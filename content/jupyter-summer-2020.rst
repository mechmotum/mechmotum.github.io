Developing a Textbook Editor Plugin Inserting Executable Code Blocks
====================================================================

:date: 2020-06-13 00:00:00 
:tags: oer, education, jupyter, textbooks, engineering, libretexts 
:category: education 
:slug: jupyter-summer-2020
:authors: Hao Huang, Tannavee Kumar, Celine Liang 
:summary: Blog post on creating a CKEditor plugin which could insert 
  executable code blocks

Background
----------

During the end of the Fall Quarter 2019 and Winter Quarter 2020, we focused
on building a `CKEditor Binder Plugin
<https://github.com/LibreTexts/ckeditor-binder-plugin>`__ to be used on
the `LibreTexts <https://libretexts.org>`__ to allow textbook authors to
insert executable code blocks. We intend for both textbook authors and
readers to have the ability to edit and run code blocks efficiently, making
online educational content more interactive.
 
Build Process
-------------
We started the project by surveying
LibreTexts authors and readers on their most requested features. 

BinderHub
^^^^^^^^^
On the backend, the CKEditor Binder plugin utilizes a project called
`BinderHub  <https://binderhub.readthedocs.io/en/latest/>`__ to run code
blocks. BinderHub is developed as part of the Jupyter project and gives
custom computing environments based on a list of requirements specified
through a GitHub repository. We intend to use a BinderHub that we deployed
on our bare-metal Kubernetes cluster as our backend environment to run
codeblocks.

Thebelab
^^^^^^^^
`Thebelab <https://github.com/minrk/thebelab>`__ and  `Juniper
<https://github.com/ines/juniper>`__ are two examples of projects which can
insert code blocks into HTML pages and running them by requesting a kernel
from a computing backend like BinderHub. We deliberated on which project to
incorporate into our plugin, and decided to use Thebelab since it seemed to
be more actively maintained and had more community support.

Creating the plugin
^^^^^^^^^^^^^^^^^^^
Our plugin is based on the `CKEditor 4
<https://ckeditor.com/docs/ckeditor4/latest/>`__, an open source “what you
see is what you get” text editor. This editor is used on the LibreTexts
website through a service called Mindtouch.

Our approach to this plugin is to make use of a `widget
<https://ckeditor.com/docs/ckeditor4/latest/guide/widget_sdk_intro.html>`__,
on the editor which allows us to place all the HTML elements of Thebelab
together as one unit. Additionally, we created a `dialog window
<https://ckeditor.com/docs/ckeditor4/latest/guide/dev_howtos_dialog_windows.html>`__
for each code block so that users can modify each block whenever they want.

Mindtouch Specific Settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^
One of the challenges we faced was working around Mindtouch, which
sometimes caused the plugin to function in unexpected ways. For instance,
Mindtouch seemed to apply its own CSS to the plugin. This caused text
overflow, addition of characters to the end of each line, etc. In order to
resolve this, we added our own `styling
<https://github.com/LibreTexts/ckeditor-binder-plugin/tree/staging/src/styles>`__
to the plugin. If one wishes to use the CKEditor plugin on their own pages,
they can remove the extra styling in the folder.

Another difference was javascript conflict. When we were trying to support
Jupyter Widgets, we found that it depended on Require.js. However, adding
Require.js to Mindtouch would break all the JQuery plugins. In order to fix
all the javascript conflicts, we created registerPlugin.js to include all
Mindtouch specific js code.


Including different programming languages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
During development, we used `environments developed by the Jupyter project
<https://github.com/binder-examples>`__. Using their Binder environments
helped us test and include different languages in our editor. Ideally, we
would utilize the same `default environment
<https://github.com/libretexts/default-env>`__ in our JupyterHub for our
editor. This default environment contains many packages that are commonly
used and requested by students and faculty. 

Github Actions
^^^^^^^^^^^^^^
We made use of Github Actions to automate two important tasks. After each
push on Github, it will trigger our custom linter to ensure code quality
and consistency. Additionally, if we push any code to the master branch, it
will trigger an automatic deploy to production.


CKEditor Capabilities
---------------------

Currently authors publishing on the LibreTexts platform have the option to
insert executable code blocks using ``Octave``, ``SageMath``, ``Julia``,
``R``, ``Python``, and ``C++``. There is a possibility that other languages
may be added in the future. Authors can choose to either copy and paste
their code into the text editor, or directly code in the text editor as
they would any other one. To ensure that it is easy for the author as well
as the reader of the textbook to view the contents within the code block,
as described in the aforementioned section, syntax highlighting is made
available via ``CodeMirror`` for all the languages except ``SageMath``
which is not supported by ``CodeMirror``. 

It is important to note that we suggest authors ``run`` the sample ``Hello
World`` print statement first to get the kernel started, once that is
successful, code can be added in the dialog box. For ``C++``, if the code
has already been ``run``, but the author wants to make any changes, they
will need to ``restart`` the kernel in order to avoid an ``Interpreter
Error`` as any variables will be assigned more than once in ``Binder``
which is not allowed in ``C++``.

Packages and libraries can be exported as they normally would; however, if
an author finds that a specific package or library that they would like to
use is not currently available they can make a request to have it added by
either sending an `email to the Jupyter Team <jupyterteam@ucdavis.edu>`__,
linked in the dialog box, or `open an issue 
<https://github.com/LibreTexts/ckeditor-binder-plugin/issues>`__ . 

Once the author is ready to insert the code block into their textbook page,
they have the option to either ‘Insert with code and output,’ ‘Insert with
code only,’ or ‘Insert with output only.’ Selection of any of these choices
depends on how the author intends to communicate the information provided
in the code block. If the code block has already been inserted into the
page, and the author wants to make any changes, they can simply double
click on that section and the dialog box will pop back up. 

Future
------ 

As mentioned before, a long term goal is to use ``default-env`` for the
packages, this is the same environment that is used for JupyterHub, and by
using this, authors will have a greater selection of packages and libraries
to choose from, and it will also be easier for us to maintain. We also want
to improve the execution time of the code blocks, as currently requesting a
kernel involves downloading an image from DockerHub and creating a Docker
container. 

==============
Guide: Writing
==============

:date: 2022-10-19
:status: hidden

Common Issues
=============

When to use a figure
--------------------

If you refer to a figure in the text, that figure should be nearby the text so
that the reader can read your interpretation of the figure while looking at it.

All figures should be referenced and discussed in the text, i.e. don't just
throw in a figure because you made and it looks nice.

Only insert a figure when it enhances the story you are telling in the text.

Figure and Table Captions
-------------------------

Figures and tables and their associated captions should be able to be removed
from the text and a reader should still be able to "read" the figure or table.
This means that the caption should help the reader know how to read the figure.
Anything that isn't obvious from teh figure's design should be include, e.g.
"The solid black lines represent the real part of the eigenvalue loci for the
fifth eigenmode." The caption should not include discussion or interpretation
of the figure, that belongs in your primary text.

Creating figures
----------------

Students often create figures that are saved from figure creation software
without any adjustements to the default settings. The default settings are
never appropriate. Search the internet for how to make publication quality
figures with your preferred software. For example here are some

Python

- https://atchen.me/research/code/data-viz/2022/01/04/plotting-matplotlib-reference.html
- https://github.com/jbmouret/matplotlib_for_papers

Matlab

- https://www.mathworks.com/matlabcentral/fileexchange/47921-plotpub-publication-quality-graphs-in-matlab

Common issues:

- The figure is poorly scaled for actual paper sizes.
- Bitmap images have either too high or too low resolution. Make your
  resolutions 300 dpi (dot per inch).
- Font sizes are too small on axis labels and legends, for example.
- Grey backgrounds are left in the figure (common for Matlab).
- Readers cannot discern indivisual lines or dots in the plot. For example, you
  may have a time series line plot of an acceleromter over 30 minutes. Showing
  all 30 minutes is simply a blob of color that is not useful. Show only 1
  minute or 30 seconds so that the reader can see the data in a useful way.

Figure Copyright
----------------

In general, you cannot include figures you did not create draw yourself in your
document. If you want to include the figure there are essentially three
options:

1. Ask the copyright holder for written permission to use their figure.
2. If the copyright holder has licensed their figure with a Creative Commons
   license (or similar) then you can use the figure if you abide by the
   license's rules. This usually means displaying the reference to the license
   and the authors.
3. It may be possible to use the figure without permission if the use falls
   under an exception in your jurisdiction. Dutch Law seems to have exceptions
   for "Illustration for teaching or scientific research", "Quotation for
   criticism or review", and "Use for the purpose of research or private
   study". https://en.wikipedia.org/wiki/Copyright_law_of_the_Netherlands

Math
----

Take time to typeset your math equations and number each equation for
referencing in the text. Follow mathematical notation standards to make it easy
for the readers.

Do not use :math:`a*b` or :math:`a\times b` to indicate scalar multiplication,
:math:`ab` is clear and more than sufficient.

LaTeX
-----

This is how you do quotes in LaTeX!

::

   `single quoted stuff`
   ``double quoted stuff''

Backticks on the left qutoes are necessary to obtain correctly formatted
quotation marks.

Code
----

There is no reason to include long scripts and programs in your thesis. If a
product of your thesis project is code, it is best to archive your code in the
proper file formats and then cited in your thesis. It is appropriate to include
code if you want the reader to read it. For example you may demonstrate an
algorithm by showing a short snippet of code.

Appendices
----------

Appendices are not just a clearing house to dump all the extra figures and
tables you generated. Appendices are ancillary chapters and sections of your
work. They provide supporting, but not necessary, information for the story in
your main chapters. For example, if you say in a main chapter "We measured the
stiffness of 10 bicycle tires and use those values in the model, see Appendix
A." then appendix A should be a new section with written content that explains
this measurement procedure. If it was in the main text it would distract the
reader from your main points, e.g. model description, but if the reader
questions your stiffness values they can then read the appendix to see how you
arrived at the values.

Style
=====

There are many writing styles; some styles fit with the norms in scientific
writing and some do not. It is extremely important to make your academmic
reports and papers as easy to understand as possible. Some style choices will
help you write more clearly.

Here are some recommendations:

- Write in active voice unless the context really needs passive voice to make
  things clearer.
- Write in present tense unless necessary to write in other tenses.

Allen has some nice style notes: https://sites.google.com/site/allendowney/style-guide

active voice vs passive voice
-----------------------------

https://allendowney.com/essays/passive.html

https://www.allendowney.com/blog/2019/12/18/please-stop-teaching-people-to-write-about-science-in-the-passive-voice/

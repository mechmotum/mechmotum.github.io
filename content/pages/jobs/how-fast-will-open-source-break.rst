========================================
How fast will my open source code break?
========================================

:date: 2020-09-18
:status: hidden
:slug: jobs/msc/how-fast-will-open-source-break

A downside about open source software is the fact that application program
interfaces (APIs) do not remain stable very long. If an author creates a
research paper using a software stack to produce the results, then doesn't
maintain the scripts as the software dependencies are updated, and then comes
back 1 year later it seems highly likely that the software will not run with
updated dependencies. One year isn't that long of a time in a research world.
This isn't good for reproducibility. There are different proposed solutions,
like shipping a virtual machine image with a paper that freezes the entire
stack. It is interesting to note that Matlab code that is 10+ years old tends
to run just fine with new version, leading to the belief that Mathworks takes
this API breakage much more seriously. Software developers are constantly faced
with the difficulties of maintain backwards compatibility and how easier it is
to introduce new features to software if the backwards compatibility shackles
are not present.

This project would work to characterize:

- how quickly changes in downstream dependencies break scientific software
- the ranking of stability in API for core software packages, i.e. can we label
  all software packages on their backwards incompatibility quality in a
  quantifiable way?
- can we determine how broadly semantic versioning is actually used and abided
  by?
- comparing the API stability culture among languages, e.g. Python and R
- how deep in the stack do you have to go to get stable APIs (for example the
  Linux kernel API is probably rock solid stable)

*Hypothesis*: On average a given script or software package that relies on a
high level scientific computing software stack will break within a year due to
unstable dependency APIs.

Possible Methods
================

Here is an idea for a method to do this:

1. Download a package or script at the top of (or near top of) the stack and
   log its release date
2. Install the dependencies specified at the time of release and ensure the
   software runs
3. Increment the dependency versions in chronological order and test if the
   script/package still runs at every increment. You can detect whether is runs
   or not and also whether deprecation warnings are emitted. If a single
   dependency fails, you can then fix it at the last working version and then
   continue to increment the other until you get to the script's release date
   or all dependencies fail.
4. Record the dates that your software gets deprecation warnings and fails.

Another method:

Track a code bases through git commits and somehow measure the frequency and
time of depredations and removals.

We will have to find a reliable way to get old dependencies installed. This is
often quite a painful process to simply get things installed as they were from
some point in the past.

Another thought:

We could check how many tests of a prior version raise errors or deprecation
warnings.

How to Apply
============

Send an email to j.k.moore@tudelft.nl with the title of the project in the
subject line. Include an approximately half-page motivation letter explaining
why you want to work in the Bicycle Lab on this project along with your current
resume or C.V.

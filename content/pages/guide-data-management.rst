======================
Guide: Data Management
======================

:date: 2022-09-21
:status: hidden

The Basics
==========

All researchers in the Bicycle Lab should establish and follow reasonable data
management practices for their project. If your data management practices
fulfill these three principles [*]_  then your approach is considered
reasonable and sufficient:

- If another researcher were to ask for the data and/or any related materials
  associated with your project, current lab members would be able to easily
  find it and send it to them without your assistance.
- If another researcher who works in the same field as us were to receive a
  copy of the data (and/or related materials) associated with your project,
  they would be able to use it without asking us too many questions.
- The lab PI will be able to find and use the data from this project five to
  ten years from now.

.. [*] Adapted from https://twitter.com/JohnBorghi/status/1356760061968740353)

Note that every new PhD has to create a data management plan in their first 5
months, see
https://www.tudelft.nl/en/library/research-data-management/r/plan/data-management-plans
for more info.

Read "The FAIR Guiding Principles for scientific data management and
stewardship" https://doi.org/10.1038/sdata.2016.18 to learn more about managing
your research outputs.

The following information details more specific tips, tools, and practices we
can follow to standardize as much as possible.

Digital Artifacts
=================

Examples of typical digital artifacts produced in our lab that should be stored
and managed:

- Editable source for your written work (LaTeX files, Word document, etc.)
- Computer scripts and programs
- Raw and/or processed data
- Editable CAD drawing source files
- Non-editable outputs: bitmap images, PDFs, etc.

Open Source Software
====================

We prefer that you share your software through one or more repositories in the
Github or Gitlab mechmotum organization. If it is encumbered by proprietary
agreements, we can create a private repository only viewable by the allowed
persons.

Example of two repositories from a single MSc project:

- https://github.com/mechmotum/TUDelft-SbW-Bicycle
- https://github.com/mechmotum/TUDelft_Bicycle_Handling_Test

Open Data
=========

If your data are not encumbered by GDPR protections, human subject
confidentiality, or proprietary agreements with project partners, we prefer
that you share your artifacts publicly in an archived repository. Some options
are:

- 4TU.ResearchData https://data.4tu.nl/
- Zenodo: https://zenodo.org/
- Figshare: https://figshare.com/

Here is an example of a past MSc project archived on Figshare:

https://figshare.com/projects/The_Water_Buffalo_Design_of_a_Portable_Bicycle_Powered_Irrigation_Pump_for_Small-Scale_African_Farmers/34397

Backup
======

- Use the 3-2-1 backup model: 3 copies of data, 2 different media, 1 off site.
  Always have a "do not touch! original data" backup elsewhere. Far far away
  :))
- Use calendar reminders to run backup or automate the backups.
- We do not advise using sync services (dropbox, google drive, etc.) for
  backup, as data can unintentionally be overwritten when synchronizing.

Security
========

- Use a different secure password for every account. These should be stored in
  an encrypted password manager.
- All employee and lab computers should have encrypted hard drives. If you make
  use of external drives, USB sticks, etc. encrypt these also.
- Copies of any usernames and passwords for lab accounts should be given to
  Jason for backup and access in the event you have left or are not available
  (do not email them!).

GDPR Protected Data
===================

If you collect privacy laden human subject data, then any personal information
about subjects should be stored via hard copy in the locked cabinet in Jason's
office. The data you work with on your computes should be anonymized with
respect to personal information.

Data Storage Options
====================

Use TU Delft supplied data storage for non-public data. Here are some options:

- TU Delft Google Drive. Ideally use a sub-folder in the "Fietslab Commons"
  folder for your work. Do not store human subject data or privacy laden data
  here. Before you graduate or end employment you must transfer ownership of
  these files to Jason or they will be deleted!
- TU Delft provides 500 Gb of Surfdrive space for every employee. Employee's
  can share a folder directly with a student for digital artifact deposition.
  Probably best for project archives < 2 Gb or so.
- Cloud storage available upon request through the 'Self-Service Portal'
  (https://tudelft.topdesk.net/tas/public/ssp/), for when 500GB isn't enough.
- Personal network drive (H:), 8 GB, just a drive for you to use by yourself,
  you can backup things there for example, but it is not recommended for
  confidential data.
- Staff group network drive (M:), 5 TB, used for having multiple staff use one
  shared network drive, don't use for confidential data (cause all staff see
  it). https://webdata.tudelft.nl
- Project network drive (UL), 5 TB, can create as many as you need for a shared
  project space. https://webdata.tudelft.nl

Closing Out a Project
=====================

- Request or create a long term data archive location.
- Provide Jason access to archive.
- Deposit your digital artifacts.
- Make clear if any data has privacy encumbrances.

Example Minimum for an MSc Project
==================================

- Request access to a Surfdrive folder from Jason.
- Collect and organize all of your digital artifacts with informative file
  names and/or folder names.
- The digital artifacts should include at least: raw data files, processed data
  files, processing scripts or spreadsheets, input files to data processing
  software, CAD files, production drawings, written document source files (e.g.
  LaTeX or MS Word), papers that you cited read in your documents, results
  figures, thesis presentation, equipment use explanations, experiment
  protocols, and human subject and equipment approvals.
- Write up READMEs for your digital artifacts so that someone can understand
  what is there.
- Upload your digital files to the Surfdrive folder.
- Absolutely make sure to transfer ownership to any files you deposited in the
  Lab Google Drive to Jason, otherwise the files will be automatically deleted
  when TU Delft removes your account post graduation/employment!

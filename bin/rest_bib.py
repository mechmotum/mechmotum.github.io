"""Generates a reStructuredText bibliography from a Zotero collection.

Depends on pyzotero.

You will need to create a Zotero account and API key and then have these values
available:

- library id : a number that identifies the Zotero user or group
- library type : either "user" or "group"
- collection id : characters that identify the collection owned by the user or
  group
- zotero api key : your API key

You can create a ``zotero_api.txt`` file adjacent to this script with your API
key as the only line in the file or you can pass the API key in via the command
line.

Display the bibliography in the terminal::

   rest_bib library_id library_type collection_id

Or save it to a file::

   rest_bib library_id library_type collection_id --file_name=page.rst

Or pipe it to generate another file type with Pandoc, for example::

   rest_bib library_id library_type collection_id | pandoc -s -o page.html

Some example input values:

library_id = "966974"  # group: mechmotum
library_type = "group"
collection_id = "3J8PXE2Z"  # "Lab Publications" collection in mechmotum

library_id = "425053"  # user: moorepants
library_type = "user"
collection_id = "B8PZ4ZAN"  # "My Publications" collection
collection_id = "7IG48IAS"  # "Products Page"

This script relies on using the Zotero item type to categorize the various
research products in specific way:

Journal Article
    Anything published in a peer reviewed journal.
Conference Paper
    Used for any full paper created for a conference that is published (peer
    reviewed or not). Do not use for conference abstracts, use "Presentation"
    for those.
Book
    Any published book (can be self-published).
Document
    Grant proposals.
Thesis
    Any BSc, MSc, or PhD thesis or dissertation.
Report
    Technical and other reports, for example a Bachelor End Project report.
Preprint
    For preprints that are hosted on an official repository.
Blog Post
    Any informal web article written by us.
Manuscript
    Draft papers (pre-pre prints), papers under review, papers submitted, in
    preparation.
Presentation
    Any conference presentation, workshop presentation, etc. Can include the
    slides or abstract as the linked material.
Computer Program
    Software repositories or archives. If the "extra" field contains text in
    the following format, badges will be generated for the software:
    ``badges{pypi:dist_name,conda-forge:package_name,github:user/repo,gitlab:user/repo}``
Dataset
    Data that has been shared on an archive.
Video Recording
    Video media coverage.
Magazine Article
    Written media coverage.

TODO:

- Add badges to software
- Add grant proposals

"""
import re
import sys
from pyzotero.zotero import Zotero

# map zotero item types to the page headings, this also defines the order of
# display
heading_map = {
    'journalArticle': 'Journal Articles',
    'conferencePaper': 'Conference Proceedings Articles',
    'book': 'Books',
    'thesis': 'Theses and Dissertations',
    'report': 'Reports',
    'document': 'Grant Proposals',
    'preprint': 'Preprints',
    'manuscript': 'Articles In Preparation or Under Review',
    'blogPost': 'Web Articles',
    'presentation': 'Presentations',
    'computerProgram': 'Software',
    'dataset': 'Data',
    'videoRecording': 'Media',
    'magazineArticle': 'Media Articles',
}


def make_author_list(creators):
    """Returns the authors string, e.g. Jason K. Moore, Christoph Konrad, and
    Mont Hubbard. Bolds presenters."""

    def make_name(creator):
        if 'name' in creator:
            name = creator['name']
        else:
            name = creator['firstName'] + " " + creator['lastName']
        if creator['creatorType'] == 'presenter':
            name = '**' + name + '**'
        else:
            name = '`' + name + '`'
        return name

    if len(creators) == 1:
        creator = creators[0]
        return make_name(creator)
    else:
        authors = ', '.join([make_name(author) for author in creators[:-1]])
        if len(creators) > 2:
            authors += ','
        name = make_name(creators[-1])
        authors += (' and ' + name)
        return authors


def formatter_preprint(data):
    template = (
        '{authors}, '
        '"{title}," '
        '{archive}, '
        '{year}, '
        '`{doi} <https://dx.doi.org/{doi}>`_'
    )

    return template.format(
        authors=make_author_list(data['creators']),
        year=data['date'].split('-')[0],
        title=data['title'],
        archive=data['repository'],
        doi=data['DOI'],
    )


def formatter_journal(data):
    template = (
        '{authors}, '
        '"{title}," '
        '{journal}, '
        '{year}, '
        '`{doi} <https://dx.doi.org/{doi}>`_'
    )

    return template.format(
        authors=make_author_list(data['creators']),
        year=data['date'].split('-')[0],
        title=data['title'],
        journal=data['publicationTitle'],
        doi=data['DOI'],
    )


def formatter_presentations(data):
    template = (
        '{authors}, '
        '"{title}," '
        '{place}, '
        '{year}, '
    )
    if data['url']:
        template += '[`{type} <{url}>`__]'
    else:
        template += '[{type}]'

    return template.format(
        authors=make_author_list(data['creators']),
        year=data['date'],
        title=data['title'],
        place=data['place'],
        url=data['url'],
        type=data['presentationType'],
    )


def formatter_proceedings(data):
    if data['DOI']:
        hyperlink = '`{DOI} <https://dx.doi.org/{DOI}>`_'.format(**data)
    elif data['url']:
        hyperlink = '`{url} <{url}>`_'.format(**data)
    else:
        hyperlink = ''
    template = (
        '{authors}, '
        '"{title}," '
        '{conference}, '
        '{year}, '
        '{hyperlink}'
    )

    return template.format(
        authors=make_author_list(data['creators']),
        year=data['date'],
        title=data['title'],
        conference=data['conferenceName'],
        hyperlink=hyperlink,
    )


def formatter_book(data):
    if data['url']:
        hyperlink = '`{url} <{url}>`_'.format(**data)
    else:
        hyperlink = ''
    template = (
        '{authors}, '
        '"{title}," '
        '{year}, '
        '{publisher}, '
        '{ISBN}'
        '{hyperlink}'
    )

    return template.format(
        authors=make_author_list(data['creators']),
        year=data['date'].split('-')[0],
        title=data['title'],
        publisher=data['publisher'],
        ISBN='ISBN ' + data['ISBN'] + ', ' if data['ISBN'] else '',
        hyperlink=hyperlink,
    )


def formatter_thesis(data):
    template = (
        '{authors}, '
        '"`{title} <{url}>`_," '
        '[{type}], '
        '{year}, '
        '{university}, '
        '{place}'
    )
    return template.format(
        authors=make_author_list(data['creators']),
        year=data['date'],
        title=data['title'],
        type=data['thesisType'],
        university=data['university'],
        place=data['place'],
        url=data['url'],
    )


def formatter_data(data):
    template = (
        '{authors}, '
        '"`{title} <{url}>`__", '
        '{year}, '
        '{repository}, '
        '`{DOI} <https://dx.doi.org/{DOI}>`_'
    )

    return template.format(
        authors=make_author_list(data['creators']),
        year=data['date'],
        title=data['title'],
        url=data['url'],
        DOI=data['DOI'],
        repository=data['repository'],
    )


def formatter_blog(data):
    if data['url']:
        template = '{authors}, "`{title} <{url}>`__", {year}, {blog}'
    else:
        template = '{authors}, "{title}", {year}, {blog}'

    return template.format(
        authors=make_author_list(data['creators']),
        year=data['date'],
        title=data['title'],
        url=data['url'] if data['url'] else 'http://',
        blog=data['blogTitle'],
    )


def formatter_manuscript(data):
    template = '{authors}, "`{title} <{url}>`__", {year}, {type}'

    return template.format(
        authors=make_author_list(data['creators']),
        year=data['date'],
        title=data['title'],
        url=data['url'] if data['url'] else 'http://',
        type=data['manuscriptType'],
    )


def formatter_report(data):
    template = '{authors}, "`{title} <{url}>`__", {typ}, {year}, {institution}'

    return template.format(
        authors=make_author_list(data['creators']),
        year=data['date'],
        title=data['title'],
        url=data['url'] if data['url'] else 'http://',
        typ=data['reportType'],
        institution=data['institution'],
    )


def formatter_software(data):
    template = '{authors}, "`{title} <{url}>`__", {year}'
    item = template.format(
        authors=make_author_list(data['creators']),
        year=data['date'],
        title=data['title'],
        url=data['url'] if data['url'] else 'http://',
    )

    badge_templates = {
        'github': (
            "https://img.shields.io/github/v/release/{name}?label=Github",
            "https://github.com/{name}",
        ),
        'gitlab': (
            "https://img.shields.io/gitlab/v/release/{name}?label=Gitlab",
            "https://gitlab.com/{name}",
        ),
        'pypi': (
            "https://img.shields.io/pypi/v/{name}.png",
            "https://pypi.org/project/{name}",
        ),
        'pypi-downloads': (
            "https://pepy.tech/badge/{name}",
            "https://pypi.org/project/{name}",
        ),
        'conda-forge': (
            "https://img.shields.io/conda/v/conda-forge/{name}.png",
            "https://anaconda.org/conda-forge/{name}",
        ),
        'conda-forge-downloads': (
            "https://img.shields.io/conda/dn/conda-forge/{name}.png",
            "https://anaconda.org/conda-forge/{name}",
        ),
    }

    badge_line = " "
    img_line = ""
    # TODO : The img_template should be indented different number of characters
    # depending on the item count, which is not accessible in this function.
    img_template = """
    .. |{tag}-{name}| image:: {badgeurl}
       :alt: {repo}-{name} badge
       :target: {targeturl}"""
    badges = re.search(r'badges\{(.*)\}', data['extra'])
    if badges:
        badges = badges.group(1)
        badge_map = badges.split(',')
        for badge in badge_map:
            repo, name = badge.split(':')
            for img_tag, (badgeurl, targeturl) in badge_templates.items():
                if img_tag.startswith(repo):
                    badge_line += f'|{img_tag}-{name}| '
                    img_line += img_template.format(
                        tag=img_tag,
                        name=name,
                        badgeurl=badgeurl.format(name=name),
                        repo=repo,
                        targeturl=targeturl.format(name=name)) + '\n'
        item += badge_line[:-1] + '\n'
        item += img_line

    return item


def formatter(data):
    template = '{authors}, "`{title} <{url}>`__", {year}'

    return template.format(
        authors=make_author_list(data['creators']),
        year=data['date'],
        title=data['title'],
        url=data['url'] if data['url'] else 'http://',
    )


formatter_map = {
    'blogPost': formatter_blog,
    'book': formatter_book,
    'computerProgram': formatter_software,
    'conferencePaper': formatter_proceedings,
    'dataset': formatter_data,
    'document': formatter,
    'journalArticle': formatter_journal,
    'magazineArticle': formatter,
    'manuscript': formatter_manuscript,
    'preprint': formatter_preprint,
    'presentation': formatter_presentations,
    'report': formatter_report,
    'thesis': formatter_thesis,
    'videoRecording': formatter,
}


def generate_bibliography(library_id, library_type, collection_id,
                          api_key=None, file_name=None):
    if api_key is None:
        with open('zotero_api.txt') as f:
            api_key = f.read().strip()

    zot = Zotero(library_id=library_id, library_type=library_type,
                 api_key=api_key)

    items = zot.everything(zot.collection_items(collection_id, sort='date'))

    reference_lists = {v: [] for k, v in heading_map.items()}
    for item in items:
        item_type = item['data']['itemType']
        if item_type != 'attachment':
            form = formatter_map[item_type]
            reference_lists[heading_map[item_type]].append(form(item['data']))

    page_txt = ""
    for heading, ref_list in reference_lists.items():
        if ref_list:
            page_txt += heading + '\n'
            page_txt += '='*len(heading) + '\n\n'
            page_txt += '\n'.join(['{}. {}'.format(str(i + 1), ref)
                                   for i, ref in enumerate(ref_list)])
            page_txt += '\n\n'

    if file_name is None:
        sys.stdout.write(page_txt)
    else:
        with open(file_name, 'w') as f:
            f.write(page_txt)


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(
        description='Generate reStructuredText bibliography')

    parser.add_argument('library_id', type=str,
                        help="Zotero Library ID Number")

    parser.add_argument('library_type', type=str,
                        help="Either user or group")

    parser.add_argument('collection_id', type=str,
                        help="Zotero Collection ID Number")

    parser.add_argument('--api_key', type=str, default=None, required=False,
                        help="Zotero API Key")

    parser.add_argument('--file_name', type=str, default=None, required=False,
                        help="Save to filename instead of to STDOUT")

    args = parser.parse_args()

    generate_bibliography(args.library_id, args.library_type,
                          args.collection_id, api_key=args.api_key,
                          file_name=args.file_name)

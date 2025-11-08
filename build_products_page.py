"""

TODO
- DOI and URL should be displayed for each item, as there may be both
- Add grant proposals
- Add data
- Add badges to software
- Subheading by year?
- Outputs for other pages on the website
- Output for my personal website

"""
import sys
from pyzotero.zotero import Zotero

library_id = "966974"  # group: mechmotum
library_type = "group"
collection_id = "3J8PXE2Z"  # Lab Publications collection in mechmotum

library_id = "425053"  # user: moorepants
library_type = "user"
collection_id = "B8PZ4ZAN"  # My publications collection
collection_id = "7IG48IAS"  # Products Page

# map zotero item types to the page headings, this also defines the order of
# display
heading_map = {
    'journalArticle': 'Journal Articles',
    'conferencePaper': 'Conference Proceedings Articles',
    'book': 'Books',
    'thesis': 'Theses and Dissertations',
    'report': 'Reports',
    'preprint': 'Preprints',
    'blogPost': 'Web Articles',
    'manuscript': 'Working Papers',
    'presentation': 'Presentations',
    'computerProgram': 'Software',
    'dataset': 'Data',
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
        '`{doi} <https://dx.doi.org/{doi}>`_ '
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
        '`{doi} <https://dx.doi.org/{doi}>`_ '
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
        hyperlink = '`{DOI} <https://dx.doi.org/{DOI}>`_ '.format(**data)
    elif data['url']:
        hyperlink = '`{url} <{url}>`_ '.format(**data)
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
        hyperlink = '`{url} <{url}>`_ '.format(**data)
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
        '`{DOI} <https://dx.doi.org/{DOI}>`_ '
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


def formatter(data):
    template = '{authors}, "`{title} <{url}>`__", {year}'

    return template.format(
        authors=make_author_list(data['creators']),
        year=data['date'],
        title=data['title'],
        url=data['url'] if data['url'] else 'http://',
    )


formatter_map = {
    'attachment': lambda data: '',  # TODO : Not sure why this is present.
    'blogPost': formatter_blog,
    'book': formatter_book,
    'computerProgram': formatter,
    'conferencePaper': formatter_proceedings,
    'dataset': formatter_data,
    'journalArticle': formatter_journal,
    'manuscript': formatter_manuscript,
    'preprint': formatter_preprint,
    'presentation': formatter_presentations,
    'report': formatter_report,
    'thesis': formatter_thesis,
}


def generate_bibliography(library_id, library_type, collection_id, api_key='',
                          file_name=None):
    if not api_key:
        # NOTE : Create a file zotero_api.txt with the key adjacent to this
        # script.
        with open('zotero_api.txt') as f:
            api_key = f.read().strip()

    zot = Zotero(library_id=library_id, library_type=library_type,
                 api_key=api_key)

    items = zot.everything(zot.collection_items(collection_id, sort='date'))

    reference_lists = {v: [] for k, v in heading_map.items()}
    for item in items:
        item_type = item['data']['itemType']
        form = formatter_map[item_type]
        if item_type != 'attachment':
            reference_lists[heading_map[item_type]].append(form(item['data']))

    page_txt = ""
    for heading, ref_list in reference_lists.items():
        page_txt += heading + '\n'
        page_txt += '='*len(heading) + '\n'
        page_txt += '\n'.join(['{}. {}'.format(str(i + 1), ref)
                               for i, ref in enumerate(ref_list)])
        page_txt += '\n\n'

    if file_name is None:
        sys.stderr.write(page_txt)
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

    #generate_bibliography(args.library_id, args.library_type,
                            #args.collection_id, api_key=args.api_key,
                            #file_name=args.file_name)

    generate_bibliography(library_id, library_type, collection_id,
                          file_name='products_page.rst')

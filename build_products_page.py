"""

TODO
- separate tutorials from presentations
- separate conference abstracts from conference papers
- DOI and URL should be displayed for each item, as there may be both

"""
from pyzotero.zotero import Zotero

library_id = "966974"  # group: mechmotum
library_type = "group"
collection_id = "3J8PXE2Z"  # Lab Publications collection in mechmotum

library_id = "425053"  # user: moorepants
library_type = "user"
collection_id = "B8PZ4ZAN"  # My publications collection

# NOTE : Create a file zotero_api.txt with the key adjacent to this script.
with open('zotero_api.txt') as f:
    api_key = f.read().strip()

zot = Zotero(library_id=library_id, library_type=library_type, api_key=api_key)

# NOTE : You can return formatted citations like this:
# items = zot.collection_items(collection_id, content="bib", style="apa")
# or better yet, it would be nice if the formatted reference is in the standard
# json file should be able to do format='json' and include="bib",
# style"ieee", but this doesn't do it

items = zot.everything(zot.collection_items(collection_id, sort='date'))

# map zotero item types to the page headings
heading_map = {
    'attachment': 'attachment',
    'blogPost': 'web_articles',
    'book': 'books',
    'computerProgram': 'software',
    'conferencePaper': 'conference_proceedings',
    'dataset': 'data',
    'journalArticle': 'journal_articles',
    'manuscript': 'review',
    'preprint': 'preprints',
    'presentation': 'presentations',
    'report': 'reports',
    'thesis': 'theses',
}

reference_lists = {v: [] for k, v in heading_map.items()}

journal_articles_text_list = []
theses_text_list = []


def make_author_list(creators):

    def make_name(creator):
        if 'name' in creator:
            name = creator['name']
        else:
            name = creator['firstName'] + " " + creator['lastName']
        if creator['creatorType'] == 'presenter':
            name = '**' + name + '**'
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
    if data['url']:
        hyperlink = '`{url} <{url}>`_ '.format(**data)
    else:
        hyperlink = ''
    template = (
        '{authors}, '
        '"{title} [{type}]," '
        '{conference}, '
        '{place}, '
        '{year}, '
        '{hyperlink}'
    )

    return template.format(
        authors=make_author_list(data['creators']),
        year=data['date'],
        title=data['title'],
        conference=data['meetingName'],
        place=data['place'],
        hyperlink=hyperlink,
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
        conference=data['proceedingsTitle'],
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
        '{ISBN}, '
        '{hyperlink}'
    )

    return template.format(
        authors=make_author_list(data['creators']),
        year=data['date'].split('-')[0],
        title=data['title'],
        publisher=data['publisher'],
        ISBN='ISBN ' + data['ISBN'] if data['ISBN'] else '',
        hyperlink=hyperlink,
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
    'attachment': lambda data: '',
    'blogPost': formatter,
    'book': formatter_book,
    'computerProgram': formatter,
    'conferencePaper': formatter_proceedings,
    'dataset': formatter,
    'journalArticle': formatter_journal,
    'manuscript': formatter,
    'preprint': formatter_preprint,
    'presentation': formatter_presentations,
    'report': formatter,
    'thesis': formatter,
}

for item in items:
    item_type = item['data']['itemType']
    form = formatter_map[item_type]
    reference_lists[heading_map[item_type]].append(form(item['data']))

with open('products_page_template.rst') as f:
    page_template = f.read()

enum_ref_txt = {}
for heading, ref_list in reference_lists.items():
    enum_ref_txt[heading] = '\n'.join(['{}. {}'.format(str(i + 1), ref)
                                       for i, ref in enumerate(ref_list)])

page_txt = page_template.format(
    books=enum_ref_txt['books'],
    conference_proceedings=enum_ref_txt['conference_proceedings'],
    data='',
    journal_articles=enum_ref_txt['journal_articles'],
    preprints=enum_ref_txt['preprints'],
    presentations=enum_ref_txt['presentations'],
    reports=enum_ref_txt['reports'],
    review=enum_ref_txt['review'],
    software=enum_ref_txt['software'],
    theses=enum_ref_txt['theses'],
    tutorials='',
    web_articles=enum_ref_txt['web_articles'],
)

with open('products_page.rst', 'w') as f:
    f.write(page_txt)

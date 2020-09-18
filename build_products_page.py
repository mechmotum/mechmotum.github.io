from pyzotero.zotero import Zotero

library_id = "966974"  # mechmotum
library_type = "group"
collection_id = "3J8PXE2Z"  # Lab Publications collection in mechmotum
# NOTE : Create a file zotero_api.txt with the key adjacent to this script.
with open('zotero_api.txt') as f:
    api_key = f.read().strip()

zot = Zotero(library_id=library_id, library_type=library_type, api_key=api_key)

# NOTE : You can return formatted citations like this:
# items = zot.collection_items(collection_id, content="bib", style="apa")

items = zot.collection_items(collection_id)

# map zotero item types to the page headings
heading_map = {
               'computerProgram': 'software',
               'conferencePaper': 'conference_proceedings',
               'journalArticle': 'journal_articles',
               'presentation': 'presentations',
               'report': 'reports',
               'thesis': 'theses',
               }

reference_lists = {v: [] for k, v in heading_map.items()}

journal_articles_text_list = []
theses_text_list = []


def formatter(data):
    template = '{authors}, "`{title} <{url}>`_", {year}'

    authors = ', '.join([author['lastName'] + ", " + author['firstName']
                         for author in data['creators']])
    return template.format(authors=authors,
                           year=data['date'],
                           title=data['title'],
                           url=data['url'] if data['url'] else 'http://')


for item in items:
    item_type = item['data']['itemType']
    #print(item_type)
    try:
        reference_lists[heading_map[item_type]].append(formatter(item['data']))
    except KeyError:
        pass

with open('products_page_template.rst') as f:
    page_template = f.read()

enum_ref_txt = {}
for heading, ref_list in reference_lists.items():
    enum_ref_txt[heading] = '\n'.join(['{}. {}'.format(str(i + 1), ref)
                                       for i, ref in enumerate(ref_list)])

page_txt = page_template.format(
    journal_articles=enum_ref_txt['journal_articles'],
    theses=enum_ref_txt['theses'],
    books='',
    conference_proceedings=enum_ref_txt['conference_proceedings'],
    reports=enum_ref_txt['reports'],
    preprints='',
    presentations=enum_ref_txt['presentations'],
    web_articles='',
    tutorials='',
    software=enum_ref_txt['software'])

with open('products_page.rst', 'w') as f:
    f.write(page_txt)

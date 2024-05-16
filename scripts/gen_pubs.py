import os
import yaml

prefix = '''---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---\n\n'''

div_id = 0


venues = {
    'EACL': 'Annual Conference of the European Chapter of the Association for Computational Linguistics',
    'ICML': 'International Conference on Machine Learning',
    'EMNLP': 'Conference on Empirical Methods in Natural Language Processing',
    'NAACL': 'Annual Conference of the North American Chapter of the Association for Computational Linguistics',
    'TACL': 'Transactions of the Association for Computational Linguistics',
    'ACL': 'Annual Meeting of the Association for Computational Linguistics',
}


def gen_venue(ve):
    short, *track = ve.split('-')
    if short not in venues:
        return ve
    if len(track) > 0:
        return venues[short] + f' ({short}, {track[0]})'
    else:
        return venues[short] + f' ({short})'


def author_list(authors):
    aus = []
    for au in authors:
        if au.endswith('*'):
            star = r'\*'
            au = au[:-1]
        else:
            star = ''
        if 'Guanghui Qin' in au:
            au = '**' + au + '**'
        aus.append(au + star)
    if len(aus) <= 2:
        return ' and '.join(aus)
    return ', '.join(aus[:-1]) + ', and ' + aus[-1]


def bib_button(bib):
    global div_id
    bib = bib.replace("\n", "<br>\n").replace(' ', '&nbsp;')
    button = f'[<a href="javascript:toggleDiv(\'{div_id}bib\')">bibtex</a>]'
    div = f'''<div id="{div_id}bib" style="display: none" class="bib">
    {bib}
    </div>'''
    div_id += 1
    return button, div


def main():
    pubs = list()
    root = 'scripts/pubs'
    for fn in os.listdir(root):
        pubs.append(yaml.load(open(os.path.join(root, fn)), yaml.Loader))
    pubs.sort(key=lambda pu: (-pu['year'], pu.get('priority', 100)))

    texts = [prefix]
    for pub in pubs:
        if 'url' in pub:
            line = f'- [{pub["title"]}]({pub["url"]}). '
        else:
            line = f'- <span style="text-decoration:underline">{pub["title"]}</span>. '
        line += author_list(pub['authors']) + '. '
        line += f'In *{gen_venue(pub["venue"])}*, {pub["year"]}. '
        if 'remark' in pub:
            line += f'<span style="color:red">**{pub["remark"]}**</span>.'

        tag_elements = []
        if 'url' in pub:
            tag_elements.append(f'[<a href="{pub["url"]}">paper</a>]')
        for k in pub.get('links', []):
            tag_elements.append(f'[<a href="{pub["links"][k]}">{k}</a>]')

        bib_div = None
        if 'bib' in pub:
            bib_tag, bib_div = bib_button(pub['bib'])
            tag_elements.append(bib_tag)

        line += '<span>' + ' '.join(tag_elements) + '</span>'
        if bib_div is not None:
            line += '\n' + bib_div

        texts.append(line)

    with open('_pages/publications.md', 'w') as fp:
        fp.write('\n'.join(texts))


if __name__ == '__main__':
    main()

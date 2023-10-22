import os
import yaml

prefix = '''---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---\n\n'''


venues = {
    'EACL': 'Annual Conference of the European Chapter of the Association for Computational Linguistics',
    'ICML': 'International Conference on Machine Learning',
    'EMNLP': 'Conference on Empirical Methods in Natural Language Processing',
    'NAACL': 'Annual Conference of the North American Chapter of the Association for Computational Linguistics',
    'TACL': 'Transactions of the Association for Computational Linguistics',
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
            star = '\\\\*'
            au = au[:-1]
        else:
            star = ''
        if 'Guanghui Qin' in au:
            au = '**' + au + '**'
        aus.append(au + star)
    aus = [f'**{au}**' if 'Guanghui Qin' in au else au for au in authors]
    if len(aus) <= 2:
        return ' and '.join(aus)
    return ', '.join(aus[:-1]) + ', and ' + aus[-1]


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
            line = '- ' + pub['title'] + '. '
        line += author_list(pub['authors']) + '. '
        line += f'*{gen_venue(pub["venue"])}*, {pub["year"]}. '
        if 'remark' in pub:
            line += f'<span style="color:red">**{pub["remark"]}**</span>.'
        texts.append(line)

    with open('_pages/publications.md', 'w') as fp:
        fp.write('\n'.join(texts))


if __name__ == '__main__':
    main()

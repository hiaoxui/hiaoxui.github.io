import os
import yaml

prefix = '''---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---\n\n

<style>
  /* ==== switch toggle ===== */
  .switch {
    --track-w: 2.4rem;   /* overall size – edit just these two lines */
    --track-h: 1.3rem;

    position: relative;
    display: inline-flex;
    align-items: center;
    font-size: 0.95rem;
    gap: 0.55rem;
    cursor: pointer;
    user-select: none;
  }

  /* hide the native checkbox but keep it accessible */
  .switch input {
    position: absolute;
    opacity: 0;
    width: 0;
    height: 0;
  }

  /* track */
  .switch .track {
    width: var(--track-w);
    height: var(--track-h);
    background: #c4c6c9;
    border-radius: var(--track-h);
    transition: background 0.2s ease;
  }

  /* thumb */
  .switch .thumb {
    position: absolute;
    top: 0.1rem;
    left: 0.1rem;
    width: calc(var(--track-h) - 0.2rem);
    height: calc(var(--track-h) - 0.2rem);
    background: #fff;
    border-radius: 50%;
    box-shadow: 0 0 2px rgba(0,0,0,.25);
    transition: transform 0.2s ease;
  }

  /* when checked → move thumb + change track color */
  .switch input:checked + .track {
    background: #007acc;            /* pick any accent color */
  }
  .switch input:checked + .track .thumb {
    transform: translateX(calc(var(--track-w) - var(--track-h)));
  }
</style>

<label class="switch">
  <input type="checkbox" id="onlySelected" checked>
  <span class="track"><span class="thumb"></span></span>
  Selected&nbsp;publications
</label>


'''

div_id = 0


venues = {
    'EACL': 'Annual Conference of the European Chapter of the Association for Computational Linguistics',
    'ICML': 'International Conference on Machine Learning',
    'EMNLP': 'Conference on Empirical Methods in Natural Language Processing',
    'NAACL': 'Annual Conference of the North American Chapter of the Association for Computational Linguistics',
    'NAACL25': 'Annual Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics',
    'TACL': 'Transactions of the Association for Computational Linguistics',
    'ACL': 'Annual Meeting of the Association for Computational Linguistics',
}


def gen_venue(ve):
    short, *track = ve.split('-')
    if short not in venues:
        return ve
    ve = venues[short]
    short = short.replace('NAACL25', 'NAACL')
    if len(track) > 0:
        return ve + f' ({short}, {track[0]})'
    else:
        return ve + f' ({short})'


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
    div = f'''\n\n\n<div id="{div_id}bib" style="display: none" class="bib">
    {bib}
    </div>\n\n\n'''
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

        if pub['show']:
            select = '{: .publication .selected}\n'
        else:
            select = '{: .publication data-selected="false"}\n'

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
        line += '\n' + select + '\n\n'
        if bib_div is not None:
            line += '\n\n' + bib_div

        texts.append(line)
    texts.append(script_text)

    to_dump = '\n'.join(texts)

    with open('_pages/publications.md', 'w') as fp:
        fp.write(to_dump)



script_text = '''
<script>
/* 🧩 3) Tiny JS controller */
const checkbox = document.getElementById('onlySelected');
const allUnselected = document.querySelectorAll('.publication[data-selected="false"]');

/* Reusable helper */
function updateVisibility() {
  const shouldHide = checkbox.checked;          // true → hide .unselected
  allUnselected.forEach(ul => {
    ul.style.display = shouldHide ? 'none' : '';  // show/hide
  });
}

/* Run once on load (because the box starts checked) */
updateVisibility();

/* And whenever the user toggles it */
checkbox.addEventListener('change', updateVisibility);
</script>
'''


if __name__ == '__main__':
    main()




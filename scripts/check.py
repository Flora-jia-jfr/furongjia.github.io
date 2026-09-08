#!/usr/bin/env python3
"""Check generated content and internal links without third-party dependencies."""
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
DATA = json.loads((ROOT / 'content/site.json').read_text())


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path, self.ids, self.links, self.titles = path, [], [], 0
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'h1':
            self.titles += 1
        for key in ('href', 'src', 'data'):
            if key in attrs:
                self.links.append(attrs[key])
        if tag == 'img':
            assert attrs.get('alt'), f'Missing alt text: {self.path.name}'


def main():
    pages = {path: Page(path) for path in ROOT.glob('*.html')}
    checked = 0
    for path, page in pages.items():
        assert len(page.ids) == len(set(page.ids)), f'Duplicate IDs in {path.name}'
        if path.name not in ('publications.html', 'service.html', 'projects.html', 'blogs.html', 'photography.html'):
            assert page.titles == 1, f'Expected one h1 in {path.name}'
        for href in page.links:
            url = urlsplit(href)
            if url.scheme or url.netloc:
                continue
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            assert target.is_relative_to(ROOT), f'Link leaves site: {href}'
            assert target.exists(), f'Broken local link in {path.name}: {href}'
            if url.fragment and target in pages:
                assert unquote(url.fragment) in pages[target].ids, f'Broken anchor in {path.name}: {href}'
            checked += 1
    expected = [paper['id'] for paper in DATA['publications']]
    for filename in ('index.html',):
        page = pages[ROOT / filename]
        assert all(page.ids.count(key) == 1 for key in expected), f'Missing or repeated papers in {filename}'
        rendered = [key for key in page.ids if key in expected]
        ordered = sorted(DATA['publications'], key=lambda p: -p['year'])
        assert rendered == [p['id'] for p in ordered], f'Unexpected paper order in {filename}'
    assert all((ROOT / p['image']).is_file() for p in DATA['publications'] if p.get('image'))
    print(f'Checked {len(pages)} HTML files, {checked} internal links, and all {len(expected)} papers on the homepage.')


if __name__ == '__main__':
    main()

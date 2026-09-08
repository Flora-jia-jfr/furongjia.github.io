#!/usr/bin/env python3
"""Build the GitHub Pages HTML from local content, using Python's standard library."""
import html
import json
from pathlib import Path
from string import Template
from urllib.parse import urljoin

ROOT = Path(__file__).resolve().parent.parent
DATA = json.loads((ROOT / 'content/site.json').read_text())
PROFILE = DATA['profile']
SHELL = Template((ROOT / 'templates/base.html').read_text())


def esc(value):
    return html.escape(str(value), quote=True)


def link(label, url, extra=''):
    return f'<a href="{esc(url)}"{extra}>{esc(label)}</a>'


def items(values):
    return '<ul class="plain-list">' + ''.join(f'<li>{esc(v)}</li>' for v in values) + '</ul>'


def section(title, body, anchor, extra=''):
    return f'<section class="section {extra}" id="{anchor}"><h2>{title}</h2>{body}</section>'


def paper_row(paper):
    title = link(paper['title'], paper['links'][0]['url']) if paper['links'] else esc(paper['title'])
    authors = esc(paper['authors']).replace(esc(PROFILE['name']), f'<strong>{esc(PROFILE["name"])}</strong>')
    links = ''.join(link(l['label'], l['url']) for l in paper['links'])
    venue = f'<span class="venue">{esc(paper["venue"])}</span>' if paper.get('venue') else ''
    return f'<li class="paper" id="{esc(paper["id"])}"><article><h3 class="paper-title">{title}</h3><p class="authors">{authors}</p><div class="paper-meta">{venue}{links}</div></article></li>'


def papers(page=False):
    tag = 'h1' if page else 'h2'
    result = f'<section class="section" id="publications"><div class="section-heading"><{tag}>Publications</{tag}><span class="equal-contribution">* Equal contribution</span></div>'
    groups = []
    for year in sorted({p['year'] for p in DATA['publications']}, reverse=True):
        groups.append((str(year), [p for p in DATA['publications'] if p['year'] == year]))
    for title, rows in groups:
        result += f'<h3 class="year-heading">{title}</h3><ul class="paper-list">' + ''.join(map(paper_row, rows)) + '</ul>'
    return result + '</section>'


def education():
    result = ''
    for row in DATA['education']:
        detail = f'<p class="muted">{esc(row["detail"])}</p>' if row['detail'] else ''
        result += f'<article class="experience"><h3>{esc(row["degree"])}</h3><p>{esc(row["institution"])}</p>{detail}</article>'
    return result


def experience():
    result = '<section class="section" id="research-experience"><h1>Research experience</h1>'
    for row in DATA['research_experience']:
        related = []
        for title in row['papers']:
            paper = next((p for p in DATA['publications'] if p['title'] == title), None)
            related.append('<li>' + (link(title, 'index.html#' + paper['id']) if paper else esc(title)) + '</li>')
        result += f'<article class="experience"><p class="period">{esc(row["period"])}</p><h2>{esc(row["institution"])}</h2><p class="mentor">Mentor: {esc(row["mentor"])}</p><ul class="plain-list">{"".join(related)}</ul></article>'
    return result + '</section>' + section('Teaching', items(DATA['teaching']), 'teaching') + section('Honors and awards', items(DATA['honors']), 'honors-and-awards')


def build_page(filename, title, content, current, description=None):
    routes = [('About', 'index.html', 'about'), ('Publications', 'publications.html', 'publications'), ('Experience', 'experience.html', 'experience'), ('Service', 'service.html', 'service'), ('CV', 'cv.html', 'cv')]
    navigation = ''.join(link(label, url, ' aria-current="page"' if key == current else '') for label, url, key in routes)
    socials = ''.join(link(row['label'], row['url']) for row in PROFILE['socials'])
    canonical = urljoin(PROFILE['url'], '' if filename == 'index.html' else filename)
    values = {key: esc(value) for key, value in PROFILE.items() if isinstance(value, str)}
    values.update(title=esc(title), description=esc(description or PROFILE['description']), canonical=esc(canonical), social_image=esc(urljoin(PROFILE['url'], PROFILE['photo'])), navigation=navigation, socials=socials, content=content)
    (ROOT / filename).write_text(SHELL.substitute(values))


def redirect(filename, target):
    # Keep old URLs useful while retiring the template-only sections.
    target = esc(target)
    (ROOT / filename).write_text(f'<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Furong Jia</title><meta name="robots" content="noindex"><meta http-equiv="refresh" content="0; url={target}"></head><body><p>This page has moved. <a href="{target}">Continue to Furong Jia’s website.</a></p></body></html>\n')


def main():
    about = '<section class="section about" id="about"><h1>About me</h1>' + ''.join(f'<p>{p}</p>' for p in DATA['about'])
    about += '</section>'
    service_summary = '<section class="section" id="academic-services"><div class="section-heading"><h2>Academic service</h2>' + link('Service & teaching →', 'service.html') + '</div>' + items(DATA['service']) + '</section>'
    build_page('index.html', 'Furong Jia', about + papers() + service_summary, 'about')
    build_page('publications.html', 'Publications · Furong Jia', papers(page=True), 'publications', 'All papers by Furong Jia, organized by year, with publication and code links.')
    build_page('experience.html', 'Experience · Furong Jia', experience(), 'experience', 'Research experience, teaching, and honors of Furong Jia.')
    service_page = '<section class="section" id="academic-services"><h1>Academic service</h1>' + items(DATA['service']) + '</section>' + section('Teaching', items(DATA['teaching']), 'teaching')
    build_page('service.html', 'Academic service · Furong Jia', service_page, 'service', 'Academic reviewing and teaching service by Furong Jia.')
    cv_url = esc(PROFILE['cv'])
    cv = f'<section class="section"><h1>Curriculum vitae</h1><div class="document-actions"><a class="document-link" href="{cv_url}">Open CV (PDF) ↗</a><a href="{cv_url}" download>Download</a></div><object class="cv-preview" data="{cv_url}" type="application/pdf" aria-label="Furong Jia curriculum vitae"><p><a href="{cv_url}">Open the CV PDF</a></p></object></section>'
    build_page('cv.html', 'CV · Furong Jia', cv + section('Education', education(), 'education'), 'cv', 'Curriculum vitae and education of Furong Jia, Computer Science Ph.D. student at Duke University.')
    for filename, target in [('projects.html', 'index.html#publications'), ('blogs.html', 'index.html'), ('photography.html', 'index.html')]:
        redirect(filename, target)
    urls = [PROFILE['url']] + [urljoin(PROFILE['url'], f) for f in ['publications.html', 'experience.html', 'service.html', 'cv.html']]
    (ROOT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>{esc(url)}</loc></url>\n' for url in urls) + '</urlset>\n')
    (ROOT / 'robots.txt').write_text(f'User-agent: *\nAllow: /\n\nSitemap: {PROFILE["url"]}sitemap.xml\n')
    (ROOT / '.nojekyll').touch()
    print(f'Built 5 pages and 3 legacy redirects with {len(DATA["publications"])} papers.')


if __name__ == '__main__':
    main()

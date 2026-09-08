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
    links = ''.join(f'<a class="paper-resource" href="{esc(l["url"])}">{esc(l["label"])}<span class="resource-arrow" aria-hidden="true">↗</span></a>' for l in paper['links'])
    venue = f'<span class="venue"><span class="venue-name">{esc(paper["venue"])}</span></span>' if paper.get('venue') else ''
    return f'<li class="paper" id="{esc(paper["id"])}"><article><h3 class="paper-title">{title}</h3><p class="authors">{authors}</p><div class="paper-meta">{venue}{links}</div></article></li>'


def papers():
    result = '<section class="section" id="publications"><div class="section-heading"><h2>Publications</h2><span class="equal-contribution">* Equal contribution</span></div>'
    rows = sorted(DATA['publications'], key=lambda p: p['year'], reverse=True)
    result += '<ul class="paper-list">' + ''.join(map(paper_row, rows)) + '</ul>'
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
        projects = ''
        for project in row['projects']:
            heading = f'<h3>{esc(project["title"])}</h3>' if project.get('title') else ''
            projects += f'<div class="research-project">{heading}{items(project["bullets"])}</div>'
        role = f'<span>{esc(row["role"])}</span>' if row.get('role') else ''
        mentor = f'<span>{esc(row["mentor_label"])}: {esc(row["mentor"])}</span>'
        result += f'<article class="experience"><div class="experience-meta"><span>{esc(row["period"])}</span><span>{esc(row["location"])}</span></div><h2>{esc(row["institution"])}</h2><p class="mentor">{role}{mentor}</p>{projects}</article>'
    return result + '</section>'


def build_page(filename, title, content, current, description=None):
    home = '' if filename == 'index.html' else 'index.html'
    routes = [('About', f'{home}#about', 'about'), ('Publications', f'{home}#publications', 'publications'), ('Experience', 'experience.html', 'experience'), ('Service', f'{home}#academic-services', 'service'), ('CV', 'cv.html', 'cv')]
    active = 'location' if filename == 'index.html' else 'page'
    navigation = ''.join(link(label, url, f' aria-current="{active}"' if key == current else '') for label, url, key in routes)
    socials = ''
    for row in PROFILE['socials']:
        icon = (ROOT / 'assets/icons' / (row['icon'] + '.svg')).read_text()
        icon = icon.replace('<svg ', '<svg aria-hidden="true" focusable="false" ', 1)
        socials += f'<a class="social-icon" href="{esc(row["url"])}" aria-label="{esc(row["label"])}" title="{esc(row["label"])}">{icon}</a>'
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
    reviewing = '; '.join(row.removeprefix('Reviewer: ') for row in DATA['service'])
    teaching = '; '.join(row.removeprefix('Teaching Assistant, ') for row in DATA['teaching'])
    service_summary = section('Academic service', f'<ul class="plain-list"><li><strong>Reviewer:</strong> {esc(reviewing)}.</li><li><strong>Teaching Assistant:</strong> {esc(teaching)}.</li></ul>', 'academic-services')
    build_page('index.html', 'Furong Jia', about + papers() + service_summary, 'about')
    build_page('experience.html', 'Experience · Furong Jia', experience(), 'experience', 'Research experience of Furong Jia.')
    cv_url = esc(PROFILE['cv'])
    cv = f'<section class="section"><h1>Curriculum vitae</h1><div class="document-actions"><a class="document-link" href="{cv_url}">Open CV (PDF) ↗</a><a href="{cv_url}" download>Download</a></div><object class="cv-preview" data="{cv_url}" type="application/pdf" aria-label="Furong Jia curriculum vitae"><p><a href="{cv_url}">Open the CV PDF</a></p></object></section>'
    build_page('cv.html', 'CV · Furong Jia', cv + section('Education', education(), 'education'), 'cv', 'Curriculum vitae and education of Furong Jia, Computer Science Ph.D. student at Duke University.')
    for filename, target in [('publications.html', 'index.html#publications'), ('service.html', 'index.html#academic-services'), ('projects.html', 'index.html#publications'), ('blogs.html', 'index.html'), ('photography.html', 'index.html')]:
        redirect(filename, target)
    urls = [PROFILE['url']] + [urljoin(PROFILE['url'], f) for f in ['experience.html', 'cv.html']]
    (ROOT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>{esc(url)}</loc></url>\n' for url in urls) + '</urlset>\n')
    (ROOT / 'robots.txt').write_text(f'User-agent: *\nAllow: /\n\nSitemap: {PROFILE["url"]}sitemap.xml\n')
    (ROOT / '.nojekyll').touch()
    print(f'Built 3 pages and 5 legacy redirects with {len(DATA["publications"])} papers.')


if __name__ == '__main__':
    main()

import os
import shutil
import json
from jinja2 import FileSystemLoader, Environment
import markdown


INDEX_TEMPLATE_HTML = 'index.html'
ARTICLE_TEMPLATE_HTML = 'article.html'
JSON_FILE = 'config.json'


def load_json_content(json_file):
    with open(json_file, 'r', encoding='utf-8') as json_content:
        return json.load(json_content)


def create_site_structure(structure):
    if not os.path.exists('site'):
        os.mkdir('site')
    if not os.path.exists('site/css'):
        shutil.copytree('templates/css', 'site/css')
    for dir in structure['articles']:
        article = dir['source']
        adrticle_dir_name = os.path.split(article)[0]
        if not os.path.exists('site/{}'.format(adrticle_dir_name)):
            os.mkdir('site/{}'.format(adrticle_dir_name))


def create_templates():
    loader = FileSystemLoader('templates',
                              followlinks=True,
                              encoding='utf-8')
    env = Environment(loader=loader, trim_blocks=True,
                      lstrip_blocks=True)
    index_template = env.get_template(INDEX_TEMPLATE_HTML)
    article_template = env.get_template(ARTICLE_TEMPLATE_HTML)
    return index_template, article_template


def get_index_page_content(structure):
    topics = structure['topics']
    articles = structure['articles']
    content = {'links': topics, 'articles': articles}
    return content


def create_index_page(template, content):
    with open("index.html", "w") as f:
        f.write(template.render(content))


def get_article_md_content(article):
    with open('articles/{}'.format(article['source']),
              mode="r",
              encoding="utf-8") as md_article:
        md_content = md_article.read()
        return md_content


def get_article_page_content(md_content):
    content = markdown.markdown(md_content)
    title = article['title']
    content = {'title': title, 'content': content}
    root, ext = os.path.splitext(article['source'])
    return content, root


def create_article_page(template, pahtway, content):
    with open('site/{}.html'.format(pahtway), "w") as f:
        f.write(template.render(content))


if __name__ == '__main__':
    try:
        structure = load_json_content(JSON_FILE)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        print('Error! Check that json file is exist and correct!')
    else:
        create_site_structure(structure)
        index_content = get_index_page_content(structure)
        index_template = create_templates()[0]
        article_template = create_templates()[1]
        create_index_page(index_template, index_content)
        articles = structure['articles']
        for article in articles:
            md_content = get_article_md_content(article)
            article_content = get_article_page_content(md_content)[0]
            pahtway = get_article_page_content(md_content)[1]
            create_article_page(article_template, pahtway, article_content)


import os
import shutil
import json
from jinja2 import FileSystemLoader, Environment
import markdown


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


def create_main_page(structure):
    loader = FileSystemLoader('templates',
                              followlinks=True,
                              encoding='utf-8')
    env = Environment(loader=loader, trim_blocks=True,
                      lstrip_blocks=True)
    template = env.get_template('index.html')
    topics = structure['topics']
    articles = structure['articles']
    data = {'links': topics, 'articles': articles}
    with open("index.html", "w") as f:
        f.write(template.render(data))


"""
def get_html_from_md(structure):
    articles = structure['articles']
    for article in articles:
        input_file = open('articles/{}'.format(article['source']),
                          mode="r",
                          encoding="utf-8")
        text = input_file.read()
        html = markdown.markdown(text)
        return html
"""


def create_articles(structure):
    loader = FileSystemLoader('templates',
                              followlinks=True
                              )
    env = Environment(loader=loader, trim_blocks=True,
                      lstrip_blocks=True)
    template = env.get_template('article.html')
    articles = structure['articles']
    for article in articles:
        input_file = open('articles/{}'.format(article['source']),
                          mode="r",
                          encoding="utf-8")
        text = input_file.read()
        title = article['title']
        content = markdown.markdown(text)
        data = {'title': title, 'content': content}
        root, ext = os.path.splitext(article['source'])
        with open('site/{}.html'.format(root), "w") as f:
            f.write(template.render(data))


if __name__ == '__main__':
    json_file = 'config.json'
    structure = load_json_content(json_file)
    create_site_structure(structure)
    create_main_page(structure)
    create_articles(structure)


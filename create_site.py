import json
from jinja2 import FileSystemLoader, Environment
import markdown

def load_json_content(json_file):
    with open(json_file, 'r', encoding='utf-8') as json_content:
        return json.load(json_content)


def test_jinja(index_page_content):
    env = Environment(loader=FileSystemLoader('site', followlinks=True, encoding='Windows-1251'), trim_blocks=True,
                      lstrip_blocks=True)
    template = env.get_template('index.html')
    topics = index_page_content['topics']
    articles = index_page_content['articles']
    data = {'links': topics, 'articles': articles}
    with open("site/new.html", "w") as f:
        f.write(template.render(data))


if __name__ == '__main__':
    json_file = 'config.json'
    index_page_content = load_json_content(json_file)
    test_jinja(index_page_content)

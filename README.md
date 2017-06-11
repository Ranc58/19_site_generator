# Encyclopedia

This program create html site with DevMan wiki about Python by markdown articles and json config file, where stored structure of site.

# How to install
1. Recomended use venv or virtualenv for better isolation.\
   Venv setup example: \
   `python3 -m venv myenv`\
   `source myenv/bin/activate`
2. Install requirements: \
   `pip3 install -r requirements.txt` (alternatively try add `sudo` before command)

# How to use
If it is needed edit `config.json` and put .md files to dir `site` in necessary folder.\
Then run program: `python3 create_site.py`.

Structure of site for example:
```
├── index.html
├── site
│   ├── css
│   │   ├── blog.css
│   │   ├── bootstrap.css
│   ├── 0_tutorial
│   │   ├──7_codenvy.html
│   │   ├──8_cli.html
│   │   ├──14_google.html
│   ├── 1_python_basics
│   │   ├──1_intro.html
│   │   ├──2_base_types.html
│   ├── 2_html
│   │   ├──html_injection.html
│   │   ├──special & symbol.html
```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

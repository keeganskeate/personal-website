import os

from django.utils.crypto import get_random_string
from markdown import markdown
from pymdownx import emoji

from personal_website import state # Save text in Firestore?

DOCS_PATH = "/static/personal_website/docs"
EXTENSIONS = [
    # "admonition",
    # "def_list",
    "codehilite",
    "fenced_code",
    # "nl2br", # Newlines treated as hard breaks
    # "smarty",  # Converts dashes, quotes, and ellipses.
    # "tables",  # Creates tables.
    # "toc",  # Creates table of contents with [TOC].
    # 'pymdownx.emoji',
    # 'pymdownx.superfences',
    # 'markdown.extensions.tables',
    # 'pymdownx.magiclink',
    # 'pymdownx.betterem',
    # 'pymdownx.highlight',
    # 'pymdownx.tilde',
    'pymdownx.emoji',
    # 'pymdownx.tasklist',
    # 'pymdownx.superfences',
    # 'pymdownx.saneheaders',
    'mdx_math',
]
EXTENSION_CONFIGS = {
    # "codehilite": {
    #     "css_class": "highlight",
    #     # "use_pygments": False,
    # },
    "pymdownx.emoji": {
        "emoji_index": emoji.gemoji,
        # "emoji_generator": emoji.to_png,
        "alt": "html_entity",
        "options": {
            # "attributes": {
            #     "align": "absmiddle",
            #     "height": "20px",
            #     "width": "20px"
            # },
            # "non_standard_image_path": None,
            # https://assets-cdn.github.com/images/icons/emoji/unicode/ # broken
            "image_path": "https://github.com/images/icons/emoji/unicode/",
            "non_standard_image_path": "https://github.com/images/icons/emoji/unicode/"
        }
    }
}


def create_page_context(context, file_path, markdown_file=None, options=None):
    """ Create context for a normal page. """
    context["state"] = state.state
    context["header"] = state.header
    context["footer"] = state.footer
    if markdown_file:
        context = load_markdown(
            context,
            file_path,
            markdown_file,
            options,
        )
    return context


def load_markdown(context, file_path, page, options=None, name="markdown"):
    """ Load markdown for context given page. """
    if options is None:
        options = EXTENSIONS
    file_name = f"{DOCS_PATH}/{page}.md"
    file_path += file_name
    markdown_file = open(file_path, "r")
    material = markdown_file.read()
    context[name] = markdown(
        material,
        extensions=options,
        extension_configs=EXTENSION_CONFIGS,
    )
    return context


def generate_secret_key(env_file_name):
    """ Generate a Django secret key. """
    env_file = open(env_file_name, "w+")
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    generated_secret_key = get_random_string(50, chars)
    env_file.write("SECRET_KEY = '{}'\n".format(generated_secret_key))
    env_file.close()

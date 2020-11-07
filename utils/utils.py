import os
from django.utils.crypto import get_random_string
from markdown import markdown

DEFAULT_OPTIONS = [
    "admonition",
    "def_list",
    "fenced_code",
    "nl2br", # Newlines treated as hard breaks
    "smarty",  # Converts dashes, quotes, and ellipses.
    "tables",  # Creates tables.
    "toc",  # Creates table of contents with [TOC].
    # "markdown_markup_emoji.markup_emoji",  # FIXME: Parses emojies!
]

def generate_secret_key(env_file_name):
    env_file = open(env_file_name, "w+")
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    generated_secret_key = get_random_string(50, chars)
    env_file.write("SECRET_KEY = '{}'\n".format(generated_secret_key))
    env_file.close()

def load_markdown(context, file_path, page, options=None, name="markdown"):
    """ Load markdown for context given page. """
    if options is None:
        options = DEFAULT_OPTIONS
    file_name = f"/static/personal_website/docs/{page}.md"
    file_path += file_name
    markdown_file = open(file_path, "r")
    material = markdown_file.read()
    context[name] = markdown(material, extensions=options)
    return context

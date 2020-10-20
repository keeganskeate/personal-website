import os
from markdown import markdown

DEFAULT_OPTIONS = [
    "admonition",
    "def_list",
    "fenced_code",
    "nl2br", # Newlines treated as hard breaks
    "smarty",  # Converts dashes, quotes, and ellipses.
    "tables",  # Creates tables.
    "toc",  # Creates table of contents with [TOC].
    # "markdown_markup_emoji.markup_emoji",  # Parses emojies!
]

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

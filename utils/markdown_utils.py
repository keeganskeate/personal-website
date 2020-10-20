import os
from markdown import markdown

DEFAULT_OPTIONS = [
    "admonition",
    "def_list",
    "fenced_code",
    # "markdown_markup_emoji.markup_emoji",  # Parses emojies!
    "smarty",  # Converts dashes, quotes, and ellipses.
    "tables",  # Creates tables.
    "toc",  # Creates table of contents with [TOC].
]

def load_markdown(context, file_path, page, options=None, context_name="markdown"):
    """ Load markdown for context given page. """
    app_name = file_path.split('\\')[-1]
    file_name = f"/static/{app_name}/docs/{page}.md"
    # file_name = os.path.join(file_path, file_name)
    markdown_file = open(file_name, "r")
    if options is None:
        options = DEFAULT_OPTIONS
    context[context_name] = markdown(
        markdown_file.read(), extensions=options
    )
    return context

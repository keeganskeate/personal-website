import os
from markdown import markdown

def load_markdown(context, file_path, page, options, context_name="markdown"):
    """ Load markdown for context given page. """
    app_name = file_path.split('\\')[-1]
    file_name = f"/static/{app_name}/docs/{page}.md"
    # file_path += file_name
    markdown_file = open(file_path + file_name, "r")
    context[context_name] = markdown(
        markdown_file.read(), extensions=options
    )
    return context

# Development

[TOC]

## Installation

You can begin by cloning the repository.

```shell

git clone https://github.com/keeganskeate/personal-website.git

```

See [architecture.md](docs/architecture.md) for information about the repository's architecture.

Next, follow [installation.md](docs/architecture.md) to create your credentials and install all of the project's dependencies.

Resources:

* [Django on Cloud Run](https://codelabs.developers.google.com/codelabs/cloud-run-django/index.html)


## Supporting Files

You can gather all supporting files into the `static` folder with:

```shell

python manage.py collectstatic

```

> Add the `--noinput` tag to suppress the overwrite warning.

You can configure static files to be served from [Firebase Storage](https://firebase.google.com/docs/storage) instead of from [Firebase Hosting](https://firebase.google.com/docs/hosting) in `personal_website/settings.py`.

## Running

You can then serve the site locally with:

```shell

python manage.py runserver

```

### Hot-Reloading (Livereload)

Hot-reloading is an important tool of development, so, you may want to install [django-live-reload-server](https://github.com/tjwalch/django-livereload-server):

```shell

pip install django-livereload-server

```

> django-livereload-server uses both [python-livereload](https://github.com/lepture/python-livereload) and [django-livereload](https://github.com/Fantomas42/django-livereload) for smooth reloading. Either project can be substituted if bugs are encountered.

In a console, start the livereload server:

```shell

python manage.py livereload

```

In another console, start the Django development server:

```shell

python manage.py runserver

```

It is an inconvinience to run 2 consoles, but a major convinience to have smooth hot-reloading. If you are using Node.js, then you can use the `npm run dev` command. If you are using [VS Code](https://code.visualstudio.com/download), then you can use the [NPM-Scripts](https://github.com/Duroktar/vscode-npm-scripts) extension to open the first terminal in VS Code.

> If you encounter a [django-livereload-server NotImplementedError](https://stackoverflow.com/questions/58422817/jupyter-notebook-with-python-3-8-notimplementederror), then it is likely that you are using Python 3.8+ and need to add the following code to `Lib\site-packages\tornado\platform\asyncio.py`.

  ```py

  import sys

  if sys.platform == 'win32':
      asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

  ```

Resources:

* [Livereload Chrome Extension](https://chrome.google.com/webstore/detail/livereload)
* [Django Livereload with Grunt](https://github.com/sinnwerkstatt/sinnwerkstatt-web/blob/master/Django/Django-livereload.md)

## Views

Views are Python functions that describe the data to be presented. [Django describes views](https://docs.djangoproject.com/en/3.1/intro/tutorial03/#write-views-that-actually-do-something) in the following quote.

> "Your view can read records from a database, or not. It can use a template system such as Django's – or a third-party Python template system – or not. It can generate a PDF file, output XML, create a ZIP file on the fly, anything you want, using whatever Python libraries you want."

## Templates

Tempaltes are Django HTML files that describe how the data is presented.

Default Django templates can be found in your Anaconda/Python directory in `Lib\site-packages\django\contrib\admin\templates\admin`.

### Text Material

All text material is either stored in JSON in `state.py` or written in Markdown in `docs` directories.

Resources:

* [`python-markdown` Extensions](https://python-markdown.github.io/extensions/)

## Data

The personal website has opted for a NoSQL approach for data management.

## Style

Style distinguishes one site from another. You are free and encouraged to modify the style to create a site that is uniquely yours. See [style.md](style.md) for a guide on the personal website's style.

## Testing and Debugging

You can check for errors with:

```shell

python manage.py check

```

You can run tests for an app with:

```shell

python manage.py test personal_website

```

See [testing](/testing) for more information.

## Helpful Resources

* [VS Code Django Guide](https://code.visualstudio.com/docs/python/tutorial-django)
* [How to reload Django?](https://stackoverflow.com/questions/19094720/how-to-automatically-reload-django-when-files-change)
* [django-livereload](https://github.com/Fantomas42/django-livereload)
* [django-livereload-server](https://github.com/tjwalch/django-livereload-server)
* [Browser Sync with Django and Docker](https://stackoverflow.com/questions/49482710/using-browser-sync-with-django-on-docker-compose)

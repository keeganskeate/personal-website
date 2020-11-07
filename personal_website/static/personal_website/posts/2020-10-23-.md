# Creating a Django Website and Hosting it with Firebase

Ever since I learned Python, I've wanted to create a website with Python. This site is built with Python Django and is open source, so, you can [clone this website](https://github.com/keeganskeate/personal-website) and tinker with it to your heart's content.

The personal website works right out of the box, however, it is recommended to setup your own credentials for deploying to production. The personal website uses [Firebase]((https://console.firebase.google.com/)) by default for many back-end services. As you are free to modify anything, you are welcome to modify the personal website to use the back-end services of your choice.

## Getting Started

First things first, clone the repository.


```shell

git clone https://github.com/keeganskeate/personal-website.git

```
## Architecture

The personal website generally follows a model-template-view (MTV) architectural pattern, where:

* The **model** is Django, the engine that sends requests to views.
* The **views** are Python functions that describe the data to be presented.
* The **templates** are Django HTML files that describe how the data is presented.

<!-- [Ducks file structure](https://github.com/erikras/ducks-modular-redux) is useful for modules and components. -->
The personal website favors a domain-style code structure for apps and material that will be edited frequently and a ducks-style code structure for concepts within the apps. Ducks 🦆 can inherit properties if needed and are encouraged to be individualized and self-contained as possible.

Directories:

* `.admin` - Project secrets (Keep secure. Do NOT upload to a public repository.)
* `assets` - All original assets; images, PDFs, etc.
* `personal_website` - Main app.
* `node_modules` - Node.js packages.
* `static` - Where static files are served, uploaded to hosting.
* `templates` - Django HTML templates for all apps.
* `utils` - Python utility (helper) functions.

Root folder files:

* `.env` - Locally save secrets (Keep secure. Do NOT upload to a public repository.)
* `.dockerignore` - Files to ignore when building a Docker container image.
* `.gitignore` - Files to ignore when committing to a Git repository.
* `cloudmigrate.yaml` - Cloud Run configuration.
* `db.sqlite3` - Default SQLite database for development or  low-volume web apps.
* `Dockerfile` - Configuration for Docker container image.
* `firebase.json` - Firebase hosting configuration.
* `LICENSE`- GNU General Public License.
* `manage.py` - Django utility.
* `package.json` - Node.js configuration.
* `readme.md` - General introduction and installation guide.
* `requirements.txt` - Python dependencies.
<!-- * `webpack.config.js` - Webpack configuration. -->

A Duck's 🦆 (an app's) directory usually contains:

* `static\${app_name}` - All app-specific supporting files.
  - `docs` - Text documents.
  - `images` - Supporting images.
  - `js` - App-related Javascript.
  - `css` - App-related CSS
* `templates\${app_name}` - App-specific tempaltes.
* `apps.py` - App configuration file.
* `state.py` - A file for storing state (a database is preferred).
* `urls.py` - App URL patterns.
* `views.py` - App view functions.

The main project app contains:

* `settings.py` - Django project settings.
* `asgi.py` - ASGI configuration.
* `wsgi.py` - WSGI configuration, enhanced with `dj-static`.

A Duck may also have:

* `forms.py` - Forms used in the app.

## Credentials

If you want to utilize the default backing services, then you will need a [Gmail or G Suite account](https://accounts.google.com/SignUp). The following documentation will assume that you are managing your own account.

### Creating Environmental Variables

Once you have an account, download the [Cloud SDK installer](https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe) and run:

```shell

gcloud init

```

Next, enable the Cloud APIs that are used:

```shell

gcloud services enable run.googleapis.com sql-component.googleapis.com sqladmin.googleapis.com compute.googleapis.com cloudbuild.googleapis.com secretmanager.googleapis.com

```

> You will need to [accept the Gcloud terms of service](https://console.developers.google.com/terms/cloud).

Second, store the configurations as a secret.

1. Open Google Cloud Shell.

2. Set project: `gcloud config set project personal-website`

3. Set the following environment variables:

```shell
PROJECT_ID=personal-website
REGION=us-central1
DJPASS="$(cat /dev/urandom | LC_ALL=C tr -dc 'a-zA-Z0-9' | fold -w 30 | head -n 1)"
GS_BUCKET_NAME=personal-website.appspot.com
echo DATABASE_URL=\"postgres://djuser:${DJPASS}@//cloudsql/${PROJECT_ID}:${REGION}:myinstance/mydatabase\" > .env
echo GS_BUCKET_NAME=\"${GS_BUCKET_NAME}\" >> .env
echo SECRET_KEY=\"$(cat /dev/urandom | LC_ALL=C tr -dc 'a-zA-Z0-9' | fold -w 50 | head -n 1)\" >> .env
echo DEBUG=\"True\" >> .env
gcloud secrets versions add application_settings --data-file .env
rm .env

```

You can create a secret if you haven't already with:

```shell

gcloud secrets create application_settings --replication-policy automatic

```

You can confirm the secret was created or updated with:

```
gcloud secrets versions list application_settings

```

Finally, you can [create a Google Cloud service account](https://cloud.google.com/docs/authentication/getting-started) and set the `GOOGLE_APPLICATION_CREDENTIALS` environmental variable to the full path to your credentials.

When you are finished, you should have a `.env` file stored in your root directory and a Gcloud service account and a Firebase service account stored in `admin/tokens`.

> Keep your `.env` file and service accounts safe and do not upload them to a public repository.

## Python

The personal website leverages the power of Python. The recommended way to install Python is "using conda. Anaconda Python is a self-contained Python environment that is particularly useful for scientific applications. If you don’t already have it, then you can start by installing [Miniconda](https://docs.conda.io/en/latest/miniconda.html), which includes a complete Python distribution and the conda package manager." The personal website is built with Python 3.

After you have installed a [distribution of Python](https://docs.conda.io/en/latest/miniconda.html), open the Anaconda Prompt, navigate to the personal website repository, and install Python dependencies:

```shell

pip install -r requirements.txt

```

You may also need to install other project and development dependencies, including:

* [dj-static](https://github.com/heroku-python/dj-static): `pip install dj-static`
* [django-livereload-server](https://github.com/tjwalch/django-livereload-server): `pip install django-livereload-server`
* [Psycopg2](https://www.psycopg.org/install/): `pip install psycopg2`
* [Python Decouple](https://pypi.org/project/python-decouple/): `pip install python-decouple`

## Node.js

The personal website utilizes Node.js for web development. You can[download Node.js](https://nodejs.org/en/download/) and install Node.js dependencies in the command prompt:

```shell

npm install

```

## Wrap-Up Installation

Great! You now have the personal website installed and are ready to start [developing](development.md). Make sure to document any bugs and your development process if you want to [contribute](contributing.md) to the project.

## Supporting Files

You can gather all supporting files into the `static` folder with:

```shell

python manage.py collectstatic

```

> Add the `--noinput` tag to suppress the overwrite warning.

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

## Data

The personal website has opted for a NoSQL approach for data management.

## Style

Style distinguishes one site from another. You are free and encouraged to modify the style to create a site that is uniquely yours.

[Bootstrap](https://getbootstrap.com/docs/4.5/getting-started/introduction/) is used for styling templates. You can install Bootstrap with:

```shell

npm install bootstrap
npm install style-loader --save

```

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

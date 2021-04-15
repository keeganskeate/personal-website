# Creating a Python Django Website and Hosting it with Firebase

11/10/2020

Ever since I learned Python, I've wanted to create a website with Python. This site is built with Django, a Python-based web framework, and is open source, so, you can [clone this website](https://github.com/keeganskeate/personal-website) and tinker with it to your heart's content. The website works right out of the box, however, it is recommended to setup your own credentials when deploying to production. The website uses [Firebase](https://console.firebase.google.com/) by default for many back-end services. As you are free to modify anything, you are welcome to modify the website to use the back-end services of your choice. Creation follows 3 broad steps:

* [Installation](#installation)
* [Development](#development)
* [Publishing](#publishing)

## Installation<a name="installation"></a>

First things first, you can clone the repository with:


```shell

git clone https://github.com/keeganskeate/personal-website.git

```

### Python<a name="python"></a>

This website leverages the power of Python. The recommended way to install Python is with [Anaconda](https://www.anaconda.com/products/individual/get-started-commercial-edition-1). Anaconda Python is a self-contained Python environment that is particularly useful for scientific applications. After you have installed a [distribution of Python](https://docs.conda.io/en/latest/miniconda.html), open the Anaconda Prompt, navigate to this website's repository, and install Python dependencies:

```shell

pip install -r requirements.txt

```

You may also need to install other project and development dependencies, including:

* [dj-static](https://github.com/heroku-python/dj-static): `pip install dj-static`
* [django-livereload-server](https://github.com/tjwalch/django-livereload-server): `pip install django-livereload-server`
* [Psycopg2](https://www.psycopg.org/install/): `pip install psycopg2`
* [Python Decouple](https://pypi.org/project/python-decouple/): `pip install python-decouple`


### Node.js<a name="node"></a>

The website utilizes Node.js for certain web development tools. You can [download Node.js](https://nodejs.org/en/download/) and install Node.js dependencies in the command prompt:

```shell

npm install

```

### Architecture

The website generally follows a model-template-view (MTV) architectural pattern, where:

* The **model** is Django, the engine that sends requests to views.
* The **views** are Python functions that describe the data to be presented.
* The **templates** are Django HTML files that describe how the data is presented.

<!-- [Ducks file structure](https://github.com/erikras/ducks-modular-redux) is useful for modules and components. -->
The website favors a domain-style code structure for apps and material that will be edited frequently and a ducks-style code structure for concepts within the apps. Ducks :duck: can inherit properties if needed and are encouraged to be individualized and self-contained as possible.

Directories:

* `.admin` - Project secrets (You should keep secure your secrets secret and NOT upload them a public repository.)
* `assets` - All original assets; images, PDFs, etc.
* `docs` - All documentation for development.
* `node_modules` - Node.js packages.
* `personal_website` - Main app.
* `public` - Static files to be uploaded to hosting and served in production.
* `templates` - Django HTML templates available for all apps.
* `utils` - Python utility (helper) functions.

Root folder files:

* `.env` - Locally saved secrets (You should keep this file secret.)
* `.dockerignore` - Files to ignore when building a Docker container image.
* `.gitignore` - Files to ignore when committing to a Git repository.
* `cloudmigrate.yaml` - Cloud Run configuration.
* `db.sqlite3` - Default (unused) SQLite database for development or low-volume web apps.
* `Dockerfile` - Configuration for Docker container image.
* `firebase.json` - Firebase hosting configuration.
* `LICENSE`- [GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.en.html).
* `manage.py` - Django utility script.
* `package.json` - Node.js configuration.
* `readme.md` - General introduction and installation guide.
* `requirements.txt` - Python dependencies.
<!-- * `webpack.config.js` - Webpack configuration. -->

A Duck's :duck: (an app's) directory usually contains:

* `static\{app_name}` - All app-specific supporting files.
  - `docs` - Text documents.
  - `images` - Supporting images.
  - `js` - App-related Javascript.
  - `css` - App-related CSS
* `templates\{app_name}` - App-specific tempaltes.
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


### Credentials<a name="credentials"></a>

If you want to utilize the default backing services, then you will need a [Gmail or G Suite account](https://accounts.google.com/SignUp). The following documentation will assume that you are managing your own account. Once you have an account, you will need to create your supporting environment variables. You can download the [Cloud SDK installer](https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe) and run:

```shell

gcloud init

```

Next, enable the Cloud APIs that are used:

```shell

gcloud services enable run.googleapis.com sql-component.googleapis.com sqladmin.googleapis.com compute.googleapis.com cloudbuild.googleapis.com secretmanager.googleapis.com

```

You will need to [accept the Gcloud terms of service](https://console.developers.google.com/terms/cloud). Next, store the configurations as a secret by following these steps.

1. Open [Google Cloud Shell](https://cloud.google.com/shell).

2. Set the project with: `gcloud config set project personal-website`

3. Set the following environment variables in the Google Cloud Shell or optionally in the Google Cloud SDK or with the command line noting that syntax will vary.

If you haven't already, then you can create a secret if you haven't already with:

```shell

gcloud secrets create etch_mobility_settings --replication-policy automatic

```

and allow Cloud Run access to access this secret:

```shell

export PROJECTNUM=$(gcloud projects describe ${PROJECT_ID} --format 'value(projectNumber)')
export CLOUDRUN=${PROJECTNUM}-compute@developer.gserviceaccount.com

gcloud secrets add-iam-policy-binding etch_mobility_settings \
  --member serviceAccount:${CLOUDRUN} --role roles/secretmanager.secretAccessor

```

Then run the following in the Google Cloud Shell:

```shell
PROJECT_ID=personal-website
REGION=us-central1
DJPASS="$(cat /dev/urandom | LC_ALL=C tr -dc 'a-zA-Z0-9' | fold -w 30 | head -n 1)"
GS_BUCKET_NAME=personal-website.appspot.com
echo DATABASE_URL=\"postgres://djuser:${DJPASS}@//cloudsql/${PROJECT_ID}:${REGION}:myinstance/mydatabase\" > .env
echo GS_BUCKET_NAME=\"${GS_BUCKET_NAME}\" >> .env
echo SECRET_KEY=\"$(cat /dev/urandom | LC_ALL=C tr -dc 'a-zA-Z0-9' | fold -w 50 | head -n 1)\" >> .env
echo DEBUG=\"True\" >> .env
echo EMAIL_HOST_USER=\"youremail@gmail.com\" >> .env
echo EMAIL_HOST_PASSWORD=\"your-app-password\" >> .env
gcloud secrets versions add application_settings --data-file .env
rm .env

```

> Set `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` with your Gmail email and [an app password](https://dev.to/abderrahmanemustapha/how-to-send-email-with-django-and-gmail-in-production-the-right-way-24ab). If you do not plan to use Django's email interface, then you exclude `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD`. You will need to setup billing for Google services at this point if you haven't already. You can allow Cloud Run access to access this secret with:

```shell

set GCS_SA==<path-to-your-service-account>

gcloud secrets add-iam-policy-binding etch_mobility_settings --member serviceAccount:${GCS_SA} --role roles/secretmanager.secretAccessor

```

You can confirm the secret was created or updated with:

```shell

gcloud secrets versions list etch_mobility_settings

```

When you are finished, you should have a `.env` file stored in your root directory. You can optionally store a Gcloud service account and/or a Firebase service account stored in `admin/tokens` if you need any Google Cloud or Firebase utilities. You can [create a Google Cloud service account](https://cloud.google.com/docs/authentication/getting-started) and set the `GOOGLE_APPLICATION_CREDENTIALS` environmental variable to the full path to your credentials to use Firebase services from within the Django app. Keep your `.env` file and service accounts secure and do not upload them to a public repository.

Helpful resources:

* [Generating Django Secret Keys](https://stackoverflow.com/questions/4664724/distributing-django-projects-with-unique-secret-keys)


## Development<a name="development"></a>

You can then serve the site locally at <http://127.0.0.1:8000/> with:

```shell

python manage.py runserver

```

You can gather all supporting files into the `static` folder with:

```shell

python manage.py collectstatic

```

You can add the `--noinput` tag to suppress the overwrite warning.

Helpful resources

* [VS Code Django Guide](https://code.visualstudio.com/docs/python/tutorial-django)
* [How to reload Django?](https://stackoverflow.com/questions/19094720/how-to-automatically-reload-django-when-files-change)
* [django-livereload](https://github.com/Fantomas42/django-livereload)
* [django-livereload-server](https://github.com/tjwalch/django-livereload-server)
* [Browser Sync with Django and Docker](https://stackoverflow.com/questions/49482710/using-browser-sync-with-django-on-docker-compose)


### Hot-Reloading (Livereload)<a name="hot-reload"></a>

Hot-reloading is an important tool of development, so, you may want to install [django-live-reload-server](https://github.com/tjwalch/django-livereload-server):

```shell

pip install django-livereload-server

```

> django-livereload-server uses both [python-livereload](https://github.com/lepture/python-livereload) and [django-livereload](https://github.com/Fantomas42/django-livereload) for smooth reloading. Either project can be substituted if bugs are encountered.

In a console, you can start the livereload server with:

```shell

python manage.py livereload

```

In another console, you can start the Django development server as usual and it will have live reloading:

```shell

python manage.py runserver

```

It is an inconvinience to run 2 consoles, but a major convinience to have smooth hot-reloading. If you are using Node.js, then you can use create a development environment with:

```shell

npm run dev

```

If you are using [VS Code](https://code.visualstudio.com/download), then you can use the [NPM-Scripts](https://github.com/Duroktar/vscode-npm-scripts) extension to open the first terminal in VS Code. If you encounter a [django-livereload-server NotImplementedError](https://stackoverflow.com/questions/58422817/jupyter-notebook-with-python-3-8-notimplementederror), then it is likely that you are using Python 3.8+ and need to add the following code to `Lib\site-packages\tornado\platform\asyncio.py`.

```python

import sys

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(
      asyncio.WindowsSelectorEventLoopPolicy()
    )

```

Helpful resources:

* [Livereload Chrome Extension](https://chrome.google.com/webstore/detail/livereload)
* [Django Livereload with Grunt](https://github.com/sinnwerkstatt/sinnwerkstatt-web/blob/master/Django/Django-livereload.md)


### Views<a name="views"></a>

Views are Python functions that describe the data to be presented. [Django describes views](https://docs.djangoproject.com/en/3.1/intro/tutorial03/#write-views-that-actually-do-something) in the following quote:

<small class="font-italic">"Your view can read records from a database, or not. It can use a template system such as Django's - or a third-party Python template system - or not. It can generate a PDF file, output XML, create a ZIP file on the fly, anything you want, using whatever Python libraries you want."</small>


### Templates<a name="templates"></a>

Tempaltes are Django HTML files that describe how the data is presented. Default Django templates can be found in your Anaconda/Python directory in `Lib\site-packages\django\contrib\admin\templates\admin`. This website has opted for a NoSQL approach for data management with Firebase's [Firestore](https://firebase.google.com/docs/firestore). All text material is either stored in JSON in `state.py` or written in Markdown in `docs` directories.

Helpful resources:

* [`python-markdown` Extensions](https://python-markdown.github.io/extensions/)


### Style<a name="style"></a>

Style distinguishes one site from another. You are free and encouraged to modify the style to create a site that is uniquely yours. [Bootstrap](https://getbootstrap.com/docs/4.5/getting-started/introduction/) is used for styling templates. You can install Bootstrap with:

```shell

npm install bootstrap
npm install style-loader --save

```

### Email<a name="email"></a>

If you are sending email with Gmail, then you can follow these steps.

- Navigate to [Gmail](mail.google.com), click your profile, and click manage your google account.
- Navigate to the [security tab](https://myaccount.google.com/security).
- Enable 2-step verification and then click on App passwords.
- Select Mail for app and enter a custom name for device.
- Click generate and Gmail will generate an app password. Copy this app password to a text file and save it where it is secure and will not be uploaded to a public repository, for example save the password in the `.admin` directory.

After you have created your app password, set your Gmail email and app password as environment variables, `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` respectively.

```shell

echo EMAIL_HOST_USER=\"youremail@gmail.com\" >> .env
echo EMAIL_HOST_PASSWORD=\"your-app-password\" >> .env
gcloud secrets versions add etch_mobility_settings --data-file .env

```

Helpful resources:

* [Email Self-Defense](https://emailselfdefense.fsf.org/en/)
* [GnuPG](https://www.gnupg.org/)
* [Django Email Templates](https://github.com/vintasoftware/django-templated-email)


### Forms<a name="forms"></a>

Django makes creating stock forms easy. Here are a few helpful resources to help you get started:

* [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/crispy_tag_forms.html)
* [How to use Bootstrap 4 Forms with Django](https://simpleisbetterthancomplex.com/tutorial/2018/08/13/how-to-use-bootstrap-4-forms-with-django.html)
* [Django Forms and Bootstrap](https://stackoverflow.com/questions/8474409/django-forms-and-bootstrap-css-classes-and-divs)


### Testing and Debugging<a name="testing"></a>

You can check for errors with:

```shell

python manage.py check

```

You can run tests for an app with:

```shell

python manage.py test personal_website

```

## Publishing<a name="publishing"></a>

Publishing is done with one command:

```shell

npm run publish

```

However, you will probably want to walk through the build process manually one time before using `npm run publish` to re-deploy when necessary. You will need to have Firebase's command line tool installed:

```shell

npm install -g firebase-tools

```

Afterwards, you can login to Firebase in the command line with:

```shell

firebase login

```

## Build process

The publishing build process contains three steps:

### 1. The app is containerized and uploaded to Container Registry.

You can build your container image using Cloud Build by running the following command from the directory containing the Dockerfile. Note that your `APP_ID` must be in snake case.

```shell

set PROJECT_ID=keegan-skeate-website
set APP_ID=personal-website
python manage.py collectstatic --noinput
gcloud builds submit --tag gcr.io/%PROJECT_ID%/%APP_ID%

```

### 2. The container image is deployed to Cloud Run.

You can containerize and deploy the website with:

```shell

set REGION=us-central1
gcloud run deploy %PROJECT_ID% --image gcr.io/%PROJECT_ID%/%APP_ID% --region %REGION% --allow-unauthenticated --platform managed

```

This project uses a fully managed Cloud Run platform. You can look into [Cloud Run for Anthos](https://cloud.google.com/anthos/run) if you desire. You can retrieve the service URL with:

```shell

gcloud run services describe etch-mobility \
  --platform managed \
  --region $REGION  \
  --format "value(status.url)"

```

### 3. Hosting requests are directed to the containerized app.

This step provides access to this containerized app from a [Firebase Hosting](https://firebase.google.com/docs/hosting) URL, so that the app can generate dynamic content for the Firebase-hosted site. You will need to be logged in with `firebase login`.

```shell

firebase deploy --project keegan-skeate-website

```

If you are using an SQL database, then you will also need to run:

```shell

gcloud builds submit --config cloudmigrate.yaml \
  --substitutions _REGION=$REGION

```


## Monitoring

You can view logs for your deployment in the Cloud Run console. When you are ready to re-deploy simply run:

```shell

npm run publish

```

<!-- You can register a domain with [Google Domains](https://domains.google.com/registrar/). You can then add a custom domain in the Firebase Hosting console. If you are using Google Domains, then use '@' for your root domain name and 'www' or 'www.domain.com' for your subdomains when registering your DNS A records. -->

You now have a simple, yet complex, website running on Cloud Run, which will automatically scale to handle your website's traffic, optimizing CPU and memory so that your website runs with the smallest footprint possible, saving you money. If you desire, you can now seamlessly integrate services such as Cloud Storage into your Python-based website. You can now plug and play and tinker to your :heart:'s content while your users enjoy your beautiful material!

# Installation

The personal website works right out of the box, however, it is recommended to setup your own credentials for deploying to production. The personal website uses Firebase by default for many back-end services. As you are free to modify anything, you are welcome to modify the personal website to use the back-end services of your choice.

[TOC]

## Getting Started

First things first, clone the repository.


```shell

git clone https://github.com/keeganskeate/personal-website.git

```

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

## Wrap-Up

Great! You now have the personal website installed and are ready to start [developing](development.md). Make sure to document any bugs and your development process if you want to [contribute](contributing.md) to the project.

## Resources

* [Django on Cloud Run](https://codelabs.developers.google.com/codelabs/cloud-run-django/index.html)


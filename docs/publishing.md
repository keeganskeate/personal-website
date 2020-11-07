# Publishing

Publishing is done with one command:

```shell

npm run publish

```

However, you will probably want to walk through the build process manually one time before using `npm run publish` to re-deploy when necessary.

You will need to have Firebase's command line tool installed:

```shell

npm install -g firebase-tools

```

Afterwards, you can login to Firebase in the command line with:

```shell

firebase login

```

## Build process

The publishing build process contains three steps:

1. The app is containerized and uploaded to Container Registry.

You can build your container image using Cloud Build by running the following command from the directory containing the Dockerfile:

```shell

set PROJECT_ID=keegan-skeate-website
set APP_ID=personal-website
python manage.py collectstatic --noinput
gcloud builds submit --tag gcr.io/%PROJECT_ID%/%APP_ID%

```

> Note that your `APP_ID` must be in snake case.

2. The container image is deployed to Cloud Run.

```shell

set REGION=us-central1
gcloud run deploy %PROJECT_ID% --image gcr.io/%PROJECT_ID%/%APP_ID% --region %REGION% --allow-unauthenticated --platform managed

```

> This project uses a fully managed Cloud Run platform. You can look into [Cloud Run for Anthos](https://cloud.google.com/anthos/run) if you desire.

> You can retrieve the service URL with:
  ```shell

  gcloud run services describe etch-mobility \
    --platform managed \
    --region $REGION  \
    --format "value(status.url)"

  ```

3. Hosting requests are directed to the containerized app.

This step provides access to this containerized app from a [Firebase Hosting](https://firebase.google.com/docs/hosting) URL, so that the app can generate dynamic content for the Firebase-hosted site.

```shell

firebase deploy --project keegan-skeate-website

```

> You will need to be logged in with `firebase login`.

> If you are using an SQL database, then you will also need to run:
  ```shell

  gcloud builds submit --config cloudmigrate.yaml \
    --substitutions _REGION=$REGION

  ```


## Monitoring

You can view logs for your deployment in the Cloud run console at https://console.cloud.google.com/run/detail/us-central1/your-project/logs?project=your-project


## Re-Deploying

When you are ready to re-deploy, simple run:

```shell

npm run publish

```


## (Optional) Setup a Custom Domain

You can register a domain with [Google Domains](https://domains.google.com/registrar/). You can then add a custom domain in the Firebase Hosting console.

> If you are using Google Domains, then use '@' for your root domain name and 'www' or 'www.domain.com' for your subdomains when registering your DNS A records.


## Takeaways

You now have a simple, yet complex, website running on Cloud Run, which will automatically scale to handle your website's traffic, optimizing CPU and memory so that your website runs with the smallest footprint possible, saving you money. If you desire, you can now seamlessly integrate services such as Cloud Storage into you Django website. You can now plug and play and tinker to your heart's content while your user's enjoy your beautiful material!

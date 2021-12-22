# HTTP

As HTTP is the easiest way to trigger a function, there isn't much additional setup required. All the configurations can be run as is but we'll point to a few things to keep in mind.

## Official Docs
For more information about HTTP triggers, check out the official [docs](https://cloud.google.com/functions/docs/calling/http).

## Cloudbuild.yaml
Because you're using an HTTP trigger, the `--trigger-http` flag is added. If this is removed, Cloud Build won't be able to properly create the function for the initial build.

## main.py
The `run_pipeline` is a simple function created to simply read in the request, unpackage it, and call your pipeline with the arguments. This is the function that will be called when the trigger is run. For more information about the request check the flask request object [docs](https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data).

# Pub/Sub

As Pub/Sub is can be used for many reasons, there isn't much configured by default. All the configurations can be run as is but we'll point to a few things to keep in mind.

## Official Docs
For more information about Pub/Sub triggers, check out the official [docs](https://cloud.google.com/functions/docs/calling/pubsub).

For more information about using it with Cloud Scheduler, check out the official [docs](https://cloud.google.com/scheduler/docs/tut-pub-sub)

## Cloudbuild.yaml
Because you're using a Pub/Sub trigger, the `--trigger-topic` flag is added with the value defaulting to your `project_slug`. If this is removed, Cloud Build won't be able to properly create the function for the initial build. To update this, simply change the value and redeploy.

## main.py
The `run_pipeline` is a simple function created to simply read in the request, unpackage it, and call your pipeline with the arguments. This is the function that will be called when the trigger is run. Note we only use the `event` variable by default and don't interact with `context`. While it can be useful, it didn't seem necessary to be used by default.

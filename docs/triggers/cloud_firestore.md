# Cloud Firestore

As a Cloud Firestore trigger is a little more complex, there are some variables that are left empty by default and MUST be filled in manually.

## Official Docs
For more information about Cloud Firestore triggers, check out the official [docs](https://cloud.google.com/functions/docs/calling/cloud-firestore).

## Cloudbuild.yaml
Because you're using a Cloud Storage trigger, the `--trigger-resource` and  `--trigger-event` are added WITHOUT the value being set. These are required to be set manually. Check the above docs for examples of what is needed.

## main.py
The `run_pipeline` is a simple function created to simply read in the request, unpackage it, and call your pipeline with the arguments. This is the function that will be called when the trigger is run. Note we only use the `event` variable by default and don't interact with `context`. While it can be useful, it didn't seem necessary to be used by default.

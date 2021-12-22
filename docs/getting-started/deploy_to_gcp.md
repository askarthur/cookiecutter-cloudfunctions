# Deploy to GCP

# Check Trigger requirements
Because some triggers are too complex to fully configure from the cookiecutter template, first check the [Triggers](../../triggers/http.md) section for your trigger type and read over any additional steps needed.

# Google Build
First, go to [Google Build](https://console.cloud.google.com/cloud-build) and select the project to use. Go to the "Trigger" page, select "Create Trigger" and follow the process with these instructions:

1. Use "Push to a branch" and it should properly autoselect main once the repository is connected
2. Connect the necessary repository
3. Leave the autoselected build configuration as cloudbuild.yaml
4. Select "Create"

Now you have a build trigger, before you can run anything you'll have to update the settings. Click the "Settings" tab and enable the role of "Cloud Functions Developer".

If your function needs other permissions like Storage, Firestore, etc. you'll have to set that up in [IAM](https://console.cloud.google.com/iam-admin). Note the service account on the "Settings" tab is what you want to permission.

If you would like to run the trigger without having to push to main, go to the "Trigger" tab and click "Run" on the newly created trigger.

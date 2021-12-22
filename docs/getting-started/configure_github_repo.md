# Configure GitHub repository

## Setup branches
Now that we've pushed our repository to GitHub we'll see a `main` branch with all the code but you rarely want to push code directly to main. To mitigate this, lets create a `development` branch for which to actively develop code and then move it to main once we think it's safe for production. To do so, simply: 

1. Click on the "main" dropdown button your repo's homepage
2. Type in "development" in the search bar
3. Select "Create branch: development from main".

**Note if 'development' is not used. You must change the branch reference in certain files within the '.github/workflows' directory for CI checks to work.**

As seen with main, you'll see Actions being run for development. This is because `main` and `development` are the two branches enabled for actions. To alter this, checkout out Line 6 in your `.github/workflows/code_quality_checks.yml` file.

That is the base needed for the CI system to work. If you wish to add further protection to your repository visit the `Settings -> Branches` section of your repo. This will allow you to add things like protected branches and/or required reviews.

# **Random Recipes**

## **Project Overview**

'Random Recipes' is a community interactive website which allows users to create accounts and ammend recipes.

The site is created using HTML, CSS, JavaScript, Python and engages users of all ages and background.

The live website can be found here

## **Table of Contents** 

  * [1. **UX**](#1-ux)
    + [**User Goals**](#user-goals)
    + [**Design**](#design)
    + [**Wireframes**](#wireframes)
      - [**Colour & Styling**](#colour--styling)
      - [**Font**](#font)
      - [**Styling Considerations**](#styling-considerations)
  * [2. **Features**](#2-features)
    + [**Existing Features**](#existing-features)
    + [**Features to consider implementing in future**](#features-to-consider-implementing-in-future)
  * [3. **Technologies Used**](#3-technologies-used)
  * [4. **Testing**](#4-testing)
  * [5. **Deployment**](#5-deployment)
    + [Database Deployment](#database-deployment)
    + [Application Hosting](#application-hosting)
    + [**Heroku**](#heroku)
      - [Creating a Heroku app](#creating-a-heroku-app)
      - [Deployment](#deployment)
    + [GitHub and GitPod repository management](#github-and-gitpod-repository-management)
  * [6. **Credits**](#6-credits)
    + [**Design and research**](#design-and-research)
    + [**Content**](#content)
    + [**Media**](#media)
      - [Recipe Category Images:](#recipe-category-images)
      - [404 Error Page](#404-error-page)
    + [**Acknowledgements**](#acknowledgements)


## 1. **UX**

  ### **User Stories**

  Browsing 
  * As a user I want to be able to navigate through the website seamlessly.
  * As a user I want to be able to be presented with popular recipes so I am introduced to new content.
    

  Searching
  * As a user I want to be able to search for new recipes using a search bar as well as through the nav bar.
  * As a user I want to be be able to save my favourite recipes
  * As a user I want to be able to view recipes by their appropriate categories.

  Uploading Recipes
  * As a user I want to be able to upload my own recipes.
  * As a user I want to edit recipes I have uploaded.
  * As a user I want to delete recipes I have uploaded.

  Users
  * As a user I want to be able to Sign up to the site
  * As a user I want to be able to Log back into the site later.
  * As a registered user I would like to be able to view my account and access my saved recipes.

    
  Administration
  *  As an admin I want to be able to edit and delete content to maintain site rules.
  *  As an admin I want to be able to add and edit food categories, to help improve user experience.

  General
  * As a user I would like to be contacted in order to recieve feedback on my site

### ***WIreframes***
View desktop wireframes [here]()




## 5. **Deployment**

  ### Database Deployment

### Application Hosting
### **Heroku**

The site is hosted using [Heroku](https://www.heroku.com/), deployed directly from the master branch of GitHub. The deployed site will update automatically as new commits are pushed to the master branch.

#### Creating a Heroku app
- From the Heroku dashboard:
  - Select "New"
  - Select "Create new app"

- Add new app details to form:
  - Add app name (must be unique)
  - Select region
  - Click "Create App"


#### Setting Environmental Variables
- From the Heroku dashboard:
  - Select your app from the list


- Select "Settings" from the top menu:
  - Under 'Config Vars', select "Reveal Config Vars"
  - Add environment variables in key-value pairs, click "Add" to add additional pairings.



  #### Deployment
- Create required deployment files in the repository:
  - requirements.txt
      - Lists the required python modules for Heroku to install.
    - To create:
      - In your IDE terminal, type: pip freeze > requirements.txt

  - Procfile
      -  Tells Heroku the command to launch the app.
    - To create:
      - in your IDE terminal, type: python app.py > Procfile

  - .gitignore (optional)
      - Lists files and directories which should be deployed to live app, such as files with environmental passkeys.
    - To create:
      - In your IDE terminal, type: touch .gitignore
      - List the files and directories to be excluded from live deployment, within the .gitignore file.
      - Save in your repository root directory.

- From the application top menu:
  - Select 'Deploy'
  - Choose your Deployment method:
    - Github:
      - Select the correct Github account.
      - Type in the repository name you wish to deploy.
      - Choose the correct repository from search results.
      - Select "Connect"


    - Manual Deployment:
      - Choose the correct branch you wish to deploy from the drop-down.
      - Select "Deploy Branch"
      - Heroku will return "Your App has successfully deployed". If this shows an error, troubleshooting will be needed.

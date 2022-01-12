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

  ### **Wireframes**
  View desktop wireframes [here](https://github.com/abdullahjr0/MS3/blob/9f5a247477dd36f72e5ab5c27bb1e7281da42dc7/wireframes.md#L29)

## 3. **Technologies used**



<details>
<summary>Languages</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/HTML">HTML</a> - Programming language providing content and structure of the website.</li>
<li><a href="https://en.wikipedia.org/wiki/CSS">CSS</a> - Programming language providing styling of the website.</li>
<li><a href="https://en.wikipedia.org/wiki/JavaScript">JavaScript</a> - Programming language used for various interactive elements of the website, including game logic, audio options etc.</li>
<li><a href="https://en.wikipedia.org/wiki/Python_(programming_language)">Python</a> - Programming language used to drive core site functionality including user login and push/retrieving database information.</li>
</ul>
</details>


<details>
<summary>Libraries</summary>
<ul>
<li><a href="https://fontawesome.com/">Font Awesome</a> - Library used for icons, such as social links and other images.</li>
<li><a href="https://fonts.google.com/">Google Fonts</a> - Font style library.</li>
<li><a href="https://flask.palletsprojects.com/en/1.1.x/">Flask</a> - Micro-framework to simplify Python scripting and web server tasks.</li>
</ul>
</details>

<details>
<summary>Editor</summary>
<ul>
<li><a href="https://github.com/">GitHub</a> - Remote code repository.</li>
<li><a href="https://gitpod.io/">GitPod</a> - IDE (Integrated Development Environment), for writing, editing and saving code.</li>
<li><a href="https://balsamiq.com/">Balsamiq</a> - Wireframes for visual design testing.</li>
</ul>
</details>


<details>
<summary>Tools</summary>
<ul>
<li><a href="https://www.remove.bg/">remove.bg</a> - Remove backgrounds from png images.</li>
<li><a href="https://coolors.co/">Coolers</a> - Color Palette Generation</li>
<li><a href="https://realfavicongenerator.net/">Real Favicon Generator</a> - Generate favicons and icons for desktop and mobile usage.</li>
<li><a href="http://ami.responsivedesign.is/">Am I Responsive?</a> - Responsive design demo in ReadMe summary.</li>
<li><a href="https://www.responsivedesignchecker.com/">Responsive Design Checker</a> - Check website response across device types.</li>
</ul>
</details>


<details>
<summary>Database Management</summary>
<ul>
<li><a href="https://www.mongodb.com/cloud/atlas/">MongoDB</a> - Cloud based database management system, used for storing user profile and recipe information.</li>
</ul>
</details>

<details>
<summary>Deployment Platform</summary>
<ul>
<li><a href="https://www.heroku.com/">Heroku</a> - Remote hosting platform, for hosting of python driven websites and applications.</li>
</ul>
</details>


## 4. **Testing**

The testing process can be seen in the [TESTING.md](testing.md) document.


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

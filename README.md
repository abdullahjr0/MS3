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

<details>
<summary>Browsing</summary>

* As a user I want to be able to navigate through the website seamlessly.
* As a user I want to be able to be presented with popular recipes so I am introduced to new content.
</details>  

<details>
<summary>Searching</summary>

* As a user I want to be able to search for new recipes using a search bar as well as through the nav bar.
* As a user I want to be be able to save my favourite recipes
* As a user I want to be able to view recipes by their appropriate categories.
</details>

<details>
<summary>Uploading Recipes</summary>

* As a user I want to be able to upload my own recipes.
* As a user I want to edit recipes I have uploaded.
* As a user I want to delete recipes I have uploaded.
</details>

<details>
<summary>Users</summary>

* As a user I want to be able to Sign up to the site
* As a user I want to be able to Log back into the site later.
* As a registered user I would like to be able to view my account and access my saved recipes.
</details>
    
<details>
<summary>Administration</summary>

*  As an admin I want to be able to edit and delete content to maintain site rules.
*  As an admin I want to be able to add and edit food categories, to help improve user experience.
</details>

<details>
<summary>General</summary>

* As a user I would like to be contacted in order to recieve feedback on my site
</details>

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

The testing process can be seen [here](https://github.com/abdullahjr0/MS3/blob/b7cb7ee1b4d806f146a3ebc26b760c1ad612dcf1/testing.md)

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


### GitHub and GitPod repository management

### **How to clone 'Random Recipes' in GitHub, GitPod and setup on Heroku.**

To run a version of the site locally, you can clone this repository using the following steps;

In a code editor of your choice;

1. Go to [GitHub.com](https://github.com/)
2. Click on 'Responsitories'
3. Click on 'Random Recipes'
4. Click on the 'Code' button.
5. Under 'HTTPS' click the clipboard icon to the right of the URL.
6. In your IDE of choice, open a repository or create a new repository.
7. Open Terminal \('Terminal' then 'New Terminal' from the top ribbon menu in GitPod.\)
8. Type 'git clone', paste URL link and press enter.

Additional information around these cloning steps can be found on [GitHub Pages Help Page](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).
&nbsp;

#### Installing Requirements
- Install all requirements modules to your local IDE with the following CL:

```
 pip3 install -r requirements.txt
```

#### Create Collections in MongoDB

- Login to your MongoDB account
- Create a Cluster

![create a cluster](https://user-images.githubusercontent.com/79915855/149137564-c255f560-15b8-4fde-a1fb-3a267c585386.png)


#### Setup Environmental Variables
- Create a '.gitignore' file in the root directoy
- Add 'env.py' and '__pycache__/' to the file list within .gitignore
- Create a 'env.py' file
- In the 'env.py' file write the following code;

```
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "[UNIQUE ID]")
os.environ.setdefault("MONGO_URI", "[UNIQUE ID]")
os.environ.setdefault("MONGO_DBNAME", "[UNIQUE ID]")

```

Note: For each sectionedn noted as [UNIQUE ID], you will need to provide your own unique identifier. These must also be aligned to Heroku environmental variables.

### Setup Unique Identifies / Environment Variables

#### SECRET_KEY

This is required when using flash() and session() functions in flask. The key can be whatever you want, but it's advisable to use a randomly generated secure key from websites such as [RandomKeyGen.com](https://randomkeygen.com/).

#### MONGO_URI

This is used to connect you application to your MongoDB cluster.

- Click 'Overview' tab from your Cluster, followed by 'Connect'.

![Connect Mongo Cluster](https://user-images.githubusercontent.com/79915855/149137563-6ca09358-f4d6-4f84-ab93-d038f0148d16.png)

- Select 'Connect your application' from following window.

![Connect Application](https://user-images.githubusercontent.com/79915855/149137561-75d21e45-3229-446f-8c17-b11a2db711a3.png)

- Select your correct version of Python and copy the connection string.

![Select your version](https://user-images.githubusercontent.com/79915855/149137566-c374f8c4-4222-4c15-8182-6a08226d19a3.png)

- Replace the 'username' and 'password' text, with the relevant criteria you setup in 'Database Access'.

![Database Access](https://user-images.githubusercontent.com/79915855/149137565-0dde3c10-ab43-4c2c-a358-72a81e0e6cae.png)

#### MONGO_DBNAME

This is the name of your database in MongoDB. Which can be foung under the 'Collections' tab, under your cluster.

#### Running Development Server

To launch a Http server using the development mode code for the application, use the following command in your IDE:

```

python3 app.py http.server

```

The IDE will then open a port with http address for you to access.


## 6. **Credits**
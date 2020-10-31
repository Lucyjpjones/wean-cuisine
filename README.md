<div align="center">
  <img src="assets/images/readme/responsive-WeanCuisine.png">
  <img src="assets/images/readme/title.png">
<hr>

**A recipe site that allows users to connect, explore and share their own weaning recipes.**

This app was built using [GitHub Pages](https://pages.github.com/) and [Heroku](https://www.heroku.com/)

[View here](https://lucyjpjones.github.io/wean-cuisine/)

</div>

---

## <u>Table of contents</u>

- [&rarr; **User Experience (UX)**](#-rarr----user-experience--ux---)
  - [Purpose](#purpose)
  - [Design](#design)
  - [User stories](#user-stories)
  - [Wireframes](#wireframes)
- [&rarr; **Features**](#-rarr----features--)
  - [Features used](#features-used)
  - [To do list](#to-do-list:)
  - [Status](#status)
- [&rarr; **Technologies**](#-rarr----technologies--)
  - [Languages](#languages)
  - [Frameworks, Libraries & Programs](#frameworks--libraries---programs)
- [&rarr; **Deployment**](#-rarr----deployment--)
  - [Deploy to Heroku](#deploy-to-heroku)
  - [Accessing code](#accessing-code)
- [&rarr; **Testing**](#-rarr----testing--)
  - [Testing user stories](#testing-user-stories)
  - [Manual function testing](#manual-function-testing)
  - [Validator checks](#validator-checks)
  - [Audits](#audits)
  - [Responsive Design](#responsive-design)
  - [Additional Testing](#additional-testing)
  - [Bugs](#bugs)
- [&rarr; **Credits**](#-rarr----credits--)
  - [Content](#content)
  - [Media](#media)
  - [Acknowledgements](#acknowledgements)
- [&rarr; **Contact**](#-rarr----contact--)

---

# &rarr; **User Experience (UX)**

### **<u>Purpose</u>**

The purpose of this app is to create a platform where parents can connect, explore and share weaning recipes, with a specific focus on type of cuisine. 

Baby-led weaning is becoming an increasingly popular way of introducing babies to different foods, carrying many benefits including the ability to simplify feeding times for parents, better appetite control, less fussiness around foods, and protection against obesity later in life.

From living in London, one of the world's most diverse cities, I am spoilt for choice when it comes to dining out. I want children to experience different cultural cuisines from an early age as I think this will have a positive impact on their palettes later in life.

I was inspired to create this application after finding out I was due to become an Auntie in December.

By completing this project I will have shown greater experience in HTML, CSS and Javascript, and demonstrated my understanding of Python+Flask and MongoDB. The project focuses on the concept of <u>CRUD</u>, creating functionality for users to create, locate, display, edit and delete recipes.

### **<u>Design</u>**

**Structure**

**Colour scheme**

<img src="static/assets/images/readme/moodboard.jpeg">

- After undergoing some research into baby focused websites and recipe books, I decided a pastel colour scheme was a appropriate for my app. I created my final palette using [Coolors](https://coolors.co).

<img src="static/assets/images/readme/palette.png">

**Typography**

**Research**

- I spent some time researching other recipe sites to gain inspiration, and created a moodboard with a collection of elements which caught my eye.

<img src="static/assets/images/readme/design-inspo.jpeg">

**Logo Design**

- For this site I created my own logo design with inspiration from [Flaticon](https://www.flaticon.com/) and [VectorStock](https://www.vectorstock.com/).

- Following website conventions, my website logo is a link to the homepage. Over time through trial and error, many people have learned that clicking on a site’s logo leads them back to the homepage so adopting this standard reduces confusion by matching the UI to users’ expectations. The logo is also left-aligned which is the most familiar placement, and is where users look to find it.

<img src="static/assets/images/readme/logo-design.png">

### **<u>User Experience</u>**

<img src="static/assets/images/readme/flowchart.png">

<u>**User profiles**</u>

**User profile: Site member**

As a first time mum, Katie  wants to be able to connect with other parents from around the world to share inspiring weaning recipes. Since Katie is a working mum, anything she can do to save time in the kitchen without comprising on nourishment is highly valuable. She wants to share her experience with others and be part of a diverse community as she begins her weaning journey.

**User profile: Site owner**

As the site owner, I want to be able to continually monitor and update the site to manage my users expectations. I have already got future plans which I have highlighted in my features section below. As my site categorisation is based around cuisines I want to be able to login as an admin user and add or update the listed cuisines for my users. By creating this application I will hopefully have gained inspiration on recipes I can cook for my niece and own children in the future.

<u>**User stories**</u>

**User stories: Site member**

|   | Needs/Goals                                                 | Task                                                                             |
|---|-------------------------------------------------------------|----------------------------------------------------------------------------------|
| **1** | An easy-to-use recipe site                                  | Simple, user-friendly site that is easy to navigate                              |
| **2** | Be part of a social community with other  parents           | Ability to register and an easily accessible button to 'Log in’                  |
| **3** | Discover and learn new nourishing recipes                   | Explore recipes posted by others                                                 |
| **4** | Save time in the kitchen by getting inspiration from others | Clear recipe categorisation and ability to search using keywords in a search bar |
| **5** | Ability to share and edit her own recipes                   | Option to add, edit and delete own recipes                                       |
| **6** | Ability to find further inspiration                         | Links for purchasing recipe books for further inspiration                        |

**User stories: Site owner**

**User stories:**


### **<u>Wireframes</u>**

As part of the design process, before starting my project I sketched out initial drawings then used [Balsamiq](https://balsamiq.com/?gclid=Cj0KCQjw28T8BRDbARIsAEOMBczzBYzsoMjbTtqNXQaE1EgOWA2u_Qux7sLl2IUHe-p0lDC-294BfVgaAr-oEALw_wcB) to create sharper-looking wireframes. Creating these mock-ups helped me plan the basic structure and arrangement of the features for my site.

- [Homepage](static/assets/files/wf-homepage.pdf)
- [Recipes page](static/assets/files/wf-recipes.pdf)
- [Add/Edit recipe page](static/assets/files/wf-addEditRecipe.pdf)
- [Recipe information page](static/assets/files/wf-recipeInfo.pdf)
- [Shop recipe books page](static/assets/files/wf-shopRecipeBooks.pdf)

---

## &rarr; **Features**

#### Features used:

- **Responsive on all device sizes**
  - Mobile-first design, responsive on all devices through using the Materialize grid system and CSS media queries.

- **A user-friendly interface with easy navigation throughout the site**
  - Attractive, minimalistic design with visuals and information presented clearly and concisely.
  - Easily readable fonts and simple navigation throughout the site.
    - Fixed navigation bar visible on every page including a menu dropdown and brand logo to link back to homepage.
  - An aestheticly pleasing 404 page if the user is directed to a non-existent page.

- **Buttons**
    - Clear interative buttons used for a effortless user journey.

- **Forms**
  - Forms used for login and register, and adding and editing the recipe and cuisine cards.
  - Materilize elements used include: input fields, textarea fields, radio buttons, select dropdowns and submit buttons.

- **Tabs**
  - Interactive tab used to allow user to flip between recipe ingredients and method.

- **Card Listings**
  - Used to display recipes, cuisine categories and recipe books.
  - Image included contributing to the visual look.

- **Modals**
  - Used for login and register form and, recipe and cusine card delete confirmation.

- **Carousel**
  - Used for recipe categories displayed on the homepage.

- **Search bar**
  - Allows user to search recipes by keywords using text index searching. Ingredients and recipe name included as keywords in query.

#### To do list:

#### Status

> Project is: <u>ongoing</u>

I will continue to update my website as I grow my platform of users. I have future development plans which I have listed below.

**Future Development plans**
- Add more cuisine cards 
- Add review option for users
- Parent forum
- Dietry requirements
- Forgot password link
---

## &rarr; **Technologies**

#### Languages

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://www.javascript.com/)
- [Python](https://www.python.org/)

#### Frameworks, Libraries & Programs

- [**MongoDB**](https://www.mongodb.com/)
  - The document database used for this project.

- [**Flask**](https://flask.palletsprojects.com/en/1.1.x/)
  - A web framework used to provide tools, libraries and technologies for the application.

- [**Werkzeug**](https://werkzeug.palletsprojects.com/en/1.0.x/)
  - Used with Flask to make user authentication more secure using password hashing.

- [**Materialize CSS**](https://materializecss.com/)

  - Materialize was used to assist with the responsiveness and styling of the website using design templates.

- [**Randomkeygen**](https://randomkeygen.com/)

  - Fort Knox Passwords for password security.

- [**Google fonts**](https://fonts.google.com/)

  - Google fonts were used to import the fonts into the CSS file which is used on all pages throughout the project.

- [**Font Awesome 4.7.0**](https://fontawesome.com/)

  - Font Awesome was used to add icons for aesthetic and UX purposes.

- [**jQuery:**](https://jquery.com/)

  - jQuery came with Materialize to make the components used responsive.
  - Included at end of body tag within HTML file to ensure a smooth running of HMTL and CSS.

- [**Git**](https://git-scm.com/)

  - Git was used for version control by utilizing the Gitpod terminal to commit to Git and push to GitHub.

- [**GitHub**](https://github.com/)

  - GitHub is used to store the project code after being pushed from Git.

- [**Heroku**](https://github.com/)

  - Heroku is used to store the project code after being pushed from Git.

- [**Balsamiq**](https://balsamiq.com/)

  - Balsamiq was used to create the wireframes during the design process.

- [**Grammarly**](https://www.grammarly.com/)

  - Grammarly was used to ensure any grammar errors are eliminated.

- [**HTML Formatter**](https://www.freeformatter.com/html-formatter.html) and [**CSS Formatter**](https://www.freeformatter.com/css-beautifier.html)

  - Used to format my HTML and CSS file with desired indentation level for optimal readability.

- [**Tablesgenerator**](https://www.tablesgenerator.com/markdown_tables)

  - Used to create tables in my readme file.

---

## &rarr; **Deployment**

#### Deploy to Heroku

The project was connected to Heroku using automatic deployment from my GitPod repository, using the following steps...

> **Note:** Before following the below steps ensure you have already created your new repo in Github and set up an env.py file to store your sensitive data.

1. In the terminal create requirements.txt and Procfile files using the commands below:
   - $ pip3 freeze --local > requirements.txt

   - $ echo web: python app.py > Procfile

   > **Note:** 
The **P**rocfile must be assigned a capital P.

2. Log in (or Register) to [Heroku](https://www.heroku.com/) and from your dashboard click 'new' > 'create new app'.

   ![New app btn](static/assets/images/readme/new-app.png)

3. Enter your 'App name' and choose the appropriate region, then click 'Create app'.
   > **Note:** 
 The app name must be unique, all lowercase and '-' to be used instead of spaces.
The region chosen should be the one closest to you.

   ![Create new app](static/assets/images/readme/create-new-app.png)

4. From the Heroku deploy tab, select the Deployment method 'GitHub'.

   ![Deployment method](static/assets/images/readme/deployment-method.jpeg)

5. On 'Connect to GitHub' section make sure your GitHub profile is displayed then add your repository name and click 'Search'.

   > **Note:** 
This is the name of your repo in GitHub. It is good practice to use an identical name for your heroku app.

    ![Deploy GitHub](static/assets/images/readme/deployment-git.jpeg)

6. Your repo should now be displayed below, click 'Connect' to connect to this app.

7. Go to Settings tab on Heroku, scroll to 'Config Vars' section and click 'Reveal Config Vars'. 

   ![Config Vars](static/assets/images/readme/config-vars.png)

   Enter variables (key and value) contained in env.py file. The keys are listed below and values are tailored to the user.
     - IP
   - PORT
   - SECRET_KEY
   - MONGO_URI
   - MONGO_DBNAME

8. Push requirements.txt and Procfile to repository:
  <u>requirements.txt</u>
    - $ git add requirements.txt
    - $ git commit -m "Added requirements.txt"
 
    <u>Procfile</u>
   - $ git add Procfile
   - $ git commit -m "Added Procfile"

9. Go to Deploy tab on Heroku and under Automatic deployment section, click 'Enable Automatic Deploys'. Then under Manual deploy click 'Deploy Branch'.

   ![Enable Automatic Deploys](static/assets/images/readme/enable-deploys.jpeg)

   - Heroku will now recieve the code from GitHub and start building the app using the required packages.
   - Once built you will recieve the message 'Your app was successfully deployed' and you can click 'View' to launch your new app.

   > **Note:** 
In Manual deploy dropdown 'master' is selected'

#### Accessing code

Follow the steps below if you are wanting to propose changes to the project or to use the project as a starting point for your own idea.

- **Forking the GitHub Repository**

  Forking allows you to create a copy of the original repository and propose changes to the repository owner via a pull request.

  1. Log in to GitHub and locate the GitHub Repository.

  2. At the top of the Repository (not top of page) just above the "Settings" button on the menu, locate the "Fork" button.

     ![forking](static/assets/images/readme/forking.png)

  3. You should now have a copy of the original repository in your GitHub account.

- **Making a Local Clone**

When you clone a repository, the repository is copied on to your local machine.

1. Log in to GitHub and locate the GitHub Repository.
   - Wean Cuisine repository can be found [here](https://github.com/Lucyjpjones/wean-cuisine/)

2. Under the repository name, click the "download code" option.

   ![Clone](static/assets/images/readme/clone.png)

3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.

   ![Clone-link](static/assets/images/readme/clone-link.png)

4. Open Git Bash

5. Change the current working directory to the location where you want the cloned directory to be made.

6. Type git clone, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/wean-cuisine.git
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/wean-cuisine.git

> Cloning into `wean-cuisine`...
> remote: Enumerating objects: 299, done.
> remote: Counting objects: 100%, (299/299),  done.
> remote: Compressing objects: 100% (156/156), done.
> Receiving objects: remove: Total 299 (delta 145), reused 267 (delta 126), pack-reused 0
> Receiving objects: 100% (299/299), 4.61MiB | 2.98 MiB/s, done.
> Resolving deltas: 100% (145/145), done. Unpacking objects: 100% (10/10), done.
```

Now, you have a local copy of your fork of the Wean Cuisine repository.

> Note: The repository name and output numbers that you see on your computer, representing the total file size, etc, may differ from the example I have provided above.

**Creating env.py file** 

1. Add a env.py file to store environment variables:
   - Import os 
   - os.environ.setdefault("IP", "To be added by user") 
   - os.environ.setdefault("PORT", "To be added by user") 
   - os.environ.setdefault("SECRET_KEY", "To be added by user") 
   - os.environ.setdefault("MONGO_URI", "To be added by user") 
   - os.environ.setdefault("MONGO_DBNAME", "To be added by user")

> **Note:** I used [RandomKeygen.com](https://randomkeygen.com/) to get my secure SECRET_KEY password. A SECRET_KEY is required when using the flash and session functions of Flask.

 2. Create a file named .gitignore and include env.py to ensure this file is never pushed to GitHub.
 > **Note:** This is important as

---

## &rarr; **Testing**

#### Testing user stories

Testing my user's <u>key priorities</u>:

**1.** Simple, user-friendly site that is easy to navigate
 - Site includes a main navbar featuring a dropdown menu with page navigation.
- Navigation menu is fixed so is always visible to the user.
- Brand logo directs user back to homepage from anywhere on the site.

![Navbar with brand logo](static/assets/images/readme/navbar.png)
 
**2.** Ability to register and an easily accessible button to 'Log in’

- Clear login button visible on navbar as soon as user enters the site.
- After clicking login button, user is presented with a modal giving the user an option to login or register.
- After logging in or registering the user has the option to add, edit and delete their own recipes.

![Login btn and modal](static/assets/images/readme/login.png)

**3.** Explore recipes posted by others

- ‘Explore recipes’ button visible on callout section as soon as user enters the site. 
- Navigation link to recipes also included in dropdown menu.

![Explore recipes nav ](static/assets/images/readme/callout.png)

- Recipe card displaying recipe image, recipe name, cuisine and who the recipe was created by.

![Recipe card page](static/assets/images/readme/recipe-card.png)

**4.** Clear recipe categorisation and ability to search using keywords in a search bar
- Search bar to allow the user to search for recipes using keywords. The search bar is set up to filter recipes based on recipe name and ingredients.

![Search bar](static/assets/images/readme/search-bar.png)

- Link in dropdown menu to page displaying cuisine categories. User can click on cuisine to view all recipes in that category.

![Dropdown menu](static/assets/images/readme/cuisine-dd.png)
- Carousel on homepage to link directly to recipes for specific cuisine.

 ![Carousel](static/assets/images/readme/carousel.png)

- Admin control over adding, editing and deleting new cuisines. Buttons only visible when specified admin is logged in.

 ![Buttons logged in vs logged out](static/assets/images/readme/cuisine-btns.png)

**5.** Option to add, edit and delete own recipes
- When user is logged the ‘add recipe’ button is visible to the user on the first view of the site. The link is also accessible via the dropdown menu.

 ![Add recipe logged in vs logged out](static/assets/images/readme/add-recipe.png)

- The edit and delete buttons are only available to the user who created the recipes. These are found on the individual recipe cards and are only visible when the user is logged in.

 ![Edit/delete btns logged in vs logged out](static/assets/images/readme/edit-delete.png)

**6.** Links for purchasing recipe books for further inspiration
- User can access the ‘shop recipe books’ page via a link on homepage or through the includes an image of the book and a buy dropdown list with links to external retailer sites.

 ![Homepage display](static/assets/images/readme/book-hp.png)

  ![Recipe book page](static/assets/images/readme/book-page.png)

#### Manual function testing

To ensure my site was working correctly I carried out some manual function testing;

**1. Site navigation**

- I checked the site dropdown menu was working correctly by starting on the home-page and navigating around the site from and to every screen the user would be faced with.

- I checked the logo homepage naviagtion was working by clicking on the image from every page.

- 404 Error page was tested by creating a broken link in the game URL and making sure it responded with my custom page.

- The links to recipe book retailers were checked by ensuring that each dropdown link navigated to the correct site opened on a new window. This was tested for every dropdown.

**2. Hover, focus and active effects**

- Hovered over the following button elements to ensure the correct brightness effects were in place;
  - 'Login' and 'Logout'
  - 'Explore recipes'
  - 'Add recipes'
  - About icons changed colour
  - Cuisine links on carousel
  - 'Shop recipe books'

**3. Log in, register and logout function**

- To check the log in functionality was working I first clicked on the 'log in' button to ensure the modal appeared. When presented with the modal I filled out the form with an already registered username and password then clicked 'Log in'. The modal closed and the log in button changed to log out and further buttons were available to me so i knew it was working. This was tested throughout all pages of the site.

- To check the register functionality was working I first clicked on the 'log in' button so the modal appeared. I then clicked on the register tab and filled out the form with a username and password, then clicked 'Register'. The modal closed and the log in button changed to log out and further buttons were available to me so i knew it was working. This was tested throughout all pages of the site.

- Once I was logged in and the 'log out' button was available I clicked this to check that it logged me out correctly. The log out button changed to log in and the additional buttons were no longer visible to me so i knew it was working. This was tested throughout all pages of the site.

**4.** Form validation checks

- Login/Register form
    - I entered an invalid username into the username field and was displayed with
  - I entered an invalid password into the password field and was displayed with

- Add/Edit recipe and cuisine forms

**5.** Explore recipes and search bar
- I clicked on the 'Explore recipes' button on the homepage callout section and the link within the dropdown menu, and both correctly navigated to the recipes page.

- I submitted a selection of words into the recipe search bar to ensure the query function was filtering the recipes correctly.

**6.** Viewing recipes
- I clicked on each recipe card to make sure it displayed the correct information to me when naviagted to the view recipes HTML template, and it did.

**7.** Adding recipe
- I clicked on the 'Add recipe' button on the homepage callout section and the link within the dropdown menu, and both correctly navigated to the add recipe page.

**8.** Editing recipe
- I logged in as different users to check that the edit button was only visible on the recipes I had added.

- I clicked on the 'Edit' button on all the recipes cards to test that I was correctly navigated to the edit recipe page.

**9.** Deleting recipe
- I logged in as different users to check that the delete button was only visible on the recipes I had added.

- I clicked on the 'Delete' button on all the recipes cards to test that I was correctly presented with a modal for delete confirmation. I then clicked the 'delete' button on the modal and checked if the recipe card had been removed.

**10.** Link to cuisine page

**11.** Adding cuisine
- I logged in as different users to check that the add cusine button was only visible when the specified admin user was logged in.

- I entered the cusine name and image URL into the form and clicked the 'add' icon to check if the new cuisine was added, and it was.

**12.** Editing cuisine
- I logged in as different users to check that the edit cusine button was only visible on the cuisine cards if i was logged in as the specified admin user.

- I clicked the edit button on various cusine cards and changed the cusine name and image URL. After clicking the edit icon the information was updated so I knew the function was working correctly.

**13.** Deleting cuisine
- I logged in as different users to check that the delete cusine button was only visible on the cuisine cards if i was logged in as the specified admin user.

- I clicked on the 'Delete' button on all the recipes cards to test that I was correctly presented with a modal for delete confirmation. I then clicked the 'delete' button on the modal and checked if the cuisine card had been removed.


#### Validator checks

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project. Code was entered through direct input. JS hint was used to check for any errors with my Javascript files. 
JS was also tested by opening the developer console window on Chrome and checking for any errors as I clicked through the site.

- [**HTML Validator**](https://validator.w3.org/nu/#textarea)

- [**CSS Validator**](https://jigsaw.w3.org/css-validator/#validate_by_input)


- [**JS hint**](https://jshint.com/)

- Python validator


#### Audits

[Lighthouse](https://developers.google.com/web/tools/lighthouse) was used to run a series of audits to improve the quality of web pages. Overall performance and errors highlighted below.

![Lighthouse overall performance](assets/images/readme/lhSummary.png)

<u>Performance</u>

![Lighthouse render-blocking resources](assets/images/readme/1-lh.png)

#### Responsive Design

- Site created as a mobile-first design.

- Viewport tag included in the head of HTML files to tell the browser how to respond to different resolutions, particularly mobile ones.

- Media queries used in the CSS file to target larger devices.

#### Additional Testing

- The Website was tested on Google Chrome, Internet Explorer, Safari browsers, Firefox and Edge. Internet Explorer was the only browser experiencing errors, specific details have been added to bugs section.

- The website was viewed on a variety of devices including HP Laptop, Macbook pro, Ipad and IPhones (Version 6,7,8,11).

- Friends and family members were asked to review the site to point out any bugs, user experience issues and/or suggestions.

  - Feedback action:

- Project posted on Slack, asking for feedback from fellow students.

#### Bugs

## &rarr; **Credits**

- My Mentor for continuous help and support throughout the project.

- The [Code Institute](https://codeinstitute.net/) Slack Community.

- Friends & Family for continuous feedback and support.

#### Content

#### Media

- [Flaticon](https://www.flaticon.com/) and [VectorStock](https://www.vectorstock.com/): used as inspiration for the Wean Cuisine logo.

#### Acknowledgements

## &rarr; **Contact**

Created by @lucyjpjones

If you have any problems, questions or suggestions for my project please contact me on the email below:

```
lucyjpjones@gmail.com
```

Thanks for visiting.

&copy;
LucyJPJones
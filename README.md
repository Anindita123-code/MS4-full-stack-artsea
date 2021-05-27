![Artsea - The workshop place](https://github.com/Anindita123-code/MS4-full-stack-artsea/blob/master/media/project_main.png)

# Artsea - the workshop place 
[live link of the website](https://anindita-artsea.herokuapp.com/)

## Table of Contents


## Project Overview

Artsea - This is the 4th Milestone project undertaken as part of Code Institute Diploma Curriculum. This has been build in the Full Stack Framework using Django.

Artsea intends to bring details of all kind of Visual Art related workshop information under one roof.
This helps the user choose within the various workshops that are available in a given point in time, and make an online payment for enrolling for the same.
The project implements stripe for payments and checkout and also has a Blog section which helps the users collaborate on a common topic thereby creating a community for art lovers
 
## User Experience

### Strategy Plane

Artsea - a workshop place was concieved having in mind anyone who would want to explore art by participating in one day workshops for various medium of arts.
The kind of workshops have been categorised for easy understanding and search. 
Through Artsea We aim to generate creative events that educate & expand the community by encouraging neighbourhood involvement into arts,
Our goal is to boost the creative community and make art truly available to everyone. 

### Scope Plane

The scope of Artsea is as follows:

1. Users will be able to register as a member, to have all their past purchase information under their logged in profile
2. All users will be able to search and view the workshops which are divided in various categories in the site. 
3. All users can choose to enrol by making an online purchase of workshop.
4. All users can read the published blogs in the website and post a comment on the same.
5. All buyers will receive a confirmation email, of their current purchase in the email id specified by them.

* Here, the focus is implementing eCommerce, and maintaining a blog

### Structure Plane 

The website is structured so that the user can navigate easily and fulfill their goal of making a purchase of art workshop after finding an appropriate one
* There is a top navbar, which is handy to navigate the breadth of the website.
* There is a workshop listing page that lists all the workshops that have been currently added by the superuser.
* Each workshop displays more details in the workshop detail pages, from where the user is provided the functionality to add the item to their shopping background
* The bag items can then be adjusted and routed for checkout and payment to block their snapshots
* There is also a blog listing page, which lists all the active blogs in the the website
* Each blog can be read in their respective blog pages which all includes the reviews or comments (if any) given by the users.


### Database Architecture

The database for Artsea is maintained using Django models, which are translated into postgres as they are deployed. 
Following is a brief understanding of the Models that have been created in Django

* Categories - stores the names of the categories under which are workshops are bucketed
* Workshops - stores details of workshops and its associated image
* Order - stores the unique order number with other details of the purchases made
* OrderlineItems - stores the details of items for each order, considering that each order number may have single or multiple items
* Profiles - user profiles created for returning users
* blogs - stores all the blog topics with associated writeup and images (if any)
* BlogComments - stores and displays all the blog reviews/comments which are posted by users for each individual blog

The Entity Relationship Diagram is as follows. 

![Entity Relationship Diagram](https://github.com/Anindita123-code/MS4-full-stack-artsea/blob/master/Design/Dbdiagram/ArtSea_artWorkshop_db.pdf)

### Skeleton Plane

A detail UX design has been done for Artsea and the wireframe designs were finalized which was the key deliverable of the design phase

The wireframes for the project can be found in the attached pdf file
* Wireframe for Web browser on Desktop/laptop [web browser](https://github.com/Anindita123-code/MS4-full-stack-artsea/blob/master/Design/Wireframes/Browser%20wireframes%20Artsea%20v1.pdf)
* Wireframe for iPad View [Ipad](https://github.com/Anindita123-code/MS4-full-stack-artsea/blob/master/Design/Wireframes/ipad%20wireframes%20Artsea%20v1.pdf)
* Wireframe for phone /iphone [Mobile](https://github.com/Anindita123-code/MS4-full-stack-artsea/blob/master/Design/Wireframes/iphone%20wireframes%20Artsea%20v1.pdf)

The representation of the information of this system is treated differently in different devices. The system uses the rule of three to organize data in accordance with the devices that run the application. 

### User stories

The user stories have been documented in the [Artsea User Stories Document](https://github.com/Anindita123-code/MS4-full-stack-artsea/blob/master/Design/User%20Stories/UserStories_artsea.xlsx)

**Viewing and Navigation**
1	Student / Shopper	View a list of Workshops	Select the workshop that I want to purchase
2	Student / Shopper	View Individual Workshop Details	Identify the fees, description, associated image, Person conducting, Venue and timings
3	Student / Shopper	Easily view the total enrolment amount 	prioritize my planned workshops
4	Student / Blogger / logged in user	View a list of Topics in the blog	Find out what are the currently active blogs in Artsea
5	Student / Blogger / logged in user	View other users comments as well as mine	Read the comments of self and others given on a particular post
**Registration and User Accounts**		
6	Site User	Easily register for an account	Have a personal account and be able to view my profile
7	Site User	Easily login or logout	Access my personal account information
8	Site User	Easily recover my password in case I forget 	Recover access to my account
9	Site User	have a personalized user profile	View and update my personal information and also view my order history
**Filtering and Searching**
10	Student / Shopper	Filter by the Medium or type of workshop	View my selected list of Workshops only
11	Student / Shopper	Search by the name or description	View the list of Workshops that matches my search criteria
12	Student / Shopper	View a list of Workshops that matches the filter or search criteria	Quickly decide that the Workshop I am looking for is available
**Purchasing and checkout**			
13	Student / Shopper	Add the selected workshop into my shopping bag	select the workshops that I want to purchase
14	Student / Shopper	See the subtotal and the Grand total of the items, including delivery charges (if any) in the shopping bag	View the breakups of the amount that I have to pay if I go ahead with the order
15	Student / Shopper	Allowing users to view items in their bag to be purchased	See my selection of items in the shopping bag
16	Student / Shopper	Modify the quantity of items in my shopping bag	Make changes in my shopping bag in the last moment
17	Student / Shopper	Delete any item from the shopping bag	Remove any items from the shopping bag if I found the correct match
18	Student / Shopper	View the new grand total once the quantity in the shopping bag Is modified or deleted	Quickly decide and move ahead for paying the new price
19	Student / Shopper	Checkout by providing a valid Credit card number	Make a purchase
20	Student / Shopper	sufficiently notified if my card number is invalid	Modify my card number and provide a valid card details
21	Student / Shopper	Get a successful purchase message once the purchase has been made	I can be sure that the purchase is successful
22	Student / Shopper	See an empty shopping bag on successful purchase	see that there is nothing in my shopping bag as the payment has been successful
23	Student / Shopper	View my order details 	get an order number which is valid and be sure that I have made a successful purchase
24	Student / Shopper	Get an email for the order made	use the mail for a formal confirmation of the items that has been purchased
**Blogs and User Comments**			
25	superuser	Create a new blog post	Connect with people using the website to comment and collaborate
26	site User	View the list of Blog Posts 	See all the blog topics at once
27	site User	Select and read any of the blog posts	Read the blog post in full
28	site User	Add a comment to the block post	Share my opinion
29	site User	Read the comments made by other site user on the blog post	Learn about others opinion
**Workshop Record Management**			
30	superuser	Create a new workshop and add the Title, Category, Description, Hosted By, Date and time, place of workshop, Image Url and price	Add workshops to the database
31	superuser	Notified of any invalid entries for creating a workshop. 	Make the necessary changes before commiting the records in the database
32	superuser	Notified if the workshop has been created successfully	Be sure that they are saved in the database and will be available for users to enrol for the same
33	superuser	Update an existing workshop data	Make any changes to the date and time or venue if required
34	superuser	Delete a workshop 	remove any cancelled workshop

### Design Choices
The website structure is kept simple, I have not used too many colors, so as to balance out the colors of the workshops which are displayed.
The hero-image has been selected keeping in mind that this is all about visual arts, and mostly dealing with bright stuffs.
I have hence chosen color combination that gives a warm feeling and is easy to go with, where the textual content is well received.
#### Fonts
* For the most part of the website, I have used the font "Roboto" which gives a good reading experience. They are nicely spaced and make the site look more fuller.
* For the Logo is a combination of the font's 'Goblin One' and 'Caveat'. The subheadings of each page, I have used a cursive version of 'Goblin One' of small size, so that it gets more weightage than the rest of the site content. 
* For the Nav bar, I have used "Roboto Slab" which I think fitted very well to put that highlight on the nav elements
* For the Blog title, I have used "Roboto Slab" and the rest of the blog contents, I have used Roboto as well.
**The fonts, used are all taken from Googlefonts**

#### Icons
* I have used Icons for specifying the User authentication, Shopping bag, Search, the + and - for quantity selection, and the back buttons of the overall site.
    - The icons has been taken from fontawesome

#### Colors
I have kept minimum colors for this website and kept a balance with white and brighter tones, as this deals with colors and visual art. 
Mostly a combination of blue, white and black

The [Materializecss color page](https://materializecss.com/color.html) has been quite handy for making the selection of colors.

#### Styling

I have used [Bootstrap Components](https://getbootstrap.com/docs/3.4/css/) for styling almost all the components of the website.
Some of the bootstrap classes have been modified to fulfill the specific needs of the website.

## Project Features

### Existing Features
**FEATURES IMPLEMENTED**
*Elements Across the wewbsite*
Bootstrap Grid system have been used to structure pages and make them responsive for various viewports.
Bootstrap NavBar navbar to allow easy navigation throughout the web app. Able to reach all pages of the app from the NavBar. For mobile and smaller devices the navbar is found in the hamburger menu.
Bootstrap NavBar contains site title, which acts as a home button, dropdowns for accessing account actions, link to shopping basket and filters to help navigate the site.
Bootstrap Footer used with social links and email.

Favicon for the title tab in the browser.
Hover used on all buttons and web/email addresses.
Bootstrap Toasts used for all flashed messages after completion of an action.
Search bar at the top of the screen that is linked to keyword searches to display workshops with matching words in the Title and Description fields.

*Home Page Elements*
A hero Image on top in-tune with the theme of the project
A short writeup about the objective of the website and a link which takes the user to the workshop page

*Login Page Elements*
User login form allowing input from the user for their username and password with "Sign In" submit button which queries the Database to check the validity of the user.
If the user is valid, a toast message is displayed and the user is redirected to the Workshops page.
If a matching user is not found, the user cannot proceed further, and an error message is generated
Links are displayed to allow the user to register or to reset their password.

*Registration Page Elements*
Registration form expecting the following input from the user: 
- email address, confirm email address, username, password, confirm password.
"Sign Up" submit button sends info to DB and shows a verification page prompting the user to confirm that they want to sign up.


### Features Left to Implement

## Technologies Used

### Languages
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) for creating the webpages
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) for designing and styling the web pages
- [Python](https://www.python.org/) for the backend development
- [Jinja Templating language](https://jinja.palletsprojects.com/en/2.11.x/) have been used in conjuction with python for the working of the website

### Database
- [SQLlite (in Development)]() and [Postgres (at deployment)]() Although Sqllite has been used as the backend databse during development, the 
### Libraries and Frameworks
- [Font Awesome](https://fontawesome.com/) - have been used for the button icons that are used in the website
- [Materialize](https://materializecss.com/) - the various components of materialize have been used to draw the webpage structures and form elements
- [Google Fonts](https://fonts.google.com/) have been used to give the website a uniform look with the help of fonts provided by google
- [JQuery](https://jquery.com) - have been used to simplify DOM manipulation.
- [Flask Framework](https://flask.palletsprojects.com/en/1.1.x/) Jinja and Werkzeug from Flask have been extensively used

### Hosting
- [Github](https://github.com/) have been used for storing the application in public repositories
- [GitPod](https://gitpod.io/workspaces/) have been used as the primary development platform
- [Heroku](https://www.heroku.com/) have been used to host the website

## Testing

### Validation Checks

#### HTML Validation
The HTML for the project has been validated using [W3C's Validation service](https://validator.w3.org/). Since the HTML is created and maintained as separate parts in templates, the page HTML's have been taken using View->Developer->View Source and the code blocks have been tested for Validity.
The HTML Code used in all the pages are Valid as per W3C standards

#### CSS Validation
The custom css style.css in the static folder of the project has been validated using [W3C Css Validation service](https://jigsaw.w3.org/css-validator/). No errors were detected. Below is the snapshot for the same.
[CSS Validation outcome](https://github.com/Anindita123-code/Milestone3_Data_Centric/blob/master/test-snapshots/css_validation.png)

#### Javascript Validation
The custom javascript code has been validated using [jshint](https://jshint.com/). There are two warnings for the 2 statements that has used 'let' to declare variables
However, since the variables used are applicable for the current block of code only, I have decided to go ahead with the two warnings. 
The screenshot for javascript validation is [Javascript validation outcome](https://github.com/Anindita123-code/Milestone3_Data_Centric/blob/master/test-snapshots/javascript_validation.png)

#### PEP8 Compliance
The python code file has been tested for PEP8 compliance, using the [PEP8 online](http://pep8online.com/)
The validation output for PEP8 is as follows [PEP8 validation outcome](https://github.com/Anindita123-code/Milestone3_Data_Centric/blob/master/test-snapshots/PEP8_validation.png)

### Test for 404 - File not found
The 404 error has been trapped to display a more Project Friendly page, which has been tested. On encountering an unknown file the user will be routed to the home page of the website. 
Below is the snapshot for the same
[on Error 404](https://github.com/Anindita123-code/Milestone3_Data_Centric/blob/master/test-snapshots/400.png)

### Test for 500 - Internal Server Error
The 500 error has been trapped to display a more Project Friendly page, which has been tested by setting Debug=False and making some code errors so that "The Internal Server Error" can be emulated.
Below is the snapshot for the same
[on Error 500](https://github.com/Anindita123-code/Milestone3_Data_Centric/blob/master/test-snapshots/500.png)

### Performance Testing
A quick Audit was run using [Lighthouse](https://developers.google.com/web/tools/lighthouse)
Following is a snapshot of the outcome of the Audit using lighthouse
![Lighthouse Summary](https://github.com/Anindita123-code/Milestone3_Data_Centric/blob/master/test-snapshots/Performance_test.png)

## Deployment

The project uses github for hosting and has been deployed using heroku. The github repository is connected to the heroku.

### Deploy to Heroku
The project is connected to Heroku using automatic deployment from GitPod , using the following steps...

**Step 1: Create the requirements.txt and the Procfile.**
    To create a requirements.txt file,  we use the following command in CLI: 
    
        $ pip3 freeze --local > requirements.txt
    
    this will redirect the output of our freeze command into a file called requirements.txt.  Once this is created, now we need to add that file to the staging area, using 'git add -A' and hit enter.
    followed by: git commit -m "Add requirements.txt"
    If we click on the file to open it, you can see that it contains a list of the dependencies needed so far, which are 'Click', 'Flask, 'itsdangerous', and 'Werkzeug'.
    Next, we need to push this file to Heroku, by using: git push 
   
    Now we need to create the Procfile. The Procfile tells Heroku how to run our application.  A Procfile is a Heroku-specific type of file that tells Heroku how to run our project. The following command is used in the CLI to create a Procfile:

        $ echo web: python app.py > Procfile

    We need to add this to github by using the git add -A Procfile command, then git commit and finally push this into the git repository using the git push command.

**Step 2: Creating a New App in Heroku.**
    After usual login into Heroku, we need to create a new App. My new app for this project is named "views-and-reviews". The next step here is to 
    choose the appropriate region, then click 'Create app'.

**Step 3: Connect your git repository to Heroku App.**
    On the Heroku Dashboard, we need to select the deploy tab and select the Deployment method 'GitHub'.

    On the 'Connect to GitHub' section I need to search for my git repository which contains my project code. This is "Milestone3_Data_Centric" that i had created in Github for my project. I will need to search for this repository and connect to this one once the search results are displayed with my repository listing.

    My Github repository "Milestone3_Data_Centric" has my codebase, which is now connected to the new Heroku App.

**Step 4: Setup the Config variables in Heroku App**
    In the Settings tab on Heroku Dashboard, we need to select "Reveal Config Vars" to enter variables (key and value) contained in the env.py file. Following are the keys that have been used in this project and also in the Config Vars of the Heroku App.
        IP
        PORT
        SECRET_KEY
        MONGO_URI
        MONGO_DBNAME

**Step 5: Deploy my project to Heroku.**
    Once all the above 4 steps are done, we need to go to the Deploy tab on Heroku Dashboard and under the Automatic deployment section, click 'Enable Automatic Deploys'. This was done, so that all subsequent git commits in my git repository is reflected in the Heroku App as well. 
    After this is done, We need to select 'Deploy Branch'.

    Heroku will now receive the code from GitHub and start building the app using the required packages.

    Once built you will receive the message 'Your app was successfully deployed' and you can click 'View' to launch your new app.

### Access to code
The codebase in github can be accessed by forking and making a local clone of the repository "Milestone3_Data_Centric"

**Forking the GitHub Repository**
By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

    STEP 1 - Log in to GitHub and locate the GitHub Repository
    STEP 2 - At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
    STEP 3 - You should now have a copy of the original repository in your GitHub account.

**Making a Local Clone**

    STEP 1 - Log in to GitHub and locate the GitHub Repository
    STEP 2 - Under the repository name, click "Clone or download".
    STEP 3 - To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
    STEP 4 - Open Git Bash
    STEP 5 - Change the current working directory to the location where you want the cloned directory to be made.
    STEP 6 - Type git clone, and then paste the URL you copied in Step 3.

    $ git clone https://github.com/Anindita123-code/Milestone3_Data_Centric.git
    
    STEP 7 - Press Enter. Your local clone will be created.

    $ git clone https://github.com/Anindita123-code/Milestone3_Data_Centric.git

Note: The repository name and output numbers that you see on your computer, representing the total file size, etc, may differ from the example I have provided above.

Add an env.py file to your workspace to include your environment variables. This should be a copy of the env.py file, and .gitignore file present in the git repository

Note: The env.py mustn't be tracked as any GitHub user can access your confidential data and hence this is included as part of the .GitIgnore file

Once this is done, the Project can be run from the local using the following command in the gitpod CLI

    $ python3 app.py

## Credits
* For creating the sitemap I have used [Gloomaps](https://www.gloomaps.com/EJjeybEnhs)
* For Creating the Data Flow Diagram I have used [Miro](https://miro.com/app/board/o9J_lWeK1kc=/)
* For generating values for Secret Keys, I have used [RandomKeygen](https://randomkeygen.com/). A SECRET_KEY is required when using the flash and session functions of Flask.
* For creating the favicon.ico I have used [Gauger.io](https://gauger.io/fonticon/)
* I have used [Dbdiagrams.io](https://dbdiagram.io/home) for creating the Entity Relationship Diagram for the website
* I owe a huge thank you to [Stack Overflow](https://stackoverflow.com/) for addressing most of my queries.
* For addressing complex searches I have referred to [MongoDB Documentation](https://docs.mongodb.com/manual/reference/operator/query/regex/)
* For error handling, I have referred to [Flask Palletprojects link](https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/#error-handlers)
* Table of contents generated in the Readme has been generated with the help of markdown-toc
* All images and contents of books have been taken from [Books at Amazon](https://www.amazon.com/books-used-books-textbooks/b?ie=UTF8&node=283155)
* I am thankful to the Peer review Group of CI for giving me a lot of feedback to improve my project
* I am thankful to my family and friends for using this site to post some real reviews 

### Content
* All images and most of the contents of books have been taken from [Books at Amazon](https://www.amazon.com/books-used-books-textbooks/b?ie=UTF8&node=283155)
* the reviews have been mostly posted by me and some of my friends who helped me test the project.

### Media
* The home page hero image has been taken from [National Endowment for humanities: Open book](https://www.neh.gov/news/press-release/2015-01-15/humanities-open-book)

### Acknowledgements
* I have been inspired to take up the book review project oweing to my daughters love of reading story books, taken after my husband, who loves to share his opinion on books he has read
* I am thankful to my mentor for guiding me appropriately to come this far.

### Contact
In case of further questions and concerns please feel free to reach out to me at aninditasom@gmail.com.
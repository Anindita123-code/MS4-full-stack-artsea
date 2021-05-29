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

| User Story | As A/An User      | I want to be able to                                                                                                  | So that I can                                                                                       |
|------------|-------------------|-----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
|            |                   |                                                                                                                       |                                                                                                     |
| 1          | Student / Shopper | View a list of Workshops                                                                                              | Select the workshop that I want to purchase                                                         |
| 2          | Student / Shopper | View Individual Workshop Details                                                                                      | Identify the fees, description, associated image, Person   conducting, Venue and timings            |
| 3          | Student / Shopper | Easily view the total enrolment   amount                                                                              | prioritize my planned workshops                                                                     |
| 4          | Any user          | View a list of Topics in the   blog                                                                                   | Find out what are the currently active blogs in Artsea                                              |
| 5          | Any user          | View other users comments as   well as mine                                                                           | Read the comments of self and others given on a particular   post                                   |
|            |                   |                                                                                                                       |                                                                                                     |
| 6          | Site User         | Easily register for an account                                                                                        | Have a personal account and be able to view my profile                                              |
| 7          | Site User         | Easily login or logout                                                                                                | Access my personal account information                                                              |
| 8          | Site User         | Easily recover my password in   case I forget                                                                         | Recover access to my account                                                                        |
| 9          | Site User         | have a personalized user profile                                                                                      | View and update my personal information and also view my order   history                            |
|            |                   |                                                                                                                       |                                                                                                     |
| 10         | Student / Shopper | Filter by the Medium or type of   workshop                                                                            | View my selected list of Workshops only                                                             |
| 11         | Student / Shopper | Search by the name or   description                                                                                   | View the list of Workshops that matches my search criteria                                          |
| 12         | Student / Shopper | View a list of Workshops that matches the   or search criteria                                                        | Quickly decide that the Workshop I am looking for is available                                      |
|            |                   |                                                                                                                       |                                                                                                     |
| 13         | Student / Shopper | Add the selected workshop into   my shopping bag                                                                      | select the workshops that I want to purchase                                                        |
| 14         | Student / Shopper | See the subtotal and the Grand total of the items,  including delivery charges (if any) in the shopping bag           | View the breakups of the amount that I have to pay if I go   ahead with the order                   |
| 15         | Student / Shopper | Allowing users to view items in   their bag to be purchased                                                           | See my selection of items in the shopping bag                                                       |
| 16         | Student / Shopper | Modify the quantity of items in   my shopping bag                                                                     | Make changes in my shopping bag in the last moment                                                  |
| 17         | Student / Shopper | Delete any item from the   shopping bag                                                                               | Remove any items from the shopping bag if I found the correct   match                               |
| 18         | Student / Shopper | View the new grand total once the quantity in the shopping bag  Is modified or deleted                                | Quickly decide and move ahead for paying the new price                                              |
| 19         | Student / Shopper | Checkout by providing a valid   Credit card number                                                                    | Make a purchase                                                                                     |
| 20         | Student / Shopper | sufficiently notified if my card   number is invalid                                                                  | Modify my card number and provide a valid card details                                              |
| 21         | Student / Shopper | Get a successful purchase message once the purchase has been made                                                     | I can be sure that the purchase is successful                                                       |
| 22         | Student / Shopper | See an empty shopping bag on   successful purchase                                                                    | see that there is nothing in my shopping bag as the payment   has been successful                   |
| 23         | Student / Shopper | View my order details                                                                                                 | get an order number which is valid and be sure that I have   made a successful purchase             |
| 24         | Student / Shopper | Get an email for the order made                                                                                       | use the mail for a formal confirmation of the items that has   been purchased                       |
|            |                   |                                                                                                                       |                                                                                                     |
| 25         | superuser         | Create a new blog post                                                                                                | Connect with people using the website to comment and   collaborate                                  |
| 26         | site User         | View the list of Blog Posts                                                                                           | See all the blog topics at once                                                                     |
| 27         | site User         | Select and read any of the blog   posts                                                                               | Read the blog post in full                                                                          |
| 28         | site User         | Add a comment to the block post                                                                                       | Share my opinion                                                                                    |
| 29         | site User         | Read the comments made by other   site user on the blog post                                                          | Learn about others opinion                                                                          |
|            |                   |                                                                                                                       |                                                                                                     |
| 30         | superuser         | Create a new workshop and add the Title, Category,  Description, Hosted By, Date and time, venue, Image Url and price | Add workshops to the database                                                                       |
| 31         | superuser         | Notified of any invalid entries   for creating a workshop.                                                            | Make the necessary changes before commiting the records in the   database                           |
| 32         | superuser         | Notified if the workshop has   been created successfully                                                              | Be sure that they are saved in   the database and will be available for users to enrol for the same |
| 33         | superuser         | Update an existing workshop data                                                                                      | Make any changes to the date and time or venue if required                                          |
| 34         | superuser         | Delete a workshop                                                                                                     | remove any cancelled workshop                                                                       |


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

***Elements Across the wewbsite***
Bootstrap Grid system have been used to structure pages and make them responsive for various viewports.
Bootstrap NavBar navbar to allow easy navigation throughout the web app. Able to reach all pages of the app from the NavBar. For mobile and smaller devices the navbar is found in the hamburger menu.
Bootstrap NavBar contains site title, which acts as a home button, dropdowns for accessing account actions, link to shopping basket and filters to help navigate the site.
Bootstrap Footer used with social links and email.

Favicon for the title tab in the browser.
Hover used on all buttons and web/email addresses.
Bootstrap Toasts used for all flashed messages after completion of an action.
Search bar at the top of the screen that is linked to keyword searches to display workshops with matching words in the Title and Description fields.

***Home Page Elements***
A hero Image on top in-tune with the theme of the project
A short writeup about the objective of the website and a link which takes the user to the workshop page

***Login Page Elements***
User login form allowing input from the user for their username and password with "Sign In" submit button which queries the Database to check the validity of the user.
If the user is valid, a toast message is displayed and the user is redirected to the Workshops page.
If a matching user is not found, the user cannot proceed further, and an error message is generated
Links are displayed to allow the user to register or to reset their password.

***Registration Page Elements***
Registration form expecting the following input from the user: 
- email address, confirm email address, username, password, confirm password.
"Sign Up" submit button sends info to DB and shows a verification page prompting the user to confirm that they want to sign up.

***Workshops Page Elements***
This page displayes Workshop information using Bootstrap cards along with the associated image of the workshop
The user can get into a more detailed understanding of the workshop by clicking the picture, which takes the user to the Workshop detail page
On Clicking the Category name, associated with the workshop, the user will be able to filter, and display, all the workshops for that Category
** Back to Top button at the bottom right of the screen.
If the user is a SuperUser, Edit/Delete pills will be displayed to allow easy Workshop Management.

***Workshop Detail Page Elements***
In the detail page for the workshop, to the left, the associated image of the workshop is displayed, if there is no image associated, then the no_image.jpg is displayed
To the right the title, description, venue, date & time, Hosted by name and price along with quantity selector is displayed.
Plus/Minus quantity icons are placed either side of Number Input Field which can also be manually updated or using the up/down arrows that appear in the field.
Two buttons - add to bag and keep shopping - are below the quantity input field.
Keep Shopping returns the user to the All Workshop page and Add to Bag adds items to the bag which displays a Bootsrap Toast success html which will show the items of the bag and the total amount purchased. 

***Shopping bag page elements***
This page is displayed after the user adds the items into the shopping bag and selects to do checkout
The user will be able to adjust the quantity of the items in the basket using the plus/minus icons and clicking the update link or remove the whole line by clicking the remove link.
The grand total along with the taxes or delivery charge (if any) is computed and displayed for a particular order
The buttons at the bottom allow the user to confirm that they wish to proceed with paying and takes them to the checkout page or to return to the all products page.

***Checkout Page Elements***
After the user finalizes their purchase, they can move ahead to do a checkout and make the payment of the purchase.
This page is divided into two parts, the first one, shows the order summary, the second part shows a form requesting for demographic information about the user.
The user must populate the form on the left before being able to continue the checkout process.
There are required fields in the form and this information will be saved to the DB if the user has logged in or creates an account prior to checkout.
The credit card field is linked to STRIPE and the form inherits the stripe validations associated with credit cards
Buttons at the bottom allow the user to go back to the shopping bag and make adjustments to the quantity purchased or move ahead to pay and complete the order.
**Once the user submits the payment information an opaque overlay appears to show that the payment is being processed.

***Checkout Success / Order Confirmation Page***
The order confirmation page lists out the order number and the detail of the purchase along with the subtotal and grandtotal.
A button under the summary directs the user to the Events page 
The user can browse back to the Workshops Page on onward to Read the Published Blogs in the site.

***Blog list Page***
A signed in or anonymous user, can navigate to the Blog page using the Navigation links at the top of the page. 
The Blog list plays displays the list of Active Blogs, their author names and the date on which the blog was published.
The user can select any one to read and is directed to the Blog detail page

***Blog detail Page elements***
Any user can read the go to the blog detail page to read and comment on the blog post. 
Users can read other users comments which are displayed below the Blog itself.
Users can post their comments on the blog by using the form below, with their names, email-id and the comments and selecting Post.
Once posted, their comments will show up in the section of view comments.

### Features Left to Implement (none)

## Technologies Used

HTML - used to create the site structure.
CSS - used to create the styling throughout the site.
JavaScript - this was used for the addition/deletion of ingredients and methods buttons
jQuery - this was used to activate the Materialize functionality.
Python - used to write the logic that operates the site.
Django - web framework used to allow a modular site to be created.
Font-Awesome - icons were taken from this site for the forms, header, footer and social buttons.
Google fonts - as previously stated, the fonts used were taken from here.
Heroku - used for hosting website.
Bootstrap - used for responsive grid framework, navigation and buttons.
Stripe - ecommerce payment system.

### Languages
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) for creating the webpages
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) for designing and styling the web pages
- [javascript] (https://www.javascript.com/)
- [Python](https://www.python.org/) for the backend development
### Database
- [SQLlite (in Development)]() and [Postgres (at deployment)]() Although Sqllite has been used as the backend database during development, the 
### Libraries and Frameworks
- [Font Awesome](https://fontawesome.com/) - have been used for the button icons that are used in the website
- [Google Fonts](https://fonts.google.com/) have been used to give the website a uniform look with the help of fonts provided by google
- [JQuery](https://jquery.com) - have been used to simplify DOM manipulation.
- [Django](https://www.djangoproject.com/) - web framework for creating modular websites
- [Bootstrap](https://getbootstrap.com/docs/3.4/css/) - css used for responsive grid framework and general styling
- [Stripe](https://stripe.com/en-dk) - used for payment with credit card
### Hosting
- [Github](https://github.com/) have been used for storing the application in public repositories
- [GitPod](https://gitpod.io/workspaces/) have been used as the primary development platform
- [Heroku](https://www.heroku.com/) have been used to host the website
- [AWS](https://aws.amazon.com/?nc2=h_lg) for static and media files

## Testing

The test results for Artsea can be found in [here]()

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
The static folder contents and the media folders of the project are deployed in AWS.

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
    After usual login into Heroku, we need to create a new App. My new app for this project is named "Artsea-anindita". The next step here is to 
    choose the appropriate region, then click 'Create app'.

**Step 3 Configure the Postgres database for Artsea**
    Before the application is deployed, We need to install the following packages using pip3 and get the databse up and running
    In the resource tab of Heroku workspace, we need to provision a new Postgres database. After this we need to get back to gitpod and install the following packages

    -- pip3 install dj_database_url and psycopg2-binary
    -- pip3 freeze > requirements.txt

    Now we need to run the migrations after connecting to the new database. This can be easily done by changing the the database configurations to dj_database_url.parse with the new DATABASE_URL (this can be found in the config vars of settings in Heroku app)
    Once the migrations are run successfully, the new table structures would be created. The commands are as follows:

    $ python3 manage.py makemigrations --dry-run
    $ python3 manage.py makemigrations
    $ python3 manage.py migrate --plan
    $ python3 manage.py migrate

    The next step is to run the fixtures for the 1) Category and then 2) Workshop table and finally 3) Blog table
    On running the fixtures the tables will have the necessary data to run the application.

    $ python3 manage.py looddata categories
    $ python3 manage.py loaddata workshop
    $ python3 manage.py loaddata blog

**Step 4: Create superuser and run the application**

    Before we start to do anything with the app. We have to create a superuser profile. Which is the admin user of Artsea. This is the artsea_admin user.

    $ Python3 manage.py createsuperuser 
    is used to create a superuser, by providing a userid and password.

    to run the application we need to install another package called gunicorn. So we run the following command

    $ pip3 install gunicorn (the webserver)
    $ pip3 freeze > requirements.txt

    Following this we create the Procfile. this is to tell Heroku to create a web dyno Which will run unicorn and serve our django app.
    Finally we need to disable collectstatic by using the following command.

    $ heroku config:set DISABLE_COLLECTSTATIC=1 --app anindita_artsea 
    This will stop collecting the static files and the media files while we push our code to heroku from github. After this we set git remote to Heroku.

    $ heroku git:remote -a anindita-artsea
    $ git push Heroku master

**Step 3: Connect your git repository to Heroku App.**
    On the Heroku Dashboard, we need to select the deploy tab and select the Deployment method 'GitHub'.

    On the 'Connect to GitHub' section I need to search for my git repository which contains my project code. This is "Milestone3_Data_Centric" that i had created in Github for my project. I will need to search for this repository and connect to this one once the search results are displayed with my repository listing.

    My Github repository "MS4-full-stack-artsea" has my codebase, which is now connected to the new Heroku App.

**Step 4: Setup the Config variables in Heroku App**
    In the Settings tab on Heroku Dashboard, we need to select "Reveal Config Vars" to enter variables (key and value) contained in the env.py file. Following are the keys that have been used in this project and also in the Config Vars of the Heroku App.
        **Config Var**	
        AWS_SECRET_KEY_ID           - obtained when you set up AWS
        AWS_SECRET_ACCESS_KEY       - obtained when you set up AWS
        DATABASE_URL	            - created when you provisioned Postgres
        EMAIL_HOST_PASS	            - obtained from your email provider
        EMAIL_HOST_USER	            - your email address
        SECRET_KEY                  - obtained from miniwebtool
        STRIPE_PUBIC_KEY            - obtained from STRIPE
        STRIPE_SECRET_KEY           - obtained from STRIPE
        STRIPE_WH_SECRET            - obtained from STRIPE
        USE_AWS	                    - Set to True

**Step 5: Deploy my project to Heroku.**
    Once all the above 4 steps are done, we need to go to the Deploy tab on Heroku Dashboard and under the Automatic deployment section, click 'Enable Automatic Deploys'. This was done, so that all subsequent git commits in my git repository is reflected in the Heroku App as well. 
    After this is done, We need to select 'Deploy Branch'.

    Heroku will now receive the code from GitHub and start building the app using the required packages.

    Once built you will receive the message 'Your app was successfully deployed' and you can click 'View' to launch your new app.

**Generate secret key for Django**

    Finally, all projects should have their separate Django secret keys, which can be obtained by using the [Django Secret key generator](https://miniwebtool.com/django-secret-key-generator/)
    The newly generated secret key is stored as a Key value pair in the Config Vars of Settings in the Heroku app.

    SECRET_KEY - key obtained from miniweb tools

**Step 6: Configure AWS for hosting static (css and js) files and media (uploaded images)**
    In order for the static css, js and media files to be stored and useable with Heroku, you need to set up an AWS account. I created a Root user account for AWS.
    In AWS we need to use the service S3 and IAM. We need to search for the service S3.

    Then do the following:
    * Search for S3.
    * Create a new bucket and ensure that the Block All Public Access tickbox is unchecked and acknowledge that the bucket will be public
    * Select Static Website hosting under Properties which would allow static files to be hosted in AWS
    * Set up the ***Cross-origin resource sharing (CORS)*** in the property tab. The following settings are done in CORS
        [   
            {       
                "AllowedHeaders": [
                                    "Authorization"
                                ],
                                    "AllowedMethods": ["GET"],
                                    "AllowedOrigins": ["*"],
                                    "ExposeHeaders": []
            }
        ]

    * Click the Policy Tab and select Policy Generator which creates a security policy for the bucket. This S3 policy needs to be generated by filling th necessary fields
    * Copy the generated policy in to the Bucket Policy Editor. 
    * Add /* at the end of the resource key as this will allow access to all resources in the bucket and then save it.
    * Click the Access Control tab and set the list object permission to everyone under the Public Access section.
    * Next we need to configure the IAM, So we need to Open IAM from the service menu.
    * Then we need to create a group and create an access policy for the group which would give access to the S3 bucket.
    * Click the JSON tab and select import managed policy, search for S3 and select S3 Full Access Policy.
    * Now we will attach the policy to the group we created (artsea-group for me) by searching the policy we just created and selecting it and then clicking the Attach Policy
    * Create a user (artsea-staticfiles-user for me), give them programmatic access and attach it to the group. And then click create policy. This takes us back to the policies page where we can see our policy has been created.
    * Download the CSV file that is generated as this contains the keys required to use AWS.

Now that we've created an s3 bucket and the appropriate user's groups and security policies for it. The next step is to connect django to it. To do this we'll need to install two new packages.
    
    $ pip3 install boto3
    $ pip3 install django-storages
    $ pip3 freeze > requirements.txt

    * To connect Jango to s3 we need to add some settings in settings.py to tell it which bucket it should be communicating with. We'll only want to do this on Heroku. So let's add an if statement
    * to check if there's an environment variable called USE_AWS in the environment. If so we will define the AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME and our access key, and secret access key, which we'll get from the environment.
    * With those settings added, we will go to Heroku and add our AWS keys to the config variables along with a key called USE_AWS which is set to true, so that our setting file knows to use the AWS configuration when we deploy to Heroku
    * Next we will need to remove the disable collectstatic variable so that with our next deployment in Heroku the static files are collected automatically into S3
    * Back in our settings file we need to tell django where our static files will be coming from in production this would be our bucket name (AWS_STORAGE_BUCKET_NAME in configvars).s3.amazonaws.com
    * The next step is to tell django that in production we want to use s3 to store our static files whenever someone runs collectstatic And that we want any uploaded product images to go there also we will do this by creating a file called custom_storages.py and create a custom class called static_storage and tell Django that we want to store static files in a location from settings.py (STATICFILES_LOCATION)
    * The same step is repeated for media files and specify the MEDIAFILES_LOCATION key in settings.py so that whenever we run python3 manage.py runserver collectstatic (While DISABLE_COLLECTSTATIC is set to 0). 
    * Whenever collectstatic is run Static files will be collected into a static folder in our s3 bucket automatically. To make sure it works, all we have to do is add all these changes. Commit them.
        and then issue a git push. Which will trigger an automatic deployment to Heroku. With that done if we look at the build log. We can see that all the static files were collected successfully.
        And if we now go to s3 We can see we have a static folder in our bucket with all our static files in it.
    * While our app is deploying we will add media files to s3. We can do this by creating a new folder in S3 called media, and upload the workshop and related images for the site
    * Next under manage public permissions, we have to grant public read access to these objects and then click upload. 

So now my AWS has both my static and my media files that are needed to run the application.

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
* For creating the favicon.ico I have used [Gauger.io](https://gauger.io/fonticon/)
* I have used [Dbdiagrams.io](https://dbdiagram.io/home) for creating the Entity Relationship Diagram for the website
* I owe a huge thank you to [Stack Overflow](https://stackoverflow.com/) for addressing most of my queries.
* The Boutique Ado application of Code Institute Training modules has been a huge inspiration for doing this project.
* Table of contents generated in the Readme has been generated with the help of markdown-toc
* All images and contents of books have been taken from real workshops of Art studios that I am connected with in Copenhagen
* I am thankful to my Mentor Aaron Signott for his able guidance in this project.
* I am thankful to the Peer review Group of CI and May-2020 group on slack for giving me a lot of feedback to improve my project, and encouraged me all along this journey.
* I am thankful to my family and friends for using this site to post some real reviews 

### Content
* All written content, of this website have been taken from facebook, and random search from google. 

### Media
* All media images have been gathered from random search using google images, which are shareable.

### Acknowledgements
* I have been inspired to take up the Artsea project, as I look forward to host a similar kind of website in the future which would tie all art studios in Denmark together and give information to users in one common place.

### Contact
In case of further questions and concerns please feel free to reach out to me at aninditasom@gmail.com.
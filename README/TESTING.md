

# Artsea - Milestone4 Project - Testing 
[live link of the website](https://anindita-artsea.herokuapp.com/)

## Table of Contents


## MANUAL TESTING
* Chrome Developer Tools were used to test responsiveness on all screen sizes.
* Physical testing was carried out on Desktop, Tablet and various Mobile devices.
    * Throughout the whole process, I was testing the responsiveness of the site in various device sizes.
    * After finally deploying it on Heroku, the link was shared with the peer code review slack channelI 
    * I also got this reviewed with my friends and family, to get an understanding of the look and feel of it.
* All links were tested to ensure they worked on all devices.
* NavBar was tested to ensure it worked on all devices.
* All CRUD functions were tested to ensure they worked on all devices.
* The Checkout functionalities were tested to ensure that they worked on all devices
* The Blog was tested to see that they were working as expected on various screen sizes.
* The confirmation emails were generated as expected, once the user completed a purchase

### Functional Testing (User Driven)

#### Viewing and Navigation
As a User I am able to 
    * Navigate easily to the Workshop and the Blogs page all over the site
    * View a list of Workshops and select the workshop that I want to purchase
    * View Individual Workshop Details and identify the fees, description, associated image, Person conducting, Venue and timings
    * Easily view the total enrolment amount in order to prioritize my planned workshops
    * View a list of Topics in the blog	in order to Find out what are the currently active blogs in Artsea
    * View other users comments as well as mine	and be able to read the comments of self and others given on a particular post

#### REGISTRATION AND USER ACCOUNTS
As a new user, I am able to     
    * Easily register for an account so that I can Have a personal account and be able to view my profile
    * Easily login or logout so that I can Access my personal account information
    * Easily recover my password in case I forget so that I can Recover access to my account
    * have a personalized user profile so that I can View and update my personal information and also view my order history

#### FILTERING AND SEARCHING
As a user of the site I am able to 
    * Filter by the Medium or type of workshop so that I can View my selected list of Workshops only
    * Search by the name or description	so that i can View the list of Workshops that matches my search criteria
    * View a list of Workshops that matches the filter or search criteria so that I can quickly decide that the Workshop I am looking for is available

#### PURCHASIMG AND Checkout
As a user / shopper of the site I am able to 
*   Add to Shopping Bag
    *   Add the selected workshop into my shopping bag so that I can select the workshops that I want to purchase
    *   See the subtotal and the Grand total of the items, including delivery charges (if any) in the shopping bag so that I can view the breakups of the amount that I have to pay if I go ahead with the order
    *   Allowing users to view items in their bag to be purchased so that i can see my selection of items in the shopping bag
    *   Modify the quantity of items in my shopping bag	Make changes in my shopping bag in the last moment
    *   Delete any item from the shopping bag by removing any items from the shopping bag if I found the correct match
    *   View the new grand total once the quantity in the shopping bag Is modified or deleted to help me quickly decide and move ahead for paying the new price

*   Checkout and Pay
    *   Checkout by providing a valid Credit card number in order to Make a purchase
    *   sufficiently notified if my card number is invalid and be able to Modify my card number and provide a valid card details
    *   Get a successful purchase message once the purchase has been made so that I can be sure that the purchase is successful
    *   See an empty shopping bag on successful purchase and see that there is nothing in my shopping bag as the payment has been successful
    *   View my order details and get an order number which is valid and be sure that I have made a successful purchase
    *   Get an email for the order made	use the mail for a formal confirmation of the items that has been purchased

#### BLOGS AND USER comments
Creating blogs in the website by the superuser, and ability to read and comment on the blog post by all other users of the website
*   CRUD operation on blog by superuser access and connect with people using the website to comment and collaborate
*   View the list of Blog Posts to see all the blog topics at once
*   Select and read any of the blog posts so that I can read the blog post in full
*   Add a comment to the block post	to share my opinion
*   Read the comments made by other site user on the blog post and earn about others opinion 

#### WORKSHOP RECORD MANAGEMENT
This is done only by the superuser of the website. The CRUD operation
*   Create a new workshop and add the Title, Category, Description, Hosted By, Date and time, place of workshop, Image Url and price and Add workshops to the database
*   Notified of any invalid entries for creating a workshop and Make the necessary changes before commiting the records in the database
*   Notified if the workshop has been created successfully.	Be sure that they are saved in the database and will be available for users to enrol for the same
*   Update an existing workshop data. Make any changes to the date and time or venue if required
*   Delete a workshop and remove any cancelled workshop


## AUTOMATED TESTING

### Validation Tests

***HTML Validation**
The HTML for the project has been validated using [W3C's Validation service](https://validator.w3.org/). 
The generated html is complaint as per W3C standards with no errors / warnings

**CSS Validation**
There are two css files used in the project the main css file is the  base.css is in the /static/css/ folder and the second one is the checkout.css in the static folder of checkout
The contents of both these files have been validated with [W3C's CSS Validator](https://jigsaw.w3.org/css-validator/). Both the files comply well with this validation.

**Javascript Validation**
The custom javascript code has been validated using [JShint](https://jshint.com/). There are two warnings 
*   One is for the use of $ which has been used for Jquery references, and hence will need to stay
*   is the use of (``) template literals, which also need to stay, as they are implemented in handling a key functionality for stripe payments. 

**PEP8 Compliance**
The python code file has been tested for PEP8 compliance, using the PEP8 online The validation output for PEP8 is as follows 
    $ Python3 -m flake8

* I have decided to ignore any warnings on files that are automatically generated. Such as migration and Imports in files that are created automatically. This is because automatically generated files may intentionally ignore style rules for efficiency reasons.
* Apart from this majority of the PEP8 issues have been taken care of.

**Test for 404 - File not found**
The 404 error has been trapped to display a more Project Friendly page, which has been tested. On encountering an unknown file the user will be routed to the home page of the website. Below is the snapshot for the same on Error 404

**Test for 500 - Internal Server Error**
The 500 error has been trapped to display a more Project Friendly page, which has been tested by setting Debug=False and making some code errors so that "The Internal Server Error" can be emulated. Below is the snapshot for the same on Error 500

**Performance Testing**
A quick Audit was run using Lighthouse Following is a snapshot of the outcome of the Audit using lighthouse Lighthouse Summary


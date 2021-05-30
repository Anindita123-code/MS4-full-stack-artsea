

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
**As a User I am able to**
* Navigate easily to the Workshop and the Blogs page all over the site
    The Navbar on the top of the page allows the user to navigate easily to the Blog as well as the Workshop pages. On wide screens the Logo will route the user to the home page while in small screen the top navbar has an extra "home" link to route the user to the home page always
    
    ![Site Home](https://github.com/Anindita123-code/MS4-full-stack-artsea/blob/master/README/snapshots/homepage.jpg)


* View a list of Workshops and select the workshop that I want to purchase
    The user can navigate to view for a filtered list of workshops, using the Workshop Navbar dropdown, and this will take the user to the Workshop list page,
    
    ![Workshop List](https://github.com/Anindita123-code/MS4-full-stack-artsea/blob/master/README/snapshots/workshop_list.jpg)


* View Individual Workshop Details and identify the fees, description, associated image, Person conducting, Venue and timings
    The user can select any one of the listed workshops and go into the workshop detail page which has more details about the individual workshop.

    ![Workshop Detail](https://github.com/Anindita123-code/MS4-full-stack-artsea/blob/master/README/snapshots/workshop_detail.jpg)


* Easily view the total enrolment amount in order to prioritize my planned workshops
    The user can add the selected workshops in the bag and view the final bag with all the workshops, where they can make a final choice of which one they would be interested in.
    The subtotals for each workshop and the final grand total is displayed in the shopping bag page.

    ![Shopping bag](https://github.com/Anindita123-code/MS4-full-stack-artsea/blob/master/README/snapshots/shopping_bag.jpg)


* View a list of Topics in the blog	in order to Find out what are the currently active blogs in Artsea
    On selecting the Blog from the Nav bar the user is routed to the Blog list page, where the currently active blogs along with their published dates are displayed.

    ![Blog List](https://github.com/Anindita123-code/MS4-full-stack-artsea/blob/master/README/snapshots/blog_list.jpg)


* View other users comments as well as mine	and be able to read the comments of self and others given on a particular post
    On selecting any particular Blog from the blog list page, the user is directed to the Blog detail page, where they can read the Blog content and then post a comment, The user can also read others comments.
    A guest user, who is not logged in can also get in and be a part of the blog community.

    ![Single Blog and comment](https://github.com/Anindita123-code/MS4-full-stack-artsea/blob/master/README/snapshots/blog_detail.jpg)


#### REGISTRATION AND USER ACCOUNTS
**As a new user, I am able to**    
    * Easily register for an account so that I can Have a personal account and be able to view my profile
    A new user can signup and create an account which can be stored for prefilling the form when they shop anything from the site.
    This is done, by selecting the User account on top right hand corner and selecting Signin. On doing so the following page shows up.

    ![New user signin](https://github.com/Anindita123-code/MS4-full-stack-artsea/blob/master/README/snapshots/user_signup.jpg)

    Once the new user account is created, the system prompts with the a Signin Success message.

    ![Successful Signup](https://github.com/Anindita123-code/MS4-full-stack-artsea/blob/master/README/snapshots/signin_success.jpg) 

**As an existing user, I can**    
    * Easily login or logout so that I can Access my personal account information
    A returning user can use their userid and password to login to their account by selecting login from the User Account in the home page. If the userid and password matches then the user is routed to the Workshops page, else an error message pops out to let the user know that he has to make another try
    Folloing is the snapshot of the login page with error message. 

    ![Login page-invalid signin](https://github.com/Anindita123-code/MS4-full-stack-artsea/blob/master/README/snapshots/invalid_userid.jpg) 
    
    * Easily recover my password in case I forget so that I can Recover access to my account
    In case the user forgets their password they can recover it using the Forgot password page as below

    ![Password Reset](https://github.com/Anindita123-code/MS4-full-stack-artsea/blob/master/README/snapshots/forgot_password.jpg)

    * have a personalized user profile so that I can View and update my personal information and also view my order history
    A logged in user can have all his information stored in a common location, under "My Profile" from where he can update his information to keep currently

    ![Uer Profile](https://github.com/Anindita123-code/MS4-full-stack-artsea/blob/master/README/snapshots/user_profile.jpg)

#### FILTERING AND SEARCHING
**As a user of the site I am able to** 
    * Filter by the Medium or type of workshop so that I can View my selected list of Workshops only
    The navbar with the workshop has a dropdown list, using which the user can filter the workshops by categories

    ![Filtering by Category](https://github.com/Anindita123-code/MS4-full-stack-artsea/blob/master/README/snapshots/sitenav.jpg)

    * Search by the name or description	so that i can View the list of Workshops that matches my search criteria
    The search bar on the top of the main navbar, can search for workshops which has matching words in the workshop title or the workshop description. Once found, the matching workshops are displayed as search results

    ![Search result page](https://github.com/Anindita123-code/MS4-full-stack-artsea/blob/master/README/snapshots/workshop_search_result.jpg)

    * View a list of Workshops that matches the filter or search criteria so that I can quickly decide that the Workshop I am looking for is available
    The workshop list matching the filter condition is displayed below.

    ![Workshop filter](https://github.com/Anindita123-code/MS4-full-stack-artsea/blob/master/README/snapshots/workshop_filter.jpg)


#### PURCHASIMG AND Checkout

**As a user / shopper of the site I am able to**

*   Add to Shopping Bag
    *   Add the selected workshop into my shopping bag so that I can select the workshops that I want to purchase
    Any user can select and read about the workshop and then add the one of their choice into the Shopping bag by selecting "Add to Bag"

    ![Add to Bag](https://github.com/Anindita123-code/MS4-full-stack-artsea/blob/master/README/snapshots/add_to_bag.jpg)

    *   See the subtotal and the Grand total of the items, including delivery charges (if any) in the shopping bag so that I can view the breakups of the amount that I have to pay if I go ahead with the order
    *   Allowing users to view items in their bag to be purchased so that i can see my selection of items in the shopping bag
    The subtotal and the grand total can be viewed in the Shopping Bag. Along with all the items that has been added by the user. Below is a snapshot of the shopping bag with items.

    ![Shopping Bag](https://github.com/Anindita123-code/MS4-full-stack-artsea/blob/master/README/snapshots/shopping_bag.jpg)
    
    *   Modify the quantity of items in my shopping bag	Make changes in my shopping bag in the last moment
    *   Delete any item from the shopping bag by removing any items from the shopping bag if I found the correct match
    The user can modify the quantity selected for the items in the shopping bag. Or remove the item completely from the bag.

    ![Update Shopping bag](https://github.com/Anindita123-code/MS4-full-stack-artsea/blob/master/README/snapshots/update_quantity.jpg) 

    *   View the new grand total once the quantity in the shopping bag Is modified or deleted to help me quickly decide and move ahead for paying the new price
    Once an item is removed from the shopping bag the Grand total is updated. And if that is the last item in the bag the Empty shopping bag is displayed with a message

    ![Delete Shopping bag item](https://github.com/Anindita123-code/MS4-full-stack-artsea/blob/master/README/snapshots/empty_bag.jpg)

*   Checkout and Pay
    *   Checkout by providing a valid Credit card number in order to Make a purchase. The user is sufficiently notified if my card number is invalid and be able to Modify my card number and provide a valid card details
    Once the shopping bag is ready, the user can proceed to checkout by providing a valid credit card. The credit card validation is done by Stripe and it displays an error message if the card details are invalid.

    ![Invalid Card Message](https://github.com/Anindita123-code/MS4-full-stack-artsea/blob/master/README/snapshots/invalid_Card.jpg)

    *   Get a successful purchase message once the purchase has been made so that I can be sure that the purchase is successful
    Once the user provides a valid card number, the order is processed and an order confirmation page is displayed to the user. With this, the shopping bag is emptied to zero items.
    *   I can View my order details and get an order number which is valid and be sure that I have made a successful purchase

    ![Successful Purchase](https://github.com/Anindita123-code/MS4-full-stack-artsea/blob/master/README/snapshots/order_Confirmation.jpg)

    *   Get an email for the order made	use the mail for a formal confirmation of the items that has been purchased
    On successful generation of Order number the user/shopper will get an order confirmation email. A snapshot of the same is found below.

    ![Order confirmation email](https://github.com/Anindita123-code/MS4-full-stack-artsea/blob/master/README/snapshots/order_email.jpg)


#### BLOGS AND USER comments
Creating blogs in the website by the superuser, and ability to read and comment on the blog post by all other users of the website
*   CRUD operation on blog by superuser access and connect with people using the website to comment and collaborate
The superuser of Artsea can create Blogs which are readily accessible to other users to read and share their perspectives. A superuser can do this by using "Blog Management" from their User Account at the top right side of the header.
The mandatory fields are marked with * and doesnot allow the superuser to go ahead without filling them. Once the Blog is created successfully, a message is displayed indicating the same.
Following is the snapshot of Add a blog page

![Add New Blog](https://github.com/Anindita123-code/MS4-full-stack-artsea/blob/master/README/snapshots/add_blog.jpg)

The superuser has the privilege to edit an exisiting blog or delete it completely. Following is the screenshot of the edit blog page

![Edit Blog](https://github.com/Anindita123-code/MS4-full-stack-artsea/blob/master/README/snapshots/edit_blog.jpg)

*   View the list of Blog Posts to see all the blog topics at once
Any user of the site can select the Blog in the navbar and will be routed to the Blog list page. From the blog list page, the user has an option to either go to the Blog detail page or move into the Workshops page.
A snapshot of the Blog detail page can be found below

![Blog List](https://github.com/Anindita123-code/MS4-full-stack-artsea/blob/master/README/snapshots/blog_list.jpg)

*   Select and read any of the blog posts so that I can read the blog post in full
When a user selects any of the Blog list, they are routed to the blog detail page, this page is divided into two sections. The top part has the Blog content, and the bottom part shows the Comments

![Read Blog](https://github.com/Anindita123-code/MS4-full-stack-artsea/blob/master/README/snapshots/blog_display.jpg)

*   Add a comment to the block post	to share my opinion
A user can add their comment for the blog in the textarea below and click on Add, their comments will be displayed in the list of Comments. There is a toggle button to show and hide the list of comments at the bottom of the page.

![Blog user-comment](https://github.com/Anindita123-code/MS4-full-stack-artsea/blob/master/README/snapshots/blog_comment.jpg)

*   Read the comments made by other site user on the blog post and earn about others opinion 

![Show hide user comment](https://github.com/Anindita123-code/MS4-full-stack-artsea/blob/master/README/snapshots/blog_detail_comment_section.jpg)


#### WORKSHOP RECORD MANAGEMENT
This is done only by the superuser of the website. The CRUD operationa on Workshop.
*   Create a new workshop and add the Title, Category, Description, Hosted By, Date and time, place of workshop, Image Url and price and Add workshops to the database
The superuser (artsea_admin) can create a new workshop from the user Account -> Workshop Management link on the page header.

![Navigate to Add workshop](https://github.com/Anindita123-code/MS4-full-stack-artsea/blob/master/README/snapshots/AccountDropdown.jpg)

![Add new Workshop](https://github.com/Anindita123-code/MS4-full-stack-artsea/blob/master/README/snapshots/add_workshop.jpg)

*   Notified of any invalid entries for creating a workshop and Make the necessary changes before commiting the records in the database
The system checks for Mandatory field entries for workshop. Following are the fields for workshop entries.
    1. Cateogory    -   is the bucket under which the workshop can be categorized, this comes from the Category Model created internally
    2. name         -   is the short name of the workshop.
    3. Title        -   is the descriptive title of the workshop.
    4. Description  -   is the description in a few lines about the workshop, which explains how it would fit your requirement
    5. Hosted By    -   is the name of the Artist or Art Studio hosting the workshop
    6. Date and time-   is the Date or From-Date to To-Date, and the timings (Start-time to End-time) during which the workshop would commense.
    7. Venue        -   is the location for the workshop, which may be online or in any studio
    8. price        -   is the enrollment fees to block a spot for the workshop in DKK
    10. Image       -   is the associated Image for the workshop.

*   Notified if the workshop has been created / Edited / Deleted successfully.	Be sure that they are saved in the database and will be available for users to enrol for the same
Once the workshop is created successfully, there will be a notification displayed to the user, indicating the same. As per the below snapshot

![Notification Message](https://github.com/Anindita123-code/MS4-full-stack-artsea/blob/master/README/snapshots/edit_workshop_message.jpg)

![Delete Workshop](https://github.com/Anindita123-code/MS4-full-stack-artsea/blob/master/README/snapshots/workshop_deleted.jpg)

If there is no image associated with the workshop. A no-image.jpg is created and is displayed.

![No Image Workshop](https://github.com/Anindita123-code/MS4-full-stack-artsea/blob/master/README/snapshots/no_image_workshop.jpg)

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

**Performance Testing**
A quick Audit was run using Lighthouse Following is a snapshot of the outcome of the Audit using lighthouse Lighthouse Summary

[BACK TO README FILE](https://github.com/Anindita123-code/MS4-full-stack-artsea/blob/master/README.md)
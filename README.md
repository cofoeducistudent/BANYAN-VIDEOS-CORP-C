# BANYAN-VIDEOS-CORP-C
BANYAN-VIDEOS-CORPORATION-C

 Live Site:
 https://banyan-videos-corp-c.herokuapp.com/


GitHub:

https://github.com/cofoeducistudent/BANYAN-VIDEOS-CORP-C


|Screen|Size|
|------|----|
|<img src="_support_docs/images/home-page.jpg" width="400">|* Mobile First - Small Screen|
|<img src="_support_docs/images/banyan-videos-corp-home-page.jpg " width="400">|* Large Screen Size|
 


USER_ACCOUNTS FOR TESTING
siteadmin -
anonuser -
memberuser -  




## Index ##

> Project Brief

Banyan videos project brief.

Banyan videos corporation has asked for a website but will help them retail their video merchandise online.

For this reason they have provided a brief stating what they would like to see on the site with features that would definately wish on it.


* Firtsly the site would be light in appearance and corporate like ( flash etc).

* The Front page should have a search facility allowing users to search for products

* It should have a carousel showing a selection of film products for sale

* It should show for news/information which banyan videos deem fit.This is not an rss-feed or an integrated feed to other sites, but a section allowing banyan videos administrators to post corporate messages and news, or whatever they wish.

* On a members section there should be more article links to other important news on the web (curated by banyan videos admin). This should have a title/description, a picture, all linkable to the source material.

* The colour theme should be plain and simplistic, and the appearance of the site should predominantly light and clean.


* The frequency and volume of the products will be centrally controlled. Therefore, they wish to have a way of populating the product line very quickly. This will ensure prices and sale discounts are also effectively controlled. The intention is for head Office (H.O) to email a file to the site admin, who will simply upload the data with a single command. BVC do not wish to have a CMS for creating items, aas that will remove a single point of control.


* In the future they wish to have a separate server to serve images for their products, which will have a commercial uniform asset look, like major retailers such as Argos or Sainsbury's. However, the division that will handle that is not yet up and running. For this reason, they simply wish to use images that are readily available online showing the video covers. These images are owned by the movie production companies and placed in the public domain for promotion. Banyan videos corp will be purchasing their videos from their main distributors, thus avoiding copyright infringement or legal entanglements.



* Videos film products should also be presented on the site within specific genre or classification for quick search if a customer does not know a specific film title but has an idea of the flavour of film they wish to purchase.


* Various Video products will have discounts applied to members.

* For members, there should be a member's area, where banyan videos will post inside news and features, and watch trailers or any sneek peak teasers posted.

* Banyan videos say that they have a corporate head office (H.O) that will deal with all issues from customers and therefore it is sufficient to have a contacts page that provides a contact form. 

* Finally, they wish website to be up and running in a quick timescale and the overall cost to be small to moderate.


> ## 1. UX ##
 
>a. Strategy
 
Following the project brief and further clarification, I have decided to approach that will facilitate banyan videos requirements in the following way.


* The site will be built using a framework for the benefit of speed. I will implement the site using the Django framework.

* The finished site will be hosted initially on the Heroku platform.I expect the site will be migrated to banyan corporations own hosting service as a future date. 


* Although the Django framework defaults to an SQL-light database, I will utilise the POSTGRES SQL relational database management system (RMDBS) hosted on Heroku.

* In addition using Django will allow me to create the database items in abstracted format (models), therefore if banyan Corporation choose to change databases in the future it will be reasonably easy to implement.

* I am not quite sure of the colour scheme to use yet, as banyan videos left this open-ended, however having seen some of their logo artwork, I will endeavor to use something in a similar style.

* For e-commerce and commerce aspects,  I will  employ "Stripe-Payment" solution. The benefit of this is the security will be strengthened, as user payment credit card (CC)details will be handled completely by the "STRIPE Corporation" and reside within our website architecture. 


<hr>

I have identified users of the site and classify them as:-

|User Type|Ability|
|---------|-------|
|Owner|Banyan Videos Corp - Online Reatiler of fine videos|
|Administrator - level|The administrator will be able create and post material to the site. In addition, there will also be able to populate the site with new products.|
|Customer(Registered) - level|Registered users will have access to browse the site make purchases, have their details on the profile page for speedier purchases, and have the ability to access a member’s page, on which they can post comments to any features set up by banyan videos. Finally, members will have access to discounted prices on products they purchase|
|Customer(Anonymous) - level|An anonymous user, or a new user to the site will have the ability to browse the site and purchase products. However, it will not have the benefit of discounted prices, or access to the members area|

<hr>

**USER STORIES**

Basic user stories suppoted the features

|User| Requirement|So that I can Achieve|
|----|------------|----------------------|
|Owner|I require a sales banner|So that I can present the merits/products/offers of our site to customers|
|Owner|I require the ability to send a file of our products to a site admin| So that they could upload it to the site, and I retain control of the prices and discounts|
|Owner|I require a membership join feature| So I can build a customer base and communicate with customers|
|Owner|I require a membership video/trailer clip ability| So I can offer members vidoe clips and trailers or premium content|
|Owner|I require a membership News/Snippets feature|So I can provide premium content to members|
|Owner|I wish a selective discount feature on products|So that I can give discounts to signed-up Members, thus providing an incentive|
|Administrator|I require a login feature| So that I can login to the site and carry out my tasks|
|Administrator|I require an upload feature/process |So I can update the product database in bulk|
|Customer|I require a feature |So I can update the product database|
|Customer|I require a registration/Login page|So that I can register or login to my account|
|Customer|I require a serach feature|So I can search for products I wish|
|Customer|I require a simple purchase facility|So I can purchase Items|
|Customer|I require a purchase_history|So I can review what I bought and spent|
|Customer|I require a shopping cart feature| So I can add items and pay once I have completed browsing|
|Customer|I wish to register my address & email|So I can receive my order and a confirmation receipt|
|Customer (Anonymous)|I wish purcahse ability without membership|So I can purchase without becomming a member|
|Customer|I wish a credit card payment feature| So that I can pay by credit card|
|Customer|I wish for a contact feature| So that I can mail the company if I have any issues|
|Customer|I require a Logout feature| So I can safely logout of the site|

<hr>

>b. Scope

- Therefore, the scope of the project will involve the following:

- The design and creation of a site to allow banyan videos corporation to post the video assets for purchase by the general public.

- The design will be of a clean and corporate style

- Inital data to support the site. ( These may be replaced by the Banyan Videos Corp to match their catalouge)

**Three specific users have been identified**

* Administrator 

* Registered user
* Anonymous user


>Summary

- The sites will offer discount prices to registered users

- The site will allow new customers membership sign-up

- The site will allow members to access to a member’s section, where they will view members only content

- Members will have the ability to complete a profile page to speed up future transactions.

- Video products on the site will be categorized by genre.

- Visitors to the site can search for products either by genre or by text on a search bar

- The site will be designed [ ** mobile first ** ] and fluid, allowing it to adjust for the you on mobile phones tablets and desktop computers.

- From technical aspects of meeting developement speed, the site will be created user Django framework.

- The database will be the Postgres SQL relational database.

- The administrator will have access the backend for the purpose of pacing a "FILE" containing new products catalouge

- Initially the site will be hosted on the "Heroku platform". It is understood it may be rehosted in the future

- A small demo catalogue of products will be loaded for testing purposes. This will be deleted and replaced by banyan videos corporation

<hr>

> c. Structure
 
DATABASE MODELS

Django uses the concept of models to abstract data-content and data-structure from the "database type".
This is fantastic and it allow the developer to not worry about specificity of databases, and the developer can remain certain it will be easy to port the application to whatever database engine the client requires!


A few database models were created to allow the django web-site to function 

|Model|Purpose|Model Implementation|
|-----|-------|--------------------|
|homepage-models|Frontpage Carousel / Article / Snippets|<img src="_support_docs/images/1-homepage-models.png" width="600">|
|my-account-models|User Profile details / User Purchase History |<img src="_support_docs/images/2-my-account-models.png" width="600">|
|search-results-models|Film Video models / Genre models |<img src="_support_docs/images/3-search-results-models.png" width="600">|
|shopping-cart models-models|shopping-cart models |<img src="_support_docs/images/4-shopping-cart-models.png" width="600">|
|contact-form-models|contact-form models |<img src="_support_docs/images/5-contact-form-model.png" width="600">|
|checkout-form-models|checkout-form models |<img src="_support_docs/images/6-checkout-form-model.png" width="600">|

 <hr>

## * (d). Skeleton

Mockups were created for the various pages required. When They were tried, I wasnt comfortable with them all, So some did change to their final incarnation. I lerant that what looks good on paper does not always translate

| Index.| Page | Mock-up|Final|
|-------|--------|------|-----|
|A|Homepage|<img src="_support_docs/images/banyan-videos-corp-homepage.png" width="200">|<img src="_support_docs/images/home-page.jpg" width="200">|
|B|Login/SignUp|<img src="_support_docs/images/banyan-videos-corp-Login_SignUp.png" width="200">|<img src="_support_docs/images/login-register-page.png" width="200">|
|C|Login page|<img src="_support_docs/images/banyan-videos-corp-Login.png" width="200">|<img src="_support_docs/images/login-page.png" width="200">|
|D|Register page|<img src="_support_docs/images/banyan-videos-corp-Register.png" width="200">|<img src="_support_docs/images/register-page.png" width="200">|
|E|Account profile page|<img src="_support_docs/images/banyan-videos-corp-profile-form.png" width="200">|<img src="_support_docs/images/my_account-page.png" width="200">|
|F|Search Results page|<img src="_support_docs/images/banyan-videos-corp-SearchResults.png" width="200">|<img src="_support_docs/images/search-results-small.jpg" width="200">|
|G|Members Area page|<img src="_support_docs/images/banyan-videos-corp-Members.png" width="200">|<img src="_support_docs/images/members-lounge.png" width="200">|
|H|Contact page|<img src="_support_docs/images/banyan-videos-corp-Contact.png" width="200">|<img src="_support_docs/images/contact-page-form.png" width="200">|
|I|Logout page|<img src="_support_docs/images/banyan-videos-corp-Logout.png" width="200">|<img src="_support_docs/images/logout-page.png" width="200">|
|J|Cart page|<img src="_support_docs/images/banyan-videos-corp-Cart.png" width="200">|<img src="_support_docs/images/shopping-cart-page.png" width="200">|
|K|Payments page|<img src="_support_docs/images/banyan-videos-corp-stripe-payment.png" width="200">|<img src="_support_docs/images/stripe-payment-panel.png" width="200">|
|L|Shipping Details page|<img src="_support_docs/images/banyan-videos-corp-Shipping Details.png" width="200">|<img src="_support_docs/images/shipping-form.png" width="200">|

<hr>


>e. Surface

The colour scheme I finally settled on is as follows. As directed I tried to make it light and airy, clean and simple

|Colour Scheme|
|-------------|
|<img src="_support_docs/images/color-pallet-1of2.png" width="200">|
|<img src="_support_docs/images/color-pallet-2of2.png" width="200">|


> ## 2. Features ##
The website will contain a few features. Some have bee explicitly requested by Banyan Videos Corp (BVC), and the others have been implicitly added as part of the design process

Feature Table

|No.|Feature|Requested|Implicit|Purpose|
|---|-------|---------|------------------|-------|
|1|Carousel on front page|Yes|-|Show selection of video films available|
|2|Search bar|Yes|-|Search for selection of video films available|
|3|Genre Search|Yes|-|Search video films available by genre|
|4|Add Banner|Yes|-|Present cycling promotion messages from BVC|
|5|Right-Side Article block|Yes|-|Present articles from BVC|
|6|Navigation Bar|-|Yes|Navigation Bar Presenting Site Links Uniformally |
|8|Classified Advert Block|Yes|-| A advert block space - holding paid classified adverts|
|9|News Snippets|Yes|-| Provides News Snippets Links -jumpoff to external sources|
|10|Members Sections|Yes|-| Provides members only space containing messages,articles,competitions|
|10|Member Discounts Only|Yes|-| Intrisic facility allowing product discount for members only|


> ## 3. Existing Features ##
Here are the features that has been implemented on the site

|No.|Feature|Implemented|
|---|-------|---------|
|1|Member Discount|<img src="_support_docs/images/member-discount.png" width="400">|
|2|Front Page Carousel|<img src="_support_docs/images/fp-carousel.jpg" width="400">|
|4|Articles|<img src="_support_docs/images/fp-articles.jpg" width="400">|
 


> ## 3. Features Left to Implement ##


* Most of the features expected have been implemented. However for the film models a feied was left for global sales.
The intention was to apply a discount to every item in Banyan Videos catalouge at once. My reasoning was for a flash sale.
having the facility to make that happen would be a plus. However BVC has said tha it is not neccesary at present and it is under consideration. Therefore the model conmtains that option , but it will not be implemented presntly.






 
> ## 4. Technologies Used ##

|Hardware|OS|
|--------|--|
|Apple Mac| - OS Catalina 10.15.7 (19H15)|


|Software Technology|Version|Purpose|
|----------|-------|-------|
|Visual Code Studio|Version: 1.51.1| Developement IDE|
|Terminal|Version 2.10 (433)| CLI interface|
|Monosnap|Version 3.6.21 (November 23, 2020)|Screenshot Capture|
|Just Color Picker|Version 3.6.21 (November 23, 2020)|Color Picker|
|Notepad|Version 1.1 (1.1)|Used to copy search, copy, and replace data segments|
|Google-Chrome-Tools|Version 87.0.4280.67 (Official Build) (x86_64)| Dev and Test|
|Safari|Version 14.0 (15610.1.28.1.9, 15610)|Dev & Test|

<hr>

|Web-Technologies|Version|Purpose|
|----------------|-------|-------|
|HTML| 5.0| Website structure|
|CSS|3.0|Web-page sattelite|
|Bootstrap|4|Helps to structure page & Mobile Firts Design|
|Django Framework|Design Framework Selected for Speed|
|Python|3.x|For backend logic|
|Javascript|Used for bespoke logic ..eg Banner Rotor on home page|
|Fontawsome|4.x|Provides Icons, especially for social media stuff|


<hr>

> ## 5. Testing ##

* The  site has been tested on most of the popular browsers

|Browser|Version|Icon|
|-------|-------|----|
|Safari|Version 14.0 (15610.1.28.1.9, 15610)|<img src="_support_docs/images/safari-icon.png" width="50">|
|Google Chrome|Version 87.0.4280.67 (Official Build) (x86_64)|<img src="_support_docs/images/google-chrome-icon.png" width="50">|
|Opera|Version:72.0.3815.400|<img src="_support_docs/images/opera-icon.png" width="50">|
|Firefox|83.0(64-bit)|<img src="_support_docs/images/firefox-icon.png" width="50">|

* Further testing was carried out 

<hr>







 
> ## 6. Deployment ##




<hr>

>## **Local Install**
The Banyan-Videos-Corp website is a full stack website. A Django framework and Postgres
backed site. The deployment of the site will be in distinct stages

* Clone the Git-Hub Site

* Install "Git" on your local drive, an  ensure it is working

* From the Github * , copy the repo-download-link and paste to a local drive like this

<img src="_support_docs/images/git-clone-link.png" width="300">

**git clone <"copied link">  (return)**

Initialize Git

**git Initialize**

Git will create a clone of the Banyan-Videos-Corp site on ypur local drive.
At this stage you you have a copy of the site on your local computer.
However, we are not done.  The site was developed on a virtual environment( This abstracts the site from its surroundings, helping keep the integrety of all its support files). You will need to 

Initialize this virtual environment (venv) to loaunch the site locally

**source venv/bin/activate**

This will launch the virtual environment. You can confirm this because in the terminal session window
you will have venv in brackets at the begining like so.

**(venv) mac1@mac1s-MacBook-Pro banyan-videos-corp-c**

Your terminmal command line will vary but essentiall look similar

<img src="_support_docs/images/terminal-project-folder.png" width="600">

What you see is the structure of the Django site. The folders individual folders represent the project and Apps of the site, as django philosophy states. Then there are some specific files that are important for the migration of the app to the Heroku platform later...

|Folder|Type|Purpose|
|------|-------|-------|
|_banyanvideos_root|Django project|
|home|app|Homepage|
|about|app|about page of site|
|charge|app|works out the and submits to Stripe Payments Corp|
|Checkout|app|summary of the shopping cart value and presents table |
|contact|app|Contact form for customers to email inquiries|
|contact_sent|app|process payment confirmation|
|delete_from_shopping_cart|app|delete shopping cart item|
|login_register|app|holds both login/register page|
|login_success|app|success on login|
|logout|app|logout logout & confirmation|
|members|app|members page content|
|my_account|app|holds customer profile & purchase history|
|search_results|app|Video film serach results & add to cart button|
|shopping_cart|app| Displays the contents of the shopping cart|
|templates|app| copy of allauth templates|
|venv|virtual environment support| * |
|_support_docs|app| contains images that support this readme file ** can be deleted *|

<img src="_support_docs/images/installed-packages.png" width="400">


**IF YOU LAUNCH THE SITE AND NOTHING SHOWS FOLLOW THE PROCESS BELOW:**
* we need to create the database strcutures by using the django models
- python manage.py makemigrations
- python manage.py migrate


* Finally we need to upload the inital data to populate the models

- python manage.py loaddata **< * JSON FILES>**


|*JSON File|Purpose|
|---------|-------|
|genre|create the genre for the films|
|films|The film product items|
|article|The articles for the sites frontpage|
|frontpagecarousel| The selected images for the frontpage carousel|
|snippet|News snippets and stuff for members area|


**IN THE TERMINAL WINDOW CREATE A SUPER USER ACCOUNT FOR THE SITE**

* python manage.py createsuperuser , and follow the prompts

* This is carried out on a new databse, as it will not have any information. 
* Keep the details secure and safe, as this is the **MASTER account** that will get you into the backend(server-side) of the Django application!

<hr>

 


To lauch the site type

**python3 manage.py runserver  (enter)**


The home page will launch if you open a local browser to 
**http:127.0.0.1:8000** which is a localhost address


<img src="_support_docs/images/banyan-videos-corp-home-page.jpg" width="400">

<hr>

>## **Heroku Install**

The local install works for two reasons
* Django has included by default a database sql-lite-3
* Django has a WSGI compatiable http server inbuilt to its suite

Running the django app on any platform other than a local setup, requires a bit more consideration.
You need to ensure that you hosting platform has 

* A webserver that supports **WSGI** 
* A platform that will run python 
* A database supporting SQL.. ( for this site I have chosen **POSTGRES** as mentioned in the strtegy spec )
* The ability to serve 'STATIC' files**

The **"HEROKU"** platform supports the first two elements, however the fourth ('STATIC' file serving ) requires the installation of a module called 'Whitenoise' to acheive it. You will see whitenoise version 5.2.0 in the pip isntalled modules list


##**Process:**##

**Ensure you have completed the local install!**


* Sign up to **Heroku.com**, and attain an account
* Create a heroku app - "banyan-videos-corp-c"
* Attach a Postgress-db resource

<img src="_support_docs/images/heroku-postgress-db.png" width="400">


* Next setup the Heroku environment variables under the settings tab - ( reveal config vars)

<img src="_support_docs/images/heroku-env-vars.png" width="400">

* The environment variables are what the sysadmin would configure in the background on a hosted server, and would not be available to the user through a http serve. Therefore it is secure.

* The important environment variables are highlighted with the red arrrow.

|Environment Variable|Purpose|
|--------------------|-------|
|DATABASE_URL|The url pointing to the heroku Postgres databse instance|
|DBKEY|The key for the database to logit in|
|DISABLE_COLLECTSTATIC| Stops heroku running a collect static files on compile|
|PRODUCTION| * This key variable django to source its database from sql-lite3(internal) or Heroku Postgres|
|SECRET_KEY|Security key required for the django app to launch|
|STRIPE_PRIVATE_KEY| Provided by stripe.com for transactions|
|STRIPE_PUBLIC_KEY|Provided by stripe.com for transactions|

* It's important to  mention that **the django application like most will depend on the database**. after all all webservers simply serve data.

* Therefore while developing it is possible to not worry so much and use the integrated sql-lite3 database. However that will not usually be possible on a foreign hosting platform. This is the reason **I chose "POSTGRES" database , an SQL - compatiable RDMBS that is available on the HEROKU platform**.

* I use the **"PRODUCTION"** environment variable to tell the APPLICATION uppon lauch to use either the integrated SQL-Lite3 database or the Heroku external( to Django Application ) database using the code below in the settings.py

<img src="_support_docs/images/database-switcher.png" width="400">


Within the filestructure of the local repo, there are two important files

* requirements.txt
* Procfile

* Heroku uses the contents of these to provision the application on heroku. The formert tells Heroku which modules to install and the latter essentially tells Heroku to provision a webserver WSGI compatiable

<img src="_support_docs/images/folders.png" width="200">


* Now follow the Heroku guide and **"use git to uplaod the local repo to Heroku"**

* we need to create the database strcutures by using the django models
- heroku run python manage.py makemigrations
- heroku run python manage.py migrate


* Finally we need to upload the inital data to populate the models

- heroku run python manage.py loaddata **< * JSON FILES>**


|*JSON File|Purpose|
|---------|-------|
|genre|create the genre for the films|
|films|The film product items|
|article|The articles for the sites frontpage|
|frontpagecarousel| The selected images for the frontpage carousel|
|snippet|News snippets and stuff for members area|


**IN THE TERMINAL WINDOW CREATE A SUPER USER ACCOUNT FOR THE SITE**

* python manage.py createsuperuser , and follow the prompts

* This is carried out on a new databse, as it will not have any information. 
* Keep the details secure and safe, as this is the **MASTER account** that will get you into the backend(server-side) of the Django application!




Finally if you send your browser to :

* Your app can be found at **https://banyan-videos-corp-c.herokuapp.com/**

You shoud see your site.

>**WARNING:**
* The site settings promote the view of the site from any host. It is possible in production that you may wish a limited range of access. The ALLOWED_HOSTS = ['*'] settings should be modified and made more specific in that instance.

* DEBUG = False  should be left as is in Production 

* DISABLE_COLLECTSTATIC=0 should be left as 0 in PRODUCTION, allowig static files to be collected and compiled to the project 'static' folder during bootup, otherwise you may recieve a internal '500 server error'


> ## 7. Credits ##



>Code from Stackoverflow - Philip Feldmann */
Keep text from overspilling out of columns */


>**.keep-insideBSol {
    -moz-hyphens: auto;
    -ms-hyphens: auto;
    -webkit-hyphens: auto;
    hyphens: auto;
    word-wrap: break-word;}**


* Video box images - owend by their respective film proruction companies

* ShoppingCart.objects.filter(pk=3).delete() -Milad Khodabandehloo / stack overflow




> ## 8. Content ##
* Some code was taken from the Bootstrap documentation ( Carousel )

* Thanks for the code snippet by Phillip Feldmann which stopped text content escaping the Bootstrap columns. Stop text moving out of bootstrap column - Stack-Overflow - Phillip Feldmann

* software code from stack-overflow - Using nav-fill w-100 with Bootstrap 4 - rav-ram Filling navbar total width - stack-overflow

 
> ## 9. Media ##

* The **site images and data** are hyperlinked, remaining the copyright of their respective owners.
* The images are not copied or stolen from a remote location, but remain within the public domain.
* Screenshots were captured from the **Mac version of Monosnap**

> ## 10. Acknowledgements ##

* Thanks to mentor **Precious Ijeje** for helpful advice
* Thanks to **Student care** for assitance
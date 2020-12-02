# BANYAN-VIDEOS-CORP-C
BANYAN-VIDEOS-CORPORATION-C

 Live Site:
 https://banyan-videos-corp-c.herokuapp.com/


GitHub:
https://github.com/cofoeducistudent/BANYAN-VIDEOS-CORP-C


<img src="_support_docs/images/home-page.jpg" width="500">
<img src="_support_docs/images/banyan-videos-corp-home-page.jpg " width="500">

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



I have identified users of the site and classify them as:-

|User Type|Ability|
|---------|-------|
|Administrator - level|The administrator will be able create and post material to the site. In addition, there will also be able to populate the site with new products.|
|Registered user - level|Registered users will have access to browse the site make purchases, have their details on the profile page for speedier purchases, and have the ability to access a member’s page, on which they can post comments to any features set up by banyan videos. Finally, members will have access to discounted prices on products they purchase|
|Anonymous user - level|An anonymous user, or a new user to the site will have the ability to browse the site and purchase products. However, it will not have the benefit of discounted prices, or access to the members area|



>b. Scope

- Therefore, in summary, the scope of the project will involve the following:

- The design and creation of a site to allow banyan videos corporation to post the video assets for purchase by the general public.

- The design will be of a clean and corporate style

Three specific users have been idenytified

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


> c. Structure
 
## * (d). Skeleton

Mockups were created for the various pages required. When They were tried, I wasnt comfortable with them all, So some did change to their final incarnation. I lerant that what looks good on paper does not always translate

| Index.| Page | Mock-up|
|-------|--------|------|
|A|Homepage|<img src="" width="200">|
|B|Login/SignUp|<img src="" width="200">|
|C|Login page|<img src="" width="200">|
|D|Register page|<img src="" width="200">|
|E|Account profile page|<img src="" width="200">|
|F|Browse page|<img src="" width="200">|
|G|Search Results page|<img src="" width="200">|
|H|Members Area page|<img src="" width="200">|
|I|Contact page|<img src="" width="200">|
|J|Logout page|<img src="" width="200">|
|K|Cart page|<img src="" width="200">|
|L|Payments page|<img src="" width="200">|
|M|Shipping Details page|<img src="" width="200">|

* e. Surface
 


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
|1|Member Discount|<img src="writeup_stuff/feature-member-sale.jpg" width="200">|
|2|Front Page Carousel|<img src="writeup_stuff/Banyan-Videos-corp-feature-carousel.jpg" width="200">|
|3|Classified Ads|<img src="writeup_stuff/Banyan-Videos-corp-classifieds.jpg" width="200">|
|4|Articles|<img src="writeup_stuff/Banyan-Videos-corp -articles.png" width="200">|
 


> ## 3. Features Left to Implement ##







 
> ## 4. Technologies Used ##









 
> ## 5. Testing ##









 
> ## 6. Deployment ##





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

To lauch the site type

**python3 manage.py runserver  (enter)**


The home page will launch if you open a local browser to 
**http:127.0.0.1:8000** which is a localhost address


<img src="_support_docs/images/banyan-videos-corp-home-page.jpg" width="400">


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

The **"HEROKU"** platform supports the first two elements, however the third requires the installation of a module called 'Whitenoise' to acheive it. You will see whitenoise version 5.2.0 in the pip isntalled modules list

First

* Sign up to Heroku, and attain an account
* Create a heroku app 





![name-of-you-image](https://cofoeducistudent/BANYAN-VIDEOS-CORP/clone-github-link.png)

 





> ## 7. Credits ##



* Code from Stackoverflow - Philip Feldmann */
* Keep text from overspilling out of columns */


* .keep-insideBSol {
    -moz-hyphens: auto;
    -ms-hyphens: auto;
    -webkit-hyphens: auto;
    hyphens: auto;
    word-wrap: break-word;}


* Video box images - owend by their respective film proruction companies

* ShoppingCart.objects.filter(pk=3).delete()
-Milad Khodabandehloo
/ stack overflow




> ## 8. Content ##



 
> ## 9. Media ##

The site images and data are hyperlinked, remaining the copyright of their respective owners.

The images are not copied or stolen from a remote location, but remain within the public domain.


> ## 10. Acknowledgements ##

* Thanks to mentor Precious Ijeje for helpful advice
* Thanks to Student care for assitance
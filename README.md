# BANYAN-VIDEOS-CORP-C
BANYAN-VIDEOS-CORPORATION-C

 
 

<img src="writeup_stuff/home_page.jpg" width="600">

## Index ##

> Project Brief

Banyan videos project brief.

Banyan videos corporation has asked for a website but will help them retail their video merchandise online.

For this reason they have provided a brief stating what they would like to see on the site and some features that would definately wish on it.
I would like the slight appearance to be plain and corporate like.

The Front page should have a search facility allowing users to search for products
a carousel showing a selection of film products for sale
on the right-hand side section for news which banyan videos been fit. This will not be an integrated feed to new sites, but a section allowing banyan videos administrators to post corporate messages and news.
On the page there should be an integrated session for classified ads. Banyan videos will sell this space to the public for their ads at a fee
on the bottom half of the screen there should be more article links to other important news on the web. This will have a small title and description, a picture, all linkable to the source material.
The colour theme should be plain and simplistic, and the appearance of the site should be whitish and clean.

The frequency and volume of the products very from small changes to a large influx. Therefore, they wish to have a way of populating the product line very quickly. In the future they wish to have a separate server to serve images for their products, which will have a commercial uniform asset look, like major retailers such as Argos or Sainsbury's. However, the division that will handle that is not yet up and running. For this reason, they simply wish to use images but are readily available online showing the video covers. These images are owned by the movie production companies, and banyan videos will be purchasing their videos from their main distributors, thus avoiding copyright infringement.

Videos products should be presented on the site within specific grouping for genres of film type
Video products should have the ability to have discount added by the administrator of the site
discounts on the products should only be given to people who have signed up and are members to the site. Otherwise people will pay the full price for the video products.
Four members of the site there should be a member's area, where banyan videos will post inside news and features, and allow users to post comments.
Banyan videos say that they have a separate corporate division that will deal with all issues from customers and therefore it is sufficient to have a contacts page that provides an email address for customers to write to. They wish this strategy to be implemented so they can holistically monitor what is going on with the marketing, as they intend to have physical retail stores and online venues.
Finally, they wish website to be up and running in a quick timescale and the overall cost to be small to moderate.


> ## 1. UX ##
 
* a. Strategy
 
Following the project brief and some clarification, I have decided to approach that will facilitate banyan videos requirements.
The site will be built using a framework for the benefit of speed. I will implement the site using the Django framework.

The finished site will be hosted initially on the Heroku	 platform. I expect the site will be migrated to banyan corporations own hosting service as a future date. 

Although Django internally has an SQL light database integrated, I will utilise the POSTGRES relational database hosted on Heroku.

Using Django will allow me to create the database items in abstracted format, therefore if banyan Corporation choose to change databases in the future it will be reasonably easy to implement.

I am not quite sure of the colour scheme yet, as banyan videos left this slightly open-ended, however having seen some of their logo artwork, I will endeavor to use something in a similar style.

For e-commerce commercial aspects all employ strike payment system. The benefit of this is the security will be strengthened, as user payment details will be left to stripe to handle and not resident within four website architecture. So, file

I identified users of the site and classify them as:-

Administrator
the administrator will have the ability to create and post material to the site. In addition, there will also be able to populate the site with new products.

Registered user
registered user will have access to browse the site make purchases, have their details on the profile page for speedier purchases, and have the ability to access a member’s page, on which they can post comments to any features set up by banyan videos. Finally, members will have access to discounted prices on products they purchase

Anonymous user
an anonymous user, or a new user to the site will have the ability to browse the site and purchase products. However, it will not have the benefit of discounted prices, or access to the members area



* b. Scope

Therefore, in summary the scope of the project will involve the following

The design and creation of a site to allow banyan videos corporation to post the video assets for purchase by the general public.

The design will be of a clean and corporate style

The site will cater for free identified primary users
an administrator
a registered user
an anonymous user


The sites will offer discount prices of their products to registered users

The site will allow users to sign up and become members

the site will allow members to post comments in response to articles in a member’s section, for which you will have access to as a member

Members will have the ability to complete a profile page to speed up transactions at future date

Video products on the site will be categorized by genre.

Visitors to the site can search for products either by genre or by text on a search bar

The site will be designed mobile first and fluid, allowing it to adjust for the you on mobile phones tablets and desktop computers.

From the technical aspects, the site will be created user Django framework.
The database will be the PostgreSQL relational database.
The administrator will have access to a CMS backend (which will allow them to add/delete products)
initially the site will be presented to banyan videos corporation on the Heroku platform

A small demo catalogue of products will be loaded for testing purposes. This will be deleted and replaced by banyan videos corporation



 
* c. Structure
 
## * (d). Skeleton

Mockups were created for the various pages required. When They were tried, I wasnt comfortable with them all, So some did change to their final incarnation. I lerant that what looks good on paper does not always translate

| Index.| Page | Mock-up|
|-------|--------|------|
|A|Homepage|<img src="writeup_stuff/banyan-videos-corp-homepage.png" width="200">|
|B|Login/SignUp|<img src="writeup_stuff/banyan-videos-corp-Login_SignUp.png" width="200">|
|C|Login page|<img src="writeup_stuff/banyan-videos-corp-Login.png" width="200">|
|D|Register page|<img src="writeup_stuff/banyan-videos-corp-Register.png" width="200">|
|E|Account page|<img src="writeup_stuff/banyan-videos-corp-Account.png" width="200">|
|F|Browse page|<img src="writeup_stuff/banyan-videos-corp-Browse.png" width="200">|
|G|Search Results page|<img src="writeup_stuff/banyan-videos-corp-SearchResults.png" width="200">|
|H|Members Area page|<img src="writeup_stuff/banyan-videos-corp-Members.png" width="200">|
|I|Contact page|<img src="writeup_stuff/banyan-videos-corp-Contact.png" width="200">|
|J|Logout page|<img src="writeup_stuff/banyan-videos-corp-Logout.png" width="200">|
|K|Cart page|<img src="writeup_stuff/banyan-videos-corp-Cart.png" width="200">|
|L|Payments page|<img src="writeup_stuff/banyan-videos-corp-Payments.png" width="200">|
|M|Shipping Details page|<img src="writeup_stuff/banyan-videos-corp-ShippingDetails.png" width="200">|

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

The Banyan-Videos-Corp website is a full stack website. A Django framework and Postgres
backed site. The deployment of the site will be in distinct stages

* Clone the Git-Hub Site

* install Git on your local drive, an  ensure it is working

* From the Github site * , copy the link and create a local repo

![name-of-you-image](https://cofoeducistudent/BANYAN-VIDEOS-CORP/clone-github-link.png)

 
> ## 7. Credits ##

* Code from Stackoverflow - Philip Feldmann */
* Keep text from overspilling out of columns */

* .keep-insideBSol {
    -moz-hyphens: auto;
    -ms-hyphens: auto;
    -webkit-hyphens: auto;
    hyphens: auto;
    word-wrap: break-word;
* }
 
> ## 8. Content ##



 
> ## 9. Media ##

The site images and data are hyperlinked, remaining the copyright ogf their respective owners.
The images are not copied or stolen from a remote location, but remain within the public domain.


> ## 10. Acknowledgements ##

Thanks for mentor Precious Ijeje for helpful advice
<h1>Flavors from Home</h1>
<h1>Fullstack Development Milestone Project</h1>

<h1>Testing</h1>


## User Experience (UX)

## User stories testing

### First Time visitor
As a First Time Visitor, I want to:
* Be able to tell the purpose of the website.
    * The header that reads "Discover Tasty Treats" announces that the website provides food related products. About section in the footer also fulfill the purpose of informing the user about the company.
* Experience smooth navigation through content.
    * A practical fixed positioned navbar that collapses into a burger button for small screens fulfill this purpose.
    * Website's header will take the user to the home page, aswell as the "home" anchor. 
* Browse products.
    * Search bar allows the users to query the database with keywords.
* View a list of products to purchase.
    * Navigation menu displays the different category dropdowns for the user to choose and display.
* Have access to product details.
    * Each product in the products page redirects to its individual product details page, where users can read about the product, rate it, review it, buy it or add it to the wishlist.
* Easily view the total of my purchases at any time
    * The bag link on the fixed navbar updates the total price with each addition.


### Returning visitor
As a Returning Visitor, I want to:
* Easily register for an account.
    * In the account link, if not logged in, the users will be able to find the registration link, which will take them to the registration page where they can choose an username, email and password.
* Receive email confirmation after registering.
    * The website will send and email to the user to confirm the data provided.
* Have a personalized user profile.
    * Each user has access, through his profile page, to their individual (updatable) shipping information and order history. 
* See new products and updates.
    * As a future feature, new products and deals will be added.
* Have a personal wishlist to store products for future orders.
    * Each user has access, through the wishlist page, to save products for future orders. Users can also remove items from the wishlist or access each product details.


### Frequent user
As a Frequent User, I want to:
* Quickly recover my password in case I forget it.
    * In the loggin page, users will be able to see the button "Forgot Password?" They will be ask to fill the email field and will receive a password reset email with a link to the password reset page.
* Easily log in and log out of the site.
    * In the account dropdown user will be able to use this functionality.
* * Have control over my shipping information. (CRUD)
    * Users can update or erase their shipping information in their profiles.
* Be able to see previous orders summaries.
    * Users can see their order history in their profiles.
* Be able to sort products.
    * Each products page, filteres by any queries, allows users to sort items by name, price, rating or category.
* Be able to search for specific product names.
    * Search bar allows the users to query the database with keywords.
* Rate and comment on products.
    * In the product details page, users can review an rate any product.
* Easily see what I've searched for and the number of results.
    * In the product page, on the top of the page, it's displayed the query and product count.
* Easily select quantity of a product when purchasing it.
    * When purchasing a product, quantity can be adjusted either from the product detail page or from the bag page.
* View items to be purchased in my bag.
    * Users can check their bags at any time through the bag link.
* Easily enter my payment information.
    * The checkout page presents an easy to fill shipping form, that will be auto-completed if the user has registered his information in the profile.
* Feel my personal and payment information is secure.
    * Stripe is used to handle all credit card transactions. 
* View an order confirmation after checkout.
    * An order confirmation will be displayed after checkout in the checkout success page.
* Receive an email confirmation after checkout.
    * An email will be sent to the user after a successfull checkout.

### Store owner
As a Store Owner, I want to:
* Be able to add new products.
    * Add product form is accessible only to admins through the product management link in the profile.
* Edit or update product details.
    * Admins can access the Edit Product page through the edit button in each individual product details page
* Delete products when necessary.
    * Admins can delete any items, either from the products page or from the product details page. 
* All previous functionality for admins also available in the django admin console.

<hr>

## Functionality Testing
##### -- (Check = Working as expected) -- 

### base.html / main-navbar.html / mobile-top-header.html / home.html / footer.html

* Wishlist button redirects to wishlist.html - Check
* Bag button redirects to wishlist.html - Check
* Shop now button redirects to products.html - Check
* Category buttons open dropdowns - Check
* Clicked header to ensure that it redirects to home page - Check
* Clicked header inside burger menu to ensure that it redirects to home page. (mobile) - Check
* Links in each subcategory redirects to products/category - Check

* ![home-html.png](/media/home-html.png)

* Links in categories footer redirects to products/category - Check
* Contact link in footer redirects to contact.html - Check
* Social media links redirects to their respective websites - Check
* ![footer-html.png](/media/footer-html.png)

* Tested search bar, displaying number of results and query - Check

* ![query.png](/media/query.png)

### Products

* Clicked products home link - Check
* Clicked individual product links - Check
* Sorted products - Check
* Clicked update product - Check
* Delete product - Check

* ![products-html.png](/media/products-html.png)

### Product Details

* Quantity selector working as expected - Check
* Star rating updates with new reviews - Check
* ![pd-html.png](/media/pd-html.png)
* Clicked every button, redirects properly - Check
* ![pd2-html.png](/media/pd2-html.png)
* Delete button has defensive modal - Check
* ![pd3-html.png](/media/pd3-html.png)
* Delete button has defensive modal - Check

### Add/Edit Products

* Form validation working - Check
* ![manage-html.png](/media/manage-html.png)
* Clicked all buttons - Check
* Items created/updated successfully - Check

### Wishlist

* Product Details button redirects to product details page - Check
* Remove from wishlist button removes item from wishlist - Check
* Category badge redirects to products/category - Check
* ![wishlist-html.png](/media/wishlist-html.png)

### Profile

* Order history displaying - Check
* Update shipping information form working - Check
* ![profile-html.png](/media/profile-html.png)

### Bag

* Remove and update buttons - Check
* Keep shopping button redirect to products page - Check
* Secure checkout button redirects to checkout page - Check
* ![bag-html.png](/media/bag-html.png)

### Checkout

* Form validation fully functional - Check
* ![checkout-html.png](/media/checkout-html.png)
* Confirmation email sent to user - Check
* ![checkout2-html.png](/media/checkout2-html.png)
* Adjust bag button redirects to bag page - Check
* Complete order starts the payment with stripe - Check
* Payment succeded in stripe events - Check
* ![checkout3-html.png](/media/checkout3-html.png)

### Checkout Success

* Back to profile button redirects to profile - Check 
* Keep shopping button redirects to products - Check

### Contact Form

* Form validation fully functional - Check
* ![contact-html.png](/media/contact-html.png)

* Submit button sends message and redirects to contact success page - Check
* ![contact2-html.png](/media/contact2-html.png)

* Store receives user inquiry by mail- Check

### Allauth templates, 404.html, 500.html, toasts

* Clicked all buttons, redirect successfully - Check
* Form validation fully functional - Check


### Known bugs

* Quantity selector in bag.html allows users to go under 0 in desktop resolutions. Is not a detrimental fix, but it would improve ux.
* Image set warning in add/edit product will only appear under one image input.



### Code Validation

* ![Valid HTML!](/media/valid-html.png) HTML has been validated by [W3C validator](https://validator.w3.org/)

* ![Valid CSS!](/media/valid-css.jpg) CSS has been validated by [Jigsaw validator](https://jigsaw.w3.org/css-validator/)

### Responsiveness
The responsiveness of the website has been tested with Chrome Developer Tools and Chrome Responsive Viewer.
* Fully responsive on all tested devices - Check--------------------------------------------
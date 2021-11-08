<h1>Flavors from Home</h1>
<h1>Fullstack Development Milestone Project</h1>

![responsive-mockup](/media/responsive-design.jpg)

This project consists of a ecommerce website for company Flavors from Home; where users can browse, discover and buy traditional argentinian products in Europe. 

Check out the [Live Project](https://flavors-from-home.herokuapp.com/) here!

#### Disclaimer
Flavors from Home online store does not exist. The creation of this project is purely educative. 
<hr>

## User Experience (UX)

## User stories

### First Time visitor
As a First Time Visitor, I want to:
* Be able to tell the purpose of the website.
* Experience smooth navigation through content.
* Browse products.
* View a list of products to purchase.
* Have access to product details.
* Easily view the total of my purchases at any time


### Returning visitor
As a Returning Visitor, I want to:
* Easily register for an account.
* Receive email confirmation after registering.
* Have a personalized user profile.
* See new products and updates.
* Have a personal wishlist to store products for future orders.


### Frequent user
As a Frequent User, I want to:
* Quickly recover my password in case I forget it.
* Easily log in and log out of the site.
* Have control over my information.
* Be able to see previous orders summaries.
* Be able to sort products.
* Be able to search for specific product names.
* Rate and comment on products.
* Easily see what I've searched for and the number of results.
* Easily select quantity of a product when purchasing it.
* View items to be purchased in my bag.
* Easily enter my payment information.
* Feel my personal and payment information is secure.
* View an order confirmation after checkout.
* Receive an email confirmation after checkout.

### Store owner
As a Store Owner, I want to:
* Be able to add new products.
* Edit or update product details.
* Delete products when necessary.

<hr>

### Strategy

#### Project Goals 
To allow argentinians living abroad to experience familiar flavors, hoping to alleviate that homesick feeling with some tasty traditional treats.
 
#### Developer Goals: 
 To showcase an attractive, well-designed django based python application that's easily updated and maintained.

<hr>

### Scope 

#### Features
* The project is presented in a multi-template layout, based on django and controlled by python on the backend.
Rendered templates customized with HTML5, CSS3, Javascript.
* Fully responsive on different screen sizes.
* It counts with a contact form.
* Full CRUD functionality. (Create, Read, Update and Delete products)
* Credit card payments with Stripe
* Wishlist 
* User reviews

#### Features by page

* Logo 
    * Presents the brand “Flavors from Home”. If the user clicks on the logo, it will return the users to the “Home” section.

* Navbar
    * Search input bar, that allows the users to filer content by keywords.
    * Categories links, that automatically filter products by the selected category.
    * Wishlist button, redirects the users to their wishlist or the log in page if user's not logged in.
    * Account button, open dropdown with user options. 
        * If logged out (log in / register).
        * if logged in (my profile, logout).
        * If admin logged in (my profile, logout, product management).
    * Bag button, redirects the users to their bag page.

Navbar collapses into a burger button in small resolutions.

* Footer
    * About Flavors from Home section, with a short paragraph explaining the purpose of the website.
    * Categories links, that automatically filter products by the selected category.
    * Quick links, where users can access the contact form (and other future features)
    * Copyright information.
    * Social media links to instagram, facebook and pinterest.
    * Back to top buttons. Only on pages that require it.

* Home page:
    * Landing page with the company banner and a big action button to guide the user into browsing the products.

* Products:
    * Grid display with product's pictures, names and rating for each, as well as links to individual product details.

* Product Detail:
    * Carousel of images for each individual product. The product details page displays name, price, rating, description, brand information, action buttons and reviews from other users.
    * Users can add a product to the shopping cart.
    * Users can add a product to the wishlist.
    * Admins can edit a product.
    * Admins can delete a product.
    * Users can write a review.
    * Users can read other users reviews.

* Add Review Page:
    * Simple form where users can set a title, rating and review content.

* Add Product Page:
    * Simple form where admins can enter new products information and pictures.

* Edit Product Page:
    * Simple form where admins can update products information and pictures.

* Profile:
    * Users can update their shipping information.
    * Users can check their order history.

* Wishlist:
    * If not ready to but it, users can add a product to their wishlists, saving a record for future orders.

* Bag:
    * On this page users can view all the selected products for purchase. 
    * Users can update the quantity.
    * Users can remove products from their bag.
    * There is a button link to a checkout page for the final step of shopping.
    * The order total, delivery cost and Total cost is displayed.

* Checkout
    * Users can enter their information to process their order. 
    * User can see an order summary.
    * Adjust bag button to go back to bag if they want to modify it.
    * Complete order button that will submit the checkout form and start the payment process.

* Checkout Success (checkout_success.html) 
    * Summary of the successful order
    * Back to profile button redirects users to profile page, where they can see the updated orders history.
    * Keep shopping button redirects users to the products page.

* Login Page
    * Simple log in form where the user can enter either their username or their email address and their password.
    * The user will receive validation or error feedback when they enter information in the input field.
    * Link to registration page if user does not have an account.
- The page where users can log in to the website and access the Profile page to see their user info, delivery info and order history
- The form with built-in functionality is created with the Django Allauth package.

* Registration Page
    * Simple registration form, where the user can input a username, email address and password.
    * Link to login page if user have an account.

* 404 & 500 Pages
    * The custom 404 & 500 Pages explains the user that they have encountered an error. Get back home will take them to the home page.


<hr>

### Skeleton
For the low fidelity wireframes, Figma software has been used to lay out the foundations of the website.

* [Mobile Wireframes](https://www.figma.com/file/DvtZaopG5Rk2rmlRjq2rjd/FLAVORS-MOBILE?node-id=0%3A1)
* [Tablet Wireframes]()
* [Desktop Wireframes](https://www.figma.com/file/x6ghJZi3aYCT4i1lB1MjAc/FLAVORS-DESKTOP?node-id=0%3A1)

### Surface

<hr>

#### Color Palette
![palette](/media/palette.png)

The fonts are:
* Milonga. Stylized as the traditional "fileteado porteño", this font is a homage to the silver river culture. Thousands of signs with this calligraphic style can be found in the streets of Buenos Aires.
* Montserrat. A more traditional font to improve readability of content.

<hr>

## Technologies

### Languages

* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Other Technologies
* [Bootstrap5](https://getbootstrap.com/) 
    * Structure of the website.
* [Heroku](https://en.wikipedia.org/wiki/Heroku)
    * Cloud platform service.
* [Jquery CDN](https://code.jquery.com)
    * Javascript.
* [W3Schools](https://www.w3schools.com/)
    * CSS documentation.
* [Figma:](https://figma.com/)
    - Figma was used to create the wireframes.
* [GitHub:](https://github.com/)
    * Code repository.
* [Gitpod](https://gitpod.io/)
    * Gitpod was used as IDE and for version control. 
* [Font Awesome:](https://fontawesome.com/)
    * Font Awesome was used solely for social media icons in footer.
* [Google Fonts:](https://fonts.google.com/)
    * Google fonts was used to import "Montserrat" and "Lora" family fonts.
* [Chrome Developer Tools:](https://developers.google.com/web/tools/chrome-devtools)
    * Used to debug and style.
* [Coolors:](https://coolors.co/)
    * Color palette.
* [Django](https://www.djangoproject.com/) 
    * Framework for Python.
* [SQLite](https://www.sqlite.org/index.html) 
    * Database in development mode.
* [PostgreSQL](https://landing.aiven.io/en/aiven-for-postgresql/) 
    * Database in production mode.
* [Stripe](https://stripe.com/en-ie) 
    * Credit card payment.
* [AWS](https://aws.amazon.com/) 
    * Hosting static files and images for the website.

## Tools

* [Gitpod](https://www.gitpod.io/)
    * Integrated Development Environment (IDE)
* [Git](https://git-scm.com/)
    * Local version control.
* [GitHub](https://github.com/)
    * Remote version control.
* [Heroku](https://www.heroku.com/)
    * Deployment.
* [W3C Markup Validator](https://validator.w3.org/) 
    * HTML code validation.
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) 
    * CSS code validation.
* [JSHint Validator](https://jshint.com/)   
    * Detecting errors and potential problems in JS files.
* [Link Checker](https://validator.w3.org/checklink) 
    * Checking all links on the website.

<hr>

## Testing

__[Click here to read testing documentation.](testing.md)__

<hr>

## **Deployment**
This project uses GitHub for version control, GitPod as the cloud-based IDE and Heroku to deploy the site into production. Heroku Postgres is used for the database. [AWS services](https://aws.amazon.com/), which is also a cloud-based platform, is used to store static files and images as Heroku has [no files system to store new files]().

The below steps are specific to Gitpod therefore depending on your IDE, you might need to adjust the below steps. 

### To clone the project:
From the application's repository, click the "code" button and download the zip of the repository. Alternatively, you can clone the repository using the following line in your terminal: 
```
git clone https://github.com/jjlg90/flavors_from_home
```

#### To install required software:
While you are still in the terminal, type pip3 install -r requirements.txt, this will install all the required softwares to run the project:
```
pip3 install -r requirements.txt
```

#### Set up an enviroment for variables
You now need to set up the database with environment variables. Create a file titled env.py and make sure it is placed in the of this file structure, on the same level as the app.py file. You can also add these in your workspace variable section. 

Option 1: Env.py file:
```
 os.environ.setdefault('SECRET_KEY', '<your_variable_here>')
 os.environ.setdefault('DEVELOPMENT', 'True')
 os.environ.setdefault('STRIPE_PUBLIC_KEY', '<your_variable_here>')
 os.environ.setdefault('STRIPE_SECRET_KEY', '<your_variable_here>')
 os.environ.setdefault('STRIPE_WH_SECRET_CH', '<your_variable_here>')
 os.environ.setdefault('STRIPE_WH_SECRET_SUB', '<your_variable_here>')
 ```
- In ` settings.py`  add:
```
if os.path.exists("env.py"):
    import env
```
-  Add your env.py file to `.gitignore`, before pushing your changes.


<br>Option 2: Workspace Variables:
```
KEY = 'SECRET_KEY', VALUE = '<your_variable_here>'
KEY = 'DEVELOPMENT', VALUE = 'True'
KEY = 'STRIPE_PUBLIC_KEY', VALUE = '<your_variable_here>'
KEY = 'STRIPE_SECRET_KEY', VALUE = '<your_variable_here>'
KEY = 'STRIPE_WH_SECRET_CH', VALUE = '<your_variable_here>'
KEY = 'STRIPE_WH_SECRET_SUB', VALUE = '<your_variable_here>'
KEY = 'AWS_ACCESS_KEY_ID', VALUE: '<your_variable_here>'
KEY = 'AWS_SECRET_ACCESS_KEY', VALUE: '<your_variable_here>'
KEY = 'USE_AWS', VALUE: 'True'
 ```

- In ` settings.py`  add:
 ```
 SECRET_KEY = os.environ.get('SECRET_KEY', '')
 ```

#### DEBUG 
```
DEBUG = 'DEVELOPMENT' in os.environ
```

### **Heroku Deployment**
- Go to the [Heroku](https://www.heroku.com/) website. Register for an account and click on "Create a new app".
- Setup a Heroku app within the Heroku dashboard - Type in the app name and select region the click on create app.
- In Heroku, in your app, click on "GitHub" to connect to your repository. Type in the repository name as on GitHub. Click on "Connect".
- Search for your repo (or sign in and connect GitHub account) and select this.
- Then click "Hide Config Vars" in Heroku.
- Go to the resources tab and search for Heroku Postgres. Choose the “hobby dev - free” option and submit the order form.
- On the `settings.py file`, you will need to comment out the 'SQLite and Postgres databases' section and uncomment the 'PostgreSQL Database' section. (this is temporary, nothing should be pushed/committed just yet).
- Add the database URL from Heroku & migrate your models to the PostgreSQL database with: 
    ```
    python3 manage.py migrate
    ```
- Create a superuser with the following command, and fill in the required information.:
    ```
    python3 manage.py createsuperuser
    ```
- In the `settings.py` file, you can now delete the 'PostgreSQL Database' section and uncomment the 'SQLite and PostgreSQL Databases' section. This means that either database can now be used interchangeably.
- Install gunicorn and freeze that to the requirements file with the following commands:
    ```
    pip3 install gunicorn
    pip3 freeze --local > requirements.txt
    ```
- Create a Procfile and inside, add the following:
    ```
    web: gunicorn flavors_from_home.wsgi:application
- In `settings.py`, use an if statement so that when the app runs on Heroku, you will connect to Postgres, and otherwise, it will connect to sqlite3, like so:
    ```
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
    ```
- Copy the variables from the variable enviroment one by one into the heroku config vars. They would be:
   ```
    KEY: 'SECRET_KEY', VALUE: “your_variable_here”
    KEY: 'DEVELOPMENT', VALUE: "True"
    KEY: 'STRIPE_PUBLIC_KEY', VALUE: "your_variable_here"
    KEY: 'STRIPE_SECRET_KEY', VALUE: "your_variable_here"
    KEY: 'STRIPE_WH_SECRET_CH', VALUE: "your_variable_here"
    KEY: 'STRIPE_WH_SECRET_SUB', VALUE: "your_variable_here"
    KEY: AWS_ACCESS_KEY_ID, VALUE: "AWS access key ID"
    KEY: AWS_SECRET_ACCESS_KEY, VALUE: "AWS secret access key"
    KEY: USE_AWS, VALUE: "True"
    ```
- Login to Heroku in the CLI and temporarity disable collectstatic, with the following command:
    ```
    heroku config:set DISABLE_COLLECTSTATIC=1 --app flavors_from_home
    ```
- Add your Heroku app and local host to allowed hosts in `settings.py.`
- Push to Github, and then to Heroku master. 
- In Heroku, go to the 'Deploy' tab. In the section 'Deployment Method' click on 'Github - Connect to Github'. Make sure your Github profile is displayed. Add the repository name and click on 'Search'. After Heroku has found the repository, click on 'Connect'. This will connect your Heroku app to your GitHub repository. Click 'Enable automatic deploys'. Your code will automatically be deployed to Heroku as well. 

### **AWS (Amazon Web Services)**
Create an account with [AWS](www.aws.amazon.com), follow the steps and sign in. 
- Go to the AWS management console and go to the S3 service. There, create a new bucket. Uncheck 'block all public access' and acknowledge that the bucket will be public.
- Go to the buckets properties, and turn on static website hosting. Select 'Use this bucket to host a website', and fill in index.html and error.html, then click 'save'.
- Go to the permissions tab, and go to CORS configuration. Paste in a CORS configuration:
```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
- Go to the Bucket policy tab and click 'policy generator', to create a policy. Choose 's3 bucket policy', allow all principals by typing a star. From the action dropdown menu select 'GetObject'. Copy the ARN and paste it into the ARN box. Then click 'add statment' and then click 'generate policy'. Copy the policy into the bucket policy editor. Add a slash star onto the end of the resource key. Click 'save'. 
- Go to access control list tab, under public access, click on 'Everyone', select 'List Objects'. Then click 'save'. 
- Go to IAM (from services menu), click on 'groups' and create a new user group. Give the group a group name (f.e. 'manage-flavors-from-home'). Then click 'create group'. 
- Click 'policies' in the dashboard, and then click 'create policy'. Go to the JSON tab. Click 'import managed policy'. Import 'AmazonS3FullAccess'. Get the bucket ARN from the bucket policy page in S3, and paste that in after 'Resource', as a list (first the ARN, then also the ARN with a slash and star). Click 'next tags' and then 'next review'. Give it a name and description. Click 'create policy'. 
- Go to 'groups'. Click the manage-flavors-from-home group. Go to 'permissions'. Click 'attach policy'. Select the policy you just created. Click 'add permissions' and then 'Attach policy'.
- Go to 'users'. Click 'add user'. As username write 'flavors-from-home-staticfiles-user. Give programmatic access. Click 'next'. Add the user to the group. Click through to the end. Download the .csv file. 

### **Connecting to DJANGO to S3**
- Go back to GitPod. Install boto3 and Django storages, and freeze them to the requirement file with the following commands:
    ```
    pip3 install boto3
    pip3 install django-storages
    pip3 freeze > requirements.txt
    ```
- Add 'storages' to the installed apps in the settings.py file.
- Add the following if statement:
    ```
    if 'USE_AWS' in os.environ:
        AWS_STORAGE_BUCKET_NAME = 'flavors-from-home'
        AWS_S3_REGION_NAME = 'eu-west-1'
        AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
        AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    ```
- On Heroku, add the AWS keys to the Config Variables (they can be found in the csv file you downloaded earlier). Also, add USE_AWS and set it to True. 
- Remove the DISABLE_COLLECTSTATIC from the variables. 
- In GitPod, create a file called custom_storages.py and add:
    ```
    from django.conf import settings
    from storages.backends.s3boto3 import S#Boto3Storage

    class StaticStorage(S3Boto3Storage):
        location = settings.STATICFILES_LOCATION


    class MediaStorage(S3Boto3Storage):
        location = settings.MEDIAFILES_LOCATION 
    ```
- To the before mentioned if statement from above, in settings.py, also add:
    ```
        STATICFILES_STORAGE = 'custom_storages.StaticStorage'
        STATICFILES_LOCATION = 'static'
        DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
        MEDIAFILES_LOCATION = 'media'

        STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
        MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
    ```
- Add, commit and push these changes. If you now go to the bucket, you will see all the static files. 
- Go to your bucket and add a new folder called media. Inside it, click 'upload' and then 'add files'. Then select all the images you'd like to use. Click 'next'. Under 'manage public permissions', select 'grant public read access'.
- On Stripe, add a new webhook endpoint, with the URL of your Heroku app, followed by 
```/checkout/wh/```. Select 'receive all events' and click 'add endpoint'.

___
<br>
<hr>

## Credits and Acknowledgements

* Home Banner created by artist Romina Storino [Check out her Instagram!](https://www.instagram.com/rominastorino_filete/)

* Boutique Ado project, by Code Institute. Followed walkthrough to prevent errors. The code served as base structure for this project.

* Concept, images and descriptions were taken form [Pampa Direct](https://pampadirect.com/), an american online retailer.

* From Slack, queries by users Eldowling and Harry-Leepz saved me a lot of development time.

* My mentor, Anthony Ugwu, who guided me through development.
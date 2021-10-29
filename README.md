<h1>Flavors from Home</h1>
<h1>Fullstack Development Milestone Project</h1>

![responsive-mockup](/static/images/doc-img/responsive-mockup.png)

This project consists of a ecommerce website for company Flavors from Home; where users can browse, discover and buy traditional argentinian products in Europe. 
Check out the [Live Project](https://wild-argentina.herokuapp.com/index)

#### Disclaimer
Flavors from Home online store does not exist. The creation of this project is purely educative. 

## User Experience (UX)

## User stories

### First Time visitor
As a First Time Visitor, I want to:
* Be able to tell the purpose of the website.
* Experience smooth navigation through content.
* Read content that is relevant and concise. 
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
  
 ### Strategy

 #### Project Goals 
 To provide WILD ARGENTINA with a presentation website, where its users can can browse, discover and share experiences.
 
 #### Developer Goals: 
 To showcase an attractive, well-designed flask based python application that's easily updated and maintained.

### Scope 

#### Features
* The project is presented in a multipage layout, based on django and controlled by python on the backend.
Rendered templates customized with HTML5, CSS3, Javascript.
* Fully responsive on different screen sizes.
* It counts with a contact form.
* Full CRUD functionality. (Create, Read, Update and Delete products)

#### Future Features

### Structure 

#### Information
 The content is distributed throughout several pages.

* Home page:
    * 
* Products:
    * 

* Product Detail:
    * 
 
* Profile:
    * 

* Wishlist:
    * 

* Bag:
    * 

### Skeleton
For the wireframes, Figma software has been used to lay out the foundations of the website.

[Wireframes]()

### Surface
 The content is easy to navigate and is neatly divided in sections.

 The colour palette is dark, looking to highlight the brightness of the images to attract attention to them. 

![palette](/static/images/doc-img/colors.png)

The fonts are:
* Milonga. 
* Montserrat. 


## Technologies

### Languages

-  [HTML5](https://en.wikipedia.org/wiki/HTML5)
-  [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-  [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
-  [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Other Technologies

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

## Testing

__[Click here to read testing documentation.](testing.md)__

## Deployment

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/jjlg90/flavors_from_home)
2. At the top of the Repository, just above the "Settings" button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/jjlg90/flavors_from_home)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/jjlg90/flavors_from_home
```

7. Press Enter. Your local clone will be created.

### Connecting to MongoDB
1. Log in to MongoDB.
2. Within the "Cluster1" tab selected, click on "Connect".
3. Select "Connect your application".
4. Select _Python_ version 3.6 or later.
5. Copy _connection string_ and then paste it to env.py
6. Create an instance of PyMongo and pass the application to that instance.
* Like:  `mongo = PyMongo(app`)

### Heroku Deployment

Preparing Local workspace for Heroku:
1. Create *__requirements.txt__*  file.
CLI: `pip freeze --local > requirements.txt`

2. Creating *__Procfile__* file.
Type in file `web: python app.py` and save.

Create Heroku application:
1. Log in Heroku.
2. Click `New` button. 
2. Select `Create a new app`.
3. Enter the app name.
4. Select region.
5. Under `Settings`, __click__ `Config Vars` to add Configuration Variables from the env.py file.
6. In your CLI install Heroku by typing `npm install -g heroku`  
7. Select `Deploy` option.
8. Under `Deployment method` select the __GitHub__ option.
9. Select Automatic deploys from the main branch and select `Deploy Branch`.
10. Click `Open App` button located in the top-right corner of your Heroku account.

## Credits

#### Media
Pictures and videos were taken from the following websites.

### Acknowledgements

* My Mentor 
* [Stack Overflow](https://stackoverflow.com/) helped me to find answers about structure and styling from other people's inquiries, posts and threads.

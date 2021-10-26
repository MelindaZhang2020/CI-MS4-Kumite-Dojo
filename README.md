# Kumite Dojo

Karate practice strengthens the mind, it teaches "Mentality over technique".

Having tried shotokan karate myself, I can say that it is a fantasic sport! It not only strengthens your body but also your mind and spirit.

My Sensei Seamus O'Dowd is a 6th Dan black belt. He has been teaching Karate for over two decades. His students are all over the world. Since 2018, he decided to give up his job and teach Karate full time in his Dojo in Stamullen Co.Meath.

This website is a mockup site designed for Sensei Seamus's Dojo.

## [Live site](CI-MS4-kumite-dojo.heroku.com)

## [Contents](#contents)

[UX](#ux)

- [User stories](#user-stories)

- [Design](#design)

- [Wireframes](#wireframes)

[Database Model](#database-model)

[Features](#features)

- [Existing Features](#existing-features)

- [Features Left to Implement](#features-left-to-implement)

[Technoloies Used](#technologies-used)

[Testing](#testing)

[Deployment](#deployment)

[Credits](#credits)

## **UX**

### **Overview**

As an user/potential learner, there are a few things they would like to find out. For example, the history of the dojo,about the instructors, what kinda martial arts classes does the dojo provide. And the class timetable.

### **User stories**

#### **Overall user expectations**

- Easy to navigate

- Intutitive

- Responsive

- Secure

- Visually pleasing

|As a...  |I want to... |So I can... |
|-----|---|---|
| Potential Student  | Immediately understand the purpose of the site | Decide whether to stay or leave  |
|   |  Know the background of the Dojo | So I have a brief idea about the dojo  |
|   | Find out who the instructor is | Decide if I want to train with him/her |
|   | Find out what kind of classes are avaliable  |  Understand what kind of martial arts are taught here |
|   | Find out the class schedule | See if the timetable matches mine  |
|   |Easily browse through the cost of membership  | Learn how much it cost and decide whether to join |
|   | Browse through the shop  | Purchase products  |
|   | Add items to my shopping bag before registering |  Avoiding registering if not neccessary |
|   | Search classes and products by name  |  Find specific class or products |
|   | Choose clothes and belts size   | Customise purchases to my preference  |
| Registered User  |  Save my default delivery details | Proceed to checkout more quickly in the future   |
|   | View my previous purchases  | Make repeat order  |
|   | Review my shopping bag prior to checkout  | Remove/Adjust quantities  |
|   | Recieve confirmation of my orders  | Have proof of purchase  |
|   | Recieve free delivery above an order threshold  |  Feel rewarded for larger purchases |
| Site Owner  | View, add, edit and delete products  | Keep the product list up to date  |
|   |  Have a simple payment system | Easily make changes for all products  |

### **Design**

#### **Color Scheme**

The main color scheme of this project is grey, white, black and red as it is Shotokan Karate logo's main color scheme. The following is the color pallatte:

![color-pallatte](static/img/color-scheme.png)

#### **Hero Images**

The hero images slides I have chose to use in the home page is mainly black and white with a soft tone to it. So it goes well with the overall color scheme.

#### **Fonts**

[Lato](https://fonts.google.com/specimen/Lato?query=lato#about) - Lato is a sans serif typeface family it gives the website a soft generic feel.

[Gemunu Libre](https://fonts.google.com/specimen/Gemunu+Libre?query=Gemunu+Libre#about) - I chose this font for the navbar as it gives the feeling of old and traditional.

[Grechen Fuemen](https://fonts.google.com/specimen/Grechen+Fuemen?query=Grechen+Fuemen#about) - I used this font for the main logo because I think it looks a little bit like Japanese writing.

### **Wireframes**

Wireframes created at the start of the project for mobile and desktop can be accessed [here.](wireframes/wireframe.md)

There were some deviations from the plan due to time constraints. There were:

- Not including a product review system.

- Not including a wishlist due to the complexity of implementing Ajax.

- Not including a pagination .
[Back to contents](#contents) ⬆️

## **Database Model**

A relational database is best suited to this project given the number of relationships between the models. SQLite was used during development and Heroku Postgres in production. The diagram below may help visualise the database and relationships between each model.

![database-schema](static/img/database-schema.png)

### **Key Models**

#### **UserProfile**

- Created on registration for each user, holds user information that can be used to speech checkout process.

- Stores order history for previous orders to encourage repeat order.

#### **Product**

- Holds the infomation about a product includes name, description, price, stock counts and rating.

- The foreign key to ProductImage is very important as it allows multiple images attach to this particular product.

- Similar to ProductImages, the variation foreign key relationship between Product and Variation is crutial. As it gives different product its individual unique sizes and colors.

- The relationship to Category is descriptive.

#### **ProductImage**

- This models stores multiple images for each product. Which is ideal in real life scenario, a product is more than likely has more than one image attach to it. Also gives the user a better user experience.

#### **Variation**

- This model allows us to give each product a different variation regardless the category/value. In my case, I was able to give the products different colors and sizes.

#### **Category**

- This model divide the products into category according to its types.

- Considering the chances of blank spaces we also give it a friendly name.

#### **Order**

- Stores information about an order such as user, order number, delivery details and total cost.

#### **OrderLineItem**

- This models stores each product in each order by its name, size, quantity and a subtotal.

[Back to contents](#contents) ⬆️

## **Features**

### **Existing Features**

#### **Across the Site**

- **Navbar** - consistent on all pages and provides quick access to all areas of the site.

- **Search Bar** - allows the user to search a particular product with a key word.

- **Toasts** - Bootstrap toasts gives interaction to users after each action carried out. Show the shopping bag view for quick checkout option. Avoid confusion and gives user a better experience.

- **Responsive** - Bootstrap
s grid system and various media queries had been used throughout the project to ensure responsiveness.

- **User Profile** - allow users to save their information for easy acess for next visit. Order history encourage repeat order.

- **Bag Item Counts** - the number of items in the shopping bag tells uers how many items they have added to the bag.

- **Navbar Banner** - tells the user about free class and free delivery offer.

- **Footer** - tells the user about the site purpose and developer info.

#### **Page Specific**

#### ***Home***

- Hero image slides gives potential customers a brife idea what the dojo providing.

- The quick links gives the users a quick access to specific area of the site.

- The featured products section draw user's attention there is a shop in the site, encourage potential purchases.

#### ***Products***

- Product cards show the essential details of the product(name, rating, price and category)

- View Prouct details button tells the user, there's more to explore.

- Bootstrap Breadcrumb indicates which page the user is on and how many products are avaliable on the page.

- The filtering bar allows the users to sort the products by specific query.

- Back to top button allows the users to go back to the top at any time.

#### ***Product Detail***

- In addtion of the information the products page gives to the user, the product detail page gives the user a brife discription about the product.

- There are also more images displayed if there are any.

- The user then has an option of choosing a color or size for that specific product if it applies.

- Two buttons provided at the bottom to add to bag or keep shopping.

#### ***Bag***

- Allows line item quantities to be altered or removed from the bag and updates on each change.

- Shows bag total, delivery, and grand total of the order.

- Provide link to the specific product, allow easy alteration to sizes and colors etc.

- If bag total is less than free delivery threshold, amount required to receive free delivery is shown.

#### ***Checkout***

- Shows order summary and form to input delivery details.

- Payment handled by Stripe and reliability improved by use of webhooks.

    *Registered users*

- If delivery details previously saved, form will be pre-populated with them.

- Option to save delivery details for future purchases.

#### ***Checkout Success***

- Shows a summary of the order identifier, contact info and delivery information provided, as well as details of the order itself. On checkout the user is sent a confirmation email with details about their order.

- A quick link to go back to the shop.

#### ***My Profile***

#### *Registered User*

- Default contact and deliver info

- Ability to update to make future checkouts quicker

- view previous orders using same template as checkout success page

#### ***Add/Edit Product***

#### *Super users*

- Can add/edit a product, chosing all of its required features.

- Can choose whether or not the product shows on home page  featured product section.

- On submitting the addition/change, super user is sent to the updated product detail page.

#### **Secure Accounts**

Account security is covered by Django's allauth.

#### **CRUD functionality**

*All users:*

- Read all products

*Registered users:*

- Update their delivery details

*Super users:*

- Create, update and delete any products

#### **Static and image file hosting**

Static and image files are served from an Amazon S3 Bucket.

#### **Confirm delete**

When users request to delete an orderline product from their shopping bag or a superuser request to delete an product, an alert pops up to confirm if they wish to do so to prevent accidental deletion.

#### **Access protection**

Routes are protected using Django's @login_required route decorators to ensure non-super-users cannot interfere with the database.

404 and 500 error handling Pages for 404 and 500 errors keep the user on the site when something goes wrong, allowing them to return to the content with minimal disruption.

### **Features Left to Implement**

- Blog app to display industry and Kumite Dojo news, including comments feature to engage with the communit and gather more feedback.

- Wishlisht for users to save their favourite products.

- Products reviews, so the users can come back and leave a review after their purchase.

- "Learning App" to show karate techniques and videos etc.

[Back to contents](#contents) ⬆️

## **Technologies Used**

### **Languages**

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)

- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)

- [Python](https://www.python.org/)

- [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

### **Frameworks**

- [Bootstrap 4.4](https://getbootstrap.com/docs/4.4/getting-started/introduction/)

- [Django](https://www.djangoproject.com/)

- [jQuery](https://jquery.com/)

### **Database**

- [sqlite3](https://www.sqlite.org/index.html)

- [Heroku Postgres](https://www.heroku.com/postgres)

### **Extensions and kits**

- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

- [Pillow](https://pillow.readthedocs.io/en/stable/)

- [stripe](https://stripe.com/docs)

### **Project Management**

- [Amazon AWS](https://aws.amazon.com/?nc2=h_lg) (S3, IAM)

- [Github](https://github.com/)

- [Heroku](https://heroku.com)

### **Tools**

- [Am I Responsive](http://ami.responsivedesign.is/)

- [Balsamiq](https://balsamiq.com/wireframes/)

- [DB Diagram](https://dbdiagram.io/home)

- [Font Awesome](https://fontawesome.com/)

- [Google Font](https://fonts.google.com/)

[Back to contents](#contents) ⬆️

## **Testing**

[Back to contents](#contents) ⬆️

## **Deployment**

### **Requirements**

[Python 3](https://www.python.org/downloads/) - core code

[pipenv](https://pypi.org/project/pipenv/) - package installation and python environment control

[Git](https://git-scm.com/) - version control

[Amazon AWS S3 Bucket](https://aws.amazon.com/) - host the site's static and media files

**Values for the env.py environment variables and Heroku Config Vars used in the sections below will be unique to each sqlight, Postgres and S3 Bucket created. Please refer to their respective documentation for further details.**

<details>
<summary>How to clone Kumite Dojo and run locally</summary>
<br>

To clone this project from its [GitHub repository](https://github.com/MelindaZhang2020/CI-MS4-kumite-dojo):

1. From the repository, click **Code**

2. In the Clone >> HTTPS section, copy the clone URL for the repository

3. In your local IDE open terminal

4. Change the current working directory to the location where you want the cloned directory to be made

5. Type `git clone`, and then paste the URL you copied in Step 2

`git clone https://github.com/MelindaZhang2020/CI-MS4-kumite-dojo.git`

6. Press Enter. Your local clone will be created

7. Create a file called env.py to hold your app's environment variables, which should contain the following:

`import os
os.environ["SECRET_KEY"] = "app secret key of your choice"
os.environ["STRIPE_PUBLIC_KEY"] = "stripe public key generated by stripe"
os.environ["STRIPE_SECRET_KEY"] = "Stripe secret key generated by stripe"
os.environ["STRIPE_WH_SECRET"] = "webhook secret key generated by stripe"`

To find your Stripe keys, login to Stripe and then under the **Developers** tab look for the 'Publishable Key' and 'Secret Key'

The webhook secret key can be found under Webhooks once you have created an endpoint, which should be set to receive all events and match this url structure:

`<your site's base url>/checkout/wh/`

You will need a different endpoint for the local version and deployed site, updating the STRIPE_WH_SECRET accordingly in their respective environment variables.

8. Make sure the following are listed in your .gitignore file to prevent any environment variables being pushed publicly:
`env.py
__pycache__/
*.sqlite3
*.pyc`
</details>
<details>
<summary>How to deploy to Heroku</summary>
<br>
This is how you dropdown.
</details>
<details>
<summary>Setting up an S3 Bucket (Amazon Simple Storage Service)</summary>
<br>
This is how you dropdown.
</details>
<details>
<summary>Setting up AWS IAM (Identity and Access Management)</summary>
<br>
This is how you dropdown.
</details>
<details>
<summary>Connecting Django to S3</summary>
<br>
This is how you dropdown.
</details>

[Back to contents](#contents) ⬆️

## **Credits**

### **Resources and Tutorials**

### **Code modified from other sources**

### **Content**

### **Media**

### **Acknowledgements**

### **Disclaimer**

This site was developed for educational purposes only.

[Back to contents](#contents) ⬆️

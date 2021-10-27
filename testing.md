Back to [README](README.md)

# **Testing**

## **[Contents](#contents)**

 - [User Stories](#user-stories)

 - [Validator](#validator)

 - [Lighthouse](#lighthouse)

 - [Manual](#manual)

 - [Automated](#automated)

 - [Responsiveness](#responsiveness)

 - [Resolved Issues](#resolved-issues)

 - [Unresolved Issues](#unresolved-issues)

## **User Stories**

### **Overall user expectations**

#### **Easy navigation**

- Heading descriptive of the content displayed.

- Navar clearly indicate page directions.

- Logo direct user back to home page.

- Easy access to user profile and shopping bag.

- Options of sort product by price, rating, name or category.

- Back to top button when the list get too long.

- Keep shopping buttons throughout checkout process.

#### **Consistency**

- Consistent visual effect throughout the whole site.

- Same navbar and footer navigation system across all pages.

- Images and elements are well contained throughtout the site.

#### **Intuitive**

- Familiar icons have been used across the site for commonly expected actions e.g.shopping bag, delete, user and search.

- Toasts pop-ups alert the user when they perform actions i.e. login, errors, sucess etc.

- Modal appears to confirm content deletion.

#### **Responsiveness**

- Pages adapt a variety of screen sizes and extensive testing in Chrome Dev Tools.

- Page structure has been modified for mobile screen size to ensure readability.

#### **Secure**

- Allauth provides a robust user account system while Stripe offers secure payments, furthered by use of webhooks to ensure transactions are recorded.

#### **Appealing Visuals**

- Simple black and white color dazzled with a bit of red, gives the user the feel of ancient Japanese Karate.

- Simple fonts ensure readability and bring content together.

### **As a potential Student I want to ...**

**Immediately understand the purpose of the site and what it can provide**

- The logo and name immediately spell out the purpose and the tone of the site, it's a Karate club.

- The hero images slides with its headlines and links further demonstrate what the club has to offer.

- The banner under the navbar tells the user there are classes and delivery involed, therefore there must be a shop.

- As the user scrolling down, it confirms that there is a shop by seeing the featured products section.

**Know the background of the dojo, and who the instrucor is**

- As the user keep browsing, they can see the about section, there are informations about the dojo and instructors.

**Findout what kind classes are avaliable and class schedule**

- The classes page contains classes and timetable information and a brife description of the classes.

**Easily Browse through the cost of membership**

- The membership page leads the user to a description about the membership and its costs.

**Browse through the shop**

- The navbar clearly marked out the shop section, and the choice of browse it by category.

**Add items to my shopping bag before registering**

- The user can add items to the shopping bag without register.

**Search classes products by name**

- The searchbar provides the user search certain products by name from the shop.

- Unfortunately the user can't search a class by it name yet, but this functionality can be developed in the future.

**Choose clothes and belts size**

- The user can choose clothes and belt by various sizes and colors.

**Contact the dojo for more informations**

- This need has been satisfied by providing a contact form to the user, and the data will be sent to the admin page, so that the site owner can contact the user to provide further information.

### **As a registered user, I want to ...**

**Save my default delivery details**

- As soon as a user checkout, if he/her tick save info box, his/her personal info will be saved into database.

**View my previous purchases**

- This also will be saved as long as the user clicked save info, and the user can click on the order number to be redirect to the checkout success page.

**Review my shopping bag prior to checkout**

- The shopping bag can be grabbed at ease, and also previewed when the user add or delete an item from the shopping bag.

**Recieve confirmation of my orders**

- An real email will be sent as soon as the order is gone throught to confirm the details of the order, delivery info and grand total.

**Recieve free delivery above an order threshold**

- This is offered and clearly stated during checkout, and encourage the user to get free delivery once they spend over 50.

### **As a site owner, I want to ...**

**View, add, edit and delete products**

- The site owner can access a quick add page through frontend page.

- And this functionality is cover with Django admin interface, and beyond... 

- The site owner can not only add, edit and delete produts, but also control inventory, add multiple images, add different sizes and colors to different products.

- The site owner can also choose to active/deactive an product, add a specific product into featured products section on home page.

- The site owner can also change hero images and taglines to offer more classes and opportunities.

**Have a simple payment system**

- The stripe payment system is simple to use and reliable.

[Back to contents](#contents) ⬆️

## **Validator**

[W3C-HTML](https://validator.w3.org/)

- Error Duplicate ID due to double navbar for desktop view and mobile view - modified ✅

[W3C-CSS](https://jigsaw.w3.org/)

- Value Error : padding-bottom Too many values or values are not recognized : [ footer-height ] 

    Error caused by making footer stays at the bottom of the page, therefore it works fine - ignored

[Unicorn revealer - overflow](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln?hl=en-GB) - no evidence of overflow **Pass** ✅ 

[JS Hint](https://jshint.com/) - no error, no warning **Pass** ✅ 

[Pep8 Online](http://pep8online.com/) - all `.py` files have been paste into pep8 onlie, 0 errors - **Pass** ✅ apart from:

- webhookhandler.py has two lines which could not be shortened without making the code illegible

- webhooks.py has one line which could not be shortened

- settings.py has two lines which could not be shortened

## **Light House** - Chrome DevTools









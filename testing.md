Back to [README](README.md)

# **Testing**

## **[Contents](#contents)**

[User Stories](#user-stories)

[Validator](#validator)

[Lighthouse](#lighthouse)

[Manual Testing](#manual-testing)

[Automated](#automated)

[Responsiveness](#responsiveness)

[Resolved Issues](#resolved-issues)

[Unresolved Issues](#unresolved-issues)

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

During testing, I used Chrome DevTools lighthouse reports. I have generated a report for each page both desktop and mobile. There were a list of actions have been taken to improve the score regarding SEO and Performance see below:

- Resize all images, and use webp format for two of the big size hero images.

- Add meta data descriptions 

- Add apple touch icon

[Back to contents](#contents) ⬆️

## **Manual Testing**

### **Navigation**

| **Element** | **Action**|  **Expected Result** |  **Pass/Fail** |
|---|---|---|---|
|  **Navbar** |   |   |   |
|  Logo/Site name | click  | redirect to home page  |  Pass |
| **Searchbar**  |   |   |   |
|  Searchbar |  Enter a query | display products related to that query  |  Pass |
|  Searchbar Icon| click | submit query | Pass |
|  **My Account Icon** |   |   |   |
|  My Accout Icon dropdown | click  |  display a dropdow list |  Pass |
|  *When user not logged in*|   |   |   |
|  Register |  click |  redirect user to sign up page | Pass   |
| Log in  |  click | redirect user to sign in page    | Pass   |
|  *When user logged in/not superuser* |   |   |   |
| My Profile |  click |  redirect user to my profile page | Pass   |
| Log out  | click  | Confirm log out page  | Pass  |
|  *When user logged in/are superuser* |   |   |   |
| Product Admin  | click   |  redirect user to add product page | Pass  |
| **Main Navbar**  |   |   |   |
| About |  click | redirect user to about page   | Pass   |
| Classes  | click  | redirect user to Classes page  | Pass   |
| Membership  | click   | display memebership category out of products  | Pass  |
| Shop  |  click | display a dropdown list   |  Pass |
| All products  | click   | redirect user to all products page  | Pass |
| By Price  | click  | display products by price in ascending order |  Pass |
| By rating  | click   | display products by rating in descending order  | Pass  |
| By category | click   | display products by their category in ascending order with the name  | Pass  |
|  *Category dropdown* |   |   |   |
| Training Gi  | click  | only display products belong to this category  |  Pass |
| Karate Belt | click  | only display products belong to this category  |  Pass |
| Books | click  | only display products belong to this category  |  Pass |
| Accessories | click  | only display products belong to this category  |  Pass |
| Membership | click  | only display products belong to this category  |  Pass |
| **Footer**  |   |   |   |
| Social icons  | click  | open up a seperate developer's social account page  | Pass  |

### **Home Page**

| **Element** | **Action**|  **Expected Result** |  **Pass/Fail** |
|---|---|---|---|
| **Hero Image Slides**  |   |   |   |
| Join us Button  | click   | redirect user to contact us page  | Pass  |
| Classes Avialiable Button  |  click | redirect user to classes page  | Pass   |
| Learn more about us button  | click | redirect user to about page  | Pass  |
| **Feature Products Section**  | None  | display all products featured by admin  | Pass  |

### **About Page**

| **Element** | **Action**|  **Expected Result** |  **Pass/Fail** |
|---|---|---|---|
|Learn more about our classes button   | click  | redirect user to classes page  | Failed  |
| Action | Added in the link |  |  |


### **Classes Page**

All classes card images are displayed and responsive.

### **Contact Us Page**

| **Element** | **Action**|  **Expected Result** |  **Pass/Fail** |
|---|---|---|---|
| text input   |  type text input | show text  | Pass  |
| submit button  | click  | send message to admin  |  Pass |
|   |   | Toast message pops up  | Pass  |
|   |   | redirect user to home page  | Pass  |

### **All Products Page**

| **Element** | **Action**|  **Expected Result** |  **Pass/Fail** |
|---|---|---|---|
| Category Buttons  | click  | display the products belong to that category accordingly  | Pass  |
| Breadcrumb  | none  | display the total of products  | Pass  |
| Breadcrumb's Product Home |  click | redirect user to all products page  |  Pass |
| Sorting bar  | click  | sort products by specific query  |  Pass |
| View Details button  | click  | redirect user to that specific product detail page  | Pass  |
| Product Image  | click  | redirect user to that specific product detail page   | Pass  |
| Back to Top button  | click  | pop the view back to the top of the page  | Pass  |
| *When a superuser logged in*  |   |   |   |
| Edit/Delete link shows  |   |   |   |
| Edit  | click  | redirect user to edit product page  | Pass  |
| Delete  | click  | a confirm deletion modal pops up  | Pass  |
|   | Press ok  | The product is deleted from database permanently  | Pass  |

### **Product Detail Page**

| **Element** | **Action**|  **Expected Result** |  **Pass/Fail** |
|---|---|---|---|
| Image  | Click  | open up the image in a seperate page  | Failed  |
| Action!  |  add  `target="_blank" `  to the  `ìmg` element |   |   |
| Sub Image  | click  | open up the image in a seperate page  |  Failed |
| Action!  | add achor tage `<a> ` to sub imgage element  |   |   |
| Select Input/Size   | click  | shows the corresponding value   | Pass  |
| Select Input/color  |  click  | shows the corresponding value   | Pass  |
| Add to bag  |  click |  add item to the shopping bag with the variation value and redirect user to the bag page | Pass  |
| Keep shopping button  | click  | redirect user to all products page  | Pass  |

### **Shopping Bag Page**

| **Element** | **Action**|  **Expected Result** |  **Pass/Fail** |
|---|---|---|---|
| Toast message  | None  | pop up with a success message  | Pass  |
| Product name  | click  | redirect user to product detail page  | Pass  |
| **Minus button**  |   |   |   |
| *When there's only one such item in the bag*  |   |   |   |
|   | click  |  removes item from the shopping bag, your bag is empty message shows up, toast success message shows up | Pass  |
| *when there are more than 1 such items in the bag*   |   |   |   |
|   | click  | reduce the item quantity by 1, Toast sucess message shows with a shopping bag preview | Pass  |
| Plus Button | click  | increase the lineitem quantity by 1, toast success message shows up | Pass  |
| Delete Button  | click  | a confirm deletion modal pops up  | Pass  |
|   | press ok  | delete the lineitem from the shopping bag  |   |
| Secure Checkout button  | click  | redirect user to the checkout page  | Pass  |
| Keep shopping button  | click  | redirect user to all products page  | Pass  |

### **Checkout Page**

| **Element** | **Action**|  **Expected Result** |  **Pass/Fail** |
|---|---|---|---|
| Form fields  | on load   | fields populated with user default info(if previously saved)  | Pass  |
| Text Input  |  leave blank | On submit: form won't submit  | Pass  |
|   |   | error message on invalid field(s)  | Pass  |
|   | just whitespace  | On submit: form won't submit  |  Pass |
|   |   |  error message at the bottom of page | Pass  |
|   | fill in correctly  | on submit: form submits  |  Pass |
| Phone number Input   | leave blank  | on submit: for won't submit  | Pass  |
|   |   | error message on field  | Pass  |
|   | Just whitespace  | on submit: form won't submit  | Pass  |
|   |   | error message on field  | Pass  |
|   | use non numeric characters  | on submit: form won't submit  | Failed (see unsolved problem)  |
|   |   | error on field | Failed (see unsolved problem) |
| Email Input   |  leave blank |  on submit: form won't submit  | Pass  |
|   |   | error message on field  | Pass  |
|   | just whitespace  | On submit: form won't submit  |  Pass |
|   |   |  error message at the bottom of page | Pass  |
|   | fill in correctly  | on submit: form submits  |  Pass |
| Form Dropdown  | click   | show dropdown options  | Pass  |



### **Checkout Success Page**

| **Element** | **Action**|  **Expected Result** |  **Pass/Fail** |
|---|---|---|---|
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |

## **Profile Page**

| **Element** | **Action**|  **Expected Result** |  **Pass/Fail** |
|---|---|---|---|
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |

### **Product Admin Page**

| **Element** | **Action**|  **Expected Result** |  **Pass/Fail** |
|---|---|---|---|
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |

### **Alluth Pages**

| **Element** | **Action**|  **Expected Result** |  **Pass/Fail** |
|---|---|---|---|
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |


[Back to contents](#contents) ⬆️

## **Automated Testing**

## **Responsiveness**

## **Solved Problem**

## **Unsolved Problem**







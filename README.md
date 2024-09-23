# thrift
Project Idea: Online thrift store where all users can sell their own clothes to other users of the site.

index.html: Opening Page with two buttons: create user or login as an existing user.

signup.html: Form created using the django form template. All fields are necessary: Username, First Name, Last Name, Email, Password and Password confirmation.

login.html: Form created using the django form template: Fields are username and password.

display_item.html: Displays all the items that other users have put up for sale. NOTE: The items shown do NOT include the current users items. Each item is a link to open a modal box that shows the image of the item, its name, size, style, price and seller. The modal box also has a button that allows user to buy that selected item. The images are mobile-responsive and form smaller column sizes as the window becomes smaller. The items shown are also the items that were not already purchased or put in another users cart.

upload_item.html: Form created using the django template: Fields are the item name, style(women, men, unisex), price, size, and an image chosen from your computer. This page is again mobile responsive, making smaller image columns as the page becomes smaller.

mystore.html: Shows only the items that the current user is selling. All images are clickable modal boxes that show the image, title, size, style, price and availability of the item. The user can also delete or edit items from the item modal box. If an item was bought by another user the modal box also includes the username of the user who bought it as well as their email and address.

edit_item.html: Form is similar to the upload_item.html form. This form allows user to make changes to their selected item. The defaults of this form are the existing information dedicated to the item making it easy for the user to just make changes to their desired field.

cart_item.html: Shows the items that the user added to their cart. User can click on the images to see its information as well as delete the item from their cart. At the top of the navbar the user can confirm their purchase.

purchase.html: Responsive form that changes in width and collapses as the window becomes smaller. Form that has many fields that are used to get the billing information and credit card information of the user. NOTE: The credit card information is not actually used it is just there for demonstration purposes. On the right of the form is the list of items that the user is purchasing with the name and price of each item as well as the total for the cart. Once the user has filled all the fields, they can confirm their purchase once again.

mypurchases.html: Shows the images of the items purchased by the current user. Each image is, again, a modal box that shows the information of the item (item name, style, price and size)

logout: the user can also logout from all pages using the sidebar located on the left and can be accessed by clicking the button on the top left corner on the navbar.

cart accessibility: the cart can accessed from all pages as well, not including the cart page.

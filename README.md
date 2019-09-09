# Coffee Culture Club: 

Pre Deployment: https://4cdd50d642a34f458982d0ef71c1c40c.vfs.cloud9.us-east-1.amazonaws.com

Coffee Culture Clubs misson is to bring people together through the love of high quality and environment ethically sourced coffee. 

New age milenaials are done with night clubs and other demographics are removing alcohol from their lifes for multiple different reasons. 

There's not yet a set space for individuals to be social without the pressure of alcohol 
~ Coffee Culture Club solves that while also providing luxury coffee beans for purchase.

##

This web application is built with responsive, mobile first design. Users have the ability to plan new meetups and comment on exisiting meetups, they can buy & review products and receive discounts by filling out survays or 
becoming a member of the club. 


#### User Stories 

**As a new user I want to be able to**:
- Visit a homepage with a site description
- Easily navigate to register a new account by either selecting `Join club` in nav bar **or** by seeing `Join Club`
card on the homepage
- See a form that creates a new user 
- Be redirected to a login page to sign in for the first time



**As a user looking to purchase a product I want to be able to**:
- Navigate to `Products` 
- See a list of products
- Search for products
- See a product details page 
- Add to cart
- View Cart, amend quality see total price
- Go to a checkout page which contains a form accepting my shipping and billing details
- See a message confirming order and payment



**As a user interested in Meetups I want to be able to**:
- Navigate to `Meetups`
- See a list of different Meetups 
- See more information about the meetup
- Get more detail about specfic meets
- See and add comments on meetups
- Back to all meetups and see the ability to add a new meetup


**As a user looking for a discount code**:
- Visit a homepage with a banner actioning discounts in exchange for filling out a form 
- See a survay with general questions 
- Submit survay and a receive discount code



Wireframes:

[ADD WIREFRAMES]

## Features

### Existing Features

- Create account
- Sign in/out
- Reset Password
- Products page
- Cart
- Checkout page using Stripe
- Review Products
- Create Meetups
- Comment on Meetups

### Features Left to Implement
- Survay
- Discounts

## Technologies Used

[HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)

[CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)

[Materialize CSS](https://materializecss.com/)

[JavaScript](https://www.javascript.com/)

[Flask](https://flask.palletsprojects.com/en/1.0.x/)

[Python](https://www.python.org/)

[Heroku](https://dashboard.heroku.com/)

[Django](https://www.djangoproject.com/)



## Testing
[TO DO]

## Deployment

### I deployed my site using Heroku

[UPDATE ONCE FULLLY DEPLOYED]

* Create a new app on Heroku 
* If Heroku is not already pre installed in the development environment then run the following CLI command:
```
$ sudo snap install --classic heroku
```
* Login to Heroku Via the command line:
```
$ heroku login 
```

* Create a new Git repository and connect Heroku
```
$ cd my-project/
$ git init
$ heroku git:remote -a datadevelopment
```

Add Requirements.txt
```
$ sudo pip3 freeze —local > requirements.txt
```
Add ProcFile
```
echo web: python app.py > Procfile
```
Deploy Site: 
```
$ git add .
$ git commit -am "make it better"
$ git push heroku master
```
Run Application:
```
$ heroku ps:scale web=1
```
In the Heroku application
Go to Settings > Config Vars
Specify IP & Port:
```
IP    
PORT
STRIPE_Settings
```


### Media
- The photos used in this site were obtained from [Unsplash](https://unsplash.com/) and [Pexels](https://www.pexels.com/search/coffee/)


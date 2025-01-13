# Away Days 
A site for football fans to review thier away day experience!!

![Am I Responsive Image](/static/media/images/Awaydays1.png)
Link to Live WebSite: [Away Days](https://awaydays-f87f2c3f3546.herokuapp.com/)

# Aims 
The Purpose of this website is to provide Football Fans a platform to review their away day experiences in order to share with others, The website enables casual users to be able to enter the site and view any reviews that have been left, 
users can register, once registered users will be able to create, update and delete thier own reviews. 

 # Table of contents

- [Away Days](#away-days)
- [Aims](#aims)
- [Table of contents](#table-of-contents)
- [User experience (ux)](#user-experience-ux)
  - [Color Scheme](#color-scheme)
  - [Fonts](#fonts)
  - [Forms](#forms)
- [Project Planning](#project-planning)
  - [User Stories](#user-stories)
  - [Project Board](#project-board)
  - [Wireframes](#wireframes)
  - [Wireframe Information](#wireframe-information)
- [Databases](#databases)
- [Features](#features)
  - [Registered \& Unregistered Users](#registered--unregistered-users)
  - [Review Form](#review-form)
  - [CRUD Functoinality](#crud-functoinality)
  - [Future Features](#future-features)
    - [User Profile](#user-profile)
    - [Comments \& Like/Dislike/Flag](#comments--likedislikeflag)
    - [Images](#images)
- [Technologies and Frameworks](#technologies-and-frameworks)
- [Version Control](#version-control)
- [Design Tools](#design-tools)
- [Testing](#testing)
  
 # User experience (ux)
 The idea for Away Days was for football fans to haver a specific place to share and post their reviews reagrding their experiences, The greater idea was to have this initial idea and to grow it into a communicty or social media page. I wanted the page to be light, and simple in design making it easy to navigate

 ## Color Scheme
 For the colors i wanted to replicate a football themed style\
  - white was used as a main theme as it contrasts well with green, white was used in all the main headings, background color for the forms and also for the navbar
  - #003300; This is a dark green color which was used as a default color to the background so when a user scrolls down the image doesnt tile instead the color image merges into a background colour, this is helpful when on mobile as it meakes scrolling more visibily appealing.
  - Red and Yellow Were used in the buttons on the forms pages and also for the edit and delete buttons, however these werent styled using CSS, they were styled using bootstrap button classes btn-warning(yellow), btn-danger(red), I wanted to use these colors for the buttons as it follows the red and yellow card system in football(soccer)
  
  ## Fonts 
- For Main Headers, sub headers and the review card headers; 'Luckiest Guy' Google font was used with a back up of sans-serif.
- For the logged in message that is displayed when the user is logged in 'Sriracha' Google font was used
- For all other fonts that are displayed such as the form fonts and the review fonts these are default system fonts. 

## Forms
All the forms use the same Style using Django imported forms, all the forms are set to a white background which makes it easy for a user to access and use, origionally the forms were just set to the background image, however this produced some contrast issues and made some text difficult to see, This was more noticeable on mobile screens, so i added a white background to the forms for ease of use. 

# Project Planning 
My Goal was to be able to provide an esy to use site that allows users to publish their reviews, I used an an agile approach, utilising user stories and a project board on GitHub.

## User Stories
Link to Project Board: [ Away Days Project Board](https://github.com/users/ajswanwick/projects/3/views/1)

MoSCoW - User Stories were split into Must Have, Should Have, Could Have
✅ - Represents User stories that were completed 
❌ - Represents User stories that were not completed in this iteration, these were put in the next iteration list. 


- As a user i want to be a ble to login so that i can post a review ✅
- As a user i want to be able to select my team from a dropdown menu ✅
- As a user i eant to be able to score my reviews using a viusal aid for example using a scoring system out of 5  ✅
- As a user i need to be able to login to add a review so that i can stop others editing my review ✅
- As a user i want to be able to register to create a profile (this was partially coompleted, as a user must register but no profile page was included)  ✅
- As a user i want to be able to upload and image of my experience so that others can view ❌
- As a user i want to be able to flag inappropriate posts❌
- As a user i want to be able to upload and image so others can view an image of my experience to support my reviews ❌
- As a user i want to be able to flag or raise inappropriate comments to the site owner ❌

## Project Board

Link to Project Board: [ Away Days Project Board](https://github.com/users/ajswanwick/projects/3/views/1)
![Project Board](/static/media/images/project_board.png) 

## Wireframes

![Wireframes](/static/media/images/Wireframes.png)

## Wireframe Information
I have included the wireframe structure for the main Homepage and for the reviews page, as the forms were used using django, these were not included in the wireframes.
Wireframes were made using balsamiq. 

 # Databases
 The Database Scheme Detailed below was my original Plan for this databse, However during the Process, i focused on creating only one Model, Which is the one named Experience, (which is named Reviews in the actual model)The extra models will be implemented or added in future Iterations
 This ERD was Created using LucidChart.  

 ![ERD](/static/media/images/ERD.png)

 # Features
 This section will highlight the different features the website offers to the users 
 
 ## Registered & Unregistered Users
 Unregistered users are able to acess the main site (Homepage)and are able to view reviews, however adding a review is disabled as only registered users can comment/edit/delete. 
 In both views the review cards are a standard size with the "click for more" added to enable a full view of the content as the character count is linmited to 100. 
 ![UnregView](/static/media/images/unreg.png)
 This View has The message displayed above the reviews, it aslo displays the message to login to edit and delete.

 ![Regview](/static/media/images/reg_view.png)
 This View shows the difference as the user has a logged in message at the top right of the screen and also has the buttons to add a review and to also edit and or delete their own review. 

## Review Form
![RevForm](/static/media/images/review_form.png)
This shows the image of a registered user, able to create a review

## CRUD Functoinality
Non Registerd users can acees the site and can read Reviews, Users are able to register and then login with their details, once logged in Users can create new Reviews, They can also Updte their own reviews and also delete the reviews completely 
![CRUD](/static/media/images/CRUD.png)

## Future Features
There are some features that are planned for future updates

### User Profile 
I would like to add a user profile section in order for users to enter more detailed user information, this would also mean that other users could search for a user and add them to a friends list, i would also change my registrtaion to allauth to allow for social media login access. users will also be able to add a profile image. 

### Comments & Like/Dislike/Flag
I would like to add a comments section so other users could post comments on a review, I would like to add a like/dislike button for a user to click and also to add flag comment/post, so the site user could review a post and delete if neccessary

### Images 
I will also add an image upload section, This will enable users to add an image to their review. 

# Technologies and Frameworks 
- HTML
- CSS
- PostgreSQL
- Python
- Bootstrap
- Django
- JavaScript
- Cloudinary (Unused in this iteration)

# Version Control
- GitHub 
- Heroku (for Deployemnt)

# Design Tools
 - Balsamiq (Wireframes)
 - LucidChart - (ERD Diagrams) 
 - ChatGPT - for Image creation 
  
# Testing

  







 
 

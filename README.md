# Next Up - Movie Recommendation System
## Submission for Microsoft Intern Engage 2022


<p align="center">
  <img src="https://user-images.githubusercontent.com/55057608/170705077-90f2292f-8d71-46de-82f6-75a68a88a2c5.png" alt="Next up image" width="50%" />
</p>


## Overview
Next up is a movie recommendation system that offers generalized recommnendations to every user based on movie popularity, genre, and year. 
The model also give personalized recommendations based on the user's choice of genre and cast.
Finally, the system suggests similar movies have a higher probability of being liked based on the movie selected by user. 

A deployed version can be checked here: [Next Up](https://next-up-movies.herokuapp.com/)


## Features
1. Sign-up and Sign-in functionality. ✔️

2. Forgot password (resetting password) functionality. ✔️

3. OTP validation. ✔️

   `User receives a mail containing OTP for validation before resetting the password.`
   
4. User's credentials are stored in database. ✔️
  
5. Completely responsive frontend. ✔️

6. A total of 4 types of recommendation:
  * Recommended movies based on user's chosen genres and casts. ✔️
  * Most popular movies based on different genres. ✔️
  * Most popular movies based on different years. ✔️
  * Recommended movies similar to user's selected movie. ✔️
  
7. Movie details and trailer linked for each movie. ✔️

8. Watch movie option. ✔️

9. Option to like or dislike a movie. ✔️

10. Client-side session tracking. ✔️

11. Continious deployment. ✔️


## Interfaces

### Landing Page
* Seamless landing page with `Sign-in` and `Sign-up` (Get Started) button.

![home page](https://user-images.githubusercontent.com/55057608/170728394-90bf8b2a-e336-4669-986d-c95426f2ec4f.png)

### Sign-up Page

![sign-up page](https://user-images.githubusercontent.com/55057608/170728671-71d36f55-c1e4-4994-8b28-1f60fea80e5a.png)

### Restrictions and validations on sign-up page
* All fields not filled
* Already registered email account

![sign-up validations](https://user-images.githubusercontent.com/55057608/170733520-297a73f7-feb2-47d2-9578-f9e7be0c55c3.PNG)

### Sign-in Page

![5 - sign-in](https://user-images.githubusercontent.com/55057608/170729606-be135836-b021-45d2-aa37-04051e0acb2f.png)

### Restrictions and validations on sign-in page
* All fields not filled
* Email account not registered
* Incorrect password

![sign-in validations](https://user-images.githubusercontent.com/55057608/170734038-e3226aa3-b716-4865-8a06-af73106922c2.PNG)

### Restrictions and validations on forgot password functionality
* Email account not entered
* Email account not registered

![forgot validations](https://user-images.githubusercontent.com/55057608/170734508-cc5822c3-2212-4326-84a7-9a61b5ffc2a9.PNG)

### OTP Validation Page

![11 - otp validation](https://user-images.githubusercontent.com/55057608/170730305-cbccfd03-cf80-45aa-b893-734503d01a30.png)

### Restrictions and validations on otp validation page
* OTP not entered
* OTP incorrect

![otp validations](https://user-images.githubusercontent.com/55057608/170734963-a6323f6d-575f-4696-b081-fcf05c665525.PNG)

### Reset password Page

![14 - reset](https://user-images.githubusercontent.com/55057608/170730899-809feb1c-eb6a-4a06-b6e8-c4ba3ea1085d.png)

### Restrictions and validations on reset password Page
* New password not entered

![10](https://user-images.githubusercontent.com/55057608/170735074-3ff1e7d0-a8f5-41a8-99c5-4421cd71f8f2.PNG)

### Choices Page
* Page for choosing prefered genres and casts used for recommending movies

![choices](https://user-images.githubusercontent.com/55057608/170731172-7ac6e050-93ab-433f-9d38-2466972cc5d6.png)

### Recommendations page
* This page shows recommended movies based on genres and casts chosen by the user.
* It also displays most popular movies based on different genres and years.

![16 - recommendations](https://user-images.githubusercontent.com/55057608/170731099-138356e1-2113-4ae1-bebb-6740431432b1.png)

### Movie Page
* This page shows details and trailer of the movie selected by the user.
* It also recommends similar movies to the user based on the selected movie.

![18 - movie](https://user-images.githubusercontent.com/55057608/170731745-71dcabad-78ca-489e-92cd-402900a14845.png)

### Watch Movie Page
* This page is to watch the movie selected.

![19 - watch](https://user-images.githubusercontent.com/55057608/170731856-2595f39a-4ea1-41e3-9160-d699d82bf578.png)


## Tech Stack and Softwares used
1. `Frontend` : HTML5, CSS3, JavaScript, BootStrap, jQuery
2. `Backend` : Python flask
3. `Database` : SQLite3
4. `ML model` : Jupyter Notebook
5. `IDE` : PyCharm
6. `Version Control` : Git
7. `Deployment` : Heroku

You can also see the list of dependencies in the [requirements.txt](/blob/main/requirements.txt) file.


## Libraries and Toolkits used
`Python` : NumPy, Pandas, ast (Abstract Syntax Trees), pickle

`ML` : ntlk (Natural Language Toolkit), sklearn (scikit-learn)

`SQLite` : sqlite3, SQLAlchemy


## Recommendation Algorithm
For recommendation of similar movies, I have implemented Cosine Algorithm after vectorization of movies. 
It is achived by using Annoy (Approximate Nearest Neighbors) mechanism.
Resource for Annoy: https://github.com/spotify/annoy


## Deployment
For Deployment, I have used `Heroku` as a platform.
A deployed version can be checked here: [Next Up](https://next-up-movies.herokuapp.com/)


## Installation/Environment Setup
1. Clone this repository in your local system.
* Open terminal in a new folder and enter the command given below.
   ```
   git clone https://github.com/kashishahuja2002/Microsoft-Intern-Engage.git
   ```

2. Install dependencies.
* Open terminal in the cloned folder and enter the command given below.
   ```
   pip3 install -r requirements.txt
   ```
  
3. Run the project.
* While you are still inside the cloned folder, write the following command in terminal to run the website locally. 
   ```
   python app.py
   ```
   
4. If everything is done in order, the app will be running at "http://127.0.0.1:5000"


## CD Setup
For continious deployment, heroku is used. Any changes pushed to the main branch will be automatically deployed. 


## Future Scope
* `Like/Dislike` : The option to like or dislike movie adds the movie to user's like/dislike list. As of now, I am just cummulating the data. This can be further extended by using the like/dislike list to recommend movies to the user.

* `Watch Movie` : The watch movie option currently displays the same movie intro for all the movies. In future, it can be customised according to the movie selected.

* `Collabrative Filtering` : The model currently uses content-based recommendation system. It can be converted into a hybrid system by adding collabrative filtering mechanism. 


## Video Demo
Here I will add the video demo.


<br><hr>
Thank you, Microsoft Team for such a wonderful mentorship program ❤️

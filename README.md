# Next Up - Movie Recommendation System
<!-- ## Submission for Microsoft Intern Engage 2022 -->
## Submission for Microsoft Intern Engage '22


<p align="center">
  <img src="https://user-images.githubusercontent.com/55057608/170705077-90f2292f-8d71-46de-82f6-75a68a88a2c5.png" alt="Next up image" width="50%" />
</p>


## Overview
Next up is a movie recommendation system that offers generalized recommendations to every user based on movie popularity, genre, and year. 
The model also gives personalized recommendations based on the user's choice of genre and cast.
Finally, the system suggests similar movies have a higher probability of being liked based on the movie selected by the user. 


## Demo Video
The demo video for the app can be checked here: [Next Up | Video](https://youtu.be/2bBJNJMQEnY)

https://github.com/kashishahuja2002/Next-Up-Microsoft-Intern-Engage/assets/55057608/a1350c89-900a-41ac-8cb2-3777957d112c


## Features
1. Sign-up and Sign-in functionality. ✔️

2. Forgot password (resetting password) functionality. ✔️

3. OTP validation. ✔️

   `The user receives a mail containing OTP for validation before resetting the password.`

4. Restrictions and validations on the sign-up page, sign-in page, forgot password functionality, OTP validation page, and reset password page. ✔️
   
5. The User’s credentials are stored in the database. ✔️
  
6. Completely responsive front end. ✔️

7. A total of 4 types of recommendations:
  * Recommended movies based on the user's chosen genres and casts. ✔️
  * Most popular movies based on different genres. ✔️
  * Most popular movies based on different years. ✔️
  * Recommended movies similar to the user's selected movie. ✔️
  
8. Movie details and trailer linked for each movie. ✔️

9. Watch a movie option. ✔️

10. Option to like or dislike a movie. ✔️

11. Client-side session tracking. ✔️

12. Continuous deployment. ✔️


## Interfaces

### Landing Page
* Seamless landing page with `Sign-in` and `Sign-up` (Get Started) button.

![home page](https://user-images.githubusercontent.com/55057608/170728394-90bf8b2a-e336-4669-986d-c95426f2ec4f.png)

### Sign-up Page

![sign-up page](https://user-images.githubusercontent.com/55057608/170728671-71d36f55-c1e4-4994-8b28-1f60fea80e5a.png)

### Sign-in Page

![5 - sign-in](https://user-images.githubusercontent.com/55057608/170729606-be135836-b021-45d2-aa37-04051e0acb2f.png)

### OTP Validation Page

![11 - otp validation](https://user-images.githubusercontent.com/55057608/170730305-cbccfd03-cf80-45aa-b893-734503d01a30.png)

### Reset password Page

![14 - reset](https://user-images.githubusercontent.com/55057608/170730899-809feb1c-eb6a-4a06-b6e8-c4ba3ea1085d.png)

### Restrictions and validations on the sign-up page, sign-in page, forgot password functionality, OTP validation page, and reset password page
* All fields not filled
* Email account already registered (sign-up), Email account not registered (sign-in)
* Incorrect password, OTP incorrect
* Email address not entered, OTP not entered, new password not entered

![6 - validations](https://user-images.githubusercontent.com/55057608/170794709-7b6623b8-6fe8-4248-ae0e-c02f49a42034.PNG)

### Choices Page
* Page for choosing preferred genres and casts used for recommending movies

![choices](https://user-images.githubusercontent.com/55057608/170731172-7ac6e050-93ab-433f-9d38-2466972cc5d6.png)

### Recommendations page
* This page shows recommended movies based on genres and casts chosen by the user.
* It also displays the most popular movies based on different genres and years.

![16 - recommendations](https://user-images.githubusercontent.com/55057608/170731099-138356e1-2113-4ae1-bebb-6740431432b1.png)

### Movie Page
* This page shows details and a trailer of the movie selected by the user.
* It also recommends similar movies to the user based on the selected movie.

![18 - movie](https://user-images.githubusercontent.com/55057608/170731745-71dcabad-78ca-489e-92cd-402900a14845.png)

### Watch Movie Page
* This page is to watch the movie selected.

![19 - watch](https://user-images.githubusercontent.com/55057608/170731856-2595f39a-4ea1-41e3-9160-d699d82bf578.png)


## Tech Stack and Software used
1. `Frontend`: HTML5, CSS3, JavaScript, BootStrap, jQuery
2. `Backend`: Python flask
3. `Database`: PostgreSQL, SQLite3
4. `ML model`: Jupyter Notebook
5. `IDE`: PyCharm
6. `Version Control`: Git
7. `Deployment`: Heroku

You can also see the list of dependencies in the [requirements.txt](/requirements.txt) file.


## Libraries and Toolkits used
`Python`: NumPy, Pandas, ast (Abstract Syntax Trees), pickle

`ML`: ntlk (Natural Language Toolkit), sklearn (scikit-learn)

`SQLite`: sqlite3, SQLAlchemy


## Recommendation Algorithm
For recommendations of similar movies, a content-based recommendation system. For recommendation, the system takes into account movie titles, genres, starring cast, keywords, overview, and the director. I have implemented the Cosine Algorithm after the vectorization of movies. 
It is achieved by using the Annoy (Approximate Nearest Neighbors) mechanism. Resource for Annoy: https://github.com/spotify/annoy


## Deployment
For Deployment, I have used `Heroku` as a platform.
A deployed version can be checked here: [Next Up](https://next-up-movies.herokuapp.com/)


## Installation/Environment Setup
1. Clone this repository in your local system.
* Open the terminal in a new folder and enter the command given below.
   <!-- ```
   git clone https://github.com/kashishahuja2002/Microsoft-Intern-Engage.git
   ``` -->
   ```
   git clone https://github.com/kashishahuja2002/Minor-Project-Next-Up.git
   ```

2. Make sure that Python is installed and updated in your machine.

3. Install dependencies.
* Open the terminal in the cloned folder and enter the command given below.
   ```
   pip3 install -r requirements.txt
   ```
  
4. Run the project.
* While you are still inside the cloned folder, write the following command in the terminal to run the website locally. 
   ```
   python app.py
   ```
   
5. If everything is done in order, the app will be running at "http://127.0.0.1:5000"


## CD Setup
For continuous deployment, Heroku is used. Any changes pushed to the main branch will be automatically deployed. 


## Future Scope
* `Like/Dislike`: The option to like or dislike a movie adds the movie to the user's like/dislike list. As of now, I am just accumulating the data. This can be further extended by using the like/dislike list to recommend movies to the user.

* `Watch Movie`: The watch movie option currently displays the same movie intro for all the movies. In the future, it can be customized according to the movie selected.

* `Collaborative Filtering`: The model currently uses a content-based recommendation system. It can be converted into a hybrid system by adding a collaborative filtering mechanism.


## Documentation
A complete project report for the system with a use case diagram, web flow, ER diagram, wireframes, etc can be found here: [Next Up | Project Report](/documents/ProjectReport.docx.pdf).

A short and crisp version of the documentation can be found here: [Next Up | Documentation](/documents/Documentation.pdf).

A presentation for the project can be found here: [Next Up | Presentation](/documents/Presentation.pdf).


<br><hr>
Thank you, Microsoft Team for such a wonderful mentorship program ❤️

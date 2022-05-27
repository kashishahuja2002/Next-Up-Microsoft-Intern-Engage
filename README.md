# Next Up - Movie Recommendation System
## Submission for Microsoft Intern Engage 2022


<p align="center">
  <img src="https://user-images.githubusercontent.com/55057608/170705077-90f2292f-8d71-46de-82f6-75a68a88a2c5.png" alt="Next up image"/>
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
   
3. Store user's credentials in database. ✔️
  
4. Completely responsive frontend. ✔️

5. Recommended movies based on user's chosen genres and casts. ✔️

6. Most popular movies based on different genres. ✔️

7. Most popular movies based on different years. ✔️

8. Recommended movies similar to user's selected movie. ✔️
 
9. Movie details and trailer display. ✔️

10. Watch movie option. ✔️

11. Option to like or dislike a movie. ✔️

12. Client-side session tracking. ✔️

13. Continious deployment. ✔️


## Interfaces
Here I will add images of frontend interfaces.


## Tech Stack and Softwares used
1. `Frontend` : HTML5, CSS3, JavaScript, BootStrap, jQuery
2. `Backend` : Python flask
3. `Database` : SQLite3
4. `ML model` : Jupyter Notebook
5. `IDE` : PyCharm
6. `Version Control` : Git
7. `Deployment` : Heroku

You can also see the list of dependencies in the `requirements.txt` file.


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

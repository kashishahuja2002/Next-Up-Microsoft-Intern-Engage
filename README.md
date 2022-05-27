
# Next Up


## Movie Recommendation System
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


## Tech Stack and Softwares used
1. `Frontend` : HTML5, CSS3, JavaScript, BootStrap, jQuery
2. `Backend` : Python flask
3. `Database` : SQLite3
4. `ML model : Jupyter Notebook
5. `IDE` : PyCharm
6. `Deployment` : Heroku


## Libraries and Toolkits used
`Python` : NumPy, Pandas, ast (Abstract Syntax Trees), pickle

`ML` : ntlk (Natural Language Toolkit), sklearn (scikit-learn)

`SQLite` : sqlite3, SQLAlchemy


## Recommendation Algorithms
For recommendation of similar movies, I have implemented Cosine Algorithm after vectorization of movies. 
It is achived by using Annoy (Approximate Nearest Neighbors) mechanism.
Resource for Annoy: https://github.com/spotify/annoy


## Deployment
For Deployment, I have used `Heroku` as a platform.
A deployed version can be checked here: [Next Up](https://next-up-movies.herokuapp.com/)


## Project Setup
1. Clone this repository in your local system.
   
   ```
   git clone https://github.com/kashishahuja2002/Microsoft-Intern-Engage.git
   ````
2. Local system must have JDK and JRE pre-installed in it.
3. Pre-installed Netbeans or Eclipse with Apache Tomcat-Server is required.
4. Open the cloned repository in Netbeans/Eclipse IDE.
5. Integrate the .jar files available inside the cloned directory in your project.
6. Now just RUN the Project.
7. If everything is done in order then this will open the website in your local machine.


## CD Setup
For continious deployment, heroku is used. Any changes pushed to the main branch will be automatically deployed. 


## Video Demo
https://user-images.githubusercontent.com/55057608/131963901-8229a2ca-b18d-4e32-8315-b4eb173b9ef3.mp4


https://user-images.githubusercontent.com/55057608/131963901-8229a2ca-b18d-4e32-8315-b4eb173b9ef3.mp4

## Online Assessment Platform
This is an online assessment platform made by Kashish Ahuja and M Boopathi as the final project of Walkover University Program.
The web application a robust online testing platform for conducting remote online examinations. The project is made over Java as backend, PostgreSQL as the  database, and HTML, CSS, JS, Boostrap4, and AJAX as frontend.

A deployed version can be checked here: https://online-assessment-platform.herokuapp.com/

## We worked for the following specifications
1. Assessment shall be MCQ pattern.✔️

2. There must be a question pool for the assessment.✔️
   
   `We have created a pool of 15 questions in database and randomly selected 10 questions in shuffled order.`
  
3. The questions displayed in the assessment shall be only from that pool.✔️

4. Number of questions in the pool shall be more than questions displayed.✔️

5. Set a time limit for the assessment (individual timer for a question/optional).✔️ 
   
   `The total time limit is of 100 seconds.`

6. Question order shall be shuffled for each candidate appearing.✔️

7. Assessment score shall be generated at the time of submission.✔️


## Additional Features
1. Great UI.
2. Completely responsive for all devices.
3. Login page for storing user's data and validation of the data of users attempting for assessment.
4. Result is displayed with Name entered at the time of login.
5. All users' name and score are displayed at the end using databse table for storing the data and scores of the user.

## Developers
1. Kashish Ahuja [https://github.com/kashishahuja2002]
2. M Boopathi [https://github.com/Mboopathi1999]

* `Frontend + JavaScript Functionality` : ***Kashish Ahuja***
* `Backend + Database` : ***M Boopathi***


## Tech Stack Used
1. `Frontend` : HTML5, CSS3, Javascript, Bootstrap, AJAX
2. `Backend` : Java
3. `Database` : PostgreSQL


## Deployment
For Deployment, we have used `Heroku` as a platform connected with `Heroku Postgres` as database.


## Project Setup
1. Clone this repository in your local system.
   
   ```
   git clone https://github.com/kashishahuja2002/Online_assessment_platform.git
   ````
2. Local system must have JDK and JRE pre-installed in it.
3. Pre-installed Netbeans or Eclipse with Apache Tomcat-Server is required.
4. Open the cloned repository in Netbeans/Eclipse IDE.
5. Integrate the .jar files available inside the cloned directory in your project.
6. Now just RUN the Project.
7. If everything is done in order then this will open the website in your local machine.


## CI/CD setup
1. Create a GitHub repository. You may initialize it with a README, license, .gitignore
2. Install git via terminal 

   (On Ubuntu you can do `sudo apt-get install git`)
3. Then do a git clone of your repository, or simply download the zip file of your repository from GitHub and extract it.
4. Copy your java project in the new folder created after cloning (its name will be same to that of the repository you cloned).
5. Add all the changes you want.
6. Then execute these commands:
   
   ````
   git add . 

   git commit -m "[mandatory commit message]" 
   
   git push [url to your repository] master/main 
7. Now your commit will be successfully pushed to the main branch of your GitHub repository.

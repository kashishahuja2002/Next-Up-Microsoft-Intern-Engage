https://navendu.me/posts/open-source-internship-programs/

https://www.markdownguide.org/cheat-sheet/
https://stackedit.io/app#

# Online Assessment Portal

This is an MCQ-based Online Assessment Portal made by Aman Kumar Singh, Kunal Jain and Divya Joshi. The web application is made using `Java Servlets` and `Java Server Pages` as backend, `MySQL` as Database and for the front-end part, we have used `HTML`, `CSS`, `JS`, `jQuery`, and `Bootstrap`.

You can find the Portal here: http://13.233.172.37:8080/QuizApp/

## Demonstration Video:

https://user-images.githubusercontent.com/67758580/131299208-4fe25312-04b3-4b0e-a098-63f045538731.mp4

## Contribution of Members:

* `Frontend` : ***Kunal Jain***
* `Backend + Database` : ***Aman Kumar Singh***
* `JavaScript Functionality` : ***Divya Joshi***

## Tech Stack:

1. `Frontend` : HTML5, SCSS, CSS3, Javascript.
2. `Backend` : Java Servlets, Java Server Pages(JSP).
3. `Database` : MySQL.


## Specifications Assigned:

1. Assessment shall be MCQ pattern.✔️

2. There must be a question pool for the assessment.✔️

3. The questions displayed in the assessment shall be only from that pool.✔️

4. Number of questions in the pool shall be more than questions displayed.✔️

5. Set a time limit for the assessment (individual timer for a question/optional).✔️

6. Question order shall be shuffled for each candidate appearing.✔️

```
All specifications are satisfied ✔️
```

## Deployment:
- For Deployment, we have used `Amazon AWS` Cloud.

- We created an instance of `Amazon Linux 2 AMI` and deployed our project into it.

- Hosted on `Apache Tomcat 9.0.10 server`.

to install tomcat server -

```
sudo wget https://downloads.apache.org/tomcat/tomcat-9/v9.0.52/bin/apache-tomcat-9.0.52.tar.gz.sha512
tar -zvxf apache-tomcat-9.0.10.tar.gz
yum install wget -y 
```

Check if server is active -

```
ps -ef | grep tomcat
```

if not active then start server -

```
cd apache-tomcat-9.0.10/bin
./startup.sh
```
- Command setup :

```
sudo su - root
cd apache-tomcat-9.0.10/webapps
git clone https://github.com/kunal2899/AssessmentPortal.git
```

- For database, we have used `AWS RDS` and integrated this database in our project.
 
- SQL database file named `source.sql` is in root folder of repository.  
  

## Pages Functionality:
   1. `Login page` - to take the data of users attempting for assessment.
   2. `Instructions page` - valid users will move forward to the instructions page where they will get all the instructions related to assessment.
   3. `Main Page` - after reading all the instructions, if the users agree that they have read intructions and accept them, then all valid users are allowed to give assessment.
   4. `Final Score Page` - after attempting the assessment, in case the user submits or runs out of time (in case of auto-submit), the user will be redirected to this page on which they will get their resultant scores.
   5. `Admin Page` - This page is isolated from normal user environment, content of that page can be accessed by authorised users only.
   
- Assessment is of 15 minutes.
- Assessment will auto-submit in case of no submission before times up.
- Assessment can be submitted anytime and at any point of assessment, score will be calculated accordingly.
- There is no negative marking.
- 15 questions asked in shuffled order from a question pool of 30 questions.

## Admin Panel:
http://13.233.172.37:8080/QuizApp/admin.html
 - Firstly user have to login to admin panel with valid credentials to prove his authenticity.
 - Only admins with valid credentials can access inner content of page.
 - For test purpose, one of the admin's username and password given below:
 ```
 username:  admin@walkover.in
 password:  admin
 ```
 - After successful login user redirected to results page where he can see results of all users attempted the assessment.
 - On Results page, records of all attempts displayed with details : `Name` , `Email ID` , `Score`.

## Project Setup: 

**Requirements:** Pre-installed `Netbeans` with `Apache Tomcat-Server` and `MySQL`.

1. Clone this repository in your local machine using the following command:

    ```git
    git clone https://github.com/kunal2899/AssessmentPortal.git
    ```

2. Open the cloned repository in `Netbeans IDE`.

3. Integrate the `.jar` files available inside the cloned directory in your Netbean's project.
   - `5_6122867091839124788.jar`
   - `gson-2.2.2.jar`
   - `mysql-connector-java-8.0.26.jar`

4. Add these lines of code to the `web.xml` file in your project:
-----
``` xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app version="3.1" xmlns="http://xmlns.jcp.org/xml/ns/javaee" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_3_1.xsd">
    <servlet>
        <servlet-name>ShowQuestionsControllerServlet</servlet-name>
        <servlet-class>QuizApp.controller.ShowQuestionsControllerServlet</servlet-class>
    </servlet>
    <servlet>
        <servlet-name>AddScoreControllerServlet</servlet-name>
        <servlet-class>QuizApp.controller.AddScoreControllerServlet</servlet-class>
    </servlet>
    <servlet>
        <servlet-name>ShowUsersControllerServlet</servlet-name>
        <servlet-class>QuizApp.controller.ShowUsersControllerServlet</servlet-class>
    </servlet>
    <servlet>
        <servlet-name>LoginControllerServlet</servlet-name>
        <servlet-class>QuizApp.controller.LoginControllerServlet</servlet-class>
    </servlet>
    <servlet-mapping>
        <servlet-name>ShowQuestionsControllerServlet</servlet-name>
        <url-pattern>/ShowQuestionsControllerServlet</url-pattern>
    </servlet-mapping>
    <servlet-mapping>
        <servlet-name>AddScoreControllerServlet</servlet-name>
        <url-pattern>/AddScoreControllerServlet</url-pattern>
    </servlet-mapping>
    <servlet-mapping>
        <servlet-name>ShowUsersControllerServlet</servlet-name>
        <url-pattern>/ShowUsersControllerServlet</url-pattern>
    </servlet-mapping>
    <servlet-mapping>
        <servlet-name>LoginControllerServlet</servlet-name>
        <url-pattern>/LoginControllerServlet</url-pattern>
    </servlet-mapping>
    <session-config>
        <session-timeout>
            30
        </session-timeout>
    </session-config>
</web-app>

```
-----

5. Now just **RUN** the Project.

6. If everything is done in order then this will open the website in your local machine at http://localhost:8080/ 

## CI/CD
We have not used any integration tool for continuous integration/continuous deployment compatability for our application.

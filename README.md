
# CMPE 282 Project of Group Cloud Bloom
<b>Course Name :</b> Cloud services

<b>Project Name  :</b> Carcorner

<b>Application URL :</b> 

<b>University Name :</b> [San Jose State University](https://www.sjsu.edu/)



<b>Professor's Name :</b> Andrew Bond

<b>Team Name:</b> Cloud Bloom

<b>Team Members:</b> <br/>
[Bhavya Hegde](www.linkedin.com/in/bhavya-hegde-145b9b123)<br/>
[Darshini Venkatesha Murthy Nag](https://www.linkedin.com/in/darshini-venkatesha-murthy-nag-90052756/)<br/>
[Sirisha Polisetty](https://www.linkedin.com/in/sirishapolisetty/)<br/>
[Blessy Dickson Daniel Moses](https://www.linkedin.com/in/blessy-dickson-348a31133/) 


## Introduction



## Application Features
* 
* 
* 
* 
* 
* 
* 
* 

## Carcorner admin Features
* List cars based on color, model, year, price, description, and the city where it is available and by the condition(Eg. if it is used)
* View enquiries from the users
* Add, update or delete users and team members

## Additional Application Features
* 
* 
* 
* 


## Tools and Technologies used
Frontend: HTML, CSS, Bootstrap, Javascript<br/>
Backend: Python Django framework<br/>
Other tools: Jenkins, Visual studio code, PyCharm<br/>
AWS components: EC2, Route 53, ELB, RDS postgreSQL, s3, certificate manager
  
## Architecture Diagram




#### CI/CD Pipeline
* 

## Instructions to run project locally
#### Create a virtual environment
```
python -m venv venv
  ```
#### Activate the virtual environment

* macOS:
```
source venv/bin/activate
```

* Windows:
```

venv\scripts\activate
```

#### Install required dependencies
```
pip install -r requirements.txt
```
#### Set up environment variables
```
touch .env
```
#### We need to add below details in env
```
SECRET_KEY=
DEBUG=True
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
EMAIL_USE_TLS=True
```

#### Run migrations
```
python manage.py makemigrations
python manage.py migrate
```

#### Create an admin user to access the Django Admin interface
```
python manage.py createsuperuser
```

#### Run the application
```
python manage.py runserver
```
## Sample Demo screenshots



## References


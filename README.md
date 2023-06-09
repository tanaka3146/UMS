# UMS
## Installation
1. Clone the backend-intern-assignment and proceed with steps mentioned below

### Install requirements

```
virtualenv env --python=python3.8
source env/bin/activate
pip install -r requirements.txt
```
### Set DB

```
export FLASK_APP=app.py
python 
from app import db,app
app.app_context().push()
db.create_all()
exit()
```
### Start Server

```
flask run
```
## Http Requests
 Use Postman to test the flask API
 
 ### create task
 set the method to POST
 request URL  - http://127.0.0.1:5000/tasks
 body - {"title":"task1","description":"this is test entry","due_date":"2023-06-11","status":"Incomplete"}
 
 ### retrive single task by id
 set the method to GET
 request URL - http://127.0.0.1:5000/tasks/<task_id>
 
 ### update task
 set the method to PUT
 request URL - http://127.0.0.1:5000/tasks/<task_id>
 body - {"status":"Complete" }
 
 ### delete task
 set the method to DELETE
 request URL - http://127.0.0.1:5000/tasks/<task_id>
 
 ### list all task
 set the method to GET
 request URL - http://127.0.0.1:5000/tasks?page=1&per_page=3
 page is parameter for the page number(default=1)
 per_page is the parameter for number of entries in single page (default=10)
 
 
 
 

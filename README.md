# UMS
## Installation
1. Clone the backend-intern-assignment branch and proceed with steps mentioned below

### Install requirements

```
virtualenv env --python=python3.8
source env/bin/activate
pip install -r requirements.txt
```
### Set DB
use set in windows and export in linux/mac
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
1. set the method to POST
2. request URL  - http://127.0.0.1:5000/tasks
3. body - {"title":"task1","description":"this is test entry","due_date":"2023-06-11","status":"Incomplete"}

### retrive single task by id
1. set the method to GET
2. request URL - http://127.0.0.1:5000/tasks/<task_id>

### update task
1. set the method to PUT
2. request URL - http://127.0.0.1:5000/tasks/<task_id>
3. body - {"status":"Complete" }

### delete task
1. set the method to DELETE
2. request URL - http://127.0.0.1:5000/tasks/<task_id>

### list all task
1. set the method to GET
2. request URL - http://127.0.0.1:5000/tasks?page=1&per_page=3
3. page is parameter for the page number(default=1)
4. per_page is the parameter for number of entries in single page (default=10)
 
 
 
 

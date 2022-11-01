### Chunify

A simple application to create rest api in lambda functions based on chalice framework.
This rest api simulates an app like spotify where we can manage users, playlists and musics.
Chunify sends a sms to all users with phone number registered When a new music is added.
The data can be stores in DymanoDB or within the process.

### How to use

*1 - Clone repository*
```bash
git clone https://github.com/rafaeldex/chunify.git path/to/folder
```

*2 - Set your aws credentials in .env*
```html
AWS_DIR=/path/to/your/.aws
```

*2 - Choose the type of data storage in /code/core/app.py*
```python
# COMPLETE, BETA
version = 'COMPLETE'
```

*4 - Run docker-compose*
```bash
docker-compose up
```

*5 - Access localhost in your browser*

### Deployment

*1 - Check containers names*
```bash
docker ps
```

*2 - Login into python container*
```html
docker exec -it python_container_name bash
```

*3 - Navigate to core dir*
```html
cd core
```

*4 - Execute deployment using chalice*
```html
chalice deploy
```

### Local requirements

-  Docker installed

### AWS requirements

-  Account with SNS unblocked before
-  DynamoDB Access Permissions for chunify-dev function

### AWS services used

-  Lambda
-  DynamoDB
-  Cloud Watch
-  SNS
-  IAM
-  Api Gateway

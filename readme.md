### Chunify

-  A simple application to create REST API in AWS Lambda based on Chalice framework.<br>
-  This REST API simulates an app like Spotify where we can manage users, playlists and musics.<br>
-  The data can be stored in DynamoDB or within the process.<br>
-  If DyanamoDB is choosed the tables are created in the initialization as the SNS topic where all users phone numbers are subscribed.<br>
-  The billing method for DynamoDB is on demand.<br>
-  Chunify sends a sms to all users with phone number registered when a new music is added.<br>

### How to use

*1 - Clone repository*
```bash
git clone https://github.com/rafaeldex/chunify.git path/to/folder
```

*2 - Set your aws credentials path in .env*
```html
AWS_DIR=/path/to/your/.aws
```

*3 - Choose the type of data storage in /code/core/app.py*
```python
# COMPLETE: Uses DynamoDB on demand
# BETA: Uses in process storage (local tests)
version = 'COMPLETE'
```

*4 - Run docker-compose*
```bash
docker-compose up
```

*5 - Access localhost in your browser*
```html
http://localhost
```

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
-  CloudWatch enabled for SNS

### AWS services used

-  Lambda
-  DynamoDB
-  CloudWatch
-  SNS
-  IAM
-  Api Gateway

### License

-  Feel free to clone, use and work with this code
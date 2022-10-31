### Chunify

A simple application to create rest api in lambda functions based on chalice framework.
This rest api simulates an app like spotify where we can manage users, playlists and musics.
Chunify sends a sms to all users with phone number registered When a new music is added.

### How to use

*1 - Clone repository*
```bash
git clone https://github.com/rafaeldex/chunify.git path/to/folder
```

*2 - Set your aws credentials in ./docker-compose.yaml*
```html
- /path/to/your/.aws:/root/.aws
```

*3 - Run docker-compose*
```bash
docker-compose up
```

*4 - Access localhost in your browser*


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

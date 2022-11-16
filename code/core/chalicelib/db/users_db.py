from uuid import uuid4
import json
from chalicelib.services.sns import Sns
import boto3
from botocore.exceptions import ClientError
from chalice import BadRequestError, ChaliceViewError, NotFoundError

class UsersDB:
  dynamodb = boto3.resource('dynamodb')
  users_table = dynamodb.Table('chunify-users')
  response = {}

  # Lists all users
  def get_users(self):
    try:
      self.response = self.users_table.scan()
    except ClientError as e:
      raise BadRequestError("%s" % e)
    else:
      try:      
        if int(self.response['ResponseMetadata']['HTTPStatusCode']) == 200:
          if 'Items' in self.response:
            users = []
            for user in self.response['Items']:
              users.append(
                {
                  'id': user['id'],
                  'name' : user['name'],
                  'age': user['age'],
                  'phone': user['phone']
                }
              )
            return users 
        return []
      except:
        raise ChaliceViewError("%s" % self.response)

  # Lists single user
  def get_user(self, user_id):
    if user_id == None:
      raise ChaliceViewError("User id must be a valid value")

    try:
      self.response = self.users_table.get_item(
        Key={
          'id': user_id
        }
      )
    except ClientError as e:
      raise BadRequestError("%s" % e)
    else:
      try:
        if int(self.response['ResponseMetadata']['HTTPStatusCode']) == 200:
          if 'Item' in self.response:
            return {
              'id': self.response['Item']['id'],
              'name' : self.response['Item']['name'],
              'age': self.response['Item']['age'],
              'phone': self.response['Item']['phone']
            }
        return {}
      except:      
        raise ChaliceViewError("%s" % self.response)

  # Inserts user
  def create_user(self, topic_arn, user):
    uid = str(uuid4())
    user['id'] = uid
    try:
      self.response = self.users_table.put_item(
        Item=user
      )
      if 'phone' in user & user['phone'] != None:
        Sns().subscribe(topic_arn, 'sms', user['phone'])
    except ClientError as e:
      raise BadRequestError("%s" % e)
    else:
      try:
        if int(self.response['ResponseMetadata']['HTTPStatusCode']) == 200:
          return {
            'id': user['id'],
            'name' : user['name'],
            'age': user['age'],
            'phone': user['phone']
          }
        return {}
      except:
        raise ChaliceViewError("%s" % self.response)


  # Updates user
  def update_user(self, user_id, user_data):
    user = self.get_user(user_id)
    if user == {}:
      raise NotFoundError("Something is wrong with the user id %s" % user_id)   
    
    if 'name' in user_data:
      user['name'] = user_data['name']
    if 'age' in user_data:
      user['age'] = user_data['age']
    if 'phone' in user_data:
      user['phone'] = user_data['phone']
    
    try:
      self.response = self.users_table.put_item(
        Item=user
      )
    except ClientError as e:
      raise BadRequestError("%s" % e)
    else:
      try:        
        if int(self.response['ResponseMetadata']['HTTPStatusCode']) == 200:
          return {
            'id': user['id'],
            'name' : user['name'],
            'age': user['age'],
            'phone': user['phone']
          }
        return {}
      except:
        raise ChaliceViewError("%s" % self.response)
   

  # Deletes user
  def delete_user(self, user_id):   
    user = self.get_user(user_id)
    if user == {}:
      raise NotFoundError("Something is wrong with the user id %s" % user_id)          

    try:
      self.response = self.users_table.delete_item(
        Key={
          'id': user['id'],
        }
      )
    except ClientError as e:
      raise BadRequestError("%s" % e)
    else:
      try: 
        if int(self.response['ResponseMetadata']['HTTPStatusCode']) == 200:
          return { 'id': user['id'] }
        return {}
      except:
        raise ChaliceViewError("%s" % self.response)

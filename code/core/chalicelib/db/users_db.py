from uuid import uuid4
import json
import boto3

class UsersDB:
  dynamodb = boto3.resource('dynamodb')
  users_table = dynamodb.Table('chunify-users')

  # Lists all users
  def show_all(self):
    return self.users_table.scan()

  # Lists single user
  def show(self, id):
    response = self.users_table.get_item(
      Key={
        'id': id
      }
    )
    return response

  # Inserts user
  def insert(self, user):
    uid = str(uuid4())    
    user['id'] = uid

    response = self.users_table.put_item(
      Item=user
    )

    if int(response['ResponseMetadata']['HTTPStatusCode']) == 200:
      return {
        'id': user['id'],
        'name' : user['name'],
        'age': user['age'],
        'phone': user['phone']
      }
    else:
      return {}

  # Updates user
  def update(self, user_data):
    user = self.show(user_data['id'])
    
    if 'id' in user_data:
      user['id'] = user_data['id']
    if 'name' in user_data:
      user['name'] = user_data['name']
    if 'age' in user_data:
      user['age'] = user_data['age']
    if 'phone' in user_data:
      user['phone'] = user_data['phone']
    
    response = self.users_table.put_item(
      Item=user
    )
    
    if int(response['ResponseMetadata']['HTTPStatusCode']) == 200:
      return {
        'id': user['id'],
        'name' : user['name'],
        'age': user['age'],
        'phone': user['phone']
      }
    else: 
      return {}      

  # Deletes user
  def delete(self, id):
    response = self.users_table.delete_item(
      Key={
        'id': id,
      }
    )

    if int(response['ResponseMetadata']['HTTPStatusCode']) == 200:
      return id
    else: 
      return None
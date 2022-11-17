from uuid import uuid4
import json
import chalicelib.memory.data_initializer as DataInitializer
from chalice import ChaliceViewError, NotFoundError

class UsersData:
  # Lists all users
  def get_users(self):
    try:
      if len(DataInitializer.data[0]) > 0:
        response = []
        for user in DataInitializer.data[0]:
          response.append({
            'id': user['id'],
            'name' : user['name'],
            'age': user['age'],
            'phone': user['phone']
          })
        return response 
      return []
    except Exception as e:
      raise ChaliceViewError("Something was wrong scanning users: %s" % e)

  # Lists single user
  def get_user(self, id):
    try:
      if len(DataInitializer.data[0]) > 0:
        for user in DataInitializer.data[0]:
          if user['id'] == id:
            return {
              'id': user['id'],
              'name' : user['name'],
              'age': user['age'],
              'phone': user['phone']
            }
      return {}
    except Exception as e:
      raise ChaliceViewError("Something was wrong looking for the user: %s" % e)

  # Inserts user
  def create_user(self, user, topic_arn=None):
    try:
      uid = str(uuid4())
      user['id'] = uid

      DataInitializer.data[0].append(user)

      return {
        'id': user['id'],
        'name' : user['name'],
        'age': user['age'],
        'phone': user['phone']
      }
    except Exception as e:
      raise ChaliceViewError("Something was wrong creating the user: %s" % e)

  # Updates user
  def update_user(self, user_id, user_data, topic_arn=None):
    user = self.get_user(user_id)
    if user == {}:
      raise NotFoundError("Something is wrong with the user id %s" % user_id)  

    try:
      index = DataInitializer.data[0].index(user)

      if 'name' in user_data:
        user['name'] = user_data['name']
      if 'age' in user_data:
        user['age'] = user_data['age']
      if 'phone' in user_data:
        user['phone'] = user_data['phone']
      
      DataInitializer.data[0][index] = user
      
      return {
        'id': user['id'],
        'name' : user['name'],
        'age': user['age'],
        'phone': user['phone']
      }    
    except Exception as e:
      raise ChaliceViewError("Something was wrong updating the user: %s" % e)    

  # Deletes user
  def delete_user(self, user_id):
    user = self.get_user(user_id)
    if user == {}:
      raise NotFoundError("Something is wrong with the user id %s" % user_id)  

    try:
      DataInitializer.data[0].remove(user)
      return { 'id': user['id'] }
    except Exception as e:
      raise ChaliceViewError("Something was wrong deleting the user: %s" % e)

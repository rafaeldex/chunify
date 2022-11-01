from uuid import uuid4
import json
import chalicelib.memory.data_initializer as DataInitializer

class UsersData:
  # Lists all users
  def show_all(self):
    return DataInitializer.data[0]

  # Lists single user
  def show(self, id):
    response = {}

    users = DataInitializer.data[0]
    for user in users:
      if user['id'] == id:
        response = {
          'id': user['id'],
          'name' : user['name'],
          'age': user['age'],
          'phone': user['phone']
        }
 
    return response

  # Inserts user
  def insert(self, user):
    uid = str(uuid4())
    user['id'] = uid

    DataInitializer.data[0].append(user)

    return {
      'id': user['id'],
      'name' : user['name'],
      'age': user['age'],
      'phone': user['phone']
    }

  # Updates user
  def update(self, user_data):
    response = {}
    user = self.show(user_data['id'])
    
    if not user == {}:
      index = DataInitializer.data[0].index(user)

      if 'name' in user_data:
        user['name'] = user_data['name']
      if 'age' in user_data:
        user['age'] = user_data['age']
      if 'phone' in user_data:
        user['phone'] = user_data['phone']
      
      DataInitializer.data[0][index] = user
      
      response = {
        'id': user['id'],
        'name' : user['name'],
        'age': user['age'],
        'phone': user['phone']
      }

    return response       

  # Deletes user
  def delete(self, id):
    response = { 'id' : ''}
    user = self.show(id)

    if not user == {}:
      DataInitializer.data[0].remove(user)
      response = { 'id': id }

    return response   

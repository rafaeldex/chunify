import json
from chalicelib.db.users_db import UsersDB
import unittest

class TestUsersDB(unittest.TestCase): 
  def test_can_insert_and_retrieve_user(self):
    user = json.loads('{ "name": "Tester", "age": 40, "phone": "5586999945388" }')
    inserted_user = UsersDB().insert(user)
    response = UsersDB().show(inserted_user['id'])
    self.assertEqual(response['Item'], user)

  def test_can_insert_and_list_all_users(self):
    found = False
    user = json.loads('{ "name": "Tester", "age": 40, "phone": "5586999945388" }')
    inserted_user = UsersDB().insert(user)
    all_users = UsersDB().show_all()
    if inserted_user in all_users['Items']:
      found = True
    self.assertEqual(found, True)

  def test_can_insert_and_update_user(self):
    user = json.loads('{ "name": "Tester", "age": 40, "phone": "5586999945388" }')
    inserted_user = UsersDB().insert(user)
    user['id'] = inserted_user['id']
    user['age'] = 40
    updated_user = UsersDB().update(user)
    self.assertEqual(updated_user, user)

  def test_can_insert_and_delete_user(self):
    user = json.loads('{ "name": "Tester", "age": 40, "phone": "5586999945388" }')
    inserted_user = UsersDB().insert(user)
    user['id'] = inserted_user['id']
    user['age'] = 40
    uid = UsersDB().delete(user['id'])
    self.assertEqual(uid, user['id'])

if __name__ == '__main__':
    unittest.main()

import json
from chalicelib.memory.data_initializer import DataInitializer
from chalicelib.memory.users_data import UsersData
import unittest

class TestUsersData(unittest.TestCase):
  def setUp(self):
    DataInitializer().initialize()

  def test_can_insert_and_retrieve_user(self):
    user = json.loads('{ "name": "Tester", "age": 33, "phone": "5585981661026" }')
    inserted_user = UsersData().insert(user)
    response = UsersData().show(inserted_user['id'])
    self.assertEqual(response, user)

  def test_can_insert_and_list_all_users(self):
    found = False
    user = json.loads('{ "name": "Tester", "age": 33, "phone": "5585981661026" }')
    inserted_user = UsersData().insert(user)
    all_users = UsersData().show_all()
    if inserted_user in all_users:
      found = True
    self.assertEqual(found, True)

  def test_can_insert_and_update_user(self):
    user = json.loads('{ "name": "Tester", "age": 33, "phone": "5585981661026" }')
    inserted_user = UsersData().insert(user)
    user['id'] = inserted_user['id']
    user['age'] = 40
    updated_user = UsersData().update(user)
    self.assertEqual(updated_user, user)

  def test_can_insert_and_delete_user(self):
    user = json.loads('{ "name": "Tester", "age": 33, "phone": "5585981661026" }')
    inserted_user = UsersData().insert(user)
    user['id'] = inserted_user['id']
    user['age'] = 40
    deleted_id = UsersData().delete(user['id'])
    self.assertEqual(deleted_id['id'], user['id'])    

if __name__ == '__main__':
    unittest.main()

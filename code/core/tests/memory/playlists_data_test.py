import json
from chalicelib.memory.data_initializer import DataInitializer
from chalicelib.memory.users_data import UsersData
from chalicelib.memory.playlists_data import PlaylistsData
import unittest

class TestPlaylistsData(unittest.TestCase): 
  def setUp(self):
    DataInitializer().initialize()

  def test_can_insert_and_retrieve_playlist(self):
    user = json.loads('{ "name": "Tester", "age": 40, "phone": "5586999945388" }')
    inserted_user = UsersData().insert(user)
    playlist = json.loads('{ "name": "Lets Rock" }')
    playlist['user_id'] = inserted_user['id']
    inserted_playlist = PlaylistsData().insert(playlist)
    response = PlaylistsData().show(inserted_playlist['id'])
    self.assertEqual(response, playlist)

  def test_can_insert_and_list_all_playlists(self):
    found = False
    user = json.loads('{ "name": "Tester", "age": 40, "phone": "5586999945388" }')
    inserted_user = UsersData().insert(user)
    playlist = json.loads('{ "name": "Lets Rock" }')
    playlist['user_id'] = inserted_user['id']
    inserted_playlist = PlaylistsData().insert(playlist)
    all_playlists = PlaylistsData().show_all()
    if playlist in all_playlists:
      found = True
    self.assertEqual(found, True)

  def test_can_insert_and_list_all_playlists_from_user(self):
    found = False
    user = json.loads('{ "name": "Tester", "age": 40, "phone": "5586999945388" }')
    inserted_user = UsersData().insert(user)
    playlist = json.loads('{ "name": "Lets Rock" }')
    playlist['user_id'] = inserted_user['id']
    inserted_playlist = PlaylistsData().insert(playlist)
    all_playlists = PlaylistsData().show_from_user(inserted_user['id'])
    if inserted_playlist in all_playlists:
      found = True
    self.assertEqual(found, True)    

  def test_can_insert_and_update_playlist(self):
    user = json.loads('{ "name": "Tester", "age": 40, "phone": "5586999945388" }')
    inserted_user = UsersData().insert(user)
    playlist = json.loads('{ "name": "Lets Rock" }')
    playlist['user_id'] = inserted_user['id']
    inserted_playlist = PlaylistsData().insert(playlist)
    playlist['id'] = inserted_playlist['id']
    playlist['name'] = 'Lets Rock Today'
    updated_playlist = PlaylistsData().update(playlist)
    self.assertEqual(updated_playlist, playlist)

  def test_can_insert_and_delete_playlist(self):
    user = json.loads('{ "name": "Tester", "age": 40, "phone": "5586999945388" }')
    inserted_user = UsersData().insert(user)
    playlist = json.loads('{ "name": "Lets Rock" }')
    playlist['user_id'] = inserted_user['id']
    inserted_playlist = PlaylistsData().insert(playlist)
    playlist['id'] = inserted_playlist['id']
    deleted_id = PlaylistsData().delete(playlist['id'])
    self.assertEqual(deleted_id['id'], playlist['id'])

if __name__ == '__main__':
    unittest.main()

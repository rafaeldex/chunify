import json
from chalicelib.db.users_db import UsersDB
from chalicelib.db.playlists_db import PlaylistsDB
import unittest

class TestPlaylistsDB(unittest.TestCase): 
  def test_can_insert_and_retrieve_playlist(self):
    user = json.loads('{ "name": "Tester", "age": 40, "phone": "5586999945388" }')
    inserted_user = UsersDB().insert(user)
    playlist = json.loads('{ "name": "Lets Rock" }')
    playlist['user_id'] = inserted_user['id']
    inserted_playlist = PlaylistsDB().insert(playlist)
    response = PlaylistsDB().show(inserted_playlist['id'])
    self.assertEqual(response['Item'], playlist)

  def test_can_insert_and_list_all_playlists(self):
    found = False
    user = json.loads('{ "name": "Tester", "age": 40, "phone": "5586999945388" }')
    inserted_user = UsersDB().insert(user)
    playlist = json.loads('{ "name": "Lets Rock" }')
    playlist['user_id'] = inserted_user['id']
    inserted_playlist = PlaylistsDB().insert(playlist)
    all_playlists = PlaylistsDB().show_all()
    if playlist in all_playlists['Items']:
      found = True
    self.assertEqual(found, True)

  def test_can_insert_and_list_all_playlists_from_user(self):
    found = False
    user = json.loads('{ "name": "Tester", "age": 40, "phone": "5586999945388" }')
    inserted_user = UsersDB().insert(user)
    playlist = json.loads('{ "name": "Lets Rock" }')
    playlist['user_id'] = inserted_user['id']
    inserted_playlist = PlaylistsDB().insert(playlist)
    all_playlists = PlaylistsDB().show_from_user(inserted_user['id'])
    if inserted_playlist in all_playlists['Items']:
      found = True
    self.assertEqual(found, True)    

  def test_can_insert_and_update_playlist(self):
    user = json.loads('{ "name": "Tester", "age": 40, "phone": "5586999945388" }')
    inserted_user = UsersDB().insert(user)
    playlist = json.loads('{ "name": "Lets Rock" }')
    playlist['user_id'] = inserted_user['id']
    inserted_playlist = PlaylistsDB().insert(playlist)
    playlist['id'] = inserted_playlist['id']
    playlist['name'] = 'Lets Rock Today'
    updated_playlist = PlaylistsDB().update(playlist)
    self.assertEqual(updated_playlist, playlist)

  def test_can_insert_and_delete_playlist(self):
    user = json.loads('{ "name": "Tester", "age": 40, "phone": "5586999945388" }')
    inserted_user = UsersDB().insert(user)
    playlist = json.loads('{ "name": "Lets Rock" }')
    playlist['user_id'] = inserted_user['id']
    inserted_playlist = PlaylistsDB().insert(playlist)
    playlist['id'] = inserted_playlist['id']
    uid = PlaylistsDB().delete(playlist['id'])
    self.assertEqual(uid, playlist['id'])

if __name__ == '__main__':
    unittest.main()

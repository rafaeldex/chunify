import json
from chalicelib.memory.data_initializer import DataInitializer
from chalicelib.memory.users_data import UsersData
from chalicelib.memory.playlists_data import PlaylistsData
from chalicelib.memory.musics_data import MusicsData
import unittest

class TestMusicsData(unittest.TestCase): 
  def setUp(self):
    DataInitializer().initialize()
      
  def test_can_insert_and_retrieve_music(self):
    user = json.loads('{ "name": "Tester", "age": 40, "phone": "5586999945388" }')
    inserted_user = UsersData().insert(user)
    playlist = json.loads('{ "name": "Lets Rock" }')
    playlist['user_id'] = inserted_user['id']
    inserted_playlist = PlaylistsData().insert(playlist)
    music = json.loads('{ "name": "Always", "artist": "Jon Bon Jovi", "album": "Cross Road", "year": "1994" }')
    music['playlist_id'] = inserted_playlist['id']
    inserted_music = MusicsData().insert(music)
    response = MusicsData().show(inserted_music['id'])
    self.assertEqual(response, music)

  def test_can_insert_and_list_all_musics(self):
    found = False
    user = json.loads('{ "name": "Tester", "age": 40, "phone": "5586999945388" }')
    inserted_user = UsersData().insert(user)   
    playlist = json.loads('{ "name": "Lets Rock" }')
    playlist['user_id'] = inserted_user['id']
    inserted_playlist = PlaylistsData().insert(playlist)
    music = json.loads('{ "name": "Always", "artist": "Jon Bon Jovi", "album": "Cross Road", "year": "1994" }')
    music['playlist_id'] = inserted_playlist['id']
    inserted_music = MusicsData().insert(music)
    all_musics = MusicsData().show_all()
    if inserted_music in all_musics:
      found = True
    self.assertEqual(found, True)

  def test_can_insert_and_list_all_music_from_playlist(self):
    found = False
    user = json.loads('{ "name": "Tester", "age": 40, "phone": "5586999945388" }')
    inserted_user = UsersData().insert(user)
    playlist = json.loads('{ "name": "Lets Rock" }')
    playlist['user_id'] = inserted_user['id']
    inserted_playlist = PlaylistsData().insert(playlist)
    music = json.loads('{ "name": "Always", "artist": "Jon Bon Jovi", "album": "Cross Road", "year": "1994" }')
    music['playlist_id'] = inserted_playlist['id']
    inserted_music = MusicsData().insert(music)
    all_musics = MusicsData().show_from_playlist(inserted_playlist['id'])
    if music in all_musics:
      found = True
    self.assertEqual(found, True)    

  def test_can_insert_and_update_music(self):
    user = json.loads('{ "name": "Tester", "age": 40, "phone": "5586999945388" }')
    inserted_user = UsersData().insert(user)
    playlist = json.loads('{ "name": "Lets Rock" }')
    playlist['user_id'] = inserted_user['id']
    inserted_playlist = PlaylistsData().insert(playlist)
    music = json.loads('{ "name": "Always", "artist": "Jon Bon Jovi", "album": "Cross Road", "year": "1994" }')
    music['playlist_id'] = inserted_playlist['id']
    inserted_music = MusicsData().insert(music)
    music['id'] = inserted_music['id']
    music['name'] = "Always - JBJ"
    updated_music = MusicsData().update(music)
    self.assertEqual(updated_music, music)

  def test_can_insert_and_delete_music(self):
    user = json.loads('{ "name": "Tester", "age": 40, "phone": "5586999945388" }')
    inserted_user = UsersData().insert(user)
    playlist = json.loads('{ "name": "Lets Rock" }')
    playlist['user_id'] = inserted_user['id']
    inserted_playlist = PlaylistsData().insert(playlist)
    music = json.loads('{ "name": "Always", "artist": "Jon Bon Jovi", "album": "Cross Road", "year": "1994" }')
    music['playlist_id'] = inserted_playlist['id']
    inserted_music = MusicsData().insert(music)
    music['id'] = inserted_music['id']
    deleted_id = MusicsData().delete(music['id'])
    self.assertEqual(deleted_id['id'], music['id'])

if __name__ == '__main__':
    unittest.main()

import json
from chalicelib.db.users_db import UsersDB
from chalicelib.db.playlists_db import PlaylistsDB
from chalicelib.db.musics_db import MusicsDB
import unittest

class TestMusicsDB(unittest.TestCase): 
  def test_can_insert_and_retrieve_music(self):
    user = json.loads('{ "name": "Tester", "age": 40, "phone": "5586999945388" }')
    inserted_user = UsersDB().insert(user)
    playlist = json.loads('{ "name": "Lets Rock" }')
    playlist['user_id'] = inserted_user['id']
    inserted_playlist = PlaylistsDB().insert(playlist)
    music = json.loads('{ "name": "Always", "artist": "Jon Bon Jovi", "album": "Cross Road", "year": "1994" }')
    music['playlist_id'] = inserted_playlist['id']
    inserted_music = MusicsDB().insert(music)
    response = MusicsDB().show(inserted_music['id'])
    self.assertEqual(response['Item'], music)

  def test_can_insert_and_list_all_musics(self):
    found = False
    user = json.loads('{ "name": "Tester", "age": 40, "phone": "5586999945388" }')
    inserted_user = UsersDB().insert(user)   
    playlist = json.loads('{ "name": "Lets Rock" }')
    playlist['user_id'] = inserted_user['id']
    inserted_playlist = PlaylistsDB().insert(playlist)
    music = json.loads('{ "name": "Always", "artist": "Jon Bon Jovi", "album": "Cross Road", "year": "1994" }')
    music['playlist_id'] = inserted_playlist['id']
    inserted_music = MusicsDB().insert(music)
    all_musics = MusicsDB().show_all()
    if inserted_music in all_musics['Items']:
      found = True
    self.assertEqual(found, True)

  def test_can_insert_and_list_all_music_from_playlist(self):
    found = False
    user = json.loads('{ "name": "Tester", "age": 40, "phone": "5586999945388" }')
    inserted_user = UsersDB().insert(user)
    playlist = json.loads('{ "name": "Lets Rock" }')
    playlist['user_id'] = inserted_user['id']
    inserted_playlist = PlaylistsDB().insert(playlist)
    music = json.loads('{ "name": "Always", "artist": "Jon Bon Jovi", "album": "Cross Road", "year": "1994" }')
    music['playlist_id'] = inserted_playlist['id']
    inserted_music = MusicsDB().insert(music)
    all_musics = MusicsDB().show_from_playlist(inserted_playlist['id'])
    if music in all_musics['Items']:
      found = True
    self.assertEqual(found, True)    

  def test_can_insert_and_update_music(self):
    user = json.loads('{ "name": "Tester", "age": 40, "phone": "5586999945388" }')
    inserted_user = UsersDB().insert(user)
    playlist = json.loads('{ "name": "Lets Rock" }')
    playlist['user_id'] = inserted_user['id']
    inserted_playlist = PlaylistsDB().insert(playlist)
    music = json.loads('{ "name": "Always", "artist": "Jon Bon Jovi", "album": "Cross Road", "year": "1994" }')
    music['playlist_id'] = inserted_playlist['id']
    inserted_music = MusicsDB().insert(music)
    music['id'] = inserted_music['id']
    music['name'] = "Always - JBJ"
    updated_music = MusicsDB().update(music)
    self.assertEqual(updated_music, music)

  def test_can_insert_and_delete_music(self):
    user = json.loads('{ "name": "Tester", "age": 40, "phone": "5586999945388" }')
    inserted_user = UsersDB().insert(user)
    playlist = json.loads('{ "name": "Lets Rock" }')
    playlist['user_id'] = inserted_user['id']
    inserted_playlist = PlaylistsDB().insert(playlist)
    music = json.loads('{ "name": "Always", "artist": "Jon Bon Jovi", "album": "Cross Road", "year": "1994" }')
    music['playlist_id'] = inserted_playlist['id']
    inserted_music = MusicsDB().insert(music)
    music['id'] = inserted_music['id']
    uid = MusicsDB().delete(music['id'])
    self.assertEqual(uid, music['id'])

if __name__ == '__main__':
    unittest.main()

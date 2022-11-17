from uuid import uuid4
import json
import chalicelib.memory.data_initializer as DataInitializer
from chalicelib.memory.users_data import UsersData
from chalicelib.memory.playlists_data import PlaylistsData
from chalice import ChaliceViewError, NotFoundError

class MusicsData:
  # Returns user
  def get_user(self, user_id):
    user = UsersData().get_user(user_id)
    if user == {}:
      raise NotFoundError("Something is wrong with the user id %s" % user_id)
    return user

  # Returns playlist
  def get_playlist(self, user_id, playlist_id):
    user = self.get_user(user_id)
    playlist = PlaylistsData().get_playlist(user['id'], playlist_id)
    if playlist == {}:
      raise NotFoundError("Something is wrong with the playlist id %s" % playlist_id)
    return playlist

  # Lists all musics
  def get_musics(self, user_id, playlist_id):
    user = self.get_user(user_id)
    playlist = self.get_playlist(user['id'], playlist_id)
    try:
      if len(DataInitializer.data[2]) > 0:
        response = []
        for music in DataInitializer.data[2]:
          if music['playlist_id'] == playlist['id']:
            response.append({
              'id': music['id'],
              'name' : music['name'],
              'artist': music['artist'],
              'album': music['album'],
              'year': music['year'],
              'playlist_id': music['playlist_id']
            })
        return response 
      return []
    except Exception as e:
      raise ChaliceViewError("Something was wrong scanning musics: %s" % e)

  # Lists single music
  def get_music(self, user_id, playlist_id, music_id):
    user = self.get_user(user_id)
    playlist = self.get_playlist(user['id'], playlist_id)
    musics = self.get_musics(user['id'], playlist['id'])
    try:
      if len(musics) > 0:
        for music in musics:
          if music['id'] == music_id:
            return {
              'id': music['id'],
              'name' : music['name'],
              'artist': music['artist'],
              'album': music['album'],
              'year': music['year'],
              'playlist_id': music['playlist_id']
            }
      return {}
    except Exception as e:
      raise ChaliceViewError("Something was wrong looking for the music: %s" % e) 

  # Inserts music
  def create_music(self, user_id, playlist_id, music):
    user = self.get_user(user_id)
    playlist = self.get_playlist(user['id'], playlist_id)
    try:
      uid = str(uuid4())
      music['id'] = uid
      music['playlist_id'] = playlist['id']

      DataInitializer.data[2].append(music)

      return {
        'id': music['id'],
        'name' : music['name'],
        'artist': music['artist'],
        'album': music['album'],
        'year': music['year'],
        'playlist_id': music['playlist_id']
      }
    except Exception as e:
      raise ChaliceViewError("Something was wrong creating the music: %s" % e)  

  # Updates music
  def update_music(self, user_id, playlist_id, music_id, music_data):
    user = self.get_user(user_id)
    playlist = self.get_playlist(user['id'], playlist_id)
    music = self.get_music(user['id'], playlist['id'], music_id)
    if music == {}:
      raise NotFoundError("Something is wrong with the music id %s" % music_id) 
    
    try:
      index = DataInitializer.data[2].index(music)
    
      if "name" in music_data:
        music["name"] = music_data["name"]
      if "artist" in music_data:
        music["artist"] = music_data["artist"]
      if "album" in music_data:
        music["album"] = music_data["album"]
      if "year" in music_data:
        music["year"] = music_data["year"]
      
      DataInitializer.data[2][index] = music
      
      return {
        'id': music['id'],
        'name' : music['name'],
        'artist': music['artist'],
        'album': music['album'],
        'year': music['year'],
        'playlist_id': music['playlist_id']
      }
    except Exception as e:
      raise ChaliceViewError("Something was wrong updating the music: %s" % e)       

  # Deletes music
  def delete_music(self, user_id, playlist_id, music_id):
    user = self.get_user(user_id)
    playlist = self.get_playlist(user['id'], playlist_id)
    music = self.get_music(user['id'], playlist['id'], music_id)
    if music == {}:
      raise NotFoundError("Something is wrong with the music id %s" % music_id) 

    try:
      DataInitializer.data[2].remove(music)
      return { 'id': music['id'] }
    except Exception as e:
      raise ChaliceViewError("Something was wrong deleting the music: %s" % e)    

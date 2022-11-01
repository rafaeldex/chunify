from uuid import uuid4
import json
import chalicelib.memory.data_initializer as DataInitializer

class MusicsData:
  # Lists all musics
  def show_all(self):
    return DataInitializer.data[2]

  # Lists single music
  def show(self, id):
    response = {}

    musics = DataInitializer.data[2]
    for music in musics:
      if music['id'] == id:
        response = {
          'id': music['id'],
          'name' : music['name'],
          'artist': music['artist'],
          'album': music['album'],
          'year': music['year'],
          'playlist_id': music['playlist_id']
        }
 
    return response

  # Lists all playlists that belongs to a playlist
  def show_from_playlist(self, playlist_id):
    response = []

    musics = DataInitializer.data[2]
    for music in musics:
      if music['playlist_id'] == playlist_id:
        response.append({
          'id': music['id'],
          'name' : music['name'],
          'artist': music['artist'],
          'album': music['album'],
          'year': music['year'],
          'playlist_id': music['playlist_id']
        })
 
    return response 

  # Inserts music
  def insert(self, music):
    uid = str(uuid4())
    music['id'] = uid

    DataInitializer.data[2].append(music)

    return {
      'id': music['id'],
      'name' : music['name'],
      'artist': music['artist'],
      'album': music['album'],
      'year': music['year'],
      'playlist_id': music['playlist_id']
    }

  # Updates music
  def update(self, music_data):
    response = {}
    music = self.show(music_data['id'])
    
    if not music == {}:
      index = DataInitializer.data[2].index(music)
    
      if "name" in music_data:
        music["name"] = music_data["name"]
      if "artist" in music_data:
        music["artist"] = music_data["artist"]
      if "album" in music_data:
        music["album"] = music_data["album"]
      if "year" in music_data:
        music["year"] = music_data["year"]   
      if "playlist_id" in music_data:
        music["playlist_id"] = music_data["playlist_id"]  
    
      DataInitializer.data[2][index] = music

      response = {
        'id': music['id'],
        'name' : music['name'],
        'artist': music['artist'],
        'album': music['album'],
        'year': music['year'],
        'playlist_id': music['playlist_id']
      }

    return response         

  # Deletes music
  def delete(self, id):
    response = { 'id' : ''}
    music = self.show(id)

    if not music == {}:
      DataInitializer.data[2].remove(music)
      response = { 'id': id }

    return response

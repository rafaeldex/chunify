from uuid import uuid4
import json
import chalicelib.memory.data_initializer as DataInitializer

class PlaylistsData:
  # Lists all playlists
  def show_all(self):
    return DataInitializer.data[1]

  # Lists single playlist
  def show(self, id):
    response = {}

    playlists = DataInitializer.data[1]
    for playlist in playlists:
      if playlist['id'] == id:
        response = {
          'id': playlist['id'],
          'name' : playlist['name'],
          'user_id': playlist['user_id']
        }
 
    return response

  # Lists all playlists that belongs to an user
  def show_from_user(self, user_id):
    response = []

    playlists = DataInitializer.data[1]
    for playlist in playlists:
      if playlist['user_id'] == user_id:
        response.append({
          'id': playlist['id'],
          'name' : playlist['name'],
          'user_id': playlist['user_id']
        })
 
    return response

  # Inserts playlist
  def insert(self, playlist):
    uid = str(uuid4())
    playlist['id'] = uid

    DataInitializer.data[1].append(playlist)

    return {
      'id': playlist['id'],
      'name' : playlist['name'],
      'user_id': playlist['user_id']
    }

  # Updates playlist
  def update(self, playlist_data):
    response = {}
    playlist = self.show(playlist_data['id'])
    
    if not playlist == {}:
      index = DataInitializer.data[1].index(playlist)
    
      if "name" in playlist_data:
        playlist["name"] = playlist_data["name"]
      if "user_id" in playlist_data:
        playlist["user_id"] = playlist_data["user_id"]
      
      DataInitializer.data[1][index] = playlist
      
      response = {
        'id': playlist['id'],
        'name' : playlist['name'],
        'user_id': playlist['user_id']
      }

    return response 
   

  # Deletes playlist
  def delete(self, id):
    response = { 'id' : ''}
    playlist = self.show(id)

    if not playlist == {}:
      DataInitializer.data[1].remove(playlist)
      response = { 'id': id }

    return response

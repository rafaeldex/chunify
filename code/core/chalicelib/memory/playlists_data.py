from uuid import uuid4
import json
import chalicelib.memory.data_initializer as DataInitializer
from chalicelib.memory.users_data import UsersData
from chalice import ChaliceViewError, NotFoundError

class PlaylistsData:
  # Returns user
  def get_user(self, user_id):
    user = UsersData().get_user(user_id)
    if user == {}:
      raise NotFoundError("Something is wrong with the user id %s" % user_id)
    return user

  # Lists all playlists
  def get_playlists(self, user_id):
    user = self.get_user(user_id)
    try:
      if len(DataInitializer.data[1]) > 0:
        response = []
        for playlist in DataInitializer.data[1]:
          if playlist['user_id'] == user['id']:
            response.append({
              'id': playlist['id'],
              'name' : playlist['name'],
              'user_id': playlist['user_id']
            })
        return response 
      return []
    except Exception as e:
      raise ChaliceViewError("Something was wrong scanning playlists: %s" % e)

  # Lists single playlist
  def get_playlist(self, user_id, playlist_id):
    user = self.get_user(user_id)
    playlists = self.get_playlists(user['id'])
    try:
      if len(playlists) > 0:
        for playlist in playlists:
          if playlist['id'] == playlist_id:
            return {
              'id': playlist['id'],
              'name' : playlist['name'],
              'user_id': playlist['user_id']
            }
      return {}
    except Exception as e:
      raise ChaliceViewError("Something was wrong looking for the playlist: %s" % e)  

  # Inserts playlist
  def create_playlist(self, user_id, playlist):
    user = self.get_user(user_id)
    try:
      uid = str(uuid4())
      playlist['id'] = uid
      playlist['user_id'] = user['id']

      DataInitializer.data[1].append(playlist)

      return {
        'id': playlist['id'],
        'name' : playlist['name'],
        'user_id': playlist['user_id']
      }
    except Exception as e:
      raise ChaliceViewError("Something was wrong creating the playlist: %s" % e)  
  
  # Updates playlist
  def update_playlist(self, user_id, playlist_id, playlist_data):
    user = self.get_user(user_id)
    playlist = self.get_playlist(user['id'], playlist_id)
    if playlist == {}:
      raise NotFoundError("Something is wrong with the playlist id %s" % playlist_id) 
    
    try:
      index = DataInitializer.data[1].index(playlist)
    
      if "name" in playlist_data:
        playlist["name"] = playlist_data["name"]
      
      DataInitializer.data[1][index] = playlist
      
      return {
        'id': playlist['id'],
        'name' : playlist['name'],
        'user_id': playlist['user_id']
      }
    except Exception as e:
      raise ChaliceViewError("Something was wrong updating the playlist: %s" % e)          

  # Deletes playlist
  def delete_playlist(self, user_id, playlist_id):
    user = self.get_user(user_id)
    playlist = self.get_playlist(user['id'], playlist_id)
    if playlist == {}:
      raise NotFoundError("Something is wrong with the playlist id %s" % playlist_id) 

    try:
      DataInitializer.data[1].remove(playlist)
      return { 'id': playlist['id'] }
    except Exception as e:
      raise ChaliceViewError("Something was wrong deleting the playlist: %s" % e)    

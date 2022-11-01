from uuid import uuid4
import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

class PlaylistsDB:
  dynamodb = boto3.resource('dynamodb')
  playlists_table = dynamodb.Table('chunify-playlists')

  # Lists all playlists
  def show_all(self):
    return self.playlists_table.scan()

  # Lists single playlist
  def show(self, id):
    response = self.playlists_table.get_item(
      Key={
        'id': id
      }
    )
    return response

  # Lists all playlists that belongs to an user
  def show_from_user(self, user_id):
    response = self.playlists_table.scan(
      FilterExpression=Attr('user_id').eq(user_id)
    )
    return response

  # Inserts playlist
  def insert(self, playlist):
    uid = str(uuid4())
    playlist['id'] = uid

    response = self.playlists_table.put_item(
      Item=playlist
    )

    if int(response['ResponseMetadata']['HTTPStatusCode']) == 200:
      return {
        'id': playlist['id'],
        'name' : playlist['name'],
        'user_id': playlist['user_id']
      }
    else:
      return {}

  # Updates playlist
  def update(self, playlist_data):
    playlist = self.show(playlist_data['id'])
    
    if 'id' in playlist_data:
      playlist['id'] = playlist_data['id']
    if 'name' in playlist_data:
      playlist['name'] = playlist_data['name']
    if 'user_id' in playlist_data:
      playlist['user_id'] = playlist_data['user_id']
    
    response = self.playlists_table.put_item(
      Item=playlist
    )
    
    if int(response['ResponseMetadata']['HTTPStatusCode']) == 200:
      return {
        'id': playlist['id'],
        'name' : playlist['name'],
        'user_id': playlist['user_id']
      }
    else: 
      return {}      

  # Deletes playlist
  def delete(self, id):
    response = self.playlists_table.delete_item(
      Key={
        'id': id,
      }
    )

    if int(response['ResponseMetadata']['HTTPStatusCode']) == 200:
      return id
    else: 
      return None
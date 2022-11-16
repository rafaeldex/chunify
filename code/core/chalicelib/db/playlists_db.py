from uuid import uuid4
import json
from chalicelib.db.users_db import UsersDB
import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
from chalice import BadRequestError, ChaliceViewError, NotFoundError

class PlaylistsDB:
  dynamodb = boto3.resource('dynamodb')
  playlists_table = dynamodb.Table('chunify-playlists')
  response = {}

  # Returns user
  def get_user(self, user_id):
    user = UsersDB().get_user(user_id)
    if user == {}:
      raise NotFoundError("Something is wrong with the user id %s" % user_id)
    return user  

  # Lists all playlists
  def get_playlists(self, user_id):
    user = self.get_user(user_id)
    try:
      self.response = self.playlists_table.scan(
        FilterExpression=Attr('user_id').eq(user['id'])
      )
    except ClientError as e:
      raise BadRequestError("%s" % e)
    else:
      try:      
        if int(self.response['ResponseMetadata']['HTTPStatusCode']) == 200:
          if 'Items' in self.response:
            playlists = []
            for playlist in self.response['Items']:
              playlists.append(
                {
                  'id': playlist['id'],
                  'name' : playlist['name'],
                  'user_id': playlist['user_id']
                }
              )
            return playlists 
        return []
      except:
        raise ChaliceViewError("%s" % self.response)    

  # Lists single playlist
  def get_playlist(self, user_id, playlist_id):
    user = self.get_user(user_id)
    if playlist_id == None:
      raise ChaliceViewError("Playlist id must be a valid value")

    try:
      self.response = self.playlists_table.get_item(
        Key={
          'id': playlist_id,
          'user_id': user['id']
        }
      )
    except ClientError as e:
      raise BadRequestError("%s" % e)
    else:
      try:
        if int(self.response['ResponseMetadata']['HTTPStatusCode']) == 200:
          if 'Item' in self.response:
            return {
              'id': self.response['Item']['id'],
              'name' : self.response['Item']['name'],
              'user_id': self.response['Item']['user_id']
            }
        return {}
      except:      
        raise ChaliceViewError("%s" % self.response)    

  # Inserts playlist
  def create_playlist(self, user_id, playlist):
    user = self.get_user(user_id) 
    uid = str(uuid4())
    playlist['id'] = uid
    playlist['user_id'] = user['id']

    try:
      self.response = self.playlists_table.put_item(
        Item=playlist
      )
    except ClientError as e:
      raise BadRequestError("%s" % e)
    else:
      try:
        if int(self.response['ResponseMetadata']['HTTPStatusCode']) == 200:
          return {
            'id': playlist['id'],
            'name' : playlist['name'],
            'user_id': playlist['user_id']
          }
        return {}
      except:
        raise ChaliceViewError("%s" % self.response)    

  # Updates playlist
  def update_playlist(self, user_id, playlist_id, playlist_data):
    user = self.get_user(user_id)
    playlist = self.get_playlist(user['id'], playlist_id)
    if playlist == {}:
      raise NotFoundError("Something is wrong with the playlist id %s" % playlist_id)         
   
    if 'name' in playlist_data:
      playlist['name'] = playlist_data['name']

    try:
      self.response = self.playlists_table.put_item(
        Item=playlist
      )
    except ClientError as e:
      raise BadRequestError("%s" % e)
    else:
      try:        
        if int(self.response['ResponseMetadata']['HTTPStatusCode']) == 200:
          return {
            'id': playlist['id'],
            'name' : playlist['name'],
            'user_id': playlist['user_id']
          }
        return {}
      except:
        raise ChaliceViewError("%s" % self.response)         

  # Deletes playlist
  def delete_playlist(self, user_id, playlist_id):
    user = self.get_user(user_id)
    playlist = self.get_playlist(user['id'], playlist_id)
    if playlist == {}:
      raise NotFoundError("Something is wrong with the playlist id %s" % playlist_id)                

    try:
      self.response = self.playlists_table.delete_item(
        Key={
          'id': playlist['id'],
          'user_id': user['id']
        }
      )
    except ClientError as e:
      raise BadRequestError("%s" % e)
    else:
      try: 
        if int(self.response['ResponseMetadata']['HTTPStatusCode']) == 200:
          return { 'id': playlist['id'] }
        return {}
      except:
        raise ChaliceViewError("%s" % self.response)

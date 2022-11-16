from uuid import uuid4
import json
from chalicelib.db.users_db import UsersDB
from chalicelib.db.playlists_db import PlaylistsDB
import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
from chalice import BadRequestError, ChaliceViewError, NotFoundError

class MusicsDB:
  dynamodb = boto3.resource('dynamodb')
  musics_table = dynamodb.Table('chunify-musics')
  response = {}

  # Returns user
  def get_user(self, user_id):
    user = UsersDB().get_user(user_id)
    if user == {}:
      raise NotFoundError("Something is wrong with the user id %s" % user_id)
    return user

  # Returns playlist
  def get_playlist(self, user_id, playlist_id):
    playlist = PlaylistsDB().get_playlist(user_id, playlist_id)
    if playlist == {}:
      raise NotFoundError("Something is wrong with the playlist id %s" % playlist_id)
    return playlist    

  # Lists all musics
  def get_musics(self, user_id, playlist_id):
    user = self.get_user(user_id)
    playlist = self.get_playlist(user['id'], playlist_id)
    try:
      self.response = self.musics_table.scan(
        FilterExpression=Attr('playlist_id').eq(playlist['id'])
      )
    except ClientError as e:
      raise BadRequestError("%s" % e)
    else:
      try:      
        if int(self.response['ResponseMetadata']['HTTPStatusCode']) == 200:
          if 'Items' in self.response:
            musics = []
            for music in self.response['Items']:
              musics.append(
                {
                  'id': music['id'],
                  'name' : music['name'],
                  'artist': music['artist'],
                  'album': music['album'],
                  'year': music['year'],
                  'playlist_id': music['playlist_id'],
                  'user_id': user['id']
                }
              )
            return musics 
        return []
      except:
        raise ChaliceViewError("%s" % self.response) 

  # Lists single music
  def get_music(self, user_id, playlist_id, music_id):
    user = self.get_user(user_id)
    playlist = self.get_playlist(user['id'], playlist_id)
    
    if music_id == None:
      raise ChaliceViewError("Music id must be a valid value")

    try:
      self.response = self.musics_table.get_item(
        Key={
          'id': music_id,
          'playlist_id': playlist['id']
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
              'artist': self.response['Item']['artist'],
              'album': self.response['Item']['album'],
              'year': self.response['Item']['year'],
              'playlist_id': self.response['Item']['playlist_id'],
              'user_id': user['id']
            }
        return {}
      except:      
        raise ChaliceViewError("%s" % self.response)      

  # Inserts music
  def create_music(self, user_id, playlist_id, music):
    user = self.get_user(user_id)
    playlist = self.get_playlist(user['id'], playlist_id)
    uid = str(uuid4())
    music['id'] = uid
    music['playlist_id'] = playlist['id']

    try:
      self.response = self.musics_table.put_item(
        Item=music
      )
    except ClientError as e:
      raise BadRequestError("%s" % e)
    else:
      try:
        if int(self.response['ResponseMetadata']['HTTPStatusCode']) == 200:
          return {
            'id': music['id'],
            'name' : music['name'],
            'artist': music['artist'],
            'album': music['album'],
            'year': music['year'],
            'playlist_id': music['playlist_id'],
            'user_id': user['id']
          }
        return {}
      except:
        raise ChaliceViewError("%s" % self.response)       

  # Updates music
  def update_music(self, user_id, playlist_id, music_id, music_data):
    user = self.get_user(user_id)
    playlist = self.get_playlist(user['id'], playlist_id)
    music = self.get_music(user['id'], playlist['id'], music_id)
    if music == {}:
      raise NotFoundError("Something is wrong with the music id %s" % music_id)       

    if 'name' in music_data:
      music['name'] = music_data['name']
    if 'artist' in music_data:
      music['artist'] = music_data['artist']
    if 'album' in music_data:
      music['album'] = music_data['album']
    if 'year' in music_data:
      music['year'] = music_data['year']   

    try:
      self.response = self.musics_table.put_item(
        Item=music
      )
    except ClientError as e:
      raise BadRequestError("%s" % e)
    else:
      try:        
        if int(self.response['ResponseMetadata']['HTTPStatusCode']) == 200:
          return {
            'id': music['id'],
            'name' : music['name'],
            'artist': music['artist'],
            'album': music['album'],
            'year': music['year'],
            'playlist_id': music['playlist_id'],
            'user_id': user['id']
          }
        return {}
      except:
        raise ChaliceViewError("%s" % self.response)       

  # Deletes music
  def delete_music(self, user_id, playlist_id, music_id):
    user = self.get_user(user_id)
    playlist = self.get_playlist(user['id'], playlist_id)
    music = self.get_music(user['id'], playlist['id'], music_id)
    if music == {}:
      raise NotFoundError("Something is wrong with the music id %s" % music_id)                

    try:
      self.response = self.musics_table.delete_item(
        Key={
          'id': music['id'],
          'playlist_id': playlist['id']
        }
      )
    except ClientError as e:
      raise BadRequestError("%s" % e)
    else:
      try: 
        if int(self.response['ResponseMetadata']['HTTPStatusCode']) == 200:
          return { 'id': music['id'] }
        return {}
      except:
        raise ChaliceViewError("%s" % self.response)

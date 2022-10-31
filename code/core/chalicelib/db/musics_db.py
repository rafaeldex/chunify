from uuid import uuid4
import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

class MusicsDB:
  dynamodb = boto3.resource('dynamodb')
  musics_table = dynamodb.Table('chunify-musics')

  # Lists all musics
  def show_all(self):
    return self.musics_table.scan()

  # Lists single music
  def show(self, id):
    response = self.musics_table.get_item(
      Key={
        "id": id
      }
    )
    return response["Item"]

  # Lists all playlists that belongs to a playlist
  def show_from_playlist(self, playlist_id):
    response = self.musics_table.scan(
      FilterExpression=Attr('playlist_id').eq(playlist_id)
    )
    return response["Items"]     

  # Insert music
  def insert(self, music):
    uid = str(uuid4())
    music["id"] = uid

    response = self.musics_table.put_item(
      Item=music
    )

    if int(response["ResponseMetadata"]["HTTPStatusCode"]) == 200:
      return {
        'id': uid,
        'name' : music["name"],
        'artist': music["artist"],
        'album': music["album"],
        'year': music["year"],
        'playlist_id': music["playlist_id"]
      }
    else:
      return {}

  # Update music
  def update(self, music_data):
    music = self.show(music_data["id"])
    
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
    
    response = self.musics_table.put_item(
      Item=music
    )
    
    if int(response["ResponseMetadata"]["HTTPStatusCode"]) == 200:
      return {
        'id': music["id"],
        'name' : music["name"],
        'artist': music["artist"],
        'album': music["album"],
        'year': music["year"],
        'playlist_id': music["playlist_id"]
      }
    else: 
      return {}      

  # Delete music
  def delete(self, id):
    response = self.musics_table.delete_item(
      Key={
        'id': id,
      }
    )

    if int(response["ResponseMetadata"]["HTTPStatusCode"]) == 200:
      return id
    else: 
      return None
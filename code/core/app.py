from chalice import Chalice
from chalicelib.db.db_initializer import DBInitializer
from chalicelib.db.users_db import UsersDB
from chalicelib.services.sns import Sns

app = Chalice(app_name='chunify')
version = 'COMPLETE'
topic_name = 'CHUNIFY_TOPIC'

if version == 'COMPLETE':
  # Creates database tables
  DBInitializer().create_user_table()
  DBInitializer().create_playlist_table()
  DBInitializer().create_playlist_table()
  # Creates sns topics
  if Sns().show_chunify_topic() == "Not found":
    Sns().create_topic(topic_name)
else:
    pass

@app.route('/')
def index():
  return {'hello': 'chunify'}

@app.route('/users', methods=['GET'])
def show_all():
  return UsersDB().show_all()

@app.route('/users/{id}', methods=['GET'])
def show(id): 
  return UsersDB().show(id)

@app.route('/users', methods=['POST'])
def insert():
  user_as_json = app.current_request.json_body
  return UsersDB().insert(user_as_json)

@app.route('/users', methods=['PUT'])
def update():
  user_as_json = app.current_request.json_body
  return UsersDB().update(user_as_json)

@app.route('/users/{id}', methods=['DELETE'])
def delete(id):
  return UsersDB().delete(id)

@app.route('/users/{id}/playlists', methods=['GET'])
def show_from_user(id):
  return PlaylistDB().show_from_user(id)  

@app.route('/playlists', methods=['GET'])
def show_all():
  return PlaylistDB().show_all()

@app.route('/playlists/{id}', methods=['GET'])
def show(id):
  return PlaylistDB().show(id)

@app.route('/playlists', methods=['POST'])
def insert():
  playlist_as_json = app.current_request.json_body
  return PlaylistDB().insert(playlist_as_json)

@app.route('/playlists', methods=['PUT'])
def update():
  playlist_as_json = app.current_request.json_body
  return PlaylistDB().update(playlist_as_json)

@app.route('/playlists/{id}', methods=['DELETE'])
def delete(id):
  return PlaylistDB().delete(id)

@app.route('/playlists/{id}/musics', methods=['GET'])
def show_from_playlist(id):
  return MusicDB().show_from_playlist(id)    

@app.route('/musics', methods=['GET'])
def show_all():
  return MusicDB().show_all()

@app.route('/musics/{id}', methods=['GET'])
def show(id):
  return MusicDB().show(id)

@app.route('/musics', methods=['POST'])
def insert():
  music_as_json = app.current_request.json_body
  return MusicDB().insert(music_as_json)

@app.route('/musics', methods=['PUT'])
def update():
  music_as_json = app.current_request.json_body
  return MusicDB().update(music_as_json)

@app.route('/musics/{id}', methods=['DELETE'])
def delete(id):
  return MusicDB().delete(id)

from chalice import Chalice
from chalicelib.db import db_initializer, users_db, playlists_db, musics_db
from chalicelib.memory import data_initializer, users_data, playlists_data, musics_data
from chalicelib.services import sns

app = Chalice(app_name='chunify')
# COMPLETE: Uses DynamoDB on demand
# BETA: Uses in process storage (local tests)
version = 'BETA'
topic_name = 'CHUNIFY_TOPIC'

if version == 'COMPLETE':
  # Creates database tables
  db_initializer.DBInitializer().initialize()
  # Creates sns topic
  if sns.Sns().show_chunify_topic() == "Not found":
    sns.Sns().create_topic(topic_name)
else:
  # Creates memory data
  data_initializer.DataInitializer().initialize()

def get_database(table_name):
  global version
  if version == 'COMPLETE':
    if table_name == 'users':
      return users_db.UsersDB()
    elif table_name == 'playlists':
      return playlists_db.PlaylistsDB()
    elif table_name == 'musics':
      return musics_db.MusicsDB()
  else:
    if table_name == 'users':
      return users_data.UsersData()
    elif table_name == 'playlists':
      return playlists_data.PlaylistsData()
    elif table_name == 'musics':
      return musics_data.MusicsData()

@app.route('/')
def index():
  return {'hello': 'chunify'}

@app.route('/users', methods=['GET'])
def show_all():
  return get_database('users').show_all()

@app.route('/users/{id}', methods=['GET'])
def show(id): 
  return get_database('users').show(id)

@app.route('/users', methods=['POST'])
def insert():
  user_as_json = app.current_request.json_body
  return get_database('users').insert(user_as_json)

@app.route('/users', methods=['PUT'])
def update():
  user_as_json = app.current_request.json_body
  return get_database('users').update(user_as_json)

@app.route('/users/{id}', methods=['DELETE'])
def delete(id):
  return get_database('users').delete(id)

@app.route('/users/{id}/playlists', methods=['GET'])
def show_from_user(id):
  return get_database('playlists').show_from_user(id)  

@app.route('/playlists', methods=['GET'])
def show_all():
  return get_database('playlists').show_all()

@app.route('/playlists/{id}', methods=['GET'])
def show(id):
  return get_database('playlists').show(id)

@app.route('/playlists', methods=['POST'])
def insert():
  playlist_as_json = app.current_request.json_body
  return get_database('playlists').insert(playlist_as_json)

@app.route('/playlists', methods=['PUT'])
def update():
  playlist_as_json = app.current_request.json_body
  return get_database('playlists').update(playlist_as_json)

@app.route('/playlists/{id}', methods=['DELETE'])
def delete(id):
  return get_database('playlists').delete(id)

@app.route('/playlists/{id}/musics', methods=['GET'])
def show_from_playlist(id):
  return get_database('musics').show_from_playlist(id)    

@app.route('/musics', methods=['GET'])
def show_all():
  return get_database('musics').show_all()

@app.route('/musics/{id}', methods=['GET'])
def show(id):
  return get_database('musics').show(id)

@app.route('/musics', methods=['POST'])
def insert():
  music_as_json = app.current_request.json_body
  return get_database('musics').insert(music_as_json)

@app.route('/musics', methods=['PUT'])
def update():
  music_as_json = app.current_request.json_body
  return get_database('musics').update(music_as_json)

@app.route('/musics/{id}', methods=['DELETE'])
def delete(id):
  return get_database('musics').delete(id)

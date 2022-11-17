from chalice import Chalice
from chalicelib.db import db_initializer, users_db, playlists_db, musics_db 
from chalicelib.memory import data_initializer, users_data, playlists_data, musics_data
from chalicelib.services import streams, sns

app = Chalice(app_name='chunify')
app.debug = True
# COMPLETE: Uses DynamoDB on demand
# BETA: Uses in process storage (local tests)
version = 'COMPLETE'
topic_name = 'CHUNIFY_TOPIC'
topic_arn = ''
users_stream_arn = ''
musics_stream_arn = ''

if version == 'COMPLETE':
  # Creates database tables
  db_initializer.DBInitializer().initialize()
  users_stream_arn = streams.Streams().get_first_stream('chunify-users')
  music_stream_arn = streams.Streams().get_first_stream('chunify-musics')
  # Creates sns topic
  if sns.Sns().show_chunify_topic(topic_name) == None:
    topic_arn = sns.Sns().create_topic(topic_name)
  else:
    topic_arn = sns.Sns().show_chunify_topic(topic_name)
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

# Endpoints for users
@app.route('/users', methods=['GET'])
def get_users():
  return get_database('users').get_users()

@app.route('/users', methods=['POST'])
def create_user():
  user_as_json = app.current_request.json_body
  return get_database('users').create_user(user_as_json, topic_arn)

@app.route('/users/{user_id}', methods=['GET'])
def get_user(user_id): 
  return get_database('users').get_user(user_id)

@app.route('/users/{user_id}', methods=['PUT'])
def update_user(user_id):
  user_as_json = app.current_request.json_body
  return get_database('users').update_user(user_id, user_as_json, topic_arn)

@app.route('/users/{user_id}', methods=['DELETE'])
def delete_user(user_id):
  return get_database('users').delete_user(user_id)

# Endpoints for playlists
@app.route('/users/{user_id}/playlists', methods=['GET'])
def get_playlists(user_id):
  return get_database('playlists').get_playlists(user_id)  

@app.route('/users/{user_id}/playlists', methods=['POST'])
def create_playlist(user_id):
  playlist_as_json = app.current_request.json_body
  return get_database('playlists').create_playlist(user_id, playlist_as_json)

@app.route('/users/{user_id}/playlists/{playlist_id}', methods=['GET'])
def get_playlist(user_id, playlist_id):
  return get_database('playlists').get_playlist(user_id, playlist_id)

@app.route('/users/{user_id}/playlists/{playlist_id}', methods=['PUT'])
def update_playlist(user_id, playlist_id):
  playlist_as_json = app.current_request.json_body
  return get_database('playlists').update_playlist(user_id, playlist_id, playlist_as_json)

@app.route('/users/{user_id}/playlists/{playlist_id}', methods=['DELETE'])
def delete_playlist(user_id, playlist_id):
  return get_database('playlists').delete_playlist(user_id, playlist_id)

# Endpoints for musics
@app.route('/users/{user_id}/playlists/{playlist_id}/musics', methods=['GET'])
def get_musics(user_id, playlist_id):
  return get_database('musics').get_musics(user_id, playlist_id)    

@app.route('/users/{user_id}/playlists/{playlist_id}/musics', methods=['POST'])
def create_music(user_id, playlist_id):
  music_as_json = app.current_request.json_body
  return get_database('musics').create_music(user_id, playlist_id, music_as_json)

@app.route('/users/{user_id}/playlists/{playlist_id}/musics/{music_id}', methods=['GET'])
def get_music(user_id, playlist_id, music_id):
  return get_database('musics').get_music(user_id, playlist_id, music_id)

@app.route('/users/{user_id}/playlists/{playlist_id}/musics/{music_id}', methods=['PUT'])
def update_music(user_id, playlist_id, music_id):
  music_as_json = app.current_request.json_body
  return get_database('musics').update_music(user_id, playlist_id, music_id, music_as_json)

@app.route('/users/{user_id}/playlists/{playlist_id}/musics/{music_id}', methods=['DELETE'])
def delete_music(user_id, playlist_id, music_id):
  return get_database('musics').delete_music(user_id, playlist_id, music_id)

# Observes the users streams
@app.on_dynamodb_record(stream_arn=users_stream_arn, batch_size=100, starting_position='LATEST', name=None, maximum_batching_window_in_seconds=0)
def handle_users_message(event):
  for record in event:
    app.log.debug("New user created: %s", record.new_image)
    app.log.debug(sns.Sns().get_subscriptions())

# Observes the music streams
@app.on_dynamodb_record(stream_arn=musics_stream_arn, batch_size=100, starting_position='LATEST', name=None, maximum_batching_window_in_seconds=0)
def handle_musics_message(event):
  for record in event:
    if record.new_image != None:
      app.log.debug("New music created: %s", record.new_image)
      message = "New music created: %s" % record.new_image
      sns.Sns().send_message_topic(topic_arn, message)

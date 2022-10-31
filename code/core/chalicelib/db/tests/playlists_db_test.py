import json
from chalicelib.db.playlists_db import PlaylistsDB

class PlaylistDBTest:
  # Tests the query for all playlists
  def show_all():
    response = PlaylistsDB().show_all()
    print("Consulta de todos os registros:")
    print(response)
    return response

  # Tests the query for unique playlist
  def show_one(id):
    response = PlaylistsDB().show(id)
    print("Consulta do registro:")
    print(response)
    return response

  # Tests the query for playlists that belongs
  # to an user
  def show_from_user(user_id):
    response = PlaylistsDB().show_from_user(user_id)
    print("Consulta do registro:")
    print(response)
    return response  

  # Tests adding a new playlist
  def insert(playlistJson):
    playlist = json.loads(playlistJson)
    response = PlaylistsDB().insert(playlist)
    if response != {}:
      print("Registro incluido com sucesso" + " :: " + json.dumps(response))
    return response

  # Tests updating an existing playlist
  def update(playlistJson):
    playlist = json.loads(playlistJson)
    response = PlaylistsDB().update(playlist)
    if response != {}:
      print("Registro atualizado com sucesso" + " :: " + json.dumps(response))
    return response

  # Tests deleting an existing playlist
  def delete(id):
    response = PlaylistsDB().delete(id)
    if response != None:
      print("Registro excluido com sucesso" + " :: " + response)
    return response


# new_playlist = PlaylistDBTest.insert("""{ "name": "Lets Rock", "user_id": "3897fe65-9838-49c3-9aef-e46e60b6c797" }""")
# {"id": "d4c8a8ba-1a4c-4ee3-9016-78c343b1de3f", "name": "Lets Rock", "user_id": "3897fe65-9838-49c3-9aef-e46e60b6c797"}
# showed_playlist = PlaylistDBTest.show_one(new_playlist["id"])
# show_all_playlists = PlaylistDBTest.show_all()
# from_user = PlaylistDBTest.show_from_user(new_playlist["user_id"])
# new_playlist["name"] = "Lets Rock Today" 
# updated_playlist = PlaylistDBTest.update(json.dumps(new_playlist))
# deleted_id = PlaylistDBTest.delete(new_playlist["id"])






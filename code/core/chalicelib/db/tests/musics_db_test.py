import json
from chalicelib.db.musics_db import MusicsDB

class MusicDBTest:
  # Tests the query for all musics
  def show_all():
    response = MusicsDB().show_all()
    print("Consulta de todos os registros:")
    print(response)
    return response

  # Tests the query for unique music
  def show_one(id):
    response = MusicsDB().show(id)
    print("Consulta do registro:")
    print(response)
    return response

  # Tests the query for musics that belongs
  # to a playlist
  def show_from_playlist(playlist_id):
    response = MusicsDB().show_from_playlist(playlist_id)
    print("Consulta do registro:")
    print(response)
    return response    

  # Tests adding a new music
  def insert(musicJson):
    music = json.loads(musicJson)
    response = MusicsDB().insert(music)
    if response != {}:
      print("Registro incluido com sucesso" + " :: " + json.dumps(response))
    return response

  # Tests updating an existing music
  def update(musicJson):
    music = json.loads(musicJson)
    response = MusicsDB().update(music)
    if response != {}:
      print("Registro atualizado com sucesso" + " :: " + json.dumps(response))
    return response

  # Tests deleting an existing music
  def delete(id):
    response = MusicsDB().delete(id)
    if response != None:
      print("Registro excluido com sucesso" + " :: " + response)
    return response


# new_music = MusicDBTest.insert("""{ "name": "Always", "artist": "Jon Bon Jovi", "album":"Cross Road", "year": "1994", "playlist_id": "d4c8a8ba-1a4c-4ee3-9016-78c343b1de3f" }""")
# {"id": "d4c8a8ba-1a4c-4ee3-9016-78c343b1de3f", "name": "Lets Rock", "user_id": "3897fe65-9838-49c3-9aef-e46e60b6c797"}
# showed_music = MusicDBTest.show_one(new_music["id"])
# show_all_musics = MusicDBTest.show_all()
# from_playlist = MusicDBTest.show_from_playlist(new_music["id"])
# new_music["year"] = "1995" 
# updated_music = MusicDBTest.update(json.dumps(new_music))
# deleted_id = MusicDBTest.delete(new_music["id"])



import json
from chalicelib.db.users_db import UsersDB

class UserDBTest:
  # Tests the query for all users
  def show_all():
    response = UsersDB().show_all()
    print("Consulta de todos os registros:")
    print(response)
    return response

  # Tests the query for unique user
  def show_one(id):
    response = UsersDB().show(id)
    print("Consulta do registro:")
    print(response)
    return response

  # Tests adding a new user
  def insert(userJson):
    user = json.loads(userJson)
    response = UsersDB().insert(user)
    if response != {}:
      print("Registro incluido com sucesso" + " :: " + json.dumps(response))
    return response

  # Tests updating an existing user
  def update(userJson):
    user = json.loads(userJson)
    response = UsersDB().update(user)
    if response != {}:
      print("Registro atualizado com sucesso" + " :: " + json.dumps(response))
    return response

  # Tests deleting an existing user
  def delete(id):
    response = UsersDB().delete(id)
    if response != None:
      print("Registro excluido com sucesso" + " :: " + response)
    return response


# new_user = UserDBTest.insert("""{ "name": "Tester", "age": 33, "phone": "5585981661026" }""")
# showed_user = UserDBTest.show_one(new_user["id"])
# show_all_users = UserDBTest.show_all()
# new_user["age"] = 35 
# updated_user = UserDBTest.update(json.dumps(new_user))
# deleted_id = UserDBTest.delete(new_user["id"])

# new_user = UserDBTest.insert("""{ "name": "Rafael", "age": 40, "phone": "5586999945388" }""")
# new_user = UserDBTest.insert("""{ "name": "Rafael DEX", "age": 40, "phone": "5586999945388" }""")

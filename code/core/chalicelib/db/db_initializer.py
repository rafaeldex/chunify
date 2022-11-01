import boto3

class DBInitializer:
  dynamodb = boto3.resource('dynamodb')
  existing_tables = boto3.client('dynamodb').list_tables()['TableNames']

  # Creates the users table
  def create_user_table(self):
    if 'chunify-users' not in self.existing_tables:
      chunify_users = self.dynamodb.create_table(
        TableName='chunify-users',
        KeySchema=[
          {'AttributeName': 'id', 'KeyType': 'HASH'}
        ],
        AttributeDefinitions=[
          {'AttributeName': 'id', 'AttributeType': 'S'}
        ],
        BillingMode='PAY_PER_REQUEST',
      )
      print(chunify_users)
    return "Users table created successifuly"

  # Creates the playlists table
  def create_playlist_table(self):
    if 'chunify-playlists' not in self.existing_tables:
      chunify_playlists = self.dynamodb.create_table(
        TableName='chunify-playlists',
        KeySchema=[
          {'AttributeName': 'id', 'KeyType': 'HASH'}
        ],
        AttributeDefinitions=[
          {'AttributeName': 'id', 'AttributeType': 'S'}
        ],
        BillingMode='PAY_PER_REQUEST',
      )
      print(chunify_playlists)
    return "Playlists table created successifuly"  

  # Creates the musics table
  def create_playlist_table(self):
    if 'chunify-musics' not in self.existing_tables:
      chunify_musics = self.dynamodb.create_table(
        TableName='chunify-musics',
        KeySchema=[
          {'AttributeName': 'id', 'KeyType': 'HASH'}
        ],
        AttributeDefinitions=[
          {'AttributeName': 'id', 'AttributeType': 'S'}
        ],
        BillingMode='PAY_PER_REQUEST',
      )
      print(chunify_musics)
    return "Musics table created successifuly"

  def initialize(self):
    self.create_user_table()
    self.create_playlist_table()
    self.create_playlist_table()
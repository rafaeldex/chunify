import boto3
from botocore.exceptions import ClientError
from chalice import BadRequestError

class DBInitializer:
  dynamodb = boto3.resource('dynamodb')
  existing_tables = boto3.client('dynamodb').list_tables()['TableNames']

  # Creates the users table
  def create_users_table(self):
    try:
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
          StreamSpecification={
            'StreamEnabled': True,
            'StreamViewType': 'NEW_AND_OLD_IMAGES'
          },
        )
        return chunify_users
      else:
        return 'Error creating users table'  
    except ClientError as e:
      raise BadRequestError("%s" % e)        

  # Creates the playlists table
  def create_playlists_table(self):
    try:
      if 'chunify-playlists' not in self.existing_tables:
        chunify_playlists = self.dynamodb.create_table(
          TableName='chunify-playlists',
          KeySchema=[
            {'AttributeName': 'id', 'KeyType': 'HASH'},
            {'AttributeName': 'user_id', 'KeyType': 'RANGE'}
          ],
          AttributeDefinitions=[
            {'AttributeName': 'id', 'AttributeType': 'S'},
            {'AttributeName': 'user_id', 'AttributeType': 'S'}
          ],
          BillingMode='PAY_PER_REQUEST',
          StreamSpecification={
            'StreamEnabled': True,
            'StreamViewType': 'NEW_AND_OLD_IMAGES'
          },
        )
        return chunify_playlists
      else:
        return 'Error creating playlists table'          
    except ClientError as e:
      raise BadRequestError("%s" % e)  

  # Creates the musics table
  def create_musics_table(self):
    try:
      if 'chunify-musics' not in self.existing_tables:
        chunify_musics = self.dynamodb.create_table(
          TableName='chunify-musics',
          KeySchema=[
            {'AttributeName': 'id', 'KeyType': 'HASH'},
            {'AttributeName': 'playlist_id', 'KeyType': 'RANGE'}
          ],
          AttributeDefinitions=[
            {'AttributeName': 'id', 'AttributeType': 'S'},
            {'AttributeName': 'playlist_id', 'AttributeType': 'S'}
          ],
          BillingMode='PAY_PER_REQUEST',
          StreamSpecification={
            'StreamEnabled': True,
            'StreamViewType': 'NEW_AND_OLD_IMAGES'
          },
        )
        return chunify_musics
      else:
        return 'Error creating musics table'          
    except ClientError as e:
      raise BadRequestError("%s" % e)  

  def initialize(self):
    chunify_users = self.create_users_table()
    chunify_playlists = self.create_playlists_table()
    chunify_musics = self.create_musics_table()

    return {
      'uses_streams': chunify_users,
      'playlists_streams': chunify_playlists,
      'musics_streams': chunify_musics,
    }
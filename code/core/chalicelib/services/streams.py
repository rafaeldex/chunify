import boto3
from botocore.exceptions import ClientError
from chalice import BadRequestError, ChaliceViewError, NotFoundError

class Streams:
  streams = boto3.client('dynamodbstreams')

  # Lists a table streams
  def get_streams(self, table_name):
    try:
      return self.streams.list_streams(TableName=table_name)
    except ClientError as e:
      raise BadRequestError("%s" % e)

  # Lists the first table streams
  def get_first_stream(self, table_name):
    try:
      streams_table = self.streams.list_streams(TableName=table_name)
    except ClientError as e:
      raise BadRequestError("%s" % e)
    else:
      try:
        latest = ''
        for stream in reversed(streams_table['Streams']):
          latest = stream['StreamArn']
        return latest    
      except Exception as e:
        raise ChaliceViewError("%s" % e)

  # Lists the latest table streams
  def get_latest_stream(self, table_name):
    try:
      streams_table = self.streams.list_streams(TableName=table_name)
    except ClientError as e:
      raise BadRequestError("%s" % e)
    else:   
      try:   
        latest = ''
        for stream in streams_table['Streams']:
          latest = stream['StreamArn']
        return latest  
      except Exception as e:
        raise ChaliceViewError("%s" % e)

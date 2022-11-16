import boto3

class Streams:
  streams = boto3.client('dynamodbstreams')

  # Lists a table streams
  def get_streams(self, table_name):
    response = self.streams.list_streams(TableName=table_name)
    return response

  # Lists the first table streams
  def get_first_stream(self, table_name):
    streams_table = self.streams.list_streams(TableName=table_name)
    latest = ''
    for stream in reversed(streams_table['Streams']):
      latest = stream['StreamArn']
    return latest    

  # Lists the latest table streams
  def get_latest_stream(self, table_name):
    streams_table = self.streams.list_streams(TableName=table_name)
    latest = ''
    for stream in streams_table['Streams']:
      latest = stream['StreamArn']
    return latest  

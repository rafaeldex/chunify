import os, sys
from chalicelib.services.sns import Sns

class SqsTest:
  # Tests creating a new topic
  def create_topic(name):
    response = Sns().create_topic(name)
    print(response)
    return response

  # Tests getting all topics
  def list_topics():
    response = Sns().list_topics()
    for topic in response:
      print(topic.arn)
    return response

  # Tests getting chunify topic
  def show_chunify_topic():
    response = Sns().show_chunify_topic()
    print(response)
    return response    

  # Tests subscribing to a topics
  def subscribe(arn, protocol, endpoint):
    response = Sns().subscribe(arn, protocol, endpoint)
    print(response)
    return response

  # Tests sending a sms to user
  def send_message_user(phone, message):
    response = Sns().send_message_user_phone(phone, message)
    print(response)
    return response

  # Tests sending a sms to topic
  def send_message_topic(phone, message):
    response = Sns().send_message_topic(phone, message)
    print(response)
    return response    

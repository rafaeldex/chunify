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

# new_topic = SqsTest.create_topic("CHUNIFY_TOPIC")
# arn:aws:sns:us-east-1:112935367069:CHUNIFY_TOPIC
# all_topics = SqsTest.list_topics()
# chunify_topic = SqsTest.show_chunify_topic()
# subscribed = SqsTest.subscribe("arn:aws:sns:us-east-1:112935367069:CHUNIFY_TOPIC", "sms", "+5586999945388")
# arn:aws:sns:us-east-1:112935367069:CHUNIFY_TOPIC:c9439885-d078-43d2-930f-7dbe8d5d69ab'
# message_sent = SqsTest.send_message_user("+5586999945388", "Bem vindo ao Chunify")
# message_sent = SqsTest.send_message_topic("arn:aws:sns:us-east-1:112935367069:CHUNIFY_TOPIC", "Bem vindo ao Chunify")

# app.log.debug(sns.Sns().subscriptions())
# sns.Sns().send_message_user_phone('+5586999945388', 'Hello from chunify!')
# sns.Sns().send_message_topic(topic_arn, 'Hello from chunify!')
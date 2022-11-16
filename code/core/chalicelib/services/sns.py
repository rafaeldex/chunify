import boto3

class Sns:
  sns = boto3.resource("sns")
  sns_client = boto3.client("sns")

  # Creates a topic
  def create_topic(self, name):
    response = self.sns.create_topic(Name=name)
    return response["TopicArn"]

  # Lists all topics
  def list_topics(self):
    response = self.sns.topics.all()
    return response

  # List chunify topic
  def show_chunify_topic(self, topic_name):
    response = self.sns.topics.all()
    for topic in response:
      if topic_name in topic.arn:
        return topic.arn
    return "Not found"

  # Subscribe an endpoint
  # Arn: chunify-arn
  # Protocol: (email,sms)
  # Endpoint: some email or phone number
  def subscribe(self, arn, protocol, endpoint):
    response = self.sns_client.subscribe(
      TopicArn=arn,
      Protocol=protocol,
      Endpoint=endpoint,
      ReturnSubscriptionArn=True
    )
    return response["SubscriptionArn"]

  # Sends a message to single user
  def send_message_user_phone(self, phone, message):
    response = self.sns_client.publish(
        PhoneNumber=phone,
        Message=message
    )
    return response

  # Sends a message to topic
  def send_message_topic(self, topic, message):
    response = self.sns_client.publish(
        TopicArn=topic,
        Message=message,
    )
    return response
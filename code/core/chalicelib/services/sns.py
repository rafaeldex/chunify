import boto3
from botocore.exceptions import ClientError
from chalice import BadRequestError, ChaliceViewError, NotFoundError

class Sns:
  sns = boto3.resource("sns")
  sns_client = boto3.client("sns")
  response = None

  # Creates a topic
  def create_topic(self, name):
    try:
      self.response = self.sns.create_topic(Name=name)
    except ClientError as e:
      raise BadRequestError("%s" % e)
    else:
      try:        
        return self.response["TopicArn"]
      except Exception as e:
        raise ChaliceViewError("%s" % e)

  # Lists all topics
  def list_topics(self):
    try:
      return self.sns.topics.all()
    except ClientError as e:
      raise BadRequestError("%s" % e)

  # List chunify topic
  def show_chunify_topic(self, topic_name):
    topics = self.list_topics()
    try:        
      for topic in topics:
        if topic_name in topic.arn:
          return topic.arn
      return None
    except Exception as e:
      raise ChaliceViewError("%s" % e)        

  # Subscribe an endpoint
  # Arn: chunify-arn topic
  # Protocol: (email,sms)
  # Endpoint: some email or phone number
  def subscribe(self, arn, protocol, endpoint):
    try:
      self.response = self.sns_client.subscribe(
        TopicArn=arn,
        Protocol=protocol,
        Endpoint=endpoint,
        ReturnSubscriptionArn=True
      )
    except ClientError as e:
      raise BadRequestError("%s" % e)
    else:
      try:           
        return self.response["SubscriptionArn"]
      except Exception as e:
        raise ChaliceViewError("%s" % e) 

  # List all subscriptions
  def get_subscriptions(self):
    try:
      self.response = self.sns_client.list_subscriptions()
    except ClientError as e:
      raise BadRequestError("%s" % e)
    else:
      try:           
        return self.response["Subscriptions"]
      except Exception as e:
        raise ChaliceViewError("%s" % e)

  # List all subscriptions
  # Endpoint: some email or phone number
  def get_subscription_arn(self, endpoint):
    subscriptions = self.get_subscriptions()
    try:
      for subscription in subscriptions:
        if subscription['Endpoint'] == endpoint:
          return subscription["SubscriptionArn"]
      return None    
    except Exception as e:
      raise ChaliceViewError("%s" % e)        

  # Unsubscribe an endpoint
  # Endpoint: some email or phone number
  def unsubscribe(self, endpoint):
    subscription_arn = self.get_subscription_arn(endpoint)
    if subscription_arn == None:
      return None

    try:
      self.response = self.sns_client.unsubscribe(
        SubscriptionArn=subscription_arn
      )
    except ClientError as e:
      raise BadRequestError("%s" % e)
    else:
      try:           
        return 'Endpoint unsubscribed successfully'
      except Exception as e:
        raise ChaliceViewError("%s" % e)                 

  # Sends a message to single user
  def send_message_user_phone(self, phone, message):
    try:
      return self.sns_client.publish(
        PhoneNumber=phone,
        Message=message
      )
    except ClientError as e:
      raise BadRequestError("%s" % e)

  # Sends a message to topic
  def send_message_topic(self, topic, message):
    try:    
      return self.sns_client.publish(
        TopicArn=topic,
        Message=message,
      )
    except ClientError as e:
      raise BadRequestError("%s" % e)
   
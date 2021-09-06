import tweepy
  
# assign the values accordingly
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
  
# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  
# set access to user's access key and access secret 
auth.set_access_token(access_token, access_token_secret)
  
# calling the api 
api = tweepy.API(auth)
  
# the ID of the status
id = 1272771459249844224

status = api.get_status(id)

full_text = status.full_text 
  
print("The text of the status is : \n\n" + full_text)
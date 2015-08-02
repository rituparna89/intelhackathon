import tweepy

consumer_key='RwPfiWmpcGsicFFUze2S8kbAG'
consumer_secret= '64HB10qRMwLJH3wekwJkv3RJP6TZFK9sJfPxfmbZZotAs96dl0'
#APP_KEY = 
#APP_SECRET = '64HB10qRMwLJH3wekwJkv3RJP6TZFK9sJfPxfmbZZotAs96dl0'
#OAUTH_TOKEN = 
#OAUTH_TOKEN_SECRET = 
# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token='2835817897-EJU8lEN2qv4cLq9CqtCqixF9y2G0PCfwEGDxpZl'
access_token_secret='WdcBJd1oBPjXTrmoIaL5fH29P0EiwArF8ucYQAXWflyvC'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out
print(api.me().name)

# If the application settings are set for "Read and Write" then
# this line should tweet out the message to your account's
# timeline. The "Read and Write" setting is on https://dev.twitter.com/apps
api.update_status(status='#IntelMaker #doothings @doo @io @rohit7gupta @jasveer2589 My intel Edison board is sending this update.')
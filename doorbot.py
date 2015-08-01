import time
import serial
from twython import TwythonStreamer

# Search terms
TERMS = '#watchmydoor'
ser = serial.Serial('/dev/ttyACM0', 9600)
# GPIO pin number of LED
LED = 22

# Twitter application authentication
# replace with your credentials
APP_KEY = 'RwPfiWmpcGsicFFUze2S8kbAG'
APP_SECRET = '64HB10qRMwLJH3wekwJkv3RJP6TZFK9sJfPxfmbZZotAs96dl0'
OAUTH_TOKEN = '2835817897-EJU8lEN2qv4cLq9CqtCqixF9y2G0PCfwEGDxpZl'
OAUTH_TOKEN_SECRET = 'WdcBJd1oBPjXTrmoIaL5fH29P0EiwArF8ucYQAXWflyvC'

# Setup callbacks from Twython Streamer
#turnn surveilenace on or off here.
class BlinkyStreamer(TwythonStreamer):
        def on_success(self, data):
                if 'text' in data:						#case 1
                    print data['text'].encode('utf-8')
 				if 'no' in data:						#case 2
 					print 'no'
 			print '-'
			ser.write('a') # turn on surveliance here

		def on_error(self, status_code, data):
        	print status_code
        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        # self.disconnect()	


# Setup GPIO as output
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)

# Create streamer
try:
        stream = BlinkyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        stream.statuses.filter(track=TERMS)
except KeyboardInterrupt:
        GPIO.cleanup()

#for posting from your account
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
    api.update_status("i wana say X @abc")


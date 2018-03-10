#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
access_token = "1177825206-3F1lDtdIG2ZXWIElTaPom1TOIw50mxmibSvZ101"
access_token_secret = "zoOzBdLYdHG0pP30UZM1znSt5RAWAp7OYrSSeG2Xe3I8N"
consumer_key = "S3ZN012qzgK1IeR6yL5gnNFFX"
consumer_secret = "EfpDZrGtfv5Aw8y687hMoOYpv3TzFwHhVDot5FTkuuCHfOC7hb"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        #print(data)
        with open('fetched_tweets.txt','a') as tf:
            tf.write(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    #stream.filter(track=['bitcoin', 'ethereum', 'coinbase', '#btc', '#bitcoin', '#cryptocurrency',
                         #'blockchain','#crypto','litecoin','ripple','stellar','TRON']);
    stream.sample();

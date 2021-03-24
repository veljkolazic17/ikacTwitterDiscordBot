#IKAC API
import twitter 
def ikac_py(search_name):
    consumer_key = ''
    consumer_secret = ''


    token = ''
    token_secret = ''
    api = twitter.Api(consumer_key =consumer_key,consumer_secret=consumer_secret,access_token_key = token,access_token_secret = token_secret, tweet_mode = 'extended')

    #print(api.VerifyCredentials())
    followers = api.GetFollowers()
    timeline = api.GetUserTimeline(screen_name = search_name)

    def count_dict(dic):
        counter = 0
        for x in dic:
            counter = counter+1
        return counter

    return timeline



import tweepy
import requests
from createBanner import createUpdatedImage
import topSecret

# twitter
consumer_key = topSecret.api_key
consumer_secret = topSecret.api_secret_key
access_token = topSecret.access_token
access_token_secret = topSecret.access_token_secret

# youtube
yt_channel_id = topSecret.yt_channel_id
yt_api_key = topSecret.yt_api_key

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def getUser():
    user = api.get_user('beyou7060')
    print(user.screen_name)
    print(user.followers_count)
    for friend in user.friends():
        print(friend.screen_name)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

def tweet(message):
    api.update_status(message)


def getActualSubCount():
    try:
        response = requests.get('https://www.googleapis.com/youtube/v3/channels?part=statistics&id='+yt_channel_id+'&key='+yt_api_key)
        youtubeResponse = response.json()
        subCount = str(youtubeResponse['items'][0]['statistics']['subscriberCount'])
        return int(subCount)
    except Exception as e:
        print(e)
        return 0


def getSubCount(subCount):
    try:
        subCount = str(subCount)
        digits = ['0️⃣','1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣']
        strCount = ''
        for d in subCount:
            strCount += digits[int(d)]
        return strCount + " Subscribers"
    except Exception as e:
        print(e)
        return 'Subscribe to my channel please'


def updateNameAndDescription(subCount):
    name = "A Little Coding: "+getSubCount(subCount)
    description = """I'm a #SoftwareEngineer.\n""" + name + """
These numbers get updated automatically. 
Subscribe to my channel to see it change."""
    print(name, description)
    api.update_profile(name=name, description=description)


if __name__ == '__main__':
    subCount = getActualSubCount()
    updateNameAndDescription(subCount)
    createUpdatedImage(subCount)
    api.update_profile_banner('banner.png')


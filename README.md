# update-twitter-account-with-api

With this script you will be able to show your youtube subscriber count on your twitter profile 
# Output:
![image](https://user-images.githubusercontent.com/30652896/129080434-f0e23257-f1f2-46f4-ac6c-18fa0999f096.png)

## Steps:
- Create twitter developer account
    - https://developer.twitter.com/en/apply-for-access
    - create api key and api secret key (save these somewhere)
    - enable read and write access for the api
    - create access token and access token secret (save these as well)

- Create Google developer account
    - https://console.developers.google.com/
    - create api key (save this too)
    - enable youtube-data-api for that api key
    - copy channel_id from your youtube channel url (save it too)

- Clone or download this repo
- add all those keys in [topSecret.py](https://github.com/Google987/update-twitter-account-with-api/blob/master/topSecret.py) file

- Install [tweepy](https://docs.tweepy.org/en/stable/)
    - `pip install tweepy`
- Install [Pillow](https://pypi.org/project/Pillow/)
    - `pip install Pillow`

- replace `background.png` with something of your choice (but make sure the file name is `background.png` only)

- now you can simply run `twitter-api.py` file
    - `python twitter-api.py`

Watch my youtube video for better understanding: https://youtu.be/4PExr-7kWL8

Also subscribe to my youtube channel please. 

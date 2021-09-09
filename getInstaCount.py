
import requests


def getFollowersCount():
    try:
        instaId = 'beyou7060'
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        response = requests.get("https://www.instagram.com/"+instaId+"/?__a=1", headers=headers)
        print(response.status_code, response.request.headers)
        instaResponse = response.json()
        # print(instaResponse)
        follwerCount = str(instaResponse['graphql']['user']['edge_followed_by']['count'])
        return int(follwerCount)
    except Exception as e:
        print(e)
        return 0


if __name__ == '__main__':
    print(getFollowersCount())

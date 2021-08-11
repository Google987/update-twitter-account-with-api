import requests
from bs4 import BeautifulSoup
import json


page = requests.get("https://www.youtube.com/c/alittlecoding")
soup = BeautifulSoup(page.text, 'html.parser')

scripts = soup.findAll('script')
subs_jsons = ''
for script in scripts:
    script = script.encode("utf-8")
    if 'subscriberCountText' in str(script):
        subs_jsons = script
        break

subs_jsons = str(subs_jsons).replace('\\"', '').replace('\\', '')
subs_jsons = subs_jsons[subs_jsons.find('{'):]
subs_jsons = subs_jsons[:subs_jsons.rfind('}')+1]
# print(subs_jsons)

# https://jsoneditoronline.org/#left=cloud.b1d852e4871e40b9b2f4e0ac3e7e2472
channel_json = json.loads(subs_jsons)
# for k in channel_json.keys():
#     print(k)
simple_text = channel_json['header']['c4TabbedHeaderRenderer']['subscriberCountText']['simpleText']

subs_count = simple_text.split(' ')[0]
print(subs_count)
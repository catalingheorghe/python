import json
from urllib.request import urlopen

#youtube gdata API is deprecated; change to a URL to a dummy resource
#url = "https://gdata.youtube.com/feeds/api/standardfeeds/top_rated?alt=json"
url = "https://raw.githubusercontent.com/koki0702/introducing-python/master/dummy_api/youTube_top_rated.json"

response = urlopen(url)
contents = response.read()

text = contents.decode('utf8')
data = json.loads(text)

for video in data['feed']['entry'][0:6]:
	print(video['title']['$t'])


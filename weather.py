#! python3
APPID='e350be07cc142db72501b9d9abd94b18'
import json, requests, sys

if len(sys.argv)<2:
    print('Usage:weather.py cityname, 2-letter_country_code')
    sys.exit()
location=' '.join(sys.argv[1:])
url ='http://api.openweathermap.org/data/2.5/weather?q=%s&cnt=3&APPID=%s' % (location,APPID) 
response = requests.get(url)
print(response.text)

weatherData = json.loads(response.text)
w = weatherData["main"]['temp']
print(w)

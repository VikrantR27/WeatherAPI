
#! python3
APPID='e350be07cc142db72501b9d9abd94b18'
import json, requests, sys, turtle

if len(sys.argv)<2:
    print('Usage:weather.py cityname, 2-letter_country_code')
    sys.exit()
location=' '.join(sys.argv[1:])
url ='http://api.openweathermap.org/data/2.5/weather?q=%s&cnt=3&APPID=%s' % (location,APPID) 
response = requests.get(url)

weatherData = json.loads(response.text)
w = weatherData["main"]
MinTemp = w["temp_min"]
MaxTemp = w["temp_max"]
CurrTemp = w["temp"]

T = turtle.Screen()
if MaxTemp == MinTemp:
	r = 1
	b = 1
else:
	r = (CurrTemp - MinTemp)/(MaxTemp - MinTemp)
	b = (MaxTemp - CurrTemp)/(MaxTemp - MinTemp)
T.bgcolor(r, 0, b)
input()
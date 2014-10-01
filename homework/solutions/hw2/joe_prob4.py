import urllib2
import json

def get_geo_data():
    resp = urllib2.urlopen('http://freegeoip.net/json/')
    data = json.load(resp)   
    return data

def get_weather_info(latiude, longitude):
    base_url = "https://api.forecast.io/forecast"
    API_KEY = "cc849413324b099ad551c0a3dd9b0d32"
    url = "%s/%s/%s,%s" % (base_url, API_KEY, latiude, longitude)
    resp = urllib2.urlopen(url)
    data = json.load(resp)
    currently = data['currently']
    return "%sF: %s" % (int(currently['temperature']), currently['summary'])

geo_data = get_geo_data()
city = geo_data['city']
state = geo_data['region_code']
weather = get_weather_info(geo_data['latitude'], geo_data['longitude'])

print("Right now in %s, %s: %s" % (city, state, weather))

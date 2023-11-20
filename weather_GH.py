import urllib.request, urllib.parse, urllib.error
import json
import ssl
import os

#Uses API key for OpenWeatherMap
apikey = 'XXXXXXXXXXXXXXXXXXXXXXXXXXX' #API key needs to be entered here for this code to function!
serviceurl = 'https://api.openweathermap.org/data/2.5/weather?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

os.system('cls')

while True:
    city = input('Enter location (or press enter to exit): ')
    if len(city) < 1: break

    parms = dict()
    parms['q'] = city
    parms['appid'] = apikey
    parms['units'] = 'imperial'
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    #print(json.dumps(js, indent=4)) 

    lat = js['coord']['lon']
    lng = js['coord']['lat']
    currtemp = js['main']['temp']
    humidity = js['main']['humidity']
    condition = js['weather'][0]['description']
    print('Weather for',parms['q'])
    print('Temperature:',currtemp,'degrees F')
    print('Humidity:',humidity,'%')
    print('Atmospheric condition:',condition)
    print()

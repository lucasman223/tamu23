import requests
import json
import censusgeocode as cg
import csv
from dotenv import load_dotenv
import os

load_dotenv()
googleAPIKey = os.getenv('googleAPIKey')
weathermapkey = os.getenv('weathermapkey')

def calc(temp, wspeed, fcast, humid, re):
  rating = re
  message = []
  message.append(fcast)
  if (temp >= 114):
    rating = rating - 4
    message.append("Temperatures above 114 can cause cancellations")
  if (temp >= 110 ) and (temp < 114):
    rating = rating - 1
    message.append("Temperature above 110 is low risk")
  if ('to' in wspeed):
    spl = wspeed.split('to')
    wspeed = spl[1]
  num = ""
  for d in wspeed:
    if d.isdigit():
        num = num + d
  speed = int(num)
  if (speed >= 30) and (speed < 45):
    rating = rating - 2
    message.append("A Moderate Threat to Life and Property from High Wind.")
  if (speed >= 45) and (speed <= 57):
    rating = rating - 6
    message.append("A High Threat to Life and Property from High Wind.")
  if (speed >= 58):
    rating = rating - 10
    message.append("An Extreme Threat to Life and Property from High Wind.")
  if (humid >= 95):
    rating = rating - 1
    message.append("Humidity is close to 100, higher risk of fog")
  if ('snow' in fcast) or ('Snow' in fcast):
    rating = rating - 2
    message.append("Presence of snow could cause delays")
  if ('thunderstorms' in fcast):
    rating = rating - 2
    message.append("Presence of thunderstorms could cause delays")

    # ADD STUFF TO ALGORITHM HEHE HAHA

  msglist = []
  msglist.append(rating)
  msglist.append(message)
  return msglist

flights = flightFinder.flightData
print("Enter Flight number: \nExample: DAL748")
def algod(airlineCode):
    airlineCity = ""
    with open('weatherAPI/Airport Codes by Country - Airport Codes List .csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if (row[2] == airlineCode):
                airlineCity = row[0]
                break
    
    geocodingAPIGrab = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address=' + airlineCity + '&key=' + googleAPIKey)
    jsonconvert = geocodingAPIGrab.json()

    longitude = "%.4f" % jsonconvert['results'][0]['geometry']['location']['lng']
    latitude = "%.4f" % jsonconvert['results'][0]['geometry']['location']['lat']

    weatherAPIGrab = requests.get('https://api.weather.gov/points/' + latitude + "," + longitude)
    weatherJSON = weatherAPIGrab.json()

    forecastAPIGrab = requests.get(weatherJSON['properties']['forecast'])
    forecastJSON = forecastAPIGrab.json()

    temperatures = []
    windSpeeds = []
    forecasts = []
    windDir = []
    humidities = []

    # 
    # LISTS OF TEMPS, WIND SPEEDS, FORECASTS, WIND DIRECTION ARE ORGANIZED STARTING WITH
    # THIS AFTERNOON, TONIGHT, TOMORROW AFTERNOON, TOMORROW NIGHT, ... FOR A WEEK 
    # 

    for i in range(0,7):
        windSpeeds.append(forecastJSON['properties']['periods'][i*2]['windSpeed'])
        temperatures.append(forecastJSON['properties']['periods'][i*2]['temperature'])
        forecasts.append(forecastJSON['properties']['periods'][i*2]['detailedForecast'])
        windDir.append(forecastJSON['properties']['periods'][i*2]['windDirection'])

    openWeatherAppAPIGrab = requests.get(f'https://api.openweathermap.org/data/3.0/onecall?lat=' + latitude + '&lon=' + longitude + '&exclude=minutely,hourly,alerts,current&units=imperial&appid=' + weathermapkey)
    openJSON = openWeatherAppAPIGrab.json()

    for i in range(0,7):
        humidities.append(openJSON['daily'][i]['humidity'])

    # humidities will be 0-7, 0 being the current day

    # temperatures, windSpeeds, forecasts, windDir, humidities
    # 
    # snow, hurricanes, extreme low/high temperatures, high humidities

    rati = 10
    sevenDayForecast = []

    for i in range(0, 7):
        sevenDayForecast.append(calc(temperatures[i],windSpeeds[i],forecasts[i],humidities[i],rati))

    return sevenDayForecast

from flask_restful import Api, Resource, reqparse

# class HelloApiHandler(Resource):
#   def get(self):
#     return {
#       'resultStatus': 'SUCCESS',
#       'message': "Hello Api Handler"
#       }

#   def post(self):
#     print(self)
#     parser = reqparse.RequestParser()
#     parser.add_argument('type', type=str)
#     parser.add_argument('message', type=str)

#     args = parser.parse_args()

#     print(args)
#     # note, the post req from frontend needs to match the strings here (e.g. 'type and 'message')

#     request_type = args['type']
#     request_json = args['message']
#     # ret_status, ret_msg = ReturnData(request_type, request_json)
#     # currently just returning the req straight
#     ret_status = request_type
#     ret_msg = request_json

#     if ret_msg:
#       message = "Your Message Requested: {}".format(ret_msg)
#     else:
#       message = "No Msg"
    
#     final_ret = {"status": "Success", "message": message}

#     return final_ret

import requests
import json
import censusgeocode as cg
import csv
import flightFinder

flights = flightFinder.flightData
print("Enter Airline Code: \nExample: DFW")
airlineCode = input("Flight number: ")
for i in flights:
    if (i[0] in airlineCode):
        airlineCode = i[1]

airlineCity = ""

with open('weatherAPI/Airport Codes by Country - Airport Codes List .csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # print(row[2])
        if (row[2] == airlineCode):
            airlineCity = row[0]
            break

print("\n")
print(airlineCity)

geocodingAPIGrab = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + airlineCity + '&key=AIzaSyA_C9RGL8hIhcIR0MhjV-mv4x2ALYDNfSU')
jsonconvert = geocodingAPIGrab.json()

longitude = "%.4f" % jsonconvert['results'][0]['geometry']['location']['lng']
latitude = "%.4f" % jsonconvert['results'][0]['geometry']['location']['lat']

# print("TEST lat & lng")
# print(latitude)
# print(longitude)

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

print("Temperatures: ")
print(temperatures)
print("\n")

print("Wind Speeds: ")
print(windSpeeds)
print("\n")

print(forecasts)
print("\n")

print(windDir)
print("\n")

openWeatherAppAPIGrab = requests.get('https://api.openweathermap.org/data/3.0/onecall?lat=' + latitude + '&lon=' + longitude + '&exclude=minutely,hourly,alerts,current&units=imperial&appid=8da0b7e95b9d416ae92fc999445bc7fc')
openJSON = openWeatherAppAPIGrab.json()

for i in range(0,7):
    humidities.append(openJSON['daily'][i]['humidity'])

print(humidities)

# humidities will be 0-7, 0 being the current day

# temperatures, windSpeeds, forecasts, windDir, humidities
# 
# snow, hurricanes, extreme low/high temperatures, high humidities

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
  msglist = []
  msglist.append(rating)
  msglist.append(message)
  return msglist

rati = 10
sevenDayForecast = []

for i in range(0, 7):
    sevenDayForecast.append(calc(temperatures[i],windSpeeds[i],forecasts[i],humidities[i],rati))

print(sevenDayForecast)
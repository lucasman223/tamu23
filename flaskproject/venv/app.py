# from flask import Flask, send_from_directory
# from flask_restful import Api, Resource, reqparse
# from flask_cors import CORS #comment this on deployment
# from api.HelloApiHandler import HelloApiHandler

# app = Flask(__name__, static_url_path='', static_folder='frontend/build')
# CORS(app) #comment this on deployment
# api = Api(app)

# @app.route("/", defaults={'path':''})
# def serve(path):
#     return send_from_directory(app.static_folder,'index.html')

# api.add_resource(HelloApiHandler, '/flask/hello')
import requests
import json
#import censusgeocode as cg
import csv
from dotenv import load_dotenv
import os

from flask import Flask, request, jsonify




from flask_cors import CORS
app = Flask(__name__)
CORS(app)
load_dotenv()
googleAPIKey = os.getenv('googleAPIKey')
weathermapkey = os.getenv('weathermapkey')

@app.route("/", methods=["POST"])
def hello_world():
    frontendData = request.json

    test_data = {
      "fnum": frontendData["flightNum"],
      "date": frontendData["date"]
    }
    # jsonData = jsonify(test_data)
    # print('hi', jsonData)
    # print()
    # fnum = jsonData['fnum']
    # date = jsonData['date']

    test = runFunc(test_data['fnum'],test_data['date'])
    print('yo', test)
    return 'hi'

    

def runFunc(flightNumber, weatherDate):
    # flightNumber = input("AA Flight number: ")
    # weatherDate = input("Date YYYY-MM-DD: ")

    aaGrab = requests.get('http://localhost:4000/flights?date='+ weatherDate)
    listJSON = aaGrab.json()

    flightData = []

    for i in range(len(listJSON)):
        flightN = []
        flightN.append(listJSON[i]['flightNumber'])
        flightN.append(listJSON[i]['origin']['code'])
        flightN.append(listJSON[i]['destination']['code'])
        flightData.append(flightN)

    airlineCodeOne = ""
    airlineCodeTwo = ""
    for i in range(0,len(flightData)):
        if (flightNumber in flightData[i][0]):
            airlineCodeOne = flightData[i][1]
            airlineCodeTwo = flightData[i][2]

    print(airlineCodeOne + ' ' + airlineCodeTwo)

    resultOne = algod(airlineCodeOne)
    resultOne[0][0] = str(10 - resultOne[0][0]) + '/10'
    resultTwo = algod(airlineCodeTwo)
    resultTwo[0][0] = str(10 - resultTwo[0][0]) + '/10'
    return [airlineCodeOne + ' ' + airlineCodeTwo, resultOne[0], resultTwo[0] ]
    # retlist = 
    # return retlist
    # flight recommender
    # aa json file organizes based on locations of arr/dep
    # save index after remembering better date
    # call another get on that specific date to get new flight number on better day




def calc(temp, wspeed, fcast, humid, re):
  rating = re
  message = []
  message.append(fcast)
  if (temp >= 114):
    rating = rating - 4
    message.append("Temperatures above 114 can cause cancellations")
  if (temp <= 32 and humid > 90):
    rating = rating - 5
    message.append("Low temperatures and high humidity can cause icing which may cause cancellations")
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
  if ('rain' in fcast):
    rating = rating - 1
    message.append("Presence of rain could cause delays")
  

    # ADD STUFF TO ALGORITHM HEHE HAHA

  msglist = []
  msglist.append(rating)
  msglist.append(message)
  return msglist


def algod(airlineCode):
    airlineCity = ""
    with open('flight.csv', newline='') as csvfile:
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
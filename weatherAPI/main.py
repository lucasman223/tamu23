import weatherAlgo
import requests
import json

flightNumber = input("AA Flight number: ")
weatherDate = input("Date YYYY-MM-DD: ")

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
for i in range(0,100):
    if (flightNumber in flightData[i][0]):
        airlineCodeOne = flightData[i][1]
        airlineCodeTwo = flightData[i][2]

print(airlineCodeOne + ' ' + airlineCodeTwo)

print(weatherAlgo.algod(airlineCodeOne)[0])
print(weatherAlgo.algod(airlineCodeTwo)[0])

# flight recommender
# aa json file organizes based on locations of arr/dep
# save index after remembering better date
# call another get on that specific date to get new flight number on better day

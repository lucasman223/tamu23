import requests
import json

flightListAPIGrab = requests.get('https://app.goflightlabs.com/flights?access_key=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI0IiwianRpIjoiMzJiMjkzMjFkZDM1NTE1MGFmYTE1YzRmMWY4OGRkZWEzNGJiM2E3NDczYmVlNGIzODFiMzI1ZWY2OGJmMDdkYTczMmJkOTg2NzM1YTk0ODQiLCJpYXQiOjE2NzQ5NTY4MjAsIm5iZiI6MTY3NDk1NjgyMCwiZXhwIjoxNzA2NDkyODIwLCJzdWIiOiIxOTg2MCIsInNjb3BlcyI6W119.uVvP1j3dLGjWHmYmP4p1mG2nm_bF5J7Kazg3oliwwdox5iu8rpzqQQghaseEKTJCqazfJQsEUeWzG1xsCcl_Fg&limit=100')
listJSON = flightListAPIGrab.json()

# print(json.load(testJSON))
# with open('weatherAPI/flightdata.json') as myfile:
#     data = myfile.read()

# print(data)
# dat = json.loads(data)
flightData = []

for i in range(0,100):
    flightN = []
    flightN.append(listJSON['data'][i]['flight']['icaoNumber'])
    flightN.append(listJSON['data'][i]['departure']['iataCode'])
    flightN.append(listJSON['data'][i]['arrival']['iataCode'])
    flightData.append(flightN)

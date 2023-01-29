import weatherAlgo

flightNumber = input("Flight number: ")
airlineCodeOne = ""
airlineCodeTwo = ""
for i in range(0,100):
    if (flightNumber in weatherAlgo.flights[i][0]):
        airlineCodeOne = weatherAlgo.flights[i][1]
        airlineCodeTwo = weatherAlgo.flights[i][2]

print(airlineCodeOne + ' ' + airlineCodeTwo)
print(weatherAlgo.algod(airlineCodeOne))
print(weatherAlgo.algod(airlineCodeTwo))

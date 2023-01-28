import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve
import requests
import json
import csv

print("Enter Airline Code: \nExample: DFW")
airlineCode = input("Airline Code: ")

with open('Airport Codes by Country - Airport Codes List .csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        print(', '.join(row))
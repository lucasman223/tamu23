import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve
import requests
import json
import openpyxl as opxl

print("Enter Airline Code: \nExample: DFW")
airlineCode = input("Airline Code: ")

path = "airlineCodes.xlsx"
airlineCodeList = opxl.load_workbook(path)
airports = airlineCodeList.active


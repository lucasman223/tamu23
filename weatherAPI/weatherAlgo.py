import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve
import requests
import json
import openpyxl

print("Enter Airline Code: \nExample: DFW")
airlineCode = input("Airline Code: ")

airlineCodeList = openpyxl.load_workbook("airlineCodes.xlsx")

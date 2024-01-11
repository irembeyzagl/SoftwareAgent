#import libs
import requests
import pandas as pd
from bs4 import BeautifulSoup
from array import *

#float control*
def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

#Presentation Currency
def currency(s):
    deleteChar = "TL"
    clearText = "".join([char for char in s[1][1] if char not in deleteChar])
    if is_float(clearText):
        return float(clearText)
    else:
        return 1

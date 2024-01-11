#import libs
import requests
import pandas as pd
from bs4 import BeautifulSoup
from array import *

def scrap ():
    url = "https://uzmanpara.milliyet.com.tr/canli-borsa/"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0"}
    page = requests.get(url, headers = headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find_all("span")
    headers_table = ["BIST100","DOLAR","EURO","ALTIN","PETROL","BONO","BITCOIN"]
    arrtable1 = []
    for i in table:
        text = i.get_text()
        arrtable1.append(text)
    del arrtable1[21:]
    matrix_table = [[]]*7
    x=0
    z=0
    h=0
    for i in matrix_table:
        line = [0]*3
        y=0
        for m in line:
            if y==0:
                line[y] = headers_table[h]
                h=h+1
            else:
                line[y] = arrtable1[z]
            y=y+1
            z=z+1
        matrix_table[x]=line
        x=x+1
    
    return matrix_table

#import libs
import requests
import pandas as pd
from bs4 import BeautifulSoup
from array import *
import BasicFunctions as bf

def scrap (name):
    url = f"https://fintables.com/sirketler/{name}/finansal-tablolar/nakit-akim-tablosu"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0"}
    page = requests.get(url, headers = headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    contentName = soup.find("div", class_="text-base md:text-lg")
    contentName=contentName.get_text()
    table = soup.find_all("td")
    header = soup.find_all("th")
    numbers = soup.find_all("span")
    arrtable = []
    arrnumber = []
    arrtext = []
    for i in numbers: # Sayıları Çeker
        text = i.get_text()
        arrtext.append(text)
    for i in table:
        text = i.get_text()
        arrtable.append(text)
    currency = arrtable[5]
    x=0
    z=0
    for i in range(6):
        del arrtable[0]
    c = int(len(arrtable)/6) # Veri setindeki satır sayısını hesaplar
    matrix_table = [[]]*c
    for i in matrix_table:  # Çektiğmiz datayı (c)*6 olacak şekilde 2 boyutlu matrise alır
        line = [0]*6
        y=0
        for m in range(6):
            if y==0 and arrtable[z]=="":
                z=z+1
            line[y] = arrtable[z]
            y=y+1
            z=z+1
        matrix_table[x]=line
        x=x+1
    delete = "."
    j=0
    for i in arrtext:   # Çektiğimiz sayılardaki noktaları kaldırır böylece artık float türüne dönüştürülebilir
        clearText = "".join([char for char in arrtext[j] if char not in delete])
        if bf.is_float(clearText):
            arrnumber.append(float(clearText))
        j=j+1
    x=0
    y=0
    z=0
    dotChar="."
    percentChar="%"
    for row in matrix_table:    # Çektiğmiz veri setindeki yüzdelik değerler kaldırır arrnumber[]'dan float türündeki sayıları yerine koyar
        for element in row:
            if dotChar in element:
                matrix_table[x][y]=arrnumber[z]
                z=z+1
            elif percentChar in element:
                matrix_table[x][y]=""
            y=y+1
        x=x+1
        y=0
    headerLine=[]
    for i in header:    # Headerdaki elemanları headerLine[] dizesine ekler
        text=i.get_text()
        headerLine.append(text)
    matrix_table = [headerLine] + matrix_table
    save_name = f"{name}_cash_flow"
    return save_name, matrix_table


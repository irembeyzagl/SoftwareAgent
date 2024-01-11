from datetime import datetime
import csv
import Scrapping as sc
import time

# update frequency
def update(delay):
    matrix = []
    with open("date_info.csv", "r", newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            matrix.append(row)
    old_delay = matrix[0][1]
    nud = matrix[2][1]
    nud = delay - int(old_delay) + int(nud) #   nud = projected next update date
    matrix[2][1] = nud
    matrix[0][1] = delay
    with open("date_info.csv", "w", newline='') as file:
        writer = csv.writer(file)
        for row in matrix:
            writer.writerow(row)

# program her açıldığında otomatik kontrol edip belirdediğimiz delay tarihi geldiyse update başlatır
def update_data():
    now = datetime.now()
    month = int(now.strftime("%m"))
    matrix = []
    with open("date_info.csv", "r", newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            matrix.append(row)
    lud = int(matrix[1][1])   # lud = last update date
    temp = month - lud 
    delay = int(matrix[0][1])
    if temp >= delay:
        print("Güncelleme yapılıyor")
        sc_data()
    else:
        print("Henüz güncelleme tarihi gelmemiştir")

# list of corps.csv deki kayıtlı tüm şirketlerin bilgisini günceller
def sc_data():
    now = datetime.now()
    month = int(now.strftime("%m"))
    matrix = []
    with open("date_info.csv", "r", newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            matrix.append(row)
    delay = int(matrix[0][1])
    matrix[1][1] = month
    matrix[2][1] = month+delay
    with open("date_info.csv", "w", newline='') as file:
        writer = csv.writer(file)
        for row in matrix:
            writer.writerow(row)
    items=[]
    with open("List of Corps.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            items.append(row[0])
    for item in items:
        sc.scrap(item)
        print(f"{item} güncellendi")

# belirlediğimiz delaya göre bir sonraki öngörülen güncelleme tarihini verir
def nud():
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    matrix = []
    with open("date_info.csv", "r", newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            matrix.append(row)
    nud = int(matrix[2][1])
    return months[nud-1]

# listeden seçilen belirli dataları günceller 
def sc_data_selected(selected_corps):
    items = selected_corps
    str_items = " "
    for item in items:
        sc.scrap(item)
        print(f"{item} güncellendi")
        str_items = str_items + item + " "
    return f"Selected Companies Updated({str_items})"
    

#import libs
import tkinter as tk
from tkinter import ttk
from tkinter import Tk, Listbox, Button, Toplevel,messagebox
import requests
import csv
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np
from array import *
import Scrapping as sc
import ScrapLive
import pandas as pd
import csv
import UpdateListBox
import UpdateData
header = [""," "," "," "," "," "]
items=[]
UpdateData.update_data()
UpdateListBox.update()
with open("List of Corps.csv", 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        items.append(row[0])

def on_item_click(event):
    for row in tree1.get_children():
        tree1.delete(row)
    selected_item = listbox.get(listbox.curselection())
    with open(f"{selected_item}_balance_sheet.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            tree1.insert('', 'end', values=row)
    for row in tree2.get_children():
        tree2.delete(row)
    with open(f"{selected_item}_income_statement.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            tree2.insert('', 'end', values=row)
    for row in tree3.get_children():
        tree3.delete(row)
    with open(f"{selected_item}_cash_flow.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            tree3.insert('', 'end', values=row)

def buton_click():
    name = inputURL.get()
    if name in items:
        sc.scrap(name)
    else:
        sc.scrap(name)
        listbox.insert(tk.END, name)

def plot(event):
    selected_index = listbox2.curselection()
    
    
    selected_value = listbox2.get(selected_index)
    with open(f"{selected_value}_balance_sheet.csv", 'r') as file:
        reader = csv.reader(file)

        # Iterate through each row in the CSV
        for index2, row in enumerate(reader):
            # Check if the first column in the row is "Dönem Karı (Zararı)"
            if row and row[0] == "Dönem Net Kar/Zararı":
                print(f"The index of the row with 'Dönem Net Kar/Zararı' is: {index2}")
                rowx=index2
                print(rowx)
    file_path = f"{selected_value}_balance_sheet.csv"
    data = pd.read_csv(file_path, header=None, encoding='latin-1')
    data = data.fillna(0)
    zaman = data.iloc[0, 1:6]
    satislar = data.iloc[rowx, 1:6].astype(float) / 100000.0
    
    print(satislar)
    plt.subplot(2, 2, 1)
    plt.plot(zaman, satislar, marker='o')
    plt.title("Balance Sheet Grafiği")
    
    
    with open(f"{selected_value}_cash_flow.csv", 'r') as file:
        reader = csv.reader(file)

        # Iterate through each row in the CSV
        for index, row in enumerate(reader):
            # Check if the first column in the row is "Dönem Karı (Zararı)"
            if row and row[0] == "Dönem Karı (Zararı)":
                print(f"The index of the row with 'Dönem Karı (Zararı)' is: {index}")
                rowx2=index
                print(rowx2)
    file_path2 = f"{selected_value}_cash_flow.csv"
    data2 = pd.read_csv(file_path2, header=None, encoding='latin-1')
    data2 = data2.fillna(0)
    zaman2 = data2.iloc[0, 1:6]
    satislar2 = data2.iloc[rowx2, 1:6].astype(float) / 100000.0
    
    with open(f"{selected_value}_income_statement.csv", 'r') as file:
        reader = csv.reader(file)

        # Iterate through each row in the CSV
        for index3, row in enumerate(reader):
            # Check if the first column in the row is "Dönem Karı (Zararı)"
            if row and row[0] == "Brüt Kar (Zarar)":
                print(f"The index of the row with 'Brüt Kar(Zarar)' is: {index3}")
                rowx3=index3
                print(rowx3)
    
    
    file_path3 = f"{selected_value}_income_statement.csv"
    data3 = pd.read_csv(file_path3, header=None, encoding='latin-1')
    data3 = data3.fillna(0)
    zaman3 = data3.iloc[0, 1:6]
    satislar3 = data3.iloc[rowx3, 1:6].astype(float) / 100000.0
   

    plt.subplot(2, 2, 2)
    plt.plot(zaman2, satislar2, marker='o')
    plt.title('Cash FLow Grafiği')

    plt.subplot(2, 2,3)
    plt.plot(zaman3, satislar3, marker='o')
    plt.title('Income Statament Grafiği')

    # Alt grafikleri sıkıştır
    plt.tight_layout()

    # Grafikleri göster
    plt.show()

# Ana pencereyi oluştur
window = tk.Tk()
window.title("Project")
window.geometry("1920x1080")

# Stil oluştur
style = ttk.Style()

# Sekme boyutunu artırmak için stil konfigürasyonu yap
style.configure("TNotebook.Tab", padding=(50,10))

# Sekmeleri oluştur
tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)
tab6=ttk.Frame(tab_control)

# Sekme başlıklarını belirle
tab_control.add(tab1, text='Home Page')
tab_control.add(tab2, text='Financial Statements')
tab_control.add(tab3, text='Company Information')
tab_control.add(tab4, text='Summary Reports')
tab_control.add(tab6,text="Inflation/Interest")
tab_control.add(tab5, text="Admin")

data=ScrapLive.scrap()

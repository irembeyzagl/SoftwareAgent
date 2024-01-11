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
content_label = tk.Label(tab1, text="Welcome!", font=("Arial", 24), padx=50, pady=50)
content_label.pack(pady=20)

label=tk.Label(tab1,text="What we are doing?",font=("Arial", 18))
label.place(x=280,y=180)

label_metin=tk.Label(tab1,text="We are show to you the companies balace sheets, \n financial tables and news.")
label_metin.place(x=270,y=250)

label2=tk.Label(tab1,text="Why you should use?",font=("Arial", 18))
label2.place(x=660,y=180)

label_metin2=tk.Label(tab1,text="If you take care of with the companies \n for example you want to make investments \n you can look at this data.")
label_metin2.place(x=665,y=250)
        
label3=tk.Label(tab1,text="Index",font=("Arial",18 ))
label3.place(x=1100,y=180)

    
text1=data[0][0]+" Değeri = "+data[0][1]+" Artış/Azalış Oranı= "
text2=data[1][0]+" Değeri = "+data[1][1]+" Artış/Azalış Oranı= "
text3=data[2][0]+" Değeri = "+data[2][1]+" Artış/Azalış Oranı= "
text4=data[3][0]+" Değeri = "+data[3][1]+" Artış/Azalış Oranı= "
text5=data[4][0]+" Değeri = "+data[4][1]+" Artış/Azalış Oranı= "
text6=data[5][0]+" Değeri = "+data[5][1]+" Artış/Azalış Oranı= "
text7=data[6][0]+" Değeri = "+data[6][1]+" Artış/Azalış Oranı= "
yekle=180
xekle=1330
xx=1330
for i in range(7):
    artis_azalis_orani_str_without_percent = data[i][2].rstrip('%').replace(',', '.')
    artis_azalis_orani_float = float(artis_azalis_orani_str_without_percent)
    yekle=yekle+50
    xekle=xekle+3
    xx=xx+3
    if artis_azalis_orani_float > 0 :
        labelveri1_1=tk.Label(tab1,text=data[i][2],fg="green")
        labelveri1_1.place(x=xekle,y=yekle)
    if artis_azalis_orani_float < 0 :
        labelveri1_1=tk.Label(tab1,text=data[i][2],fg="red")
        labelveri1_1.place(x=xx,y=yekle)
labelveri=tk.Label(tab1,text=text1)
labelveri.place(x=1100,y=230)
labelveri2=tk.Label(tab1,text=text2)
labelveri2.place(x=1100,y=280)
labelveri3=tk.Label(tab1,text=text3)
labelveri3.place(x=1100,y=330)
labelveri4=tk.Label(tab1,text=text4)
labelveri4.place(x=1100,y=380)
labelveri5=tk.Label(tab1,text=text5)
labelveri5.place(x=1100,y=430)
labelveri6=tk.Label(tab1,text=text6)
labelveri6.place(x=1100,y=480)
labelveri7=tk.Label(tab1,text=text7)
labelveri7.place(x=1100,y=530)

inputURL = tk.Entry(tab2, width=100)
inputURL.place(x=500,y=15)
buttonURL = tk.Button(tab2, text="Search", command=buton_click)
buttonURL.place(x=1200,y=13)
listbox = tk.Listbox(tab2, selectmode=tk.SINGLE, height="43")
listbox.place(x=10, y=90)
for item in items:
        listbox.insert(tk.END, item)
listbox.bind("<ButtonRelease-1>", on_item_click)
columns = header
tree1 = ttk.Treeview(tab2, columns=columns, show='headings')
for col in columns:
    tree1.heading(col, text=col)
    tree1.column(col, width=300)
tree1.place(x=150, y=90)
tree2 = ttk.Treeview(tab2, columns=columns, show='headings')
for col in columns:
    tree2.heading(col, text=col)
    tree2.column(col, width=300)
tree2.place(x=150,y=325)
tree3 = ttk.Treeview(tab2, columns=columns, show='headings')
for col in columns:
    tree3.heading(col, text=col)
    tree3.column(col, width=300)
tree3.place(x=150,y=560)
def get_all_table_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all tables on the page
    tables = soup.find_all('table')

    # Extract data from each table
    all_table_data = []
    for table in tables:
        header_row = table.find('tr')
        headers = [cell.text.strip() for cell in header_row.find_all(['th', 'td'])]

        data_rows = table.find_all('tr')[1:]
        table_data = []
        for row in data_rows:
            row_data = [cell.text.strip() for cell in row.find_all('td')]
            table_data.append(row_data)

        all_table_data.append({'headers': headers, 'data': table_data})

    return all_table_data
def clear_treeviews():
    for widget in tab3.winfo_children():
        if isinstance(widget, ttk.Treeview):
            widget.destroy()
def show_all_table_data(all_table_data):
    clear_treeviews()
    for table_data in all_table_data:
        headers, data = table_data['headers'], table_data['data']
        tree = ttk.Treeview(tab3)
        tree.place(x=150,y=150,width=1000,height=500)
        tree["columns"] = headers
        tree["show"] = "headings"

        for header in headers:
            tree.heading(header, text=header)
            tree.column(header, anchor="center")

        for row in data:
            tree.insert("", "end", values=row)

        tree.pack(expand=False,padx=50,pady=20, fill="both")

    

def on_company_selected(event):
    selected_index = company_listbox.curselection()
    selected_company = company_listbox.get(selected_index)
    selected_company_url = f"https://fintables.com/sirketler/{selected_company.upper()}/sirket-bilgileri"
    
    all_table_data = get_all_table_data(selected_company_url)
    
    if all_table_data:
        show_all_table_data(all_table_data)
    else:
        print(f"No tables found for {selected_company} on {selected_company_url}")

# Example website URL
url = "https://fintables.com/sirketler/"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract company names from the page
company_names = [a.text.strip() for a in soup.find_all('a', class_='sirket-adi')]

# Create a Listbox to display company names
company_listbox = tk.Listbox(tab3)

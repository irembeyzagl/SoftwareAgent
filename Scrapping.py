import ScrapBalanceSheet as sbs
import ScrapIncomeStatement as sit
import ScrapCashFlow as scf
import SaveData as sd
import time

def scrap(name):
    name_to_be_recorded_1, balance_sheet = sbs.scrap(name)
    name_to_be_recorded_2, income_statement = sit.scrap(name)
    name_to_be_recorded_3, cash_flow = scf.scrap(name)
    sd.save_data(name,name_to_be_recorded_1,name_to_be_recorded_2,name_to_be_recorded_3,balance_sheet,income_statement,cash_flow)

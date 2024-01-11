import csv
import UpdateListBox
def save_data(name,name_to_be_recorded_1,name_to_be_recorded_2,name_to_be_recorded_3,balance_sheet,income_statement,cash_flow):
    with open("List of Corps.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name])
    with open(f"{name_to_be_recorded_1}.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        for row in balance_sheet:
            writer.writerow(row)
    with open(f"{name_to_be_recorded_2}.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        for row in income_statement:
            writer.writerow(row)
    with open(f"{name_to_be_recorded_3}.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        for row in cash_flow:
            writer.writerow(row)
    UpdateListBox.update()

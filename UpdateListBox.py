import csv

def update():
    with open("List of Corps.csv", mode='r', newline='') as file:
        reader = csv.reader(file)
        data = []
        for row in reader:
            data.append(row[0])
        unique_set = set(data)
        sorted_list = sorted(unique_set)
        c = len(sorted_list)
        data = [sorted_list[i:i + 1] for i in range(0, len(sorted_list), 1)]
    with open("List of Corps.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

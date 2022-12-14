import csv 
header = ['Name', 'Phone', 'Email', 'Address']
data = ['Sparsh', '987394032', 'hero@gmail.com','Kathmandu']

with open('details.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(header)

    writer.writerow(data)
import csv


with open('data-upsell-27.csv', 'r') as file, open('bomobi27.csv', 'w') as file_out:
    reader = csv.reader(file)
    writer = csv.writer(file_out)
    for row in reader:
        if row[3] != 'MobiFone':
            writer.writerow(row[:3])
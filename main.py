import csv


viettel_prefix = ['086', '096', '097', '098', '032', '033', '034', '035', '036', '037', '038', '039']

vina_prefix = ['088', '091', '094', '083', '084', '085', '081', '082']

mobi_prefix = ['089', '090', '093', '070', '079', '077', '076', '078']

vietnamobile_prefix = ['092', '056', '058']

gmobile_prefix = ['099', '059']

itelecom_prefix = ['087', '055']

with open('data-upsell-26.csv', 'r') as file, open('upsell.csv', 'w') as file_out:
    reader = csv.reader(file)
    writer = csv.writer(file_out)
    for row in reader:
        phone = row[1][:3]
        if phone in viettel_prefix:
            network = 'Viettel'
        elif phone in vina_prefix:
            network = 'VinaPhone'
        elif phone in mobi_prefix:
            network = 'MobiFone'
        elif phone in vietnamobile_prefix:
            network = 'Vietnamobile'
        elif phone in gmobile_prefix:
            network = 'Gmobile'
        elif phone in itelecom_prefix:
            network = 'Itelecom'
        else:
            network = 'Unknown'
        writer.writerow(row + [network])


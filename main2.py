import phonenumbers
import csv
from phonenumbers import carrier

phone = "+84966308398"




# try:
#     network = carrier.name_for_number(phone_obj, "en")
#     print(f"Số điện thoại thuộc nhà mạng: {network}")
# except phonenumbers.phonenumberutil.NumberFormatException:
#     print("Số điện thoại không hợp lệ.")
# except phonenumbers.phonenumberutil.NumberFormatError:
#     print("Không thể xác định nhà mạng cho số điện thoại này.")


with open('data-upsell-26.csv', 'r') as file, open('upsell2222.csv', 'w') as file_out:
    reader = csv.reader(file)
    writer = csv.writer(file_out)
    for row in reader:
        phone = "+84" + row[1][1:]
        print(phone)
        phone_obj = phonenumbers.parse(phone)
        network = carrier.name_for_number(phone_obj, "en")
        writer.writerow(row + [network])
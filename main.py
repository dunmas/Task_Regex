from pprint import pprint
import csv
import re
with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

for string in contacts_list:
    # Разбиваем ФИО контакта
    initials = ' '.join([string[0], string[1], string[2]])
    initials = initials.split()

    while len(initials) < 3:
        initials.append('')

    for i in range(0, 3):
        string[i] = initials[i]

    # Шаблоны для номера телефона и добавочного номера
    phone_pattern = r'((8|\+7)[\- ]?)?(\(?(\d{3})\)?[\- ]?)?([\d]{3})[\- ]*([\d]{2})[\- ]*([\d]{2})' \
                    r'([\s(]*доб.\s*(\d+)\)?)?'
    ext_phone_pattern = r'([\s(]?доб.\s*(\d+)\)?)'
    ext_phone = ''

    ext_find_res = re.findall(ext_phone_pattern, string[5])
    if ext_find_res:
        ext_phone = f' доб.{ext_find_res[0][1]}'

    substitution = r'+7(\4)\5-\6-\7'
    string[5] = re.sub(phone_pattern, substitution, string[5]) + ext_phone

#pprint(contacts_list)

from pprint import pprint
import csv
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

pprint(contacts_list)

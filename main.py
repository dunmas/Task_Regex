from pprint import pprint
import csv
import re
with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


# Gользовательская функция для объединения записей телефонной книги в нашем задании
def opt_concat(list1, list2, list_length):
    for i in range(0, list_length):
        if list2[i] != '':
            list1[i] = list2[i]


result_list = []
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

    match_flag = False
    for res_string in result_list:
        if res_string[0] == string[0] and res_string[1] == string[1]:
            match_flag = True
            opt_concat(res_string, string, len(string))

    if not match_flag:
        result_list.append(string)

with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(result_list)

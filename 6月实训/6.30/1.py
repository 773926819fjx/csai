import csv

wlist = [['NAME', 'DEP', 'ENG', 'MATH', 'CHINESE'],
         ['Rose', '法学', '89', '78', '65'],
         ['Mike', '历史', '56', '', '44'],
         ['John', '数学', '45', '65', '67']]
with open('1.csv', 'w', newline='', encoding='utf-8') as file:
    fwrite = csv.writer(file)
    fwrite.writerows(wlist)

with open('1.csv', 'r', encoding='utf-8') as F:
    fread = csv.reader(F)
    for item in fread:
        print(item)

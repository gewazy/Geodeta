import csv
import datetime
import re
import pyodbc
from tkinter import Tk
from tkinter.filedialog import askopenfilename


import init

'''
Dominik Jurkowski
2024-07-28
Wypełnianie bazy danych danymi z boomboxa
'''

print('\n'+34*'#'+' DYNAMIT v5 '+35*'#'+'\n')

# wskazanie pliku do otwarcia
Tk().withdraw()
open_filename = askopenfilename()
print("Otworz plik: " + open_filename)

save_filename = open_filename[:-4] + '_OK.csv'
print("Zapisz plik: " + save_filename)

file = open(open_filename)
numline = len(file.readlines()) - 1
print(f'Strzelono {numline} punktów.')
dzien = re.findall(r'\d{8}', open_filename)[-1]
dzien = f'{dzien[0:4]}-{dzien[4:6]}-{dzien[6:8]}'
y, m, d = dzien.split(sep='-')
jd = datetime.datetime(int(y), int(m), int(d)).strftime('%Y%j')

input(f'\nDzień juliański: {jd}, Ok? -> Enter ')

# zapis do pliku wynikowego
with open(open_filename, 'r') as r_BB:
    with open(save_filename, 'w', newline='') as w_BB:

        dict_reader = csv.DictReader(r_BB)
        fieldnames = dict_reader.fieldnames + ['Name', 'JulianDay', 'Local Easting', 'Local Northing']
        writer_csv = csv.DictWriter(w_BB, fieldnames)
        writer_csv.writeheader()

        prog = 0
        for row in dict_reader:
            prog += 1
            row['Name'] = str(int(float(row['Line']))) + str(int(float(row['Station'])))
            row['JulianDay'] = jd
            try:
                row['Local Northing'], row['Local Easting'] = init.tran(float(row['Lat(deg N)']), float(row['Lon(deg E)']))
            except TypeError:
                row['Local Northing'], row['Local Easting'] = (0, 0)
            writer_csv.writerow(row)
            print(f"\rpostęp {prog} z {numline} procentowo {int(prog * 100 / numline)} %", end="")

input('\nENTER żeby wgrać do bazy danych ; zamknij okno żeby wyjść')

params = []

# uwzględnia także błąd operatora boomboxa - brak pomiaru współrzędnych (wszystkie else). dj
with open(save_filename, 'r') as r_DYN:
    dict_reader_DYN = csv.DictReader(r_DYN)
    for row in dict_reader_DYN:
        params.append(
                      (row['Crew'] if row['Crew'] else '',
                       row['Unit'] if row['Unit'] else '',
                       row['ID'],
                       row['Line'] if row['Line'] else 0,
                       row['Station'] if row['Station'] else 0,
                       row['Time'][0:19] if row['Time'] else dzien,  # wstawienie daty eksportu boomboxa w sytuacji gdy nie ma zapisanego czasu odpalenia ładunku
                       row['Status'] if row['Status'] else '',
                       row['Lat(deg N)'] if row['Lat(deg N)'] else 0,
                       row['Lon(deg E)'] if row['Lon(deg E)'] else 0,
                       row['Alt(m)'] if row['Alt(m)'] else 0,
                       row['Name'] if row['Name'] else 0,
                       row['JulianDay'],
                       row['Local Easting'],
                       row['Local Northing'])
                     )

for row in params:
    print(row[3], row[4], row[-3], round(float(row[-2]), 2), round(float(row[-1]), 2))


# łaczenie z bazą danych i wgranie danych
cnxn = pyodbc.connect(init.CONN_STR)  # łączenie z bazą danych
crsr = cnxn.cursor()

# tworzenie tabeli DYN jeśli nie istnieje
try:
    crsr.execute('select * from DYN;')
except pyodbc.ProgrammingError:
    crsr.execute(
                 "CREATE TABLE DYN ("
                 "[Crew] text(32),"
                 "[Unit] text(32),"
                 "[ID] text(32),"
                 "[Line] Long,"
                 "[Station] Long,"
                 "[Time] Date,"
                 "[Status] text(32),"
                 "[Lat(deg N)] Double, "
                 "[Lon(deg E)] Double, "
                 "[Alt(m)] Single,"
                 "[Name] Long,"
                 "[JulianDay] Long, "
                 "[Local Easting] Double, "
                 "[Local Northing] Double);")

# Wgranie danych do tabeli
crsr.executemany("INSERT INTO DYN ([Crew], [Unit], [ID], [Line], [Station], [Time], [Status], "
                 "[Lat(deg N)], [Lon(deg E)], [Alt(m)], [Name], [JulianDay], [Local Easting], [Local Northing])"
                 "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", params)

crsr.close()
cnxn.commit()
cnxn.close()
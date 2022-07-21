import csv
import pyproj
import pyodbc
from tkinter import Tk
from tkinter.filedialog import askopenfilename

import init


def tran(lat, lon):
    # Transformacja wgs84(EPSG:4326) do cs92(EPSG:2180)
    trans = pyproj.Transformer.from_crs(4326, 2180)
    return trans.transform(lat, lon)

print(f"REDUKCJA WYSOKOŚCI NA VIB: -{init.REDUKCJA}m")

Tk().withdraw()
open_filename = askopenfilename()
print("Otworz plik: " + open_filename)

save_filename = open_filename[:-4] + '_OK.csv'
print("Zapisz plik: " + save_filename)


file = open(open_filename)
numline = len(file.readlines()) - 1

with open(open_filename, 'r') as r_PSS:
    with open(save_filename, 'w', newline='') as w_PSS:

        dict_reader = csv.DictReader(r_PSS)
        fieldnames = dict_reader.fieldnames + ['Name', 'Descriptor', 'VIB_easting', 'VIB_northing',
                                               'VIB_height', 'VIB_NMT']
        writer_csv = csv.DictWriter(w_PSS, fieldnames)
        writer_csv.writeheader()

        prog = 0
        for row in dict_reader:
            prog += 1
            row['Name'] = row['Line'][:4] + row['Station'][:4]
            row['Altitude'] = float(row['Altitude']) - init.REDUKCJA
            row['VIB_northing'], row['VIB_easting'] = tran(float(row['Lat']), float(row['Lon']))
            writer_csv.writerow(row)
            print(f"\rpostęp {prog} z {numline} procentowo {int(prog * 100 / numline)} %", end="")

input('\nENTER żeby wgrać do bazy danych ; zamknij okno żeby wyjść')

params = []

with open(save_filename, 'r') as r_VIB:
    dict_reader_VIB = csv.DictReader(r_VIB)
    for row in dict_reader_VIB:
        params.append(
                      (row['Encoder Index'],
                       row['Void'],
                       row['Shot ID'] if row['Shot ID'] != '' else None,
                       row['File Num'],
                       row['EP ID'],
                       row['Line'] if row['Shot ID'] != '' else None,
                       row['Station'] if row['Station'] != '' else None,
                       row['Date'],
                       row['Time'],
                       row['Comment'],
                       row['Record Index'],
                       row['EP Count'],
                       row['Crew ID'],
                       row['Unit ID'],
                       row['Start Code'],
                       row['GPS Time'],
                       row['Lat'],
                       row['Lon'],
                       row['Altitude'],
                       row['GPS Altitude'],
                       row['Sats'],
                       row['PDOP'],
                       row['HDOP'],
                       row['VDOP'],
                       row['Age'],
                       row['Quality'],
                       row['Start Time Delta'],
                       row['Sweep Number'],
                       row['Vibrator QC'],
                       row['X'] if row['X'] != '' else None,
                       row['Y'] if row['Y'] != '' else None,
                       None,
                       row['Name'] if row['Name'] != '' else None,
                       row['Descriptor'],
                       row['VIB_easting'],
                       row['VIB_northing'],
                       None,
                       None,
                       None)
                     )

for par in params:
    print(par)

# łaczenie z bazą danych i wgranie danych
cnxn = pyodbc.connect(init.CONN_STR)
crsr = cnxn.cursor()
crsr.executemany("INSERT INTO VIB ([Encoder Index], [Void], [Shot ID], [File Num], [EP ID], "
                 "[Line], [Station], [Date], [Time], [Comment], [Record Index], "
                 "[EP Count], [Crew ID], [Unit ID], [Start Code], "
                 "[GPS Time], [Lat], [Lon], [Altitude], [GPS Altitude], [Sats], [PDOP], "
                 "[HDOP], [VDOP], [Age], [Quality], [Start Time Delta], [Sweep Number], [Vibrator QC], "
                 "[X], [Y], [Uwagi_biur_vib], [Name], [Descriptor], [VIB_easting], [VIB_northing], "
                 "[VIB_height], [VIB_NMT], [deltaH(vib_NMT)])"
                 "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, "
                 "?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", params)
crsr.close()
cnxn.commit()
cnxn.close()


input('zrobione!! \n\nENTER żeby zamknąć okno')

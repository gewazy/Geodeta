import openpyxl
import pyodbc
from datetime import date, timedelta
from time import sleep

'''Generowanie pliku excel ze studniami dla permitingu '''

print("Tworzę połaczenie z bazą danych")
sleep(1)
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=..\01_database\PL-182 HUSOW.mdb;'  # ścieżka do bazy danych, do zmiany jeśli potrzeba
    )

cnxn = pyodbc.connect(conn_str)
crsr = cnxn.cursor()

# dane z bazy studnii, jak trzeba popraw kwerendę
qra = "Select " \
      "`Surveyor` AS 'NUMER GARMIN GPS', " \
      "`Station (value)` AS 'NUMER STUDNI', " \
      "`Local Northing` AS 'WSPÓŁRZĘDNE GPS N', " \
      "`Local Easting` AS 'WSPÓŁRZĘDNE GPS E', " \
      "`Survey Time (Local)` " \
      "From [POM_STUD] " \
      "where datediff ('d',`Survey Time (Local)`, Now()) <= 7 " \
      "Order By [POM_STUD].`Surveyor`, [POM_STUD].`Station (value)`"

std = crsr.execute(qra).fetchall()

crsr.close()
cnxn.close()

print('Tworzę plik Excel')

wb = openpyxl.Workbook()
ws = wb.active

ws.append(['NUMER GARMIN GPS', 'NUMER STUDNI', 'WSPÓŁRZĘDNE GPS N', 'WSPÓŁRZĘDNE GPS E', 'DATA POMIARU'])
for row in std:
    ws.append(item for item in row)

wb.save(f".\output\studnie\{str((date.today() - timedelta(days=1)).strftime('%Y%m%d'))}.xlsx")

print('Gotowe')
input("'Enter' by zakończyć")
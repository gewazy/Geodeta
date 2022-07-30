import xlrd
import pyodbc
from datetime import date
from time import sleep
import init

print('Pobieram dane z raportu wiertnictwa')
sleep(1)

try:
    plik = xlrd.open_workbook(init.DRILL_RAPORT)
    raport = plik.sheet_by_index(-2)
except FileNotFoundError as BladRaportu:
    print("Nie mogę znaleśźć pliku z raportem wiertnictwa, sprawdź ścieżkę w init.py\n\n", str(BladRaportu))
    input('Enter by zakończyć')


sleep(0.5)

input("\nOstatni dzien w rapocie to: {} "
      "\nOdwiercili: {} otworów"
      "\nNaciśnij ENTER by kontynuować lub zamknij okno by anulować".format(raport.name, raport.nrows - 3))


sleep(0.3)

print("\nPrzetwarzam dane do wgrania?")
data = "{}-{}-{}".format('0' + raport.name.strip().split('.')[0] if len(raport.name.strip().split('.')[0]) == 1
                         else raport.name.strip().split('.')[0], raport.name.strip().split('.')[1], date.today().year)
print()

params = []

# formatowanie danych z raportu do prawidłowej postaci
for rw in range(3, raport.nrows):
    params.append((int(str(int(raport.row(rw)[1].value)) + str(int(raport.row(rw)[2].value))), raport.row(rw)[4].value,
                   raport.row(rw)[8].value, raport.row(rw)[9].value.upper(), data, None, ''))
sleep(0.2)
print('Wgrywam do tabeli Drilling_Tab dane:\n')
sleep(0.5)

for p in params:
    print(p)
    sleep(0.2)
sleep(1)


# szukanie dubletów w raporcie wiertnictwa
if len([p[0] for p in params]) == len(set([p[0] for p in params])):
    print('\nNie ma dubletów w nazwach punktu, idę dalej\n')
else:
    print('\n***UWAGA!***\n DUBLET w nazwie punktu - Sprawdź w MDB  - kwerenda 84 \n')


# łaczenie z bazą danych i wgranie danych
try:
    cnxn = pyodbc.connect(init.CONN_STR)  # łączenie z bazą danych
except pyodbc.Error:
    print("Nie mogę znaleźć pliku MBD, sprawdź ścieżkę w init.py")
else:
    crsr = cnxn.cursor()
    crsr.executemany("INSERT INTO Drilling_Tab (station, depth, dr_name, dr_eq, dr_date, status, Uwagi_Biuro) "
                    "VALUES (?, ?, ?, ?, ?, ?, ?);", params)
    crsr.close()
    cnxn.commit()
    cnxn.close()

    print('Gotowe! '
          '\nSprawdź czy baza danych została zaktualizowana!\n'
          '\nPamiętaj by skontrolować dane i zrobić update postplotu.\n')
finally:
    input('Enter by zakończyć!')

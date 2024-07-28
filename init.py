import pyodbc
import pyproj
from datetime import datetime


def comment(a):
    '''Zapytanie o komentarz do raportu DPR'''
    return a + input(f"\nWprowadź komentarz: \n{a}")


def ddiff():
    '''Zapytanie  o dzień, z którego chemy zrobić raport'''

    try:
        a = int(input('Wpisz Daydiff:\n 0 -> dzisiejsze dane, 1-> dane wczorajsze [2, 3 ...itd...]:\n'))
    except ValueError:
        print('Podaj wartość liczbową.')
        ddiff()
    else:
        return a


def tran(lat, lon):
    transformer = pyproj.Transformer.from_crs(4326, 2180)
    return transformer.transform(lat, lon)


# Dane podstawowe:
GRUPA = 'PL202'
GEODETA = "Dominik Jurkowski"
ZUPT_BRYG = '[Goleń, Szatkowski], [Krawczyk, Dyja], [Istal, Nizioł]\n'
KOMENTARZ = 'Mało dróg, istniejące drogi trudne i niebezpieczne, długie przejścia. Bardzo dalekie dojazdy (ponad 1h) '
DDIFF = ddiff()
## ************************* PLIKI *********************************************

## pliki wejsciowe
MDB = r"c:\PL-202_LAGIEWNIKI_3D\database\PL-202_LAGIEWNIKI_3D.mdb"
DRILL_RAPORT = r"c:\PL-202_LAGIEWNIKI_3D\wiertnictwo\Raport wiertnictwa PL202.xls"

## pliki wyjściowe
DPR = (r'c:\PL-202_LAGIEWNIKI_3D\raporty\\PL-202_Łagiewniki W_Raport_geodezyjny_dzienny.xls',
       r'c:\PL-202_LAGIEWNIKI_3D\raporty\\2024_PL-202_ raport geodezja.xlsm')
JSON_FILE = r'.\output\line_station.json'
UKO_FILE = f'.\\output\\uko\\{str(datetime.now().strftime("%Y%m%d_%H%M"))}.uko'
QC_DOMIAR_GPS = rf'.\output\{GRUPA}_QC_Domiar_GPS.csv'
QC_DOMIAR_ZUPT = rf'.\output\{GRUPA}_QC_Domiar_ZUPT.txt'
WZNAWIANIE_FILE = rf'.\output\{GRUPA}_max_indeks.txt'


# ***********************ZMIENNE PODSTAWOWE ************************************

# zakresy linii punktów strzałowych i geofonów
SOURCES_TRACK = "4163 And 4514"
RECEIVERS_TRACK = "3100 And 3630"


# descriptory
VIBRATORY_DSC = "('x40', 'x45', 'x30', 'x35', 'x20', 'x25', 'x10', 'x15', 'xu', 'xu5', 'h40', 'h45', 'h30', 'h35', 'h20', 'h25', 'h10', 'h15')"
DYNAMITY_DSC = "('xt', 'xr')"

# redukcja wysokości dla wibratorów
REDUKCJA = 2.75

# *********************** STEROWNIK MDB oraz łączenie z bazą danych ************

sterownik = [x for x in pyodbc.drivers() if x.startswith('Microsoft Access Driver')]

if not sterownik:
    print('Brak zainstalowanych sterowników do MDB,\n'
          '- zainstaluj lub zaktualizuj MS Office do wersji 64 bit.\n'
          '- możesz również zainstalować Microsoft Access Database Engine 2010 Redistributable:\n'
          '  https://www.microsoft.com/en-US/download/details.aspx?id=13255')
    input('Enter by zakończyć')
else:
    CONN_STR = (r'DRIVER={' + sterownik[0] + '};' + fr'DBQ={MDB};')  # sterownik mdb


# *********************** ADRESY EMAIL *****************************************

SENDER = f"{GRUPA}surveyor@geofizyka.pl"
SUPERVISOR = 'xxxx@o2.pl'
RECIPIENT_DPR = (f"{GRUPA.lower()}partychief@geofizyka.pl",
                 "Wojciech.Burczynski@geofizyka.pl", "maciej.gruza@geofizyka.pl",
                 "tomasz.stankiewicz@geofizyka.pl", "ryszard.kolacz@geofizyka.pl", "renata.ciechanska@geofizyka.pl",
                 "andrzej.czemerzynski@geofizyka.pl", f"{GRUPA.lower()}geophysicist@geofizyka.pl")
RECIP_JSON = (f"{GRUPA.lower()}transcriber@geofizyka.pl", f"{GRUPA.lower()}lineboss@geofizyka.pl", "Slawomir.Bloniarz@geofizyka.pl")
RECIP_UKO = (f"{GRUPA.lower()}geophysicist@geofizyka.pl")


if __name__ == "__main__":
    print('Plik przechowuje podstawowe parametry')

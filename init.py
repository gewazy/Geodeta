import pyodbc

GRUPA = 'PL186'
GEODETA = "Dominik Jurkowski"
ZUPT_BRYG = '[Warzycki, Prządka], [Szetlak, Gubała], [Zaleski, Nizioł], [Adamski, Rygielski]\n'

# ************************* PLIKI **********************************************

## pliki wejsciowe
MDB = r"c:\PL-186_Zapalow_3D\01_database\Pl-186_Zapalow_3D.mdb"
DRILL_RAPORT = r"c:\PL-186_Zapalow_3D\09_wiertnictwo\Raport wiertnictwa PL186.xls"

## pliki wyjściowe
DPR = (r'c:\PL-186_Zapalow_3D\08_raport_geodezyjny\PL_186_Raport_geodezyjny_DPR.xlsx',
       r'c:\PL-186_Zapalow_3D\08_raport_geodezyjny\2022 PL186_ raport geodezja.xls')
JSON_FILE = r'.\output\line_station.json'
QC_DOMIAR_GPS = rf'.\output\{GRUPA}_QC_Domiar_GPS.csv'
QC_DOMIAR_ZUPT = rf'.\output\{GRUPA}_QC_Domiar_ZUPT.txt'
WZNAWIANIE_FILE = rf'.\output\{GRUPA}_max_indeks.txt'


# ***********************ZMIENNE PODSTAWOWE ************************************

# zakresy linii punktów strzałowych i geofonów
SOURCES_TRACK = "2064 And 2424"
RECEIVERS_TRACK = "3001 And 3761"

# w zależności kiedy robimy raport, domyślnie ddiff = 0
DDIFF = 0

# descriptory
VIBRATORY_DSC = "('x40', 'x45', 'x30', 'x35', 'x20', 'x25', 'x10', 'x15', 'xm', 'xm5')"
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
SUPERVISOR = 'Katarzyna.Szkliniarz@pgnig.pl'
RECIPIENT_DPR = (f"{GRUPA}partychief@geofizyka.pl",
                 "Wojciech.Burczynski@geofizyka.pl", "maciej.gruza@geofizyka.pl",
                 "tomasz.stankiewicz@geofizyka.pl", "ryszard.kolacz@geofizyka.pl",
                 "andrzej.czemerzynski@geofizyka.pl", f"{GRUPA}geophysicist@geofizyka.pl")
RECIP_JSON = (f"{GRUPA}transcriber@geofizyka.pl", f"{GRUPA}lineboss@geofizyka.pl")

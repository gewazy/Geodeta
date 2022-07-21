import csv, pyproj, tkinter, pyodbc
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def tran(lat, lon):
    '''transformacja współrzędnych miedzy układami, numer epsg układu'''
    transformer = pyproj.Transformer.from_crs(4326, 2180)
    return transformer.transform(lat, lon)

print("REDUKCJA WYSOKOŚCI NA VIB- 2.75m")

# ????
Tk().withdraw()
open_filename = askopenfilename()
print("Otworz plik: " + open_filename)

#from tkinter.filedialog import asksaveasfilename
#Tk().withdraw()
#save_filename = asksaveasfilename()
save_filename = open_filename[:-4] + '_OK.csv'
print("Zapisz plik: "+save_filename)
#'c:\\PL-173_Wielkie_Oczy_3D\\07_produkcja\\OK_PSS.csv

#row_count = sum(1 for row in open_filename)
#print(row_count)

#global prog
prog = 0
#print(prog)
file = open(open_filename)
numline = len(file.readlines()) - 1
#print (numline)

with open(open_filename,'r') as r_PSS:
    with open(save_filename,'w', newline='') as w_PSS:

        dict_reader = csv.DictReader(r_PSS)
        fieldnames = dict_reader.fieldnames  + ['Name','Descriptor','VIB_easting','VIB_northing','VIB_height','VIB_NMT']
        writer_csv = csv.DictWriter(w_PSS,fieldnames)
        writer_csv.writeheader()
        #numline = len(r_PSS.readlines())
        #print (numline - 1)




        for row in dict_reader:
            prog += 1
            row['Name']=row['Line'][:4] +row['Station'][:4]
            row['Altitude']=float(row['Altitude'])-2.75
            row['VIB_northing'],row['VIB_easting'] = tran(float(row['Lat']),float(row['Lon']))
            writer_csv.writerow(row)
            print(f"\rpostęp {prog} z {numline} procentowo {int(prog * 100 / numline)} %",end="")
        #print(f"\n{prog}")

#dbf.from_csv('c:\PG\python test\OK_PSS.csv',field_names='Encod_Ind Vod Shot_ID File_Num EP_ID Line Station Date Time Comment TB_Date TB_Time TB_Micro Record_Ind EP_Count Crew_ID Unit_ID Start_Code Sweep_Chec Param_Chec Phase_Max Phase_Avg Force_Max Force_Avg THD_Max THD_Avg Force_Out GPS_Time Lat Lon Altitude GPS_Alti Sats PDOP HDOP VDOP Age Quality St_Tim_Del Sweep_Num Signat Flsh_Stor Flsh_Stat USB_Stor Vib_QC Encoder_ID Encoder_IP Max_Viscos Min_Viscos Avg_Viscos Max_Stiff Min_Stiff Avg_Stiff Trgt_Force Bearing X Y  Name Descriptor VIBeasting VIBnorting VIBheight'.split(),to_disk=True)

w_PSS.close()
r_PSS.close()
#input('\nENTER żeby zamknąć okno')

input('\nENTER żeby wgrać do bazy danych ; zamknij okno żeby wyjść')

params = []

with open(save_filename,'r') as r_VIB:
    dict_reader_VIB = csv.DictReader(r_VIB)
    for row in dict_reader_VIB:
        params.append((
        row['Encoder Index'],
        row['Void'],
        row['Shot ID'] if row['Shot ID'] != '' else None,
        row['File Num'],
        row['EP ID'],
        row['Line'] if row['Shot ID'] != '' else None,
        row['Station'] if row['Station'] != '' else None,
        row['Date'],
        row['Time'],
        row['Comment'],
        row['TB Date'],
        row['TB Time'],
        row['TB Micro'],
        row['Record Index'],
        row['EP Count'],
        row['Crew ID'],
        row['Unit ID'],
        row['Start Code'],
        row['Phase Max'],
        row['Phase Avg'],
        row['Force Max'],
        row['Force Avg'],
        row['THD Max'],
        row['THD Avg'],
        row['Force Out'],
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
        row[''],
        row['Name'] if row['Name'] != '' else None,
        row['Descriptor'],
        row['VIB_easting'],
        row['VIB_northing'],
        None,
        None,
        None
        ))

print(params)

# łaczenie z bazą danych i wgranie danych
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=c:\PL-182_Husow_3D\01_database\PL-182 HUSOW.mdb;'  # ścieżka do bazy danych, do zmiany jeśli potrzeba
    )

cnxn = pyodbc.connect(conn_str)  # łączenie z bazą danych
crsr = cnxn.cursor()
crsr.executemany("INSERT INTO VIB ([Encoder Index], [Void], [Shot ID], [File Num], [EP ID], [Line], [Station], [Date], [Time], [Comment], [TB Date], [TB Time], [TB Micro], [Record Index], [EP Count], [Crew ID], [Unit ID], [Start Code], [Phase Max], [Phase Avg], [Force Max], [Force Avg], [THD Max], [THD Avg], [Force Out], [GPS Time], [Lat], [Lon], [Altitude], [GPS Altitude], [Sats], [PDOP], [HDOP], [VDOP], [Age], [Quality], [Start Time Delta], [Sweep Number], [Vibrator QC], [X], [Y], [Uwagi_biur_vib], [Name], [Descriptor], [VIB_easting], [VIB_northing], [VIB_height], [VIB_NMT], [deltaH(vib_NMT)])"
                 "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", params)
crsr.close()
cnxn.commit()
cnxn.close()


input('zrobione!! \n\nENTER żeby zamknąć okno')

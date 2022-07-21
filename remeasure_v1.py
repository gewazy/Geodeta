import pyodbc



# łączenie z bazą
conn_str = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' # sterownik mdb
            r'DBQ=..\01_database\PL-182 HUSOW.mdb;')  # ścieżka do bazy danych

cnxn = pyodbc.connect(conn_str)  # łączenie z bazą danych
crsr = cnxn.cursor()

# tworzę kwerendy

#KWERWNDA TESTOWA !!! nie działa
upd = "UPDATE [REMEASURE] " \
      "SET [REMEASURE].`Status` = [POSTPLOT].`Status` " \
      "FROM [REMEASURE] INNER JOIN [POSTPLOT] ON [REMEASURE].`Station (value)` = [POSTPLOT].`Station (value)` " \

# te kwerendy działają
upd_s = "UPDATE [REMEASURE],[POSTPLOT] " \
       "SET " \
       "[REMEASURE].`COG Local Easting` = [POSTPLOT].`COG Local Easting`, " \
       "[REMEASURE].`COG Local Northing` = [POSTPLOT].`COG Local Northing`, " \
       "[REMEASURE].`COG Local Height` = [POSTPLOT].`COG Local Height`, " \
       "[REMEASURE].`Acquired_Julian_Day` = [POSTPLOT].`Acquired_Julian_Day`, " \
       "[REMEASURE].`Descriptor` = [POSTPLOT].`Descriptor`, " \
       "[REMEASURE].`Comment` = [POSTPLOT].`Comment`, " \
       "[REMEASURE].`Indeks` = [POSTPLOT].`Indeks`, " \
       "[REMEASURE].`Description1` = [POSTPLOT].`Description1`, " \
       "[REMEASURE].`Description2` = [POSTPLOT].`Description2`, " \
       "[REMEASURE].`depth` = [POSTPLOT].`depth`, " \
       "[REMEASURE].`dr_name` = [POSTPLOT].`dr_name`, " \
       "[REMEASURE].`dr_eq` = [POSTPLOT].`dr_eq`, " \
       "[REMEASURE].`dr_date` = [POSTPLOT].`dr_date`, " \
       "[REMEASURE].`Uwagi_Biuro` = [POSTPLOT].`Uwagi_Biuro`, " \
       "[REMEASURE].`PPV` = [POSTPLOT].`PPV`, " \
       "[REMEASURE].`Status` = '2' " \
       "WHERE " \
       "[POSTPLOT].`Station (value)` > 0 And " \
       "[POSTPLOT].`Track` Between 4060 And 4550 And " \
       "datediff ('d', [REMEASURE].`Survey Time (Local)`, now()) = 0 And " \
       "[REMEASURE].`Indeks` = [POSTPLOT].`Indeks` And " \
       "[REMEASURE].`Station (value)` = [POSTPLOT].`Station (value)` "

upd_r = "UPDATE [REMEASURE],[POSTPLOT] " \
        "SET " \
        "[REMEASURE].`Descriptor` = [POSTPLOT].`Descriptor` " \
        "WHERE " \
        "[POSTPLOT].`Station (value)` > 0 And " \
        "[POSTPLOT].`Track` Between 1175 And 1930 And " \
        "datediff ('d', [REMEASURE].`Survey Time (Local)`, now()) = 0 And " \
        "[REMEASURE].`Indeks` = [POSTPLOT].`Indeks` And " \
        "[REMEASURE].`Station (value)` = [POSTPLOT].`Station (value)` "


upd_s_postplot = "UPDATE [REMEASURE],[POSTPLOT] " \
                 "SET " \
                 "[POSTPLOT].`Station (value)` = '0' " \
                 "WHERE " \
                 "[POSTPLOT].`Station (value)` > 0 And " \
                 "[POSTPLOT].`Track` Between 4060 And 4550 And " \
                 "datediff ('d', [REMEASURE].`Survey Time (Local)`, now()) = 0 And " \
                 "[REMEASURE].`Indeks` = [POSTPLOT].`Indeks` And " \
                 "[REMEASURE].`Station (value)` = [POSTPLOT].`Station (value)` "

upd_r_postplot = "UPDATE [REMEASURE],[POSTPLOT] " \
                 "SET " \
                 "[POSTPLOT].`Station (value)` = '0' " \
                 "WHERE " \
                 "[POSTPLOT].`Station (value)` > 0 And " \
                 "[POSTPLOT].`Track` Between 1175 And 1930 And " \
                 "datediff ('d', [REMEASURE].`Survey Time (Local)`, now()) = 0 And " \
                 "[REMEASURE].`Indeks` = [POSTPLOT].`Indeks` And " \
                 "[REMEASURE].`Station (value)` = [POSTPLOT].`Station (value)` "

input('\n jestem gotowy aby wypełnić pola w tablicy [REMEASURE]'
      '\n CZY INDEKSY SIĘ ZGADZAJĄ ??? jeżeli tak daj ENTER')

#wykonuje update pól w tabeli [REMEASURE]
crsr.execute(upd_s)
crsr.execute(upd_r)

#zatwierdza update pól w tabeli [REMEASURE]
cnxn.commit()

input('\n ENTER by wyzerować [POSTPLOT].`Station (value)` = 0 lub zrezygnuj zamykając okno')

#wykonuje zerowanie pól w tabeli [POSTPLOT]
crsr.execute(upd_s_postplot)
crsr.execute(upd_r_postplot)


cnxn.commit()
cnxn.close()

input('\n wyzerowałem [POSTPLOT].`Station (value)` na pomierzonych punktach w tablicy [REMEASURE]'
      '\n mozesz podpiąć tablicę [REMEASURE] do tablicy [POSTPLOT]'
      '\n daj ENTER żeby zamknąć okno')


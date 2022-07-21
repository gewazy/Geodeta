import pyodbc, time



# łączenie z bazą
conn_str = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' # sterownik mdb
            r'DBQ=c:\PL-182_Husow_3D\!_PL182PY\baza\PL-182.mdb;')  # ścieżka do bazy danych


cnxn = pyodbc.connect(conn_str)  # łączenie z bazą danych
crsr = cnxn.cursor()

# tworzę kwerendy

upd_postplot_all = "UPDATE [POSTPLOT] " \
                   "SET [POSTPLOT].`IsDuplicate` = NULL "

# działa bardzo długo!!!!!! - śmieć
# upd_dup_all = "UPDATE [POSTPLOT] " \
#              "SET [POSTPLOT].`IsDuplicate` = '1' " \
#              "WHERE " \
#              "[POSTPLOT].`Station (value)` IN (SELECT [POSTPLOT].`Station (value)`  FROM [POSTPLOT] WHERE [POSTPLOT].`Station (value)` > 0 GROUP BY [POSTPLOT].`Station (value)` HAVING COUNT ([POSTPLOT].`Station (value)`)>1)"

# nie działa
upd_dup_all_1 = "UPDATE [POSTPLOT], " \
                "SET [POSTPLOT].`IsDuplicate` = '1'" \
                "FROM" \
                "(SELECT [POSTPLOT].`Station (text)`  FROM [POSTPLOT]  GROUP BY [POSTPLOT].`Station (text)` HAVING COUNT ([POSTPLOT].`Station (text)`) > 1 ) as dup" \
                "WHERE " \
                "[POSTPLOT].`Station (text)` = [Dup].`Station (text)`"

select = "SELECT [POSTPLOT].`Station (text)`  FROM [POSTPLOT]  GROUP BY [POSTPLOT].`Station (text)` HAVING COUNT ([POSTPLOT].`Station (text)`) > 1  "

# może podejscie:
# -- wybierz wszystkie punkty z dnia dzisiejszego (station Text) -
# -- wyszukuje wszystkie duplikaty
# update tylko na punktach z dnia dzisiejszego....

'''
qra_all_dup = "SELECT [POSTPLOT].`Station (text)`  FROM [POSTPLOT]  GROUP BY [POSTPLOT].`Station (text)` HAVING COUNT ([POSTPLOT].`Station (text)`) > 1  "

qra_daily = "UPDATE [POSTPLOT] " \
            "SET [POSTPLOT].`IsDuplicate` = '1' " \
            "WHERE " \
            "datediff('d',[POSTPLOT].`Survey Time (Local)`, Now()) = 0  and [POSTPLOT].`Station (value)` IN (SELECT [POSTPLOT].`Station (value)`  FROM [POSTPLOT] WHERE [POSTPLOT].`Station (value)` > 0 GROUP BY [POSTPLOT].`Station (value)` HAVING COUNT ([POSTPLOT].`Station (value)`)>1)"
'''
# wykonuje select na bazie danych
crsr.execute(select)
sel = crsr.fetchall()


# tworzy i wypelnia liste wynikiem kwerendy select
duplikaty = []
for row in sel:
    duplikaty.append(row[0])


upd_dup_daily = f"UPDATE [POSTPLOT] SET [POSTPLOT].`IsDuplicate` = \'1\' WHERE datediff('d',[POSTPLOT].`Survey Time (Local)`, Now()) = 2 and  [POSTPLOT].`Station (text)` IN ({str(duplikaty)[1:-1]})"
upd_dup_all = f"UPDATE [POSTPLOT] SET [POSTPLOT].`IsDuplicate` = \'1\' WHERE [POSTPLOT].`Station (Value)` > 0 and [POSTPLOT].`Station (text)` IN ({str(duplikaty)[1:-1]})"

#wykonuje czyszczenie pola `IsDuplicate` w tabeli [POSTPLOT]
cnxn.autocommit = True
# crsr.execute(upd_postplot_all)


input('ok? UWAGA bedzie dlugo: około 140 sekund')


# zmienna do pomiaru czasu - poczatek

start = time.perf_counter()

#wykonuje update pola `IsDuplicate` w tabeli [POSTPLOT]
# crsr.execute(upd_dup_daily)
crsr.execute(upd_dup_all)

# zmienna do pomiaru czasu - koniec
end = time.perf_counter()

# wynik pomieru czasu
run_time = end -start
print(f'Wypełnienie IsDuplicate wykonano w: {run_time:.4f} sekund\n')

input('sprawdz update')

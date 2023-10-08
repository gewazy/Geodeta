import pyodbc
import init
import kury


# łączenie z bazą danych
cnxn = pyodbc.connect(init.CONN_STR)
crsr = cnxn.cursor()


input('\nWypełnić pola w tablicy [REMEASURE]?'
      '\nJeśli indeksy się zgadzają -> ENTER.')

#wykonuje update pól w tabeli [REMEASURE]
crsr.execute(kury.UPD_S)
crsr.execute(kury.UPD_R)
cnxn.commit()
print('Tablica [REMEASURE] wypełniona')


input('\nWyzerować [POSTPLOT].`Station (value)` = 0?'
      '\nEnter lub zrezygnuj zamykając okno.')

#wykonuje zerowanie pól w tabeli [POSTPLOT]
crsr.execute(kury.POSTPLOT_ZEROWANIE)
cnxn.commit()
print('[Postplot].`station (value)` wyzerowane')

# kopiowanie danych z REMEASURE do POSTPLOTU
input('\nSkopiować dane z [REMEASURE] do [POSTPLOT]?'
      '\nEnter lub zrezygnuj zamykając okno.')
crsr.execute(kury.COPY_REMEASURE)
cnxn.commit()
print('Skopiowano [REMEASURE] do [POSTPLOT]u.')

cnxn.close()

input('\nWykonano.'
      '\nENTER by zamknąć okno')


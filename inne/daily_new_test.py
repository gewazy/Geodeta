import pyodbc
import xlsxwriter

import init

qra = "Select " \
      "`Station (text)`, `Station (value)`, " \
      "`Track`, `Bin`, " \
      "`Descriptor`, `Description1`, `Description2`, `Comment`, " \
      "`Survey Time (Local)`, `Survey Mode (text)`, `Surveyor` " \
      "From [POSTPLOT] " \
      "Where " \
      f"(datediff ('d', `Survey Time (Local)`,Now()) = {init.DDIFF}) And " \
      "(" \
      "(`Station (value)` > 0 and `Station (text)` Not Like '88%') " \
      "OR `Station (text)` Like 'cp%' " \
      "OR `Station (text)` Like '?88%'" \
      ")  " \
      "Order By `Surveyor`,`Survey Time (Local)`"



cnxn = pyodbc.connect(init.CONN_STR)  # łączenie z bazą danych
crsr = cnxn.cursor()


crsr.execute(qra)
daily_data = crsr.fetchall()


crsr.close()
cnxn.close()


print(daily_data)

workbook = xlsxwriter.Workbook(r".\input\2022 PL186_raport geodezja.xlsm")
workbook.op
wsheets = workbook.worksheets()

print(wsheets)

wsheets[-2].write("A2", 'Hello my Master!!')
workbook.close()

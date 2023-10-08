import init


'''
Zapytania SQL

W pliku init.py podajemy przedziały linii oraz descriptory używane na grupie.
Tu kwerend nie zmieniajmy, chyba że zmiana okazuje się niezbędna. 
'''


''' Zapytania do raportu DPR '''
TYCZ_R = f"Select " \
         "[Ludziki].`Nr_auta`,  " \
         "'1', " \
         "IIF (`Survey Mode (value)`=5, 'ZUPT ', IIF (`Survey Mode (value)`=6,'TACHIMETR', IIF (`Survey Mode (value)` in (3, 10, 1, 2, 13, 12, 9),'GPS',''))) & ' ' & [POSTPLOT].`Surveyor`, " \
         "Count (*) " \
         "From " \
         "[POSTPLOT] Left Join [Ludziki] on [POSTPLOT].`Surveyor`=[Ludziki].`Surveyor` " \
         "Where " \
         "[POSTPLOT].`Offset (North)` is not NULL " \
         "and `Is_Duplicate` is NULL " \
         "And [POSTPLOT].`Station (value)` > 0 " \
         f"And [POSTPLOT].`Track` Between {init.RECEIVERS_TRACK} " \
         f"And datediff('d',[POSTPLOT].`Survey Time (Local)`,Now()) = {init.DDIFF} " \
         "Group By " \
         "IIF (`Survey Mode (value)`=5, 'ZUPT ', IIF (`Survey Mode (value)`=6, 'TACHIMETR', IIF (`Survey Mode (value)` in (3, 10, 1, 2, 13, 12, 9),'GPS',''))), " \
         "[POSTPLOT].`Surveyor`, " \
         "[POSTPLOT].`Julian Date (Local)`, " \
         "[Ludziki].`Nr_auta`"

TYCZ_S = f"Select " \
         "[Ludziki].`Nr_auta`, " \
         " '1', " \
         "IIF (`Survey Mode (value)`=5, 'ZUPT ', IIF (`Survey Mode (value)`=6,'TACHIMETR', IIF (`Survey Mode (value)` in (3, 10, 1, 2, 13, 12, 9),'GPS',''))) & ' ' & [POSTPLOT].`Surveyor`, " \
         "Count (*) " \
         "From " \
         "[POSTPLOT] Left Join [Ludziki] on [POSTPLOT].`Surveyor`=[Ludziki].`Surveyor` " \
         "Where " \
         "[POSTPLOT].`Offset (North)` is not NULL " \
         "and `Is_Duplicate` is NULL " \
         "And [POSTPLOT].`Station (value)` > 0 " \
         f"And  [POSTPLOT].`Track` Between {init.SOURCES_TRACK}" \
         f"And datediff ('d',[POSTPLOT].`Survey Time (Local)`,Now()) = {init.DDIFF} " \
         "Group By " \
         "IIF (`Survey Mode (value)`=5, 'ZUPT ', IIF (`Survey Mode (value)`=6, 'TACHIMETR', IIF (`Survey Mode (value)` in (3, 10, 1, 2, 13, 12, 9),'GPS',''))), " \
         "[POSTPLOT].`Surveyor`, " \
         "[POSTPLOT].`Julian Date (Local)`, " \
         "[Ludziki].`Nr_auta`"

ZM_R = f"Select " \
       "[Ludziki].`Nr_auta`,  " \
       "'1' , " \
       "IIF (`Survey Mode (value)`=5, 'ZUPT ', IIF (`Survey Mode (value)`=6,'TACHIMETR', IIF (`Survey Mode (value)` in (3, 10, 1, 2, 13, 12, 9),'GPS',''))) & ' ' & [POSTPLOT].`Surveyor` , " \
       "Count (*) " \
       "From " \
       "[POSTPLOT] Left Join [Ludziki] on [POSTPLOT].`Surveyor`=[Ludziki].`Surveyor` " \
       "Where " \
       "[POSTPLOT].`Offset (North)` is not NULL " \
       "and `Is_Duplicate` is not NULL " \
       "And [POSTPLOT].`Station (value)` > 0 " \
       f"And  [POSTPLOT].`Track` Between {init.RECEIVERS_TRACK}" \
       f"And datediff ('d',[POSTPLOT].`Survey Time (Local)`,Now()) = {init.DDIFF} " \
       "Group By " \
       "IIF (`Survey Mode (value)`=5, 'ZUPT ', IIF (`Survey Mode (value)`=6, 'TACHIMETR', IIF (`Survey Mode (value)` in (3, 10, 1, 2, 13, 12, 9),'GPS',''))), " \
       "[POSTPLOT].`Surveyor`, " \
       "[POSTPLOT].`Julian Date (Local)`, " \
       "[Ludziki].`Nr_auta`"

ZM_S = f"Select " \
       "[Ludziki].`Nr_auta`,  " \
       "'1', " \
       "IIF (`Survey Mode (value)`=5, 'ZUPT ', IIF (`Survey Mode (value)`=6,'TACHIMETR', IIF (`Survey Mode (value)` in (3, 10, 1, 2, 13, 12, 9),'GPS',''))) & ' ' & [POSTPLOT].`Surveyor`, " \
       "Count (*) " \
       "From " \
       "[POSTPLOT] Left Join [Ludziki] on [POSTPLOT].`Surveyor`=[Ludziki].`Surveyor` " \
       "Where " \
       "[POSTPLOT].`Offset (North)` is not NULL " \
       "and `Is_Duplicate` is not NULL " \
       "And [POSTPLOT].`Station (value)` > 0 " \
       f"And  [POSTPLOT].`Track` Between {init.SOURCES_TRACK}" \
       f"And datediff ('d',[POSTPLOT].`Survey Time (Local)`,Now()) = {init.DDIFF} " \
       "Group By " \
       "IIF (`Survey Mode (value)`=5, 'ZUPT ', IIF (`Survey Mode (value)`=6, 'TACHIMETR', IIF (`Survey Mode (value)` in (3, 10, 1, 2, 13, 12, 9),'GPS',''))), " \
       "[POSTPLOT].`Surveyor`, " \
       "[POSTPLOT].`Julian Date (Local)`, " \
       "[Ludziki].`Nr_auta`"

RE_S = "Select " \
       "[Ludziki].`Nr_auta`, " \
       " '1' , " \
       "IIF (`Survey Mode (value)`=5, 'ZUPT ', IIF (`Survey Mode (value)`=6,'TACHIMETR', IIF (`Survey Mode (value)` in (3, 10, 1, 2, 13, 12, 9),'GPS',''))) & ' ' & [REMEASURE].`Surveyor` , " \
       "Count (*) " \
       "From " \
       "[REMEASURE] Left Join [Ludziki] on [REMEASURE].`Surveyor`=[Ludziki].`Surveyor` " \
       "Where " \
       "[REMEASURE].`Offset (North)` is not NULL " \
       "and `Is_Duplicate` is NULL " \
       "And [REMEASURE].`Station (value)` > 0 " \
       f"And  [REMEASURE].`Track` Between {init.SOURCES_TRACK} " \
       f"And datediff ('d',[REMEASURE].`Survey Time (Local)`,Now()) = {init.DDIFF} " \
       "Group By " \
       "IIF (`Survey Mode (value)`=5, 'ZUPT ', IIF (`Survey Mode (value)`=6, 'TACHIMETR', IIF (`Survey Mode (value)` in (3, 10, 1, 2, 13, 12, 9),'GPS',''))), " \
       "[REMEASURE].`Surveyor`, " \
       "[REMEASURE].`Julian Date (Local)`, " \
       "[Ludziki].`Nr_auta`"

RE_R = "Select " \
       "[Ludziki].`Nr_auta`,  " \
       "'1', " \
       "IIF (`Survey Mode (value)`=5, 'ZUPT ', IIF (`Survey Mode (value)`=6,'TACHIMETR', IIF (`Survey Mode (value)` in (3, 10, 1, 2, 13, 12, 9),'GPS',''))) & ' ' & [REMEASURE].`Surveyor`, " \
       "Count (*) " \
       "From " \
       "[REMEASURE] Left Join [Ludziki] on [REMEASURE].`Surveyor`=[Ludziki].`Surveyor` " \
       "Where " \
       "[REMEASURE].`Offset (North)` is not NULL " \
       "and `Is_Duplicate` is NULL " \
       "And [REMEASURE].`Station (value)` > 0 " \
       f"And [REMEASURE].`Track` Between {init.RECEIVERS_TRACK} " \
       f"And datediff('d',[REMEASURE].`Survey Time (Local)`,Now()) = {init.DDIFF} " \
       "Group By " \
       "IIF (`Survey Mode (value)`=5, 'ZUPT ', IIF (`Survey Mode (value)`=6, 'TACHIMETR', IIF (`Survey Mode (value)` in (3, 10, 1, 2, 13, 12, 9),'GPS',''))), " \
       "[REMEASURE].`Surveyor`, " \
       "[REMEASURE].`Julian Date (Local)`, " \
       "[Ludziki].`Nr_auta`"

OTG = "Select " \
      "[Ludziki].`Nr_auta`,  " \
      "'1', " \
      "IIF (`Survey Mode (value)`=5, 'ZUPT ', IIF (`Survey Mode (value)`=6,'TACHIMETR', IIF (`Survey Mode (value)` in (3, 10, 1, 2, 13, 12, 9),'GPS',''))) & ' ' & [OTG].`Surveyor`, " \
      "Count (*) " \
      "From " \
      "[OTG] Left Join [Ludziki] on [OTG].`Surveyor`=[Ludziki].`Surveyor` " \
      "Where " \
      "[OTG].`Station (value)` > 0 " \
     f"And datediff('d',[OTG].`Survey Time (Local)`,Now()) = {init.DDIFF} " \
      "Group By " \
      "IIF (`Survey Mode (value)`=5, 'ZUPT ', IIF (`Survey Mode (value)`=6, 'TACHIMETR', IIF (`Survey Mode (value)` in (3, 10, 1, 2, 13, 12, 9),'GPS',''))), " \
      "[OTG].`Surveyor`, " \
      "[OTG].`Julian Date (Local)`, " \
      "[Ludziki].`Nr_auta`"

QC_R = "Select [POSTPLOT].`Station (value)`, [POSTPLOT].`Local Easting`, [POSTPLOT].`Local Northing`, [POSTPLOT].`WGS84 Latitude`, [POSTPLOT].`WGS84 Longitude`, [POSTPLOT].`Local Height`, [POSTPLOT].`Index`" \
       "From [POSTPLOT] " \
      f"Where [POSTPLOT].`Station (value)` > 0 And [POSTPLOT].`Track` Between {init.RECEIVERS_TRACK} And [POSTPLOT].`Status` >=1 And [POSTPLOT].`Status` <= 11 And (([POSTPLOT].`Survey Mode (value)` Not In (3,5,6)) Or ([POSTPLOT].`Survey Mode (value)` = 3 And ([POSTPLOT].`Number of Satellites` < 5 Or [POSTPLOT].`PDOP` > 6 Or [POSTPLOT].`CQ` > 0.3)))" \
       "Order By [POSTPLOT].`Station (text)`"

QC_S = "Select [POSTPLOT].`Station (value)`, " \
       "IIF ([POSTPLOT].`Status` in (3, 4, 5), [POSTPLOT].`COG Easting`, [POSTPLOT].`Local Easting`) AS `Easting`," \
       "IIF ([POSTPLOT].`Status` in (3, 4, 5), [POSTPLOT].`COG Northing`, [POSTPLOT].`Local Northing`) AS `Northing`," \
       "IIF ([POSTPLOT].`Status` in (3, 4, 5), [POSTPLOT].`COG Latitude`, [POSTPLOT].`WGS84 Latitude`) AS `Latitude`," \
       "IIF ([POSTPLOT].`Status` in (3, 4, 5), [POSTPLOT].`COG Longitude`, [POSTPLOT].`WGS84 Longitude`) AS `Longitude`," \
       "[POSTPLOT].`Local Height`," \
       "[POSTPLOT].`Descriptor`, " \
       "[POSTPLOT].`Index` " \
       "From [POSTPLOT] " \
      f"Where [POSTPLOT].`Station (value)` > 0 And [POSTPLOT].`Track` Between {init.SOURCES_TRACK} And (([POSTPLOT].`Status` IN (2,4) And [POSTPLOT].`Survey Mode (value)` Not In (3,5,6)) Or ([POSTPLOT].`Status` IN (2,4) And [POSTPLOT].`Survey Mode (value)` In (3) And ([POSTPLOT].`Number of Satellites` < 5 Or [POSTPLOT].`PDOP` > 6 Or [POSTPLOT].`CQ` > 0.3)) or [POSTPLOT].`Status` in (5, 6))" \
       "Order By [POSTPLOT].`Station (value)`"

VIB = "Select [POSTPLOT].* From [POSTPLOT] " \
     f"Where  [POSTPLOT].`Status` <> 0 And  [POSTPLOT].`Track` Between {init.SOURCES_TRACK}  And [POSTPLOT].`Station (value)` > 0 " \
     f"And (([POSTPLOT].`Descriptor` in {init.VIBRATORY_DSC} OR ([POSTPLOT].`Descriptor` in {init.DYNAMITY_DSC} and [POSTPLOT].`Status` in (3,4,5)))) " \
      "Order By [POSTPLOT].`Station (value)`"

XR = f"Select [POSTPLOT].* From [POSTPLOT] Where [POSTPLOT].`Status` <> 0 And [POSTPLOT].`Track` Between {init.SOURCES_TRACK}  " \
      "And [POSTPLOT].`Station (value)`<> 0 And (([POSTPLOT].`Descriptor` Like 'xr' And [POSTPLOT].`dr_date` is NULL) OR ([POSTPLOT].`dr_date` is not NULL And ([POSTPLOT].`dr_eq` Like 'EMCI' Or [POSTPLOT].`dr_eq` Like  'LPHB'))) And [POSTPLOT].`Status` not in (3,4,5) Order By [POSTPLOT].`Station (value)`"

XT = "Select [POSTPLOT].* From [POSTPLOT] " \
    f"Where [POSTPLOT].`Status` <> 0 And [POSTPLOT].`Track` Between {init.SOURCES_TRACK} And [POSTPLOT].`Station (value)`<>0 And (([POSTPLOT].`Descriptor` Like 'xt' " \
     "And [POSTPLOT].`dr_date` is NULL) OR ([POSTPLOT].`dr_date` is not NULL And [POSTPLOT].`dr_eq` Like 'PAT')) And [POSTPLOT].`Status` not in (3,4,5) " \
     "Order By [POSTPLOT].`Station (value)`"

PATERNY = f"Select [POSTPLOT].* From [POSTPLOT] " \
          f"Where [POSTPLOT].`Station (value)` > 0 And [POSTPLOT].`Status` >= 0 And [POSTPLOT].`Track` Between {init.SOURCES_TRACK} And [POSTPLOT].`Descriptor` in {init.DYNAMITY_DSC} and [POSTPLOT].`depth` like '%x%'" \
          f"Order By [POSTPLOT].`Station (value)`"


'''zapytania do bazy danych (SHP, UKOOA, JSON, etc)'''
UKO = "Select " \
     f"IIF (([PREPLOT].`Track` Between {init.RECEIVERS_TRACK}), 'G', 'S')," \
      "[PREPLOT].`Track`," \
      "([PREPLOT].`Bin`), " \
      "IIF (([POSTPLOT].`Station (value)` not like '%' Or [POSTPLOT].`Status`=0),[PREPLOT].`Local Easting`, IIF([POSTPLOT].`Status` in (1, 2, 6, 12, 22), [POSTPLOT].`Local Easting`, [POSTPLOT].`COG Easting`))," \
      "IIF (([POSTPLOT].`Station (value)` not like '%' Or [POSTPLOT].`Status`=0),[PREPLOT].`Local Northing`, IIF([POSTPLOT].`Status` in (1, 2, 6, 12, 22), [POSTPLOT].`Local Northing`, [POSTPLOT].`COG Northing`))," \
      "IIF (([POSTPLOT].`Station (value)` not like '%' OR [POSTPLOT].`Status`=0), [PREPLOT].`NMT`, IIF([POSTPLOT].`Status` = 3,[POSTPLOT].`COG Elev`, IIF([POSTPLOT].`Status` = 5, [POSTPLOT].`COG NMT`, IIF ([POSTPLOT].`Status` in (1, 2, 4, 6), [POSTPLOT].`Local Height`, IIF([POSTPLOT].`Status` in (12, 22), [POSTPLOT].`NMT`, [POSTPLOT].`COG NMT`)))))," \
     f"IIF ([POSTPLOT].`Station (value)` not like '%', '1', IIF(( [POSTPLOT].`Track` Between {init.RECEIVERS_TRACK}),[POSTPLOT].`Index` & '  ', IIF([POSTPLOT].`Descriptor` like 'x[tzr]', [POSTPLOT].`Index` & ' ' &'D',IIF (([POSTPLOT].`Descriptor` like '[xh]%'),([POSTPLOT].`Index` & ' ' & 'V'), ([POSTPLOT].`Index` & '  ')))))," \
     f"IIF ([POSTPLOT].`Status` in (1, 12), 1, IIF ([POSTPLOT].`Status`>1 , IIF([PREPLOT].`Track` Between {init.RECEIVERS_TRACK}, 1, 2), IIF ([POSTPLOT].`Status`= 0, '0', '10')))" \
      "From " \
      "[POSTPLOT] Right Join [PREPLOT] On [POSTPLOT].`Station (value)`=[PREPLOT].`Station (value)` " \
      "Where " \
     f"([PREPLOT].`Track` Between {init.RECEIVERS_TRACK}  ) Or (([PREPLOT].`Track` Between {init.SOURCES_TRACK}) And [POSTPLOT].`Status` > 0 ) " \
      "Order By [PREPLOT].`Track`, [PREPLOT].`Bin`, [POSTPLOT].`Index`"

# kwerendy json i wznawianie wybierają z bazy danych punkty z najwyższym Indexem
JSON = "Select " \
       "`Track`, `Bin`, `WGS84 Longitude`, `WGS84 Latitude`" \
      f"From [POSTPLOT], (Select [POSTPLOT].`Station (value)` as `Station` , Count(*) as `ilosc`  From [POSTPLOT] Where [POSTPLOT].`Station (value)` > 0 And [POSTPLOT].`Status` >= 0 And [POSTPLOT].`Track` Between {init.RECEIVERS_TRACK} Group by [POSTPLOT].`Station (value)`) as MxInd " \
      f"Where [POSTPLOT].`Station (value)` > 0 And [POSTPLOT].`Status` >= 0 And [POSTPLOT].`Track` Between {init.RECEIVERS_TRACK} AND [POSTPLOT].`Station (value)` = MxInd.`Station` AND [POSTPLOT].`Index` = MxInd.`ilosc` Order By [POSTPLOT].`Station (value)`"

WZNAWIANIE = "Select [POSTPLOT].`Station (value)`, [POSTPLOT].`Local Easting`, [POSTPLOT].`Local Northing` " \
             "From [POSTPLOT], " \
            f"(Select [POSTPLOT].`Station (value)` as `Station` , Count(*) as `ilosc`  From [POSTPLOT] Where [POSTPLOT].`Station (value)` > 0 And [POSTPLOT].`Status` >= 0 And [POSTPLOT].`Track` Between {init.RECEIVERS_TRACK} Group by [POSTPLOT].`Station (value)` ) as MxInd " \
            f"Where [POSTPLOT].`Station (value)` > 0 And [POSTPLOT].`Status` >= 0 And [POSTPLOT].`Track` Between {init.RECEIVERS_TRACK} AND [POSTPLOT].`Station (value)` = MxInd.`Station` AND [POSTPLOT].`Index` = MxInd.`ilosc` Order By [POSTPLOT].`Station (value)`"

MAX_IND = "Select [POSTPLOT].* " \
             "From [POSTPLOT], " \
            f"(Select [POSTPLOT].`Station (value)` as `Station` , Count(*) as `ilosc`  From [POSTPLOT] Where [POSTPLOT].`Station (value)` > 0 And [POSTPLOT].`Status` >= 0 And [POSTPLOT].`Track` Between {init.RECEIVERS_TRACK} Group by [POSTPLOT].`Station (value)` ) as MxInd " \
            f"Where [POSTPLOT].`Station (value)` > 0 And [POSTPLOT].`Status` > 0 And [POSTPLOT].`Track` Between {init.RECEIVERS_TRACK} AND [POSTPLOT].`Station (value)` = MxInd.`Station` AND [POSTPLOT].`Index` = MxInd.`ilosc` Order By [POSTPLOT].`Station (value)`"



'''Kwerendy potrzebne do robienia plików shp'''
POSTPLOT_S = "Select [POSTPLOT].* From [POSTPLOT] " \
             f"Where [POSTPLOT].`Station (value)` > 0 And [POSTPLOT].`Status` >= 0 And [POSTPLOT].`Track` Between {init.SOURCES_TRACK}"

POSTPLOT_R = "Select [POSTPLOT].* From [POSTPLOT] " \
             f"Where [POSTPLOT].`Station (value)` > 0 And [POSTPLOT].`Status` >= 0 And [POSTPLOT].`Track` Between {init.RECEIVERS_TRACK}"

DO_TYCZENIA_SP = "Select [PREPLOT].* From [PREPLOT] " \
                f"Where ([PREPLOT].`Track` Between {init.SOURCES_TRACK}) And [PREPLOT].`IsSurveyed` = 0"

DO_TYCZENIA_RP = "Select [PREPLOT].* From [PREPLOT] " \
                f"Where ([PREPLOT].`Track` Between {init.RECEIVERS_TRACK})  And [PREPLOT].`IsSurveyed` = 0"

SKIP_S = "Select [POSTPLOT].* From [POSTPLOT] " \
        f"Where [POSTPLOT].`Status` = 0 And [POSTPLOT].`Station (value)` > 0 And [POSTPLOT].`Track` Between {init.SOURCES_TRACK}"


SKIP_R = "Select [POSTPLOT].* From [POSTPLOT] " \
        f"Where [POSTPLOT].`Status` = 0 And [POSTPLOT].`Station (value)` > 0 And [POSTPLOT].`Track` Between {init.RECEIVERS_TRACK}"
"""
QC_DOMIAR_S_SHP = "Select " \
                  "[POSTPLOT].`Station (text)`," \
                  "[POSTPLOT].`Station (value)`, " \
                  "[POSTPLOT].`Track`, [POSTPLOT].`Bin`, " \
                  "IIF ([POSTPLOT].`Status` in (3, 4, 5),[POSTPLOT].`COG Easting`,[POSTPLOT].`Local Easting`)," \
                  "IIF ([POSTPLOT].`Status` in (3, 4, 5),[POSTPLOT].`COG Northing`,[POSTPLOT].`Local Northing`)," \
                  "[POSTPLOT].`Uwagi_biuro`, " \
                  "[POSTPLOT].`Descriptor`, " \
                  "[POSTPLOT].`Survey Mode (value)`," \
                  "[POSTPLOT].`Status`," \
                  "[POSTPLOT].`Index` " \
                  "From [POSTPLOT] " \
                  "Where " \
                  f"[POSTPLOT].`Station (value)` > 0 And " \
                  f"[POSTPLOT].`Track` Between {init.SOURCES_TRACK}  And " \
                  f"(([POSTPLOT].`Status` IN (1,2,4) And  [POSTPLOT].`Survey Mode (value)` Not In (3,5,6))  Or " \
                  f"( [POSTPLOT].`Status` = 5  And  [POSTPLOT].`Survey Mode (value)` In (3) And ([POSTPLOT].`Number of Satellites` < 5 Or [POSTPLOT].`PDOP` > 6 Or [POSTPLOT].`CQ` > 0.3) )  or " \
                  f"[POSTPLOT].`Status` = 5 or [POSTPLOT].`Status` = 6 )"
"""

QC_DOMIAR_S_SHP = "Select " \
                  "[POSTPLOT].* " \
                  "From [POSTPLOT] " \
                  "Where " \
                  f"[POSTPLOT].`Station (value)` > 0 And " \
                  f"[POSTPLOT].`Track` Between {init.SOURCES_TRACK}  And " \
                  f"(([POSTPLOT].`Status` IN (2, 4) And  [POSTPLOT].`Survey Mode (value)` Not In (3,5,6))  Or " \
                  f"( [POSTPLOT].`Status`IN (2, 4)  And  [POSTPLOT].`Survey Mode (value)` In (3) And ([POSTPLOT].`Number of Satellites` < 5 Or [POSTPLOT].`PDOP` > 6 Or [POSTPLOT].`CQ` > 0.3) )  or " \
                  f"[POSTPLOT].`Status` = 5 or [POSTPLOT].`Status` = 6 )"

QC_DOMIAR_R_SHP = "Select [POSTPLOT].* From [POSTPLOT] " \
                 f"Where  [POSTPLOT].`Station (value)` > 0 And [POSTPLOT].`Track` Between {init.RECEIVERS_TRACK}  And [POSTPLOT].`Status` >=1 And [POSTPLOT].`Status` <= 11 And (([POSTPLOT].`Survey Mode (value)` Not In (3,5,6) ) Or ( [POSTPLOT].`Survey Mode (value)` = 3 And ([POSTPLOT].`Number of Satellites` < 5 Or [POSTPLOT].`PDOP` > 6 Or [POSTPLOT].`CQ` > 0.3))) Order By [POSTPLOT].`Station (text)`"

UWAGI_GEODEZJA = "Select [POSTPLOT].* From [POSTPLOT] Where [POSTPLOT].`Station (text)` Like '@%'"

STUDNIE_GEODEZJA = "Select [POSTPLOT].* From POSTPLOT " \
                   "Where [POSTPLOT].`Station (text)` Like 'stu%' Or [POSTPLOT].`Station (text)` Like 'STU%' Or " \
                   "[POSTPLOT].`Station (text)` Like 'std%' Or [POSTPLOT].`Station (text)` Like 'STD%' Or " \
                   "[POSTPLOT].`Station (text)` Like 'st%' Or [POSTPLOT].`Station (text)` Like 'ST%' " \
                   "Order By [POSTPLOT].`Station (text)`"

STUDNIE_STUDNIARZ = "Select [studniarze_pom].* From [studniarze_pom] Where [studniarze_pom].`Station (text)` Not Like 'W%' And [studniarze_pom].`Station (value)` > 0 Order By [studniarze_pom].`Station (text)`"

WYSTAWKI = "Select [POSTPLOT].* From POSTPLOT " \
           "Where " \
           "([POSTPLOT].`Station (text)` Like '88_______' or " \
               "[POSTPLOT].`Station (text)` Like '99_______' or " \
               "[POSTPLOT].`Station (text)` Like '88________' or " \
               "[POSTPLOT].`Station (text)` Like 'PP*') " \
           "And [POSTPLOT].`Survey Mode (value)` IN (3,6) " \
           "Order By [POSTPLOT].`Station (text)`"


VIBRATORY = "Select [POSTPLOT].* From POSTPLOT " \
           f"Where [POSTPLOT].`Status` <> 0 And  [POSTPLOT].`Track` Between {init.SOURCES_TRACK} And [POSTPLOT].`Station (value)`> 0 And ([POSTPLOT].`Descriptor` IN {init.VIBRATORY_DSC} OR ([POSTPLOT].`Descriptor` IN {init.DYNAMITY_DSC} and [POSTPLOT].`Status` in (3,4,5)))"

DYNAMITY = "Select [POSTPLOT].* From POSTPLOT " \
          f"Where [POSTPLOT].`Status` <> 0 And [POSTPLOT].`Track` Between {init.SOURCES_TRACK} And [POSTPLOT].`Station (value)`<>0 And [POSTPLOT].`Descriptor` IN {init.DYNAMITY_DSC} And [POSTPLOT].`Status` not in (3,4,5)"

QC_DOMIAR_S_SHP_COG = "Select " \
                  "[POSTPLOT].* " \
                  "From [POSTPLOT] " \
                  "Where " \
                  f"[POSTPLOT].`Station (value)` > 0 And " \
                  f"[POSTPLOT].`Track` Between {init.SOURCES_TRACK}  And " \
                  f"(([POSTPLOT].`Status` IN (2,4) And  [POSTPLOT].`Survey Mode (value)` Not In (3,5,6))  Or " \
                  f"( [POSTPLOT].`Status` IN (2, 4)  And  [POSTPLOT].`Survey Mode (value)` In (3) And ([POSTPLOT].`Number of Satellites` < 5 Or [POSTPLOT].`PDOP` > 6 Or [POSTPLOT].`CQ` > 0.3) )  or " \
                  f"[POSTPLOT].`Status` = 5 or [POSTPLOT].`Status` = 6 )"

####### Kwerendy UPDATE REMEASURE ###

UPD_S = "UPDATE [REMEASURE],[POSTPLOT] " \
       "SET " \
       "[REMEASURE].`COG Easting` = [POSTPLOT].`COG Easting`, " \
       "[REMEASURE].`COG Northing` = [POSTPLOT].`COG Northing`, " \
       "[REMEASURE].`COG Elev` = [POSTPLOT].`COG Elev`, " \
       "[REMEASURE].`Acquired_Data` = [POSTPLOT].`Acquired_Data`, " \
       "[REMEASURE].`Descriptor` = [POSTPLOT].`Descriptor`, " \
       "[REMEASURE].`Comment` = [POSTPLOT].`Comment`, " \
       "[REMEASURE].`Index` = [POSTPLOT].`Index`, " \
       "[REMEASURE].`Description1` = [POSTPLOT].`Description1`, " \
       "[REMEASURE].`Description2` = [POSTPLOT].`Description2`, " \
       "[REMEASURE].`depth` = [POSTPLOT].`depth`, " \
       "[REMEASURE].`dr_name` = [POSTPLOT].`dr_name`, " \
       "[REMEASURE].`dr_eq` = [POSTPLOT].`dr_eq`, " \
       "[REMEASURE].`dr_date` = [POSTPLOT].`dr_date`, " \
       "[REMEASURE].`Uwagi_biuro` = [POSTPLOT].`Uwagi_biuro`, " \
       "[REMEASURE].`PPV` = [POSTPLOT].`PPV`, " \
       "[REMEASURE].`Status` = '2' " \
       "WHERE " \
       "[POSTPLOT].`Station (value)` > 0 And " \
       f"[POSTPLOT].`Track` Between {init.SOURCES_TRACK} And " \
       "datediff ('d', [REMEASURE].`Survey Time (Local)`, now()) = 0 And " \
       "[REMEASURE].`Index` = [POSTPLOT].`Index` And " \
       "[REMEASURE].`Station (value)` = [POSTPLOT].`Station (value)` "

UPD_R = "UPDATE [REMEASURE],[POSTPLOT] " \
       "SET " \
       "[REMEASURE].`Descriptor` = [POSTPLOT].`Descriptor`, " \
       "[REMEASURE].`Comment` = [POSTPLOT].`Comment`, " \
       "[REMEASURE].`Index` = [POSTPLOT].`Index`, " \
       "[REMEASURE].`Description1` = [POSTPLOT].`Description1`, " \
       "[REMEASURE].`Description2` = [POSTPLOT].`Description2`, " \
       "[REMEASURE].`Uwagi_biuro` = [POSTPLOT].`Uwagi_biuro`, " \
       "[REMEASURE].`Status` = '1' " \
       "WHERE " \
       "[POSTPLOT].`Station (value)` > 0 And " \
       f"[POSTPLOT].`Track` Between {init.RECEIVERS_TRACK} And " \
       "datediff ('d', [REMEASURE].`Survey Time (Local)`, now()) = 0 And " \
       "[REMEASURE].`Index` = [POSTPLOT].`Index` And " \
       "[REMEASURE].`Station (value)` = [POSTPLOT].`Station (value)` "


POSTPLOT_ZEROWANIE = "UPDATE [REMEASURE],[POSTPLOT] " \
                     "SET " \
                     "[POSTPLOT].`Station (value)` = '0' " \
                     "WHERE " \
                     "[POSTPLOT].`Station (value)` > 0 " \
                    f"AND ([POSTPLOT].`Track` Between {init.RECEIVERS_TRACK} OR [POSTPLOT].`Track` Between {init.SOURCES_TRACK})" \
                     "AND datediff ('d', [REMEASURE].`Survey Time (Local)`, now()) = 0" \
                     "AND [REMEASURE].`Index` = [POSTPLOT].`Index` " \
                     "AND [REMEASURE].`Station (value)` = [POSTPLOT].`Station (value)`" \
                     "AND [POSTPLOT].`Status` > 0; "

COPY_REMEASURE = "INSERT INTO [POSTPLOT]" \
                 "SELECT * FROM [REMEASURE]" \
                 "WHERE datediff('d', [REMEASURE].`Survey Time (Local)`, now()) = 0"

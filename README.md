# !!!_Geodeta

---
Jest to tutorial do rozwojowej wersji programu.  

Co musisz mieć:
	  
* python 3.8 lub wyższy  
* zainstalowane pakiety:
	* pyodbc
	* smtlib
	* xlrd
	* pyproj
	* tkinter (powinnien być domyślnie)
	* openpyxl
___  


## Ustawienia (`init.py`)

Wszystkie najważniejsze parametry i zmienne wprowadzasz w pliku `init.py`
Jak usiądziesz za konsoletą wprowadź zmienne:

* GEODETA
* ZUPT_BRYG
* w zakładce `ADRESY EMAIL` zmień jeśli potrzeba:
	+ SUPERVISOR
	+ RECIPENT_DPR (tu podajesz odbiorów wiadomości email z raportami)
	+ RECIP_JSON (odbiorcy pliku JSON)





## Wiertnictwo (`raport_wiertnictwo.py`)

W katalogu `!!!_Geodeta` znajdź program `raport_wiertnictwo`  
Z wiadomośći mail od wiertnika ściągnij plik `Raport wiertnictwa PL186.xls`  
i zapisz go w katalogu `c:\PL-186_Zapalow_3D\09_wiertnictwo`  

Uruchom program `raport_wiertnictwo`, postępuj zgodnie z instrukcjami. 
Jak w [tym filmie.](https://youtu.be/tqdZMXO47vU)


## Dniówka
Skopiuj produkcję z wymiany do katalogu `C:\PL-186_Zapalow_3D\07_produkcja`
Znajdź programy:

- PSS_v4_mdb.py (credits to Gawroński/zm.Jurkowski)
- DYN_v5_mdb.py (credits to Gawroński/zm.Jurkowski)

Pliki które wychodzą (te z `_OK`) pomogą ci się zorientować, że już przerobiłeś dane. Do niczego innego ich nie wykorzystujesz. Obydwa skrypty wgrywają dane bezpośrednio do bazy danych.

### Dynaity
program DYN_v5_mdb.py szykuje i wgrywa dane do mdb. Postępujesz zgodnie instrukcjami z programu i jak w [tym filmie](https://youtu.be/fYXNvTsrr9U)

### Wibratory
program PSS_v4_mdb.py, liczy współrzędne płaskie (tak wiem, że obecnie wychodzą takie z pss-a), redukuje wysokość o wysokość wibratora, wgrywa dane do mdb; Także informacje o jakości pomiaru. 
Postępujesz zgodnie z tym co mówi skrypt i [ten film](https://youtu.be/iCaRjUyLMFY)

### Czynności końcowe, przy obrabianiu dniówki.

Robisz jak w [filmie](https://youtu.be/dy8FfkrK35M)

Następnie szukasz programów:  

- `UKO` - generujesz plik uko -> zapisuje się bezpośrednio na wymianie w katalogu `Geodezja\UKO`, jeśli wymiana jest nie dostępna (np. pracujesz offline) plik zapisze się w katalogu `!!!_Geodeta\output` 

- po zakończeniu obrabiania dniówki geodetów, warto wysłać plik json do transcribera, zrobisz to przy pomocu programu `json_maxInd`, json jest wysyłany pocztą bezpośrednio do transcribera i linebossa, oraz do ciebie w kopi ukrytej. Program generuje także pliki:
	* PL186_QC_Domiar_ZUPT.txt
	* PL186_QC_Domiar_GPS.csv
	* PL186_max_indeks.txt
	* PL186_max_indeks.csv  

Nazwy są samoopisujące, wszystkie znajdziesz w katalogu `!!!_Geodeta\output` 
Pliki do domiaru uwzględniaja statusy, metodę pomiaru, jakość gps, itd. Dla wibratorów pozycja jest z COG (chyba że wibratory nie odezłały pozycji - wtedy GPS), dla dynamitu pozycja z pomiaru Geodety, chyba że punkt był już domierzony.  
Wszystko powinnno być plug&play. 

Raporty, jak już będziesz miał gotowe wysyłasz programem: `send_mail` - program wysyła raport dpr i dniówkowy jak zwykle do wszystkich świętych, oraz tylko dpr do przedstawiciela klienta. Pamiętaj o aktualizacji swojego nazwiska i adresów odbiorców maili w pliku 'init'. 

Wszyskie zmiany możesz wprowadzać w zwykłym notatniku, jeśli nie masz IDLE.  

Wszystkie pliki w katalogu są niezbędne by działał program. 

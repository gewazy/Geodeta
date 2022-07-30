import pyodbc
import smtplib
from email.message import EmailMessage
from time import sleep

import init
import kury
import password

'''
Przygotowanie pliku json, oraz wysłanie go do trancribera
'''

plik = init.JSON_FILE

cnxn = pyodbc.connect(init.CONN_STR)
crsr = cnxn.cursor()

# Listy z dnymi z zapytań
json = crsr.execute(kury.JSON).fetchall()
qc_s = crsr.execute(kury.QC_S).fetchall()
qc_r = crsr.execute(kury.QC_R).fetchall()
wzn = crsr.execute(kury.WZNAWIANIE).fetchall()

cnxn.commit()
cnxn.close()

# json file
with open(plik, 'w') as file:
    file.write('{"locations":[\n')
    for row in json[:-1]:
        file.write('{' + f'"line":{row[0]}.0,"station":{row[1]}.0,"longitude":{format(row[2], ".8f")},"latitude":{format(row[3], ".9f")}' + '},\n')
    file.write('{' + f'"line":{json[-1][0]}.0,"station":{json[-1][1]}.0,"longitude":{format(json[-1][2], ".8f")},"latitude":{format(json[-1][3], ".9f")}' + '}]}')
print('\nPlik Json gotowy')


print("Tworzę pliki do domiaru:")
print(f'-Punktów wzbudzania do domiaru: {len(qc_s)}')
print(f'-Punktów odbioru do domiaru: {len(qc_r)}')

# QC_DOMIAR_GPS
with open(init.QC_DOMIAR_GPS, 'w') as file:
    for row in qc_s:
        file.write(f"{int(row[0])}-{row[7]},{format(round(row[1], 2), '.2f')},{format(round(row[2], 2), '.2f')},{format(round(row[5], 2), '.2f')},{row[6]}\n")
    for row in qc_r:
        file.write(f"{int(row[0])}-{row[6]},{format(round(row[1], 2), '.2f')},{format(round(row[2], 2), '.2f')},{format(round(row[5], 2), '.2f')},{row[6]}\n")

print('\nPlik QC_Domiar_GPS.csv gotowy!')

# QC_DOMIAR_ZUPT
try:
    with open(init.QC_DOMIAR_ZUPT, 'w') as file:
        for row in qc_s:
            file.write(f"{int(row[0])}-{row[7]} {format(round(row[3], 8), '.8f')} {format(round(row[4], 8), '.8f')} 0.00 0 7 1 0 \n")
        for row in qc_r:
            file.write(f"{int(row[0])}-{int(row[6])} {format(round(row[3], 8), '.8f')} {format(round(row[4], 8), '.8f')} 0.00 0 7 1 0 \n")
except TypeError:
    print('\nPRAWDOPODOBNIE NIE POLICZYŁEŚ COG WGS!!')
else:
    print('Plik QC_Domiar_ZUPT.txt gotowy!\n')


# Do wznawiania csv
with open(init.WZNAWIANIE_FILE, 'w') as file:
    for row in wzn:
        file.write(f"{int(row[0])},{format(round(row[1], 2), '.2f')},{format(round(row[2], 2), '.2f')}\n")

# ******************* MAIL z jasonem do transcribera ***************************
msg_json = EmailMessage()
msg_json['Subject'] = 'JSON'
msg_json['From'] = init.SENDER
msg_json['To'] = init.RECIP_JSON
msg_json['BCC'] = init.SENDER

mail_json = f"Json w załączniku.\n\npzdr\n\n{init.GEODETA}\nGrupa sejsmiczna {init.GRUPA}"

msg_json.set_content(mail_json)

# dodanie załącznika
plik = init.JSON_FILE
with open(plik, 'rb') as f:
    zalacznik = f.read()

msg_json.add_attachment(zalacznik, maintype="application",
                        subtype=plik.split('.')[-1], filename=plik.split('\\')[-1])


# ******************* Logowanie na serwerze i wysłanie maila *******************
smtp_server = smtplib.SMTP("smtp.geofizyka.pl", 587, timeout=120)
smtp_server.ehlo()  # setting the ESMTP protocol
smtp_server.starttls()  # setting up to TLS connection
smtp_server.login(f'{init.GRUPA.lower()}surveyor', password.PASSWORD)  # user and pass
smtp_server.send_message(msg_json)
print(f'JSON został wysłany do {init.RECIP_JSON}.')
smtp_server.quit()

sleep(2)
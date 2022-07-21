import smtplib
from email.message import EmailMessage
from time import sleep

import init
import password

'''
Obecnie wysyła 3 wiadomości:
1. raport DPR oraz szczegółowy do GT
2. raport geodezyjny DPR do Supervisora

Uruchamianie na koniec dniówki.
'''

# ******************* MAIL Raport geodezyjny ***********************************
msg_dpr = EmailMessage()
msg_dpr['Subject'] = f'{init.GRUPA} Raport Geodezyjny'
msg_dpr['From'] = init.SENDER
msg_dpr['BCC'] = init.SENDER
msg_dpr['To'] = init.RECIPIENT_DPR

mail_dpr = f'''
Dzień dobry,\n\nraporty geodezyjne  w załączniku.\n
{input('Jeśli chcesz coś dodać do maila, pisz teraz, jak nie -> ENTER: ')}
\n{init.GEODETA}\nGrupa sejsmiczna {init.GRUPA} '''

msg_dpr.set_content(mail_dpr)

# dodanie załączników do maila z raportem
for plik in init.DPR:
    with open(plik, 'rb') as f:
        zalacznik = f.read()
    msg_dpr.add_attachment(zalacznik, maintype="application",
                           subtype=plik.split('.')[-1], filename=plik.split('\\')[-1])


# ******************* MAIL Raport geodezyjny supervisor ************************
msg_dpr_su = EmailMessage()
msg_dpr_su['Subject'] = f'{init.GRUPA} Raport Geodezyjny'
msg_dpr_su['From'] = init.SENDER
msg_dpr_su['To'] = init.SUPERVISOR  # do zmiany po testach
msg_dpr_su['CC'] = init.SENDER
msg_dpr_su['BCC'] = 'djurkowski@geofizyka.pl'

mail_dpr_su = f'Dzień dobry,\n\nraport geodezyjny  w załączniku.\n\n{init.GEODETA}\nGrupa sejsmiczna {init.GRUPA}'

msg_dpr_su.set_content(mail_dpr_su)

# dodanie załącznika
plik = init.DPR[0]
with open(plik, 'rb') as f:
    zalacznik = f.read()
    msg_dpr_su.add_attachment(zalacznik, maintype="application",
                              subtype=plik.split('.')[-1], filename=plik.split('\\')[-1])


# ******************* Logowanie na serwerze i wysłanie maili *******************
smtp_server = smtplib.SMTP("smtp.geofizyka.pl", 587, timeout=120)
smtp_server.ehlo() # setting the ESMTP protocol
smtp_server.starttls() # setting up to TLS connection
smtp_server.login(f'{init.GRUPA.lower()}surveyor', password.PASSWORD)  # user and pass
smtp_server.send_message(msg_dpr)
print('Wysłano wiadomość z raportem geodezyjnym do GT.')
sleep(1)
smtp_server.send_message(msg_dpr_su)
print('Wysłano wiadomość z raportem geodezyjnym do Supervisora.')
smtp_server.quit()
sleep(3)
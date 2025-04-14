import smtplib
import os

email_id = os.environ.get('EMAIL_ADDR')
email_pass = os.environ.get('EMAIL_PASS')
with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(email_id, email_pass)

    subject = 'Fight against coronavirus'
    body = "Hey, hi let's flight against cornavirus by stayong at home"

    msg = f'subject: {subject}\n\n\n{body}'
    smtp.sendmail(email_id,'jathu59seelan@gmail.com', msg)



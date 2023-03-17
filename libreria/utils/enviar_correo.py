from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP
from os import environ

def enviar_correo(destinatarios, titulo, cuerpo):
    mensaje = MIMEMultipart()
    email_emisor = environ.get('EMAIL_SENDER')
    password_email_emisor = environ.get('PASSWORD_SENDER')

    mensaje['Subject'] = titulo

    mensaje.attach(MIMEText(cuerpo))

    emisor = SMTP('smtp.gmail.com', 587) 

    emisor.starttls()
    emisor.login(user = email_emisor, password= password_email_emisor)

    emisor.sendmail(from_addr= email_emisor, to_addrs= destinatarios, msg=mensaje.as_string())

    emisor.quit()
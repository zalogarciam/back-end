from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

def enviar_correo(destinatarios, titulo, cuerpo):
    mensaje = MIMEMultipart()
    email_emisor = 'gegarciam95@gmail.com'
    password_email_emisor = 'xiwtoyfueoqmoogd'

    mensaje['Subject'] = titulo

    mensaje.attach(MIMEText(cuerpo))

    emisor = SMTP('smtp.gmail.com', 587) 

    emisor.starttls()
    emisor.login(user = email_emisor, password= password_email_emisor)

    emisor.sendmail(from_addr= email_emisor, to_addrs= destinatarios, msg=mensaje.as_string())

    emisor.quit()
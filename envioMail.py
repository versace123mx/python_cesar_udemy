import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def sendMail():
    fromaddr = 'hola@gmail.com'
    toaddr = 'hola@gmail.com'
    password = '123'
    asunto = 'Correo de prueba python'
    html = '''
    <html>
        <head></head>
        <body>
            <h1>Hola desde mi script Python</h1>
        </body>
    </html>
    '''
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = asunto

    msg.attach(MIMEText(html,'html'))

    server = smtplib.SMTP('smtp.google.com')
    #server.starttls()
    server.login(fromaddr,password)

    text = msg.as_string()
    server.sendmail(fromaddr,toaddr,text)
    server.quit()

sendMail()
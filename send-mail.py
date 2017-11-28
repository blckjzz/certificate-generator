import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

def sendCertificate(name):
    fromaddr = ""
    toaddr = "xdiegocerqueira@gmail.com"
    
    msg = MIMEMultipart()
    
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "SUBJECT OF THE EMAIL"
    
    body = "Mensagem título"
    
    msg.attach(MIMEText(body, 'plain'))
    

    attachment = open("certificados - virada/certificado " + name, "rb")
    
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % name)
    
    msg.attach(part)
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
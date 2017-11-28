#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import time
import datetime

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
import string
def sendCertificate(name, fileName, toaddr):
    fromaddr = "xdiegocerqueira@gmail.com"
    #toaddr = "xdiegocerqueira@gmail.com"
    
    msg = MIMEMultipart()
    
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Virada Legislativa - Agradecimentos e certificado de participação"
    
    body = getHtmlTemplate(name)
    
    msg.attach(MIMEText(body, 'html'))
    
    attachment = open("certificados - virada/" + fileName, "rb")
    
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % fileName)
    
    msg.attach(part)
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "macacada9788")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print("Certificado de " + name + "enviado!")


# template da mensagem
def getHtmlTemplate(name):
    return """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml"><head> <meta http-equiv="content-type" content="text/html; charset=UTF-8"> <title>Certificado - Virada Legislativa</title> <style type="text/css"> @media only screen and (max-width: 480px) { #templateContainer { width: 100% !important; } } @media only screen and (max-width: 480px) { #templateBody { border-radius: 0 !important; width: 100% !important; font-size: 15px !important; line-height: 25px !important; } } @media only screen and (max-width: 480px) { #templateBody .greeting { font-size: 20px !important; } } @media only screen and (max-width: 480px) { #templateBody .primary-button { font-size: 15px !important; padding: 18px 30px !important; min-width: 0 !important; } } @media only screen and (max-width: 480px) { #templateBody .signature { font-size: 19px !important; } } @media only screen and (max-width: 480px) { #templateHeader { width: 100% !important; } } @media only screen and (max-width: 480px) { #templateFooter { width: 100% !important; font-size: 9px !important; } } @media only screen and (max-width: 480px) { #templateBody .panel { padding: 30px 0 !important; } } @media only screen and (max-width: 480px) { #templateHeader .logo { height: 60px !important; } } </style></head><body leftmargin="0" marginwidth="0" topmargin="0" marginheight="0" offset="0" style="margin:0;padding:0;background-color:#f9f9f9;color:#646464;font-family:" merriweather="" sans="" sans-serif=""> <center> <table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" id="bodyTable" style="height:100% !important;margin:0;padding:0;background-color:#f9f9f9;color:#646464;font-family:'Merriweather Sans', sans-serif;font-weight:300;border-collapse:collapse !important;width:100% !important;"> <tr> <td align="center" valign="top" id="bodyCell" style="margin:0;padding:0;height:100% !important;width:100% !important;"> <table border="0" cellpadding="0" cellspacing="0" id="templateContainer" style="width:620px;border-collapse:collapse !important;"> <tr> <td valign="top"> <table border="0" cellpadding="18" cellspacing="0" id="templateHeader" width="100%" style="border-collapse:collapse !important;"> <tr> <td valign="top"> <img src="https://s3-sa-east-1.amazonaws.com/mudamos-images/images/logo-2.png" class="logo" style="border:0;height:auto;line-height:100%;outline:none;text-decoration:none;padding-left:22px;" alt="logo-2.png"> </td> </tr> </table> </td> </tr> <tr> <td align="center" valign="top"> <table border="0" cellpadding="40" cellspacing="0" width="100%" id="templateBody" style="background-color:#ffffff;border-radius:6px;font-size:20px;line-height:34px;border-collapse:collapse !important;"> <tr> <td valign="top"> <p class="greeting" style="margin:0;font-size:28px;padding-bottom:12px;">Olá
                                                <strong>"""+str(name)+"""</strong>,</p>
                                                <p style="margin:0;">
                                                <p> Nós da equipe Mudamos ficamos felizes por sua presença em um momento capáz de transformar sua
                                                    cidade.
                                                </p>
                                                <p> Anexado a esta mensagem está seu certificado de participação.</p>
                                                <p>Obrigado JAMPA, nos vemos em breve!</p>
                                                <p>Construindo a democracia digital,</p>
                                                <p>Equipe Mudamos.</p>
            </td> </tr> </table> </td> </tr> </table> </td> </tr> </table> </center></body></html>"""
#end html template



def geraCertVirada(alunos,mail):
    

    roboto16 = ImageFont.truetype("fonts/Roboto/Roboto-Regular.ttf", 16)    
    roboto12 = ImageFont.truetype("fonts/Roboto/Roboto-Regular.ttf", 12)
    roboto12Italic = ImageFont.truetype("fonts/Roboto/Roboto-Italic.ttf", 12)
    roboto12Italic = ImageFont.truetype("fonts/Roboto/Roboto-Italic.ttf", 12)
    roboto12Bold = ImageFont.truetype("fonts/Roboto/Roboto-Bold.ttf", 12)
    roboto16Bold = ImageFont.truetype("fonts/Roboto/Roboto-Bold.ttf", 16)
    roboto16BoldItalic = ImageFont.truetype("fonts/Roboto/Roboto-BoldItalic.ttf", 16)
    roboto22 = ImageFont.truetype("fonts/Roboto/Roboto-Regular.ttf", 22)
    roboto22Bold = ImageFont.truetype("fonts/Roboto/Roboto-Bold.ttf", 22)
    roboto40Bold = ImageFont.truetype("fonts/Roboto/Roboto-Bold.ttf", 40)

    for aluno in alunos:
        #declara dicionario de alunos
        img = Image.open("templates/certificado_virada.jpg")
        draw = ImageDraw.Draw(img)
        print("Gerando o certificado de: " + aluno)
        #escreve nome do aluno'
        nomeAluno = aluno.decode('utf-8')

        if(len(nomeAluno) < 13):
            draw.text((680, 700), nomeAluno.upper() , (0,0,0),font=roboto40Bold)
        elif(len(nomeAluno) > 20):
            draw.text((600, 700), nomeAluno.upper() , (0,0,0),font=roboto40Bold)
        else:
            draw.text((650, 700), nomeAluno.upper() , (0,0,0),font=roboto40Bold)
        #gera o certificado
        img.save("certificados - virada/certificado_" + aluno + ".png")
        fileName = "certificado_" + aluno + ".png"
        sendCertificate(aluno,fileName, mail)

    final = time.time()  

    tempoPassado = time.time() - comeco

    duracao = time.strftime("%H:%M:%S", time.gmtime(tempoPassado))

    print("Você gerou: "+ str(len(alunos)) + " certificados em:" + str(duracao))
    #fim da função de gerar certificados


p_nomes = []
p_mail  = []
alunos = []
f = open('/Users/dc/Downloads/presenca-virada.csv', 'rU')
reader = csv.reader(f)
for row in reader:
    alunos.append(' '.join(row))

comeco = time.time()



for aluno in alunos:
    p = aluno.find(';')

    #print(aluno[:p] + ' - ' + aluno[p+1:])
    nome = aluno[:p]
    mail = aluno[p+1:]
    
    p_nomes.append(string.capwords(nome))
    p_mail.append(string.lower(mail))

#print(p_nomes)
#print(p_mail)
'''for i in range(len(p_nomes)):
    print(p_nomes[i] + " - " + p_mail[i])
'''
geraCertVirada(p_nomes, p_mail)    
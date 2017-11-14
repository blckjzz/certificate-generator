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

def sendCertificate(name, fileName):
    fromaddr = "xdiegocerqueira@gmail.com"
    toaddr = "xdiegocerqueira@gmail.com"
    
    msg = MIMEMultipart()
    
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Seu certificado da Virada Legislativa"
    
    body = "Em anexo seu certificado da Virada Legislativa - João Pessoa"
    
    msg.attach(MIMEText(body, 'plain'))
    
    attachment = open("certificados - virada/" + fileName, "rb")
    
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % fileName)
    
    msg.attach(part)
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print("Certificado de " + name + "enviado!")



def geraCertVirada(alunos):
    

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
        sendCertificate(aluno,fileName)

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

    print(aluno[:p] + ' - ' + aluno[p+1:])
    nome = aluno[:p]
    mail = aluno[p+1:]
    p_nomes.append(nome)
    p_mail.append(mail)
    #print(p_nomes)
    #print(p_mail)



geraCertVirada(p_nomes)    




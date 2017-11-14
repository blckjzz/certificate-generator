#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import time
import datetime

# 186 x 140 = nome do curso
# 144 x 244 = nome do aluno
# 369 x 270 = nome do curso rodapé
# 363 x 291 = carga horaria

#declara dicionario de alunos

alunos = []
f = open('alunos.csv', 'rb')
reader = csv.reader(f)
for row in reader:
    alunos.append(' '.join(row))

comeco = time.time()

cargaHoraria = 8
curso = "Bitcoin para iniciantes"
curso = curso.decode('utf-8')
for aluno in alunos:
    roboto16 = ImageFont.truetype("fonts/Roboto/Roboto-Regular.ttf", 16)
    roboto12 = ImageFont.truetype("fonts/Roboto/Roboto-Regular.ttf", 12)
    roboto12Italic = ImageFont.truetype("fonts/Roboto/Roboto-Italic.ttf", 12)
    roboto12Italic = ImageFont.truetype("fonts/Roboto/Roboto-Italic.ttf", 12)
    roboto12Bold = ImageFont.truetype("fonts/Roboto/Roboto-Bold.ttf", 12)
    roboto16Bold = ImageFont.truetype("fonts/Roboto/Roboto-Bold.ttf", 16)
    roboto16BoldItalic = ImageFont.truetype("fonts/Roboto/Roboto-BoldItalic.ttf", 16)
    roboto22 = ImageFont.truetype("fonts/Roboto/Roboto-Regular.ttf", 22)
    roboto22Bold = ImageFont.truetype("fonts/Roboto/Roboto-Bold.ttf", 22)
    print("Gerando o certificado de: " + aluno)
       
    img = Image.open("templates/template_certificado.png")
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    # draw.text((x, y),"Sample Text",(r,g,b))

    draw.text((150, 135), "Curso" , (0,0,0),font=roboto12)
    #escreve nome do curso
    
    draw.text((185, 135), curso , (0,0,0),font=roboto12Bold)

    #Escreve Data
    data = str(datetime.datetime.today().strftime('%d/%m/%Y')) + " |"
    data1 = "| ITS Rio"
    draw.text((150, 150), data , (0,0,0),font=roboto12Italic)
    draw.text((225, 150), str(cargaHoraria) + " Horas" , (0,0,0),font=roboto12Bold)
    draw.text((270, 150), data1 , (0,0,0),font=roboto12Italic)


    #escreve nome do aluno'
    nomeAluno = aluno.decode('utf-8')

    draw.text((140, 220), nomeAluno.upper() , (0,0,0),font=roboto22Bold)

    #escreve o texto sobre que apresenta o nome e etc.

    tx = "Concluiu o curso de extensão "
    txn = tx.decode('utf-8')
    txCurso = str(curso).decode('utf-8')
    txx =  "com a carga hora de " 
    tx2 = str(cargaHoraria) + " Horas"
    tx3 = "oferecido pelo Instituto de Tecnologia e Sociedade"
    tx4 = "do Rio."
    texto = tx3.decode('utf-8')
    
    draw.text((140, 255), txn , (0,0,0),font=roboto16)
    draw.text((350, 255), txCurso , (0,0,0),font=roboto16BoldItalic)
    draw.text((140, 275), txx , (0,0,0),font=roboto16)
    draw.text((290, 275), tx2 , (0,0,0),font=roboto16Bold)
    draw.text((350, 275), texto , (0,0,0),font=roboto16)
    draw.text((140, 295), tx4 , (0,0,0),font=roboto16)

    #gera o certificado
    img.save("certificados/certificado - " + aluno + ".png")


final = time.time()  

tempoPassado = time.time() - comeco

duracao = time.strftime("%H:%M:%S", time.gmtime(tempoPassado))

print("Você gerou: "+ str(len(alunos)) + " certificados em:" + str(duracao))
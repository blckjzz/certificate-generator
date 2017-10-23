#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import time


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

for aluno in alunos:
    print("Gerando o certificado de: " + aluno)
        
    ch = 8

    img = Image.open("template_certificado.png")
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("fonts/Roboto/Roboto-Regular.ttf", 12)
    fontBlack = ImageFont.truetype("fonts/Roboto/Roboto-Black.ttf", 16)
    # draw.text((x, y),"Sample Text",(r,g,b))
    curso = "Bitcoin para iniciantes"
    curso = curso.decode('utf-8')

    #escreve nome do curso
    draw.text((150, 135), "Curso: " + curso , (0,0,0),font=font)

    #Escreve Data
    data = "24/10/2017 | " + str(ch) + " Horas | ITS Rio"
    draw.text((150, 150), data , (0,0,0),font=font)


    #escreve nome do aluno'
    nomeAluno = aluno.decode('utf-8')
    font = ImageFont.truetype("fonts/Roboto/Roboto-Regular.ttf", 22)

    draw.text((140, 220), nomeAluno.upper() , (0,0,0),font=fontBlack)

    #escreve o texto sobre que apresenta o nome e etc.

    font = ImageFont.truetype("fonts/Roboto/Roboto-Regular.ttf", 16)
    #carga horaria do curso

    tx = "Concluiu o curso de extensão " + str(curso)

    tx += "\ncom a carga hora de " + str(ch) + " horas, oferecido pelo Instituto de Tecnologia e Sociedade \ndo Rio."
    texto = tx.decode('utf-8')
            

    draw.text((140, 255), texto , (0,0,0),font=font)

    #gera o certificado
    img.save("certificados/certificado - " + aluno + ".png")


final = time.time()  

tempoPassado = time.time() - comeco

duracao = time.strftime("%H:%M:%S", time.gmtime(tempoPassado))

print("Você gerou: "+ str(len(alunos)) + " certificados em:" + str(duracao))
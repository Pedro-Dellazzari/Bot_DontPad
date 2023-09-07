#Biblioteca
from bs4 import BeautifulSoup
import requests
import json
import random

import time


from Arts.arts import sex1, sex2, sex3, sex4, sex5, sex6, sex7, sex8, sex9

#Agrupando 
sex_ascii_arts = [sex1, sex2, sex3, sex4, sex5, sex6, sex7, sex8, sex9]


#Url padrão 
url_API_dp = 'https://api.dontpad.com/25abd.body.json?lastModified=0'
Url_Padrao = 'https://api.dontpad.com/25abd'

#Configurando headers
headers={'Authority':"api.dontpad.com",
         "Method":"POST",
         "Path":"/25pedro",
         "Scheme":"https",
         "Accept":"application/json, text/javascript, */*; q=0.01",
         "Accept-Encoding":"gzip, deflate, br",
         "Accept-Language":"pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7",
         "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
         "Origin":"https://dontpad.com",
         "Referer":"https://dontpad.com/",
         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
         }

#Criando a função para armazenar o body fixo 
def Fixed_Body(url):
    #Fazendo o requests dentro do site 
    response = requests.get(url_API_dp)

    #Lendo o html do response
    data_json = response.text

    #Pegando o data_json e transformando em json
    Text_Full = json.loads(data_json)

    #Pegando o body do texto 
    Text_Fixed = Text_Full['body']

    #Fazendo o return 
    return Text_Fixed

#Criando a função para fazer o request 
def Requests_DontPad(url):

    #Fazendo o requests dentro do site 
    response = requests.get(url_API_dp)
    #Vendo status do response
    print(response.status_code)

    #Lendo o html do response
    data_json = response.text

    #Pegando o data_json e transformando em json
    Text_Full = json.loads(data_json)

    #Pegando o body do texto 
    Text_Body = Text_Full['body']
    Text_Fixed = Text_Full['body']
    LastModified = Text_Full['lastModified']

    #Fazendo o return 
    return Text_Body,LastModified

#Criando a função para ver se existe as variavéis e colocar o ASCII arte dentro do site 
def Put_Art(TextBody, TokenModified, Text_Fixed):
    #criação de variáveis
    var_teste = "!python"

    #Separando o texto 
    words = TextBody.split()


    for word in words:
        if var_teste == word:
            print("Encontrou")
            playload = {'text':Text_Fixed + "\n" + random_art_sex,
                        'lastModified':TokenModified,
                        'force':'false'}
            response = requests.post(Url_Padrao, data=playload, headers=headers)
            print(response.status_code)
        
#Pegando o texto fixo 
Text_Fixed = Fixed_Body(Url_Padrao)
#Fazendo o while para ficar rodando sem parar nada

while True: 
    #Fazendo o time sleep para carregar o conteúdo 
    time.sleep(3)

    #Pegando um deste lista aleatória
    random_art_sex = random.choice(sex_ascii_arts)

    #Pegando o texto e o ModifiedToken
    TextSite, ModifiedToken = Requests_DontPad(Url_Padrao)

    #Colocando a arte
    Put_Art(TextSite, ModifiedToken,Text_Fixed)





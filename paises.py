# Rodrigo Viana - rsviana@gmail.com -
import json
import sys

import requests

URL = "https://restcountries.com/v2/all"
URL_NAME = "https://restcountries.com/v2/name"
def requisicao(url):
    try:
        resposta = requests.get(url)
        if  resposta.status_code == 200:
            return resposta.text

    except:
        print("Erro de conexão em", url)

def parsing(textoResposta):
    try:
        return json.loads(textoResposta)
    except:
        print("Erro ao fazer parsing")

def contaPais():
    resposta = requisicao(URL)
    if resposta:
        listaPais = parsing(resposta)
        if listaPais:
            return len(listaPais)

def listaPais(allPais):
    for pais in allPais:
        print(pais['name'])

def listaPopulacao(namePais):
   resposta = requisicao("{}/{}".format(URL_NAME,namePais))
   if resposta:
       listaPais = parsing(resposta)
       if listaPais:
           for pais in listaPais:
               print("{}: {}".format(pais['name'], pais['population']))
       else:
            print("Pais nao encontrado")

def mostrarMoedas(namePais):
   resposta = requisicao("{}/{}".format(URL_NAME,namePais))
   if resposta:
       listaPais = parsing(resposta)
       if listaPais:
           for pais in listaPais:
               print()
               print("Moedas do",pais['name'])
               moedas = pais['currencies']
               for moeda in moedas:
                   print("{} - {}".format(moeda['name'], moeda['code']))
   else:
        print("Pais nao encontrado")
def lerNomePais():
    try:
        argumento2 = sys.argv[2]
        return argumento2
    except:
        print("É preciso passar o nome do país")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Bem vindo ao sistema de Países")
        print("Uso: python paises.py <acao> <nome do pais>")
        print("Ações disponíveis: contagem, moeda, populacao")
    else:
        argumento1 = sys.argv[1]

        if argumento1 == "contagem":
           nPaises = contaPais()
           print("Existem {} ao todo no planeta".format(nPaises))

        elif argumento1 == "moeda":
            pais = lerNomePais()
            if pais:
                mostrarMoedas(pais)
        elif argumento1 == "populacao":
            pais = lerNomePais()
            if pais:
                listaPopulacao(pais)
        else:
            print("Argumento invalido")
# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer
from gtts import gTTS
from chatterbot import ChatBot
import sys
import subprocess as s
import pyttsx

 

bot = ChatBot('Test')

convI = ['oi','olá','oi','olá, qual é o seu nome?','bom dia', 'bom dia','boa noite','boa noite','tudo bem?','Eu estou bem, e você?','Qual é o seu nome?','Meu nome é Pascalzim']

convMatematica = ['Tenho dúvidas em matemática','Qual é a sua dúvida?','Gostaria de sua ajuda','claro, é só dizer qual seu problema',
'vamos mudar de assunto', 'você gosta de matemática?', 'eu amo matemática, com ela conseguimos fazer cosas fantásticas','Você é muito bom com extas','nossa, que legal!']


bot.set_trainer(ListTrainer)
bot.train(convI)
bot.train(convMatematica)


def soma(pergunta):
	soma = 0

	a = pergunta

	b = a.split()

	resposta = []

	temp = '' # variável usada para armazenar os caracteres de cada número encontrado na entrada

	for x in range(0, len(a)):
		if (a[x] == '-'): # se TRUE o sinal será adicionado a temp
			if (temp != ''): # se TRUE quer dizer que já existe outro número em temp, então adiciono a lista para não perder
				resposta.append(temp)
			temp = a[x]
		elif (a[x].isdigit()):
			temp = temp + str(a[x])

			if (x == len(a)-1): # se for um número e estiver na última posição da string já é adicionado diretamente a lista
				resposta.append(temp)
		elif(a[x] == '.'): # se TRUE quer dizer que é um número real então concateno com temp
			temp = temp + a[x]
		else:
			if (temp != ''):
				resposta.append(temp)
				temp = ''

	for x in resposta:
		soma = soma+float(x)

	resposta = ('A soma é: '+str(soma))
	print(resposta)
	falar(resposta)
	


def falar(resposta):
	en = pyttsx.init()
	en.say(resposta)
	en.setProperty('voice',b'brazil')
	en.runAndWait()

while True:
	
	pergunta = input('Você: ')
	resposta = bot.get_response(pergunta)
	#despedida
	if ('TCHAU' in pergunta.upper()):
		print('Pascalzinho: Tchau mestre, nos vemos em breve')
		resposta = 'tchau mestre, nos vemos em breve'
		falar(resposta)
		break


	#Executar um comando linux
	if ('EXECUTE' in pergunta.upper()):
		comando = pergunta.replace('execute ','')
		try:
			s.Popen(comando)
			print('ok')
		except FileNotFoundError:
			print('Comando não encontrado, tendizer "execute ***"')
	#respostas

	elif ('some' in pergunta) or ('+' in pergunta):
		soma(pergunta)

	#incremento
	elif float(resposta.confidence)>0.5:
		print('Pascalzinho:', resposta)
		r = str(resposta)
		falar(r)
	else:
		resposta = 'Não sei o que é, por enquanto, mas você pode me ensinar'
		print('Pascalzim: Não sei o que é, por enquanto, mas você pode me ensinar :D')
		falar(resposta)

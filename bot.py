# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import sys
import subprocess as s
 

bot = ChatBot('Test')

convI = ['oi','olá, qual é o seu nome?','bom dia', 'bom dia','boa noite','boa noite','tudo bem?','Eu estou bem, e você?','Qual é o seu nome?','Meu nome é Pascalzim']

convMatematica = ['Tenho dúvidas em matemática','Qual é a sua dúvida?','Gostaria de sua ajuda','claro, é só dizer qual seu problema',
'vamos mudar de assunto', 'você gosta de matemática?', 'eu amo matemática, com ela conseguimos fazer cosas fantásticas','Você é muito bom com extas','nossa, que legal!']


bot.set_trainer(ListTrainer)
bot.train(convI)
bot.train(convMatematica)

def soma_Simples(pergunta):
	soma = 0
	for x in pergunta:
		if x.isdigit():
			soma = soma+int(x)
	print('Pascalzim:',soma)
 

while True:
	
	pergunta = input('Você: ')
	resposta = bot.get_response(pergunta)
	#despedida
	if ('TCHAU' in pergunta.upper()):
		print('Pascalzinho: Tchau mestre, nos vemos em breve')
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
		soma_Simples(pergunta)

	#incremento
	elif float(resposta.confidence)>0.45:
		print('Pascalzinho:', resposta)
	else:
		print('Pascalzim: Não entendo, por enquanto, mas você pode me ensinar :D')
	
# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import sys
import subprocess as s
 

bot = ChatBot('Test')

convI = ['oi','olá','olá','bom dia', 'bom dia','boa noite','boa noite','como vai?','tudo bem?','Eu estou bem','Qual é o seu nome?','Meu nome é Pascalzim']

convMatematica = ['tenho dúvidas em matemática','qual sua dúvida?','Gostaria de sua ajuda','claro, é só dizer qual seu problema *-*',
'vamos mudar de assunto', 'você gosta de matemática?', 'eu amo matemática, com ela conseguimos fazer cosas fantásticas', 'muito obrigado',
'você é muito bom com extas','nossa, que legal']


bot.set_trainer(ListTrainer)

bot.train(convI)
bot.train(convMatematica)

 
while True:
	pergunta = input('Você: ')
	resposta = bot.get_response(pergunta)
	
	#Executar um comando linux
	if ('execute' in pergunta):
		comando = pergunta.replace('execute ','')
		s.Popen(comando)
		print('ok')
	#despedida
	if (pergunta.upper() == 'TCHAU'):
		print('Pascalzinho: Tchau mestre, nos vemos em breve')
		break
	#respostas
	if float(resposta.confidence)>0.3:
		print('Pascalzinho:', resposta)
	else:
		print('Pascalzim: Não entendo muito sobre isso ainda, me desculpe.')

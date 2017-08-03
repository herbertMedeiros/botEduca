# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Test')

convI = ['oi','olá','olá','bom dia', 'bom dia','boa noite','boa noite','como vai?','tudo bem?','estou bem','qual é o seu nome?','meu nome é Pascalzim']

convMatematica = ['tenho dúvidas em matemática','qual sua dúvida?','Gostaria de sua ajuda','claro, é só dizer qual seu problema *-*',
'vamos mudar de assunto', 'você gosta de matemática?', 'eu amo matemática, com ela conseguimos fazer cosas fantásticas', 'muito obrigado',
'você é muito bom com extas','nossa, que legal']

convConceito = ['quanto é 2+2?','2+2 é igual a 4, essa é fácil, você conta nos dedos kkkk...', 'o que é somar?','somar é formar o tatal das coisas']

bot.set_trainer(ListTrainer)

bot.train(convI)
bot.train(convMatematica)
bot.train(convConceito)
 
while True:
	pergunta = input('Você: ')
	resposta = bot.get_response(pergunta)
	
	if float(resposta.confidence) > 0.5:
		print('Bot:', resposta)
	else:
		print('Bot: Não entendi, repete por favor.')



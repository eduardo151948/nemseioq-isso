#-*- coding: utf-8
# ---------------------------------------------------------------
print('Bem vindo ao Sistema de Filas')
print('Digite a seguir o Numero do Seu computador_senha')
print('Por exemplo: pc1_feijaocombatata')
comando = input('Digite seu computador_senha: ')
computador1 = 'pc1_senha'
computador2 = 'pc2_senha'
computador3 = 'pc3_senha'
computador4 = 'pc4_senha'
computador5 = 'pc5_senha'
computador6 = 'pc6_senha'
computador7 = 'pc7_senha'
computador8 = 'pc8_senha'
computador9 = 'pc9_senha'
computador10 = 'pc10_senha'
computador11 = 'pc11_senha'
supervisor = 'mona_senha'
# ---------------------------------------------------------------

#                    AREA SUPERVISOR

# ---------------------------------------------------------------
if comando == supervisor :

	positivo = 'sim'
	negativo = 'nao'
	lançar1 == 'lançar_pc1'
	lançar2 == 'lançar_pc2'
	lançar3 == 'lançar_pc3'
	lançar4 == 'lançar_pc4'
	lançar5 == 'lançar_pc5'
	lançar6 == 'lançar_pc6'
	lançar7 == 'lançar_pc7'
	lançar8 == 'lançar_pc8'
	lançar9 == 'lançar_pc9'
	lançar10 == 'lançar_pc10'
	lançar11 == 'lançar_pc11'
	mostrar == 'verfilas'

	print('Bem vinda Monalisa')
	print('Caso queira fazer o lançamento de um cliente digite lançar_numerodocomputador')
	print('Caso queira ver as filas digite verfilas')
	print('Exemplo lançar_pc2')
	comandomona = input('Digite aqui o comando: ')
	

	if comandomona == mostrar :
		print('Aguarde, carregando arquivos')
		print('======================PC1==================================')
		arquivo = open("pc1.txt")
		linhas = arquivo.readlines()
		print(linhas)
		for linha in linhas: # colcoar linha por linha
			print(linha)
		print('======================PC2==================================')
		arquivo = open("pc2.txt")
		linhas = arquivo.readlines()
		print(linhas)
		for linha in linhas: # colcoar linha por linha
			print(linha)
		print('======================PC3==================================')
		arquivo = open("pc3.txt")
		linhas = arquivo.readlines()
		print(linhas)
		for linha in linhas: # colcoar linha por linha
			print(linha)
		print('======================PC4==================================')
		arquivo = open("pc4.txt")
		linhas = arquivo.readlines()
		print(linhas)
		for linha in linhas: # colcoar linha por linha
			print(linha)
		print('======================PC5==================================')
		arquivo = open("pc5.txt")
		linhas = arquivo.readlines()
		print(linhas)
		for linha in linhas: # colcoar linha por linha
			print(linha)
		print('======================PC6==================================')
		arquivo = open("pc6.txt")
		linhas = arquivo.readlines()
		print(linhas)
		for linha in linhas: # colcoar linha por linha
			print(linha)
		print('======================PC7==================================')
		arquivo = open("pc7.txt")
		linhas = arquivo.readlines()
		print(linhas)
		for linha in linhas: # colcoar linha por linha
			print(linha)
		print('======================PC8==================================')
		arquivo = open("pc8.txt")
		linhas = arquivo.readlines()
		print(linhas)
		for linha in linhas: # colcoar linha por linha
			print(linha)
		print('=====================PC9===================================')
		arquivo = open("pc9.txt")
		linhas = arquivo.readlines()
		print(linhas)
		for linha in linhas: # colcoar linha por linha
			print(linha)
		print('======================PC10==================================')
		arquivo = open("pc10.txt")
		linhas = arquivo.readlines()
		print(linhas)
		for linha in linhas: # colcoar linha por linha
			print(linha)
		print('========================================================')
		
# ---------------------------------------------------------------

#                    AREA SUPERVISOR LANÇAMENTOS

# ---------------------------------------------------------------

	elif comandomona == lançar1 :
		
		arquivo1 = open('pc1.txt','a') # abrindo modo escrita
		print('Separando Por duas barras //')
		print('Digite o número do cliente , CNPJ , Nome , e dia que o cliente entrou em contato.')
		dadopc1 = input('Por favor digite conforme as instruções acima: ')
		arquivo1.write('{}\n'.format(dadopc1))
		print('Lançado com sucesso\n')
		arq.close() #O arquivo é fechado do modo de adição para ser aberto
            	#posteriormente no modo de leitura

	elif comandomona == lançar2 :

		arquivo2 = open('pc2.txt','a') # abrindo modo escrita
		print('Separando Por duas barras //')
		print('Digite o número do cliente , CNPJ , Nome , e dia que o cliente entrou em contato.')
		dadopc1 = input('Por favor digite conforme as instruções acima: ')
		arquivo2.write('{}\n'.format(dadopc2))
		print('Lançado com sucesso\n')
		arq.close() #O arquivo é fechado do modo de adição para ser aberto
            	#posteriormente no modo de leitura    
	elif comandomona == lançar3 :
		
		arquivo3 = open('pc3.txt','a') # abrindo modo escrita
		print('Separando Por duas barras //')
		print('Digite o número do cliente , CNPJ , Nome , e dia que o cliente entrou em contato.')
		dadopc3 = input('Por favor digite conforme as instruções acima: ')
		arquivo3.write('{}\n'.format(dadopc3))
		print('Lançado com sucesso\n')
		arq.close() #O arquivo é fechado do modo de adição para ser aberto
            	#posteriormente no modo de leitura
	elif comandomona == lançar4 :
		
		arquivo4 = open('pc4.txt','a') # abrindo modo escrita
		print('Separando Por duas barras //')
		print('Digite o número do cliente , CNPJ , Nome , e dia que o cliente entrou em contato.')
		dadopc4 = input('Por favor digite conforme as instruções acima: ')
		arquivo4.write('{}\n'.format(dadopc4))
		print('Lançado com sucesso\n')
		arq.close() #O arquivo é fechado do modo de adição para ser aberto
            	#posteriormente no modo de leitura            	            	            	
	elif comandomona == lançar5 :
		
		arquivo5 = open('pc5.txt','a') # abrindo modo escrita
		print('Separando Por duas barras //')
		print('Digite o número do cliente , CNPJ , Nome , e dia que o cliente entrou em contato.')
		dadopc5 = input('Por favor digite conforme as instruções acima: ')
		arquivo5.write('{}\n'.format(dadopc5))
		print('Lançado com sucesso\n')
		arq.close() #O arquivo é fechado do modo de adição para ser aberto
            	#posteriormente no modo de leitura            	            	            	
	elif comandomona == lançar6 :
		
		arquivo6 = open('pc6.txt','a') # abrindo modo escrita
		print('Separando Por duas barras //')
		print('Digite o número do cliente , CNPJ , Nome , e dia que o cliente entrou em contato.')
		dadopc6 = input('Por favor digite conforme as instruções acima: ')
		arquivo6.write('{}\n'.format(dadopc6))
		print('Lançado com sucesso\n')
		arq.close() #O arquivo é fechado do modo de adição para ser aberto
            	#posteriormente no modo de leitura            	            	            	
	elif comandomona == lançar7 :
		
		arquivo7 = open('pc7.txt','a') # abrindo modo escrita
		print('Separando Por duas barras //')
		print('Digite o número do cliente , CNPJ , Nome , e dia que o cliente entrou em contato.')
		dadopc7 = input('Por favor digite conforme as instruções acima: ')
		arquivo7.write('{}\n'.format(dadopc7))
		print('Lançado com sucesso\n')
		arq.close() #O arquivo é fechado do modo de adição para ser aberto
            	#posteriormente no modo de leitura            	            	            	
	elif comandomona == lançar8 :
		
		arquivo8 = open('pc8.txt','a') # abrindo modo escrita
		print('Separando Por duas barras //')
		print('Digite o número do cliente , CNPJ , Nome , e dia que o cliente entrou em contato.')
		dadopc8 = input('Por favor digite conforme as instruções acima: ')
		arquivo8.write('{}\n'.format(dadopc8))
		print('Lançado com sucesso\n')
		arq.close() #O arquivo é fechado do modo de adição para ser aberto
            	#posteriormente no modo de leitura            	            	            	            	            	           	           	
	elif comandomona == lançar9 :
		
		arquivo9 = open('pc9.txt','a') # abrindo modo escrita
		print('Separando Por duas barras //')
		print('Digite o número do cliente , CNPJ , Nome , e dia que o cliente entrou em contato.')
		dadopc9 = input('Por favor digite conforme as instruções acima: ')
		arquivo9.write('{}\n'.format(dadopc9))
		print('Lançado com sucesso\n')
		arq.close() #O arquivo é fechado do modo de adição para ser aberto
            	#posteriormente no modo de leitura            	            	            		
	elif comandomona == lançar10 :
		
		arquivo10 = open('pc10.txt','a') # abrindo modo escrita
		print('Separando Por duas barras //')
		print('Digite o número do cliente , CNPJ , Nome , e dia que o cliente entrou em contato.')
		dadopc10 = input('Por favor digite conforme as instruções acima: ')
		arquivo10.write('{}\n'.format(dadopc10))
		print('Lançado com sucesso\n')
		arq.close() #O arquivo é fechado do modo de adição para ser aberto
            	#posteriormente no modo de leitura            	            	            		
	else:
		print('Erro, tente novamente')  

# ---------------------------------------------------------------

#                    AREA COMPUTADORES

# ---------------------------------------------------------------
elif comando == computador1 :

	print('Você entrou Como Computador 1')
	print('Aguarde, carregando arquivos')
	print('======================PC1==================================')
	print('Ligue sempre para o Primeiro número, poís ele será excluido')
	arquivo = open("pc1.txt")
	linhas = arquivo.readlines()
	print(linhas)
	for linha in linhas: # colcoar linha por linha
		print(linha)
	excluir = 'limpeza'
	limpar = input('Quando terminar a lista digite limpeza: ')

	if limpar == excluir :
		print('Foi enviado uma solicitação de limpeza para o supervisor.')
		print('O Programa será fechado para aguardar uma nova fila')
		fechar = input('Todos os serviços foram encerrados, feche o programa para continuar.')
	else:
		print('Algo deu errado, Erro: 403')
		fechar = input('Todos os serviços foram encerrados, feche o programa para continuar.')
# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------

elif comando == computador2 :

	print('Você entrou Como Computador 2')
	print('Aguarde, carregando arquivos')
	print('======================PC2==================================')
	arquivo = open("pc2.txt")
	linhas = arquivo.readlines()
	print(linhas)
	for linha in linhas: # colcoar linha por linha
		print(linha)
	excluir = 'limpeza'
	limpar = input('Quando terminar a lista digite limpeza: ')

	if limpar == excluir :
		print('Foi enviado uma solicitação de limpeza para o supervisor.')
		print('O Programa será fechado para aguardar uma nova fila')
		fechar = input('Todos os serviços foram encerrados, feche o programa para continuar.')
	else:
		print('Algo deu errado, Erro: 403')
		fechar = input('Todos os serviços foram encerrados, feche o programa para continuar.')
# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------		
elif comando == computador3 :

	print('Você entrou Como Computador 3')
	print('Aguarde, carregando arquivos')
	print('======================PC3==================================')
	arquivo = open("pc3.txt")
	linhas = arquivo.readlines()
	print(linhas)
	for linha in linhas: # colcoar linha por linha
		print(linha)
	excluir = 'limpeza'
	limpar = input('Quando terminar a lista digite limpeza: ')

	if limpar == excluir :
		print('Foi enviado uma solicitação de limpeza para o supervisor.')
		print('O Programa será fechado para aguardar uma nova fila')
		fechar = input('Todos os serviços foram encerrados, feche o programa para continuar.')
	else:
		print('Algo deu errado, Erro: 403')
		fechar = input('Todos os serviços foram encerrados, feche o programa para continuar.')	
# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------
elif comando == computador4 :

	print('Você entrou Como Computador 4')
	print('Aguarde, carregando arquivos')
	print('======================PC4==================================')
	arquivo = open("pc4.txt")
	linhas = arquivo.readlines()
	print(linhas)
	for linha in linhas: # colcoar linha por linha
		print(linha)
	excluir = 'limpeza'
	limpar = input('Quando terminar a lista digite limpeza: ')

	if limpar == excluir :
		print('Foi enviado uma solicitação de limpeza para o supervisor.')
		print('O Programa será fechado para aguardar uma nova fila')
		fechar = input('Todos os serviços foram encerrados, feche o programa para continuar.')
	else:
		print('Algo deu errado, Erro: 403')
		fechar = input('Todos os serviços foram encerrados, feche o programa para continuar.')

# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------		
elif comando == computador5 :

	print('Você entrou Como Computador 5')
	print('Aguarde, carregando arquivos')
	print('======================PC5==================================')
	arquivo = open("pc5.txt")
	linhas = arquivo.readlines()
	print(linhas)
	for linha in linhas: # colcoar linha por linha
		print(linha)
	excluir = 'limpeza'
	limpar = input('Quando terminar a lista digite limpeza: ')

	if limpar == excluir :
		print('Foi enviado uma solicitação de limpeza para o supervisor.')
		print('O Programa será fechado para aguardar uma nova fila')
		fechar = input('Todos os serviços foram encerrados, feche o programa para continuar.')
	else:
		print('Algo deu errado, Erro: 403')
		fechar = input('Todos os serviços foram encerrados, feche o programa para continuar.')

# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------		
elif comando == computador6 :

	print('Você entrou Como Computador 6')
	print('Aguarde, carregando arquivos')
	print('======================PC6==================================')
	arquivo = open("pc6.txt")
	linhas = arquivo.readlines()
	print(linhas)
	for linha in linhas: # colcoar linha por linha
		print(linha)
	excluir = 'limpeza'
	limpar = input('Quando terminar a lista digite limpeza: ')

	if limpar == excluir :
		print('Foi enviado uma solicitação de limpeza para o supervisor.')
		print('O Programa será fechado para aguardar uma nova fila')
		fechar = input('Todos os serviços foram encerrados, feche o programa para continuar.')
	else:
		print('Algo deu errado, Erro: 403')
		fechar = input('Todos os serviços foram encerrados, feche o programa para continuar.')

# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------		
elif comando == computador7 :

	print('Você entrou Como Computador 7')
	print('Aguarde, carregando arquivos')
	print('======================PC7==================================')
	arquivo = open("pc7.txt")
	linhas = arquivo.readlines()
	print(linhas)
	for linha in linhas: # colcoar linha por linha
		print(linha)
	excluir = 'limpeza'
	limpar = input('Quando terminar a lista digite limpeza: ')

	if limpar == excluir :
		print('Foi enviado uma solicitação de limpeza para o supervisor.')
		print('O Programa será fechado para aguardar uma nova fila')
		fechar = input('Todos os serviços foram encerrados, feche o programa para continuar.')
	else:
		print('Algo deu errado, Erro: 403')
		fechar = input('Todos os serviços foram encerrados, feche o programa para continuar.')

# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------		
elif comando == computador8 :	

	print('Você entrou Como Computador 8')
	print('Aguarde, carregando arquivos')
	print('======================PC8==================================')
	arquivo = open("pc8.txt")
	linhas = arquivo.readlines()
	print(linhas)
	for linha in linhas: # colcoar linha por linha
		print(linha)
	excluir = 'limpeza'
	limpar = input('Quando terminar a lista digite limpeza: ')

	if limpar == excluir :
		print('Foi enviado uma solicitação de limpeza para o supervisor.')
		print('O Programa será fechado para aguardar uma nova fila')
		fechar = input('Todos os serviços foram encerrados, feche o programa para continuar.')
	else:
		print('Algo deu errado, Erro: 403')
		fechar = input('Todos os serviços foram encerrados, feche o programa para continuar.')

# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------		
elif comando == computador9 :

	print('Você entrou Como Computador 9')
	print('Aguarde, carregando arquivos')
	print('======================PC9==================================')
	arquivo = open("pc9.txt")
	linhas = arquivo.readlines()
	print(linhas)
	for linha in linhas: # colcoar linha por linha
		print(linha)
	excluir = 'limpeza'
	limpar = input('Quando terminar a lista digite limpeza: ')

	if limpar == excluir :
		print('Foi enviado uma solicitação de limpeza para o supervisor.')
		print('O Programa será fechado para aguardar uma nova fila')
		fechar = input('Todos os serviços foram encerrados, feche o programa para continuar.')
	else:
		print('Algo deu errado, Erro: 403')
		fechar = input('Todos os serviços foram encerrados, feche o programa para continuar.')

# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------		
elif comando == computador10 :	

	print('Você entrou Como Computador 10')
	print('Aguarde, carregando arquivos')
	print('======================PC10==================================')
	arquivo = open("pc10.txt")
	linhas = arquivo.readlines()
	print(linhas)
	for linha in linhas: # colcoar linha por linha
		print(linha)
	excluir = 'limpeza'
	limpar = input('Quando terminar a lista digite limpeza: ')

	if limpar == excluir :
		print('Foi enviado uma solicitação de limpeza para o supervisor.')
		print('O Programa será fechado para aguardar uma nova fila')
		fechar = input('Todos os serviços foram encerrados, feche o programa para continuar.')
	else:
		print('Algo deu errado, Erro: 403')
		fechar = input('Todos os serviços foram encerrados, feche o programa para continuar.')

else:
	print('Computador não encontrado.')	
	print('Algo deu errado, Erro: 403')
	fechar = input('Todos os serviços foram encerrados, feche o programa para continuar.')

from cgitb import reset
from distutils.command.clean import clean
from http.cookies import SimpleCookie
import os
from turtle import clear
print('BEM VINDO AO SISTEMA DE ACOMPANHAMENTO DE DOAÇÕES DA INFINITY SCHOOL.')

print('''ESTE SISTEMA POSSUI COMO FINALIDADE ACOMPANHAR AS INSCRIÇÕES PARA O PROGRAMA HACKATON E, ATRIBUIR, CONFORME DECISÃO DO USUARIO, A INSTIUIÇÃO
DE CARIDADE QUE DEVERÁ RECEBER A DOAÇÃO DA TAXA DE PARTICIPAÇÃO.''')


#curso = input('Selecione o seu curso:')
#alouconv = 0
#doacao =  
#qtddoacao = 
#instituicao = 
finalizacao = 1
while (finalizacao == 1):
    nome = input('Digite o seu nome: \n')
    idade = int(input('Qual a sua idade? \n'))
    if idade < 18:
        print('Fala garoto! Bem vindo, só não esquece que open bar pra você só de coca cola, tá?')
    else:
        print('Open BAR Liberado sem precisar registrar hoje ein.')
    print(f'{nome}!, Seja bem vindo ao Hackathon da Infinity School. Conta pra gente, você é aluno ou convidado?')
    alouconv = int(input('Digite: 1 - Aluno ; 2 - Convidado: \n'))
    if alouconv == 1:
        print(f'Que daora {nome}! Bom te ver participando do nosso Hackathon. ')
        print('Precisamos saber qual o seu curso, digite: 1 - Programação Full Stack ; 2 - Outros')
        alouconv = 'Aluno'
        curso = int(input('Qual o seu curso? \n'))
        if curso == 1:
            curso = 'Programação Full Stack'
        else:
            curso = input("Você escolheu OUTROS. Informe qual o seu curso? \n")
    else:
        alouconv = 'Convidado'
        print(f'Bem vindo {nome}! Aproveite para conhecer a nossa escola com o Prof. Marcus Azevedo! O cara é fera e vai te ajudar da melhor forma.')

    doacao = int(input('''A participação no nosso evento, foi condicionada a doação de pelo menos 1 kg de alimento não perecivel. Você realizou a doação de
1 ou mais kg(s) de alimento? \n Digite: \n 1 para SIM. \n 2 para NÃO. \n 3 para DOEI MAIS DE 1KG.\n Digite a opção escolhida:\n'''))

    if doacao == 1:
        print('Doação registrada. Obrigado.')
        doacao = 1
    elif doacao == 3:
        doacao = int(input('Quantos kg de alimento você doou? \n'))
        print(f'Doação de {doacao} kgs de alimento registrada. Obrigado.')

    else:
        doacao = 0
        print('Você precisa realizar uma doação para ser avaliado no Hakathon da Infinity.')
        exit()

    print('''TODAS AS DOAÇÕES RECEBIDAS SERÃO ENTREGUES A(S) INSTITUIÇÕES DE OPÇÃO DO ALUNO DOADOR. NESTE MOMENTO, PRECISAMOS QUE VOCÊ ESCOLHA UMA DAS INSTITUIÇÕES A SEGUIR: \n 
    OPÇÕES:\n
    1 para OBRAS SOCIAIS IRMÃ DULCE.
    2 para CASA DE CARIDADE CORAÇÃO DE MARIA.
    3 para LAR FREI LUCAS DE MORAES.
    4 para informar sua própria instiuição de interesse.''')

    instituicao = int(input('Digite a opção desejada:\n'))
    
    if instituicao == 4:
        instituicao = input('Informe a instituição desejada:\n')
        print('A doação será adicionada para contagem final a favor da instituição escolhida. Obrigado!')
    elif instituicao == 1:
        instituicao = 'OBRAS SOCIAIS IRMÃ DULCE'
        print('A doação será adicionada para contagem final a favor da instituição escolhida. Obrigado!')
    elif instituicao == 2:
        instituicao = 'CASA DE CARIDADE CORAÇÃO DE MARIA'
        print('A doação será adicionada para contagem final a favor da instituição escolhida. Obrigado!')
    elif instituicao == 3:
        instituicao = 'LAR FREI LUCAS DE MORAES'
        print('A doação será adicionada para contagem final a favor da instituição escolhida. Obrigado!')
    else:
        print('Você deve escolher uma instituição. Por favor, reinicie o programa.')
        exit()

    print('''Deseja continuar a rodar o programa?
    Digite 1 para SIM 
    Digite 2 para NÃO''')
    finalizacao = int(input('Insira a opção desejada:  \n'))

    print(f'Segue abaixo o resumo das informações cadastradas pelo ultimo usuário:\n')
    print(f'Nome do doador: {nome}')
    print(f'A idade do doador é: {idade} anos.')
    print(f'O doador identificou-se como: {alouconv} do curso de {curso}.')
    print(f'A doação realizada foi de: {doacao}kg(s).')
    print(f'A instituição escolhida pelo doador foi: {instituicao}')
    print(f'''
A doação de {doacao}kg(s) de alimento será realizada a instituição {instituicao} em breve! Obrigado {nome} por sua participação em nosso evento.''')
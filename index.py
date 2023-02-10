import time
import funcoes as fn
import textoMenu as txtM
import os
import login as lg
# Loop para repetir o processo de login até que o usuário forneça credenciais válidas
i = 1
while i <= 4: 
    login = input("Nome de usuário: ") 
    senha = input("Senha: ") 
    if lg.autenticar(login, senha): 
        print("Login realizado com sucesso!") 
        time.sleep(2)
        if True:os.system('cls')     
        start = input('Digite sim para csv ou digite não para digitar o gabarito e respostas \n').lower()
        if start != 'sim':
            qtdAlunos = int(input('Digite a quantidade de alunos: '))
            while qtdAlunos == 0:
                qtdAlunos = int(input('Digite uma quantidade de alunos maior que zero: '))
            gabarito = input('Digite o gabarito da prova: ').lower()
            info = fn.infoAlunos(qtdAlunos, gabarito)
            loop = 'sim'
            while loop == 'sim':
                print(txtM.menu)
                opcao = int(input())
                print('\n')
            #estrutura de condição para saber qual função deve ser apresentada na tela
                if opcao == 1:
                    ordenar = fn.ordenarNome(qtdAlunos)
                if opcao == 2:
                    ordenar = fn.ordenarNota(qtdAlunos)
                if opcao == 3:
                    ordenar = fn.ordemMaior7(qtdAlunos)
                if opcao == 4:
                    ordenar = fn.ordemMenor7(qtdAlunos)
                if opcao == 5:
                    aprovacao = fn.percentualAprovacao(qtdAlunos)
                if opcao == 6:
                    frequencia = fn.maiorFrequencia(qtdAlunos)
                if opcao == 7:
                    maior = fn.maiorNota(qtdAlunos)
                if opcao == 8:
                    menor = fn.menorNota(qtdAlunos)
                if opcao == 9:
                    media = fn.mediaTurma(qtdAlunos)
                print('\n')
                print('Deseja voltar para o menu? Digite sim ou não')
                loop = input().lower()
                print('\n')
                if loop == 'sim':os.system('cls')
                    
        else:
            qtdAlunos = int(input('Digite a quantidade de alunos: '))
            while qtdAlunos == 0:
                qtdAlunos = int(input('Digite uma quantidade de alunos maior que zero: '))
            info = fn.infoAlunosCSV()
            loop = 'sim'
            while loop == 'sim':
                print(txtM.menu)
                opcao = int(input())
                print('\n')
            #estrutura de condição para saber qual função deve ser apresentada na tela
                if opcao == 1:
                    ordenar = fn.ordenarNome(qtdAlunos)
                if opcao == 2:
                    ordenar = fn.ordenarNota(qtdAlunos)
                if opcao == 3:
                    ordenar = fn.ordemMaior7(qtdAlunos)
                if opcao == 4:
                    ordenar = fn.ordemMenor7(qtdAlunos)
                if opcao == 5:
                    aprovacao = fn.percentualAprovacao(qtdAlunos)
                if opcao == 6:
                    frequencia = fn.maiorFrequencia(qtdAlunos)
                if opcao == 7:
                    maior = fn.maiorNota(qtdAlunos)
                if opcao == 8:
                    menor = fn.menorNota(qtdAlunos)
                if opcao == 9:
                    media = fn.mediaTurma(qtdAlunos)
                print('\n')
                print('Deseja voltar para o menu? Digite sim ou não')
                loop = input().lower()
                print('\n')
                if loop == 'sim':os.system('cls')
            break
            
    else:
        if i <= 4: 
            print("Falha no login. Por favor, tente novamente.")
            i+=1
            time.sleep(1)
            if True:os.system('cls') 

print('Você ultrapassou o numero de tentativas, o sistema será desligado....')
time.sleep(2)
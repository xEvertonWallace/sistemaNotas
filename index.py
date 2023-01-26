import funcoes as fn
import textoMenu as txtM
import os

start = input('Digite sim para csv ou digite não para digitar o gabarito e respostas \n').lower()
if start != 'sim':
    gabarito = input('Digite o gabarito da prova: ').lower()
    qtdAlunos = int(input('Digite a quantidade de alunos: '))
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

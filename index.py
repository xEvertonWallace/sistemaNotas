gabarito = input('Digite o gabarito da prova: ').lower()
qtdAlunos = int(input('Digite a quantidade de alunos: '))
dados = list()

#função para receber as informaçoes do aluno e enviar para a lista.   
def infoAlunos(qtdAlunos, gabarito):
    for i in range(qtdAlunos):
        matricula = int(input('Matricula do Aluno: '))
        nome = str(input('Nome do aluno: ').lower())
        resp = str(input('Resposta do aluno: ').lower())
        nota = calcularNota(resp, gabarito)
        dados.append({'nome': nome, 'matricula': matricula, 'nota': nota})

#função para calcular quantas questões o aluno acertou

def calcularNota(resp, gaba):
    nota = 0
    for x in range(len(gaba)):
        if resp[x] == gaba[x]:
            nota += 1
    return nota

#função para ordenar os alunos em ordem alfabética
def ordenarNome(qtdAlunos):
    for i in range(qtdAlunos):     
        ordenar = sorted(dados, key=lambda row: row['nome']) # função anonima que filtra as linhas da chave nome.  
        print(ordenar[i])

#função para ordernar as notas do aluno em ordem crescente.
def ordenarNota(qtdAlunos):
    for i in range(qtdAlunos):
        ordenar = sorted(dados, key=lambda row: row['nota'])
        print(ordenar[i])

#função para ordenar as notas dos alunos aprovados em ordem crescente.
def ordemMaior7(qtdAlunos):
    ordenar = sorted(dados, key=lambda row: row['nota'])
    for i in range(qtdAlunos):
        if ordenar[i]['nota'] >= 7:
            aux = ordenar[i]
            print(aux)

#função para ordenar as notas dos alunos aprovados em ordem decrescente.
def ordemMenor7(qtdAlunos):
    ordenar = sorted(dados, key=lambda row: row['nota'], reverse=True)
    for i in range(qtdAlunos):
        if ordenar[i]['nota'] < 7:
            aux = ordenar[i]
            print(aux)

#função para apresentar o percentual de alunos aprovados.
def percentualAprovacao(qtdAlunos):
    cont = 0
    aprovado = 0
    for i in range(qtdAlunos):
        if dados[i]['nota'] >= 7:
            aprovado += 1
            cont += 1
        else:
            cont += 1
    percent = (aprovado/cont)*100
    print(f'O percentual de aprovação é {percent:,.2f}%')

#função que apresenta a nota com maior frenquencia
def maiorFrequencia(qtdAlunos):
    ordem = list()
    for i in range(qtdAlunos):
        nota = dados[i]['nota']
        ordem.append(nota)
        res = max(set(ordem), key=ordem.count)#verifica as notas que mais se repetem e utiliza o metodo set para armazenar apenas uma dessas notas.
    print("A nota com maior frequencia é: " + str(res))

#função que apresenta a maior nota
def maiorNota(qtdAlunos):
    notas = list()
    for i in range(qtdAlunos):
        nota = dados[i]['nota']
        notas.append(nota)
        maiorNota = max(notas) #verifica a maior nota e armazena na variavel maiorNota
    for i in range(qtdAlunos):
        if notas[i] == maiorNota: #faz uma verificação da nota cpm so dados do aluno e printa as informações do aluno juntamente com a nota
            print(dados[i]) 
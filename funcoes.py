import leituraGabarito as ltg
dados = list()

# funcao que irá calcular a notas: 
def calcularNota(resp, gaba, csv): 
    nota = 0 
    if csv == 'N': 
        for x in range(len(gaba)): 
            if resp[x] == gaba[x]: 
                nota += 1 
        return nota 
    else: 
        for x in range(len(gaba)): 
            if resp[x] == gaba[x]: 
                nota += 1 
        return nota 
#função para receber as informaçoes do aluno e enviar para a lista.   
def infoAlunos(qtdAlunos, gabarito):
    for i in range(qtdAlunos):
        matricula = int(input('Matricula do Aluno: '))
        nome = str(input('Nome do aluno: ').lower())
        resp = str(input('Resposta do aluno: ').lower())
        nota = calcularNota(resp, gabarito, csv = 'N')
        dados.append({'nome': nome, 'matricula': matricula, 'nota': nota})

# funcao que irá receber as informações dos estudantes a partir do csv: 
def infoAlunosCSV(): 
    for i in open('respostas.csv', 'r'): 
        aux = i.split(';') 
        matricula = aux[0][10:] 
        nome = aux[1][5:] 
        resps = aux[2][10:]
        nota = calcularNota(resp=resps, gaba=ltg.gabarito, csv='S') 
        dados.append({'nome': nome, 'matricula': matricula, 'nota': nota})  
    return dados 

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
    ordem = list()#cria uma lista com as notas dos alunos
    for i in range(qtdAlunos):
        nota = dados[i]['nota']
        ordem.append(nota)
    unicos = set(ordem)
    aux = dict()
    aux1 = list()
    for i in unicos:
        freq = ordem.count(i)# verifica a frequencia da nota
        aux[i] = freq
        aux1.append(freq)      
    maiorFREQ = max(aux1)
    res = list()
    for j in aux:
        if aux[j] == maiorFREQ:
            res.append(j)#armazena as notas com as maiores frenquencias
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
#função que apresenta a maior nota
def menorNota(qtdAlunos):
    notas = list()
    for i in range(qtdAlunos):
        nota = dados[i]['nota']
        notas.append(nota)
        menorNota = min(notas) #verifica a menor nota e armazena na variavel menorNota
    for i in range(qtdAlunos):
        if notas[i] == menorNota: #faz uma verificação da nota com so dados do aluno e printa as informações do aluno juntamente com a nota
            print(dados[i])

#função para calcular a media da turma
def mediaTurma(qtdAlunos):
    nota = 0
    for i in range(qtdAlunos):
        nota += dados[i]['nota']
    media = (nota/qtdAlunos)
    print(f'A média da turma é: {media:,.2f}')
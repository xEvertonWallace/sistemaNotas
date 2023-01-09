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

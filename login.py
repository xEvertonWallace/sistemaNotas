# Armazenamos os usuários e senhas em uma lista de dicionários 
usuarios = [ 
    { 
        "login": "everton542@hotmail.com", 
        "senha": "1997" 
    }, 
    { 
        "login": "wallace542@hotmail.com", 
        "senha": "4567" 
    }, 
    { 
        "login": "luiz123@hotmail.com", 
        "senha": "6789" 
    } 
] 
 
# Função para autenticar o usuário 
def autenticar(login, senha): 
    for usuario in usuarios: 
        if usuario["login"] == login and usuario["senha"] == senha: 
            return True 
    return False 
 

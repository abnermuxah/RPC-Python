#Client RPC
from xmlrpc.client import ServerProxy
cliente = ServerProxy('http://localhost:20064', allow_none=True)
while True:
    nome = input("Digite o nome para receber o número \n")
    cliente.nome(nome)
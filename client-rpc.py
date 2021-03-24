#Client RPC
from xmlrpc.client import ServerProxy # RPC do Python usa HTTP como protocolo de transporte
cliente = ServerProxy('http://localhost:20064', allow_none=True) # criar uma instância cliente localhost e na porta do servidor
while True:
    nome = input("Digite o nome para receber o número \n")
    cliente.nome(nome) # chama a função que está implementada do lado do servidor
# Server RPC
from xmlrpc.server import SimpleXMLRPCServer
# classe que implementa RPC
class RPC:
    # métodos que vamos trabalhar com RPC
    _metodos_rpc = ['nome'] # 'nome2' ...
    def __init__(self, direcao): # Construtor
        self._servidor = SimpleXMLRPCServer(direcao, allow_none=True) # instanciar o servidor RPC
        # dados que serão instanciados ao criar o servidor RPC
        self.agenda = {'Glaucia' : '84 9 9874 9658', 'Abner':'84 9 9135 8465', 'Allyson':'84 9 9486 5132'} # ... ('chave':'valor)
        # registrar os metodos no RPC da lista _metodos_rpc (posso acrescentar mais metodos)
        for metodo in self._metodos_rpc:
            self._servidor.register_function(getattr(self, metodo))
    def nome(self, nome):
        if nome in self.agenda: # se o nome existir na agenda retorne telefone correspondente
            return self.agenda[nome]
        else:
            return "\n este nome nao ta na agenda :( \n" 
    def iniciar_servidor(self): # funcao p iniciar o servidor
        self._servidor.serve_forever()
if __name__ == '__main__' : # função principal
    rpc = RPC(('', 20064)) # o servidor vai ficar escurando no localhost e na porta 20064
    print("Servidor RPC iniciado ... ")
    rpc.iniciar_servidor()
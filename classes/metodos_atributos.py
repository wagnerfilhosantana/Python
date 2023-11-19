"""
public, protected, private
_ protected
__ private
"""

class BasedeDados:
    def __init__(self):
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados

    def inserir_clientes(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados ['clientes'] = { id: nome}
        else:
            self.__dados ['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)
    
    def apagar_cliente(self, id):
        del self.__dados['clientes'][id]

bd = BasedeDados()
bd.inserir_clientes(1, 'Wagner')
bd.inserir_clientes(2, 'Ana Kelly')
bd.inserir_clientes(3, 'Wesley')
bd.inserir_clientes(4, 'Isabelly')
bd.inserir_clientes(5, 'Gabriele')
bd.inserir_clientes(6, 'Cleonice')
bd.lista_clientes()
print(bd.dados)

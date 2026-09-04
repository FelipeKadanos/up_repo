class Participante:
    def __init__(self, nome, idade, email, categoria, valor_pago):
        self.nome = nome
        self._idade = idade
        self.email = email
        self.categoria = categoria
        self.__valor_pago = valor_pago

    @property
    def categoria(self):
        return self._categoria
    
    @categoria.setter
    def categoria(self, nova_categoria):
        nova_categoria.upper()
        
        if nova_categoria == "ESTUDANTE" or nova_categoria == "PROFISSIONAL" or nova_categoria == "PALESTRANTE":
            self._categoria = nova_categoria

        else:
            print("Categoria inválida.")

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, nova_idade):
        if nova_idade >= 0:
            self._idade = nova_idade
        else:
            print("Idade inválida.")

    @property
    def valor_pago(self):
        return self.__valor_pago

    @valor_pago.setter
    def valor_pago(self, novo_valor_pago):
        if novo_valor_pago >= 0:
            self.__valor_pago = novo_valor_pago
        else:
            print("Valor pago não pode ser negativo.")

    def mostrar_dados(self):
        print("================================")
        print(f"Nome        : {self.nome}")
        print(f"Idade       : {self._idade}")
        print(f"Email       : {self.email}")
        print(f"Categoria   : {self.categoria}")
        print(f"Valor pago  : {self.__valor_pago}")
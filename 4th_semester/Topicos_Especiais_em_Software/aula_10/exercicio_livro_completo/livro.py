class Livro:
    def __init__(self, titulo, autor, ano, editora, preco):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.editora = editora
        self.preco = preco

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, novo_ano):
        if novo_ano > 0:
            self._ano = novo_ano
        else:
            print("Ano inválido.")

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco >= 0:
            self.__preco = novo_preco
        else:
            print("Preço inválido.")

    def mostrar_dados(self):
        print("=====================")
        print(f"Título  : {self.titulo}")
        print(f"Autor   : {self.autor}")
        print(f"Ano     : {self.ano}")
        print(f"Editora : {self.editora}")
        print(f"Preço   : {self.preco}")
    

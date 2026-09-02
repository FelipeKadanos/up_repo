# ORIENTAÇÃO A OBJETOS

class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self._idade = idade
        self.__cpf = cpf  # atributo privado
        # nome é um parâmetro recebido
        # self.nome é um atributo do objeto

        # _idade significa que esse atributo é interno.
        # Não deveria ser manipulado diretamente fora da classe.

        # __cpf (name mangling) significa que esse atributo é privado.

    @property # Getter
    def idade(self):
        return self._idade
    
    @idade.setter # Setter
    def idade(self, idade):
        if idade <= 0:
            print("Idade invalida.")
        else:
            self._idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")



class Aluno(Pessoa):
    def __init__(self, nome, idade, cpf, matricula):
        super().__init__(nome, idade, cpf)
        self.matricula = matricula

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, eu tenho {self.idade} anos e minha matrícula é {self.matricula}.")



aluno = Aluno("João", 20, "123.456.789-00", "2026001")
print(aluno.nome)  # Acesso ao atributo público
print(aluno.idade)  # Acesso ao atributo protegido via getter
print(aluno.matricula)  # Acesso ao atributo público
aluno.apresentar()  # Acesso ao método da classe Aluno


# POLIMORFISMO

class Pessoa:
    def apresentar(self):
        print("Sou uma pessoa.")

class Aluno(Pessoa):
    def apresentar(self):
        print("Sou um aluno.")

class Professor(Pessoa):
    def apresentar(self):
        print("Sou um professor.")

pessoa = Pessoa()
aluno = Aluno()
professor = Professor()

pessoa.apresentar()  # Saída: Sou uma pessoa.
aluno.apresentar()   # Saída: Sou um aluno.
professor.apresentar()  # Saída: Sou um professor.
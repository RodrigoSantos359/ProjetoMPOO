class Pessoa:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self, nome, cpf, idade, matricula, curso):
        super().__init__(nome, cpf, idade)
        self.matricula = matricula
        self.curso = curso

class Servidor(Pessoa):
    def __init__(self, nome, cpf, idade, cargo):
        super().__init__(nome, cpf, idade)
        self.cargo = cargo

class Professor(Servidor):
    def __init__(self, nome, cpf, idade, cargo, disciplinas):
        super().__init__(nome, cpf, idade, cargo)
        self.disciplinas = disciplinas

class Diretor(Servidor):
    def __init__(self, nome, cpf, idade, cargo, atributos_especificos):
        super().__init__(nome, cpf, idade, cargo)
        self.atributos_especificos = atributos_especificos

class Coordenador(Servidor):
    def __init__(self, nome, cpf, idade, cargo, atributos_especificos):
        super().__init__(nome, cpf, idade, cargo)
        self.atributos_especificos = atributos_especificos

class Curso:
    def __init__(self, disciplinas):
        self.disciplinas = disciplinas

class Disciplina:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor

class Sala:
    def __init__(self, numero):
        self.numero = numero

class Endereco:
    def __init__(self, rua, numero, bairro):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
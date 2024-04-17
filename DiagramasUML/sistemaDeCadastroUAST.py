class Aluno:
    def __init__(self, nome, matricula, curso, endereco):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.endereco = endereco

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getMatricula(self):
        return self.matricula

    def setMatricula(self, matricula):
        self.matricula = matricula

    def getCurso(self):
        return self.curso

    def setCurso(self, curso):
        self.curso = curso

    def getEndereco(self):
        return self.endereco

    def setEndereco(self, endereco):
        self.endereco = endereco


class Curso:
    def __init__(self, nome, codigo, departamento):
        self.nome = nome
        self.codigo = codigo
        self.departamento = departamento

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getCodigo(self):
        return self.codigo

    def setCodigo(self, codigo):
        self.codigo = codigo

    def getDepartamento(self):
        return self.departamento

    def setDepartamento(self, departamento):
        self.departamento = departamento


class Endereco:
    def __init__(self, rua, cidade, estado, cep):
        self.rua = rua
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

    def getRua(self):
        return self.rua

    def setRua(self, rua):
        self.rua = rua

    def getCidade(self):
        return self.cidade

    def setCidade(self, cidade):
        self.cidade = cidade

    def getEstado(self):
        return self.estado

    def setEstado(self, estado):
        self.estado = estado

    def getCep(self):
        return self.cep

    def setCep(self, cep):
        self.cep = cep


class Disciplina:
    def __init__(self, nome, codigo, cargaHoraria):
        self.nome = nome
        self.codigo = codigo
        self.cargaHoraria = cargaHoraria

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getCodigo(self):
        return self.codigo

    def setCodigo(self, codigo):
        self.codigo = codigo

    def getCargaHoraria(self):
        return self.cargaHoraria

    def setCargaHoraria(self, cargaHoraria):
        self.cargaHoraria = cargaHoraria


class Professor:
    def __init__(self, nome, departamento, endereco):
        self.nome = nome
        self.departamento = departamento
        self.endereco = endereco

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getDepartamento(self):
        return self.departamento

    def setDepartamento(self, departamento):
        self.departamento = departamento

    def getEndereco(self):
        return self.endereco

    def setEndereco(self, endereco):
        self.endereco = endereco


class Sala:
    def __init__(self, numero, capacidade, localizacao, endereco):
        self.numero = numero
        self.capacidade = capacidade
        self.localizacao = localizacao
        self.endereco = endereco

    def getNumero(self):
        return self.numero

    def setNumero(self, numero):
        self.numero = numero

    def getCapacidade(self):
        return self.capacidade

    def setCapacidade(self, capacidade):
        self.capacidade = capacidade

    def getLocalizacao(self):
        return self.localizacao

    def setLocalizacao(self, localizacao):
        self.localizacao = localizacao

    def getEndereco(self):
        return self.endereco

    def setEndereco(self, endereco):
        self.endereco = endereco
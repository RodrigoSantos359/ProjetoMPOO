# Projeto de MPOO

Este repositório contém o projeto da disciplina de Modelagem e Programação Orientada a Objetos (MPOO). O objetivo deste projeto é aplicar os conceitos aprendidos durante o curso em atividades práticas.

## Estrutura do Projeto

- `Atividas/`: Pasta com as atividades
   - `Atividade 1/`: atividade para modela um controle de TV
   - `Atividade 2/`: atividade para diagrama de herança
   - `Atividade 3`: atividade para sistema de cadastro da UAST
- `Projetos/`: Pasta para projetos
- `MIT License`: Arquivo com a licença
- `README.md`: Este arquivo

## Atividades

### Primeira Atividade: Controle de TV

**Objetivos:**
- Compreender os conceitos básicos de Programação Orientada a Objetos (POO).
- Implementar classes básicas e métodos.
- Exercitar a utilização de atributos e construtores.

**Descrição:**
Nesta atividade, você deve criar uma classe para simular um controle de TV. A classe deve permitir alterar o canal, aumentar/diminuir o volume e ligar/desligar a TV.

**Exemplo de Tarefas:**
1. Criar uma classe `TV` com atributos `canal`, `volume` e `ligada`.
2. Implementar métodos para mudar de canal, aumentar e diminuir o volume, e ligar/desligar a TV.
3. Testar a criação de objetos da classe `TV` e os métodos implementados.

### Segunda Atividade: Sistema de Cadastro da UFRPE

**Objetivos:**
- Aprender sobre herança e polimorfismo em POO.
- Implementar classes derivadas e sobrescrever métodos.
- Utilizar o conceito de classes abstratas e interfaces.

**Descrição:**
Nesta atividade, você deve criar um sistema de cadastro para a UFRPE. O sistema deve permitir o cadastro de diferentes tipos de usuários, como alunos e professores, com atributos específicos para cada tipo.

**Exemplo de Tarefas:**
1. Criar uma classe base `Usuario` com atributos `nome`, `cpf` e `email`.
2. Criar classes derivadas `Aluno` e `Professor` que herdam de `Usuario`.
3. Adicionar atributos específicos às classes derivadas, como `matricula` para `Aluno` e `departamento` para `Professor`.
4. Implementar métodos específicos para cada classe derivada, como `realizarMatricula` para `Aluno` e `ministrarAula` para `Professor`.

### Terceira Atividade: Sistema de Cadastro com Herança

**Objetivos:**
- Aprender sobre encapsulamento e acesso a atributos.
- Implementar getters e setters.
- Utilizar tratamento de exceções para garantir a robustez do código.

**Descrição:**
Nesta atividade, você deve criar um sistema de cadastro que utilize o conceito de herança para diferentes tipos de contas. Além disso, deve implementar mecanismos de encapsulamento e tratamento de exceções.

**Exemplo de Tarefas:**
1. Criar uma classe base `Conta` com atributos `titular`, `saldo` e `limite`.
2. Criar classes derivadas `ContaCorrente` e `ContaPoupanca` que herdam de `Conta`.
3. Implementar métodos para depositar e sacar dinheiro, utilizando encapsulamento para proteger os atributos.
4. Implementar tratamento de exceções para evitar saques que excedam o saldo ou o limite.

## Como Usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/projeto-mpoo.git

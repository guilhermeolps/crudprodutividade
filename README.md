# Sistema de Gestão de Produtividade

Sistema desenvolvido em **Python** para gerenciamento de tarefas e acompanhamento da produtividade diária.

A aplicação funciona através do terminal e permite cadastrar, visualizar, atualizar e remover tarefas, além de registrar o histórico das alterações e armazenar os dados em um arquivo JSON.

## Funcionalidades

* **ABOUT** — Exibe informações sobre o sistema.
* **ADD** — Adiciona novas tarefas e registra um resumo da produtividade do dia.
* **LIST** — Lista todas as tarefas cadastradas, seus respectivos status e histórico.
* **UPDATE** — Permite alterar o nome e o status de uma tarefa.
* **DELETE** — Remove uma tarefa da lista.
* **QUIT** — Encerra a aplicação.
* Armazenamento permanente das tarefas através de um arquivo `JSON`.
* Registro do histórico das alterações realizadas nas tarefas.
* Validação das entradas fornecidas pelo usuário.

## Tecnologias utilizadas

* **Python**
* **JSON**
* **Git**
* **GitHub**

## Conceitos praticados

O desenvolvimento do projeto permitiu colocar em prática conceitos fundamentais de programação, como:

* Funções e organização de responsabilidades;
* Listas e dicionários;
* Estruturas condicionais;
* Estruturas de repetição;
* Tratamento de exceções com `try/except`;
* Manipulação de arquivos;
* Serialização e leitura de dados em JSON;
* Tipagem com `Optional`;
* Entrada e saída de dados pelo terminal;
* Operações de CRUD;
* Versionamento de código com Git.

##  Armazenamento dos dados

As tarefas são armazenadas no arquivo `tarefas.json`.

O programa utiliza o módulo `json` do Python para salvar e carregar os dados, permitindo que as tarefas continuem disponíveis mesmo depois que a aplicação seja encerrada.

Exemplo da estrutura de uma tarefa:

```json
{
    "nome": "Estudar Python",
    "concluido": true,
    "historico": [
        ["criação", true, "Estudar Python"]
    ]
}
```

## ▶️ Como executar

### 1. Clone o repositório

```bash
git clone URL_DO_REPOSITORIO
```

### 2. Acesse a pasta do projeto

```bash
cd crudprodutividade
```

### 3. Execute o programa

```bash
python main.py
```

Após iniciar, o sistema apresentará os comandos disponíveis:

```text
ABOUT
ADD
LIST
UPDATE
DELETE
QUIT
```

## Objetivo do projeto

O projeto foi desenvolvido como parte dos estudos em **Análise e Desenvolvimento de Sistemas**, com o objetivo de praticar conceitos de programação através da criação de uma aplicação funcional para gerenciamento de tarefas e acompanhamento da produtividade.

##  Autor

**Guilherme**

Projeto desenvolvido para fins acadêmicos e de aprendizado.

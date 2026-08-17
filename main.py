from time import sleep
from typing import Optional
import json


# Buscar tarefa por índice
def buscar_tarefa_por_indice(lista_tarefas, indice) -> Optional[dict]:
    if 0 <= indice < len(lista_tarefas):
        return lista_tarefas[indice]
    return None


# About
def about():
    print("Olá usuário, Boas-vindas ao Sistema de Gestão de produtividade!, Navegue pelos comandos aqui:)")


# List
def listar_tarefas(lista_tarefas):
    if not lista_tarefas:
        print("Nenhuma tarefa registrada ainda.")
    else:
        print("Lista de tarefas:")
        for i, tarefa in enumerate(lista_tarefas):
            status = "✔️" if tarefa["concluido"] else "❌"
            print(f"{i+1}. Nome: {tarefa['nome']} | Status: {status}")

            print("Histórico:")
            for evento in tarefa["historico"]:
                print(f"  - {evento}")


# Add
def adicionar_tarefa(lista_tarefas):
    try:
        quantidade = int(input("Quantas tarefas você concluiu hoje? (apenas números): "))
    except ValueError:
        print("Entrada inválida.")
        return

    if quantidade <= 0:
        print("Quantidade inválida.")
        return

    for i in range(quantidade):
        nome = input(f"Informe a {i+1}° tarefa: ").strip()

        if not nome:
            print("Nome inválido.")
            continue

        tarefa = {
            "nome": nome,
            "concluido": True,
            "historico": [["criação", True, nome]]
        }

        lista_tarefas.append(tarefa)
        print(f"Tarefa: {nome} registrada com sucesso!")

    # salva uma vez apenas
    salvar_tarefas(lista_tarefas)

    try:
        horas = int(input("Quantas horas você estudou hoje? "))
        nota = int(input("De 0 a 10, qual a nota do seu dia? "))
    except ValueError:
        print("Entrada inválida.")
        return

    print(f"Resumo do seu dia: {quantidade} tarefas concluídas | {horas}h estudadas | Dia nota {nota}")


# Update
def atualizar_tarefa(lista_tarefas):
    if not lista_tarefas:
        print("Nenhuma tarefa para atualizar.")
        return

    try:
        indice = int(input("Digite o número da tarefa: ")) - 1
    except ValueError:
        print("Digite um número válido.")
        return

    tarefa = buscar_tarefa_por_indice(lista_tarefas, indice)

    if tarefa is None:
        print("Número inválido.")
        return

    novo_nome = input("Novo nome: ").strip()
    status_input = input("Está concluída? (s/n): ").lower()
    novo_status = status_input == "s"

    tarefa["historico"].append(["hoje", novo_status, novo_nome])
    tarefa["nome"] = novo_nome
    tarefa["concluido"] = novo_status

    salvar_tarefas(lista_tarefas)

    print("Tarefa atualizada com sucesso!")


#  Função Delete
def deletar_tarefa(lista_tarefas):
    if not lista_tarefas:
        print("Nenhuma tarefa para remover.")
        return

    try:
        indice = int(input("Digite o número da tarefa: ")) - 1
    except ValueError:
        print("Digite um número válido.")
        return

    tarefa = buscar_tarefa_por_indice(lista_tarefas, indice)

    if tarefa is None:
        print("Número inválido.")
        return

    lista_tarefas.pop(indice)
    salvar_tarefas(lista_tarefas)

    print("Tarefa removida com sucesso!")


# salvar tarefas
def salvar_tarefas(lista_tarefas):
    with open("tarefas.json", "w", encoding="utf-8") as f:
        json.dump(lista_tarefas, f, ensure_ascii=False, indent=4)


# carregar as tarefas
def carregar_tarefas():
    try:
        with open("tarefas.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


tarefas = carregar_tarefas()


# loop que chama as funções.
while True:
    comando = input("Digite um comando (ABOUT, ADD, LIST, UPDATE, DELETE, QUIT): ").strip().upper()
    print("Processando...")
    sleep(1)

    if comando == "ABOUT":
        about()

    elif comando == "ADD":
        adicionar_tarefa(tarefas)

    elif comando == "LIST":
        listar_tarefas(tarefas)

    elif comando == "UPDATE":
        atualizar_tarefa(tarefas)

    elif comando == "DELETE":
        deletar_tarefa(tarefas)

    elif comando == "QUIT":
        print("Saindo do software, até a próxima!")
        break

    else:
        print("Comando não reconhecido.")
import argparse
import json

ARQUIVO_GASTOS = "gastos.json"

parser = argparse.ArgumentParser(description="Controle de Despesas com CLI")

parser.add_argument("acao", choices=["adicionar", "visualizar", "editar"], help="Ações disponíveis")
parser.add_argument("--id", type=int, help="ID do produto a ser editado") 
parser.add_argument("--nome", type=str, help="Nome do gasto")  
parser.add_argument("--valor", type=float, help="Custo do gasto")  
args = parser.parse_args()



# Função para carregar gastos do arquivo
def carregar_gastos():
    try:
        with open(ARQUIVO_GASTOS, "r") as f: # Abre o arquivo no modo read ("r")
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError): # Retorna vazio caso não ache o arquivo ou ele esteja corrompido
        return []

# Função para salvar gastos no arquivo
def salvar_gastos(gastos):
    with open(ARQUIVO_GASTOS, "w") as f: # Abre o arquivo no modo write ("w")
        json.dump(gastos, f, indent=4)

# Função para adicionar gastos
def adicionar(nome, valor):
    gastos = carregar_gastos() # Chama a função
    novo_gasto = {"id": len(gastos)+1, "nome":  nome, "valor":valor} # Os dados que ele vai salvar
    gastos.append(novo_gasto) # Adiciona o novo_gasto pro final da lista
    salvar_gastos(gastos) 
    print(f"{nome} foi adicionado")

# Função para editar valor do gasto
def editar(id_gasto, novo_valor):
    gastos = carregar_gastos()
    for gasto in gastos:
        if gasto["id"] == id_gasto: # Procura pelo ID
            gasto["valor"] = novo_valor  # Atualiza o valor
            salvar_gastos(gastos)
            print(f"Gasto [{id_gasto}] atualizado para {novo_valor}")
            return

    print(f"Gasto com ID {id_gasto} não encontrado.")

# Função para visiualizar os gastos
def visualizar():
    gastos = carregar_gastos() # Carregar a lista
    if not gastos:
        print("Nenhum gasto registrado ainda.") # Caso a lista esteja vazia
    else:
        for gasto in gastos:
            print(f"{gasto['id']} | {gasto['nome']}  {gasto['valor']}")



#Ações
if args.acao == "adicionar":
    adicionar(args.nome, args.valor) # Chama a função e passa os argumentos

elif args.acao == "editar":
    if args.id is None or args.valor is None:
        print("Erro: Para editar, forneça um ID e um novo valor.")
    else:
        editar(args.id, args.valor)

elif args.acao == "visualizar":
    visualizar() # Chama a função visualizar


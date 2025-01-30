import argparse

parser = argparse.ArgumentParser()

parser.add_argument("nome", help="Nome do usuário")

args = parser.parse_args()

print(f"Olá, {args.nome}!")
# Controle de Despesas CLI

Este projeto é uma aplicação de linha de comando (CLI) para gerenciar despesas, permitindo adicionar, visualizar e editar gastos.

## Funcionalidades
- Adicionar novos gastos com nome e valor
- Visualizar todos os gastos cadastrados
- Editar o valor de um gasto existente

## Tecnologias Utilizadas
- Python 3
- Biblioteca `argparse` para interpretação de argumentos
- Biblioteca `json` para armazenamento de dados

## Como Usar
### 1. Clonar o repositório
```sh
git clone https://github.com/ZKNs1/Despesas_CLI.git
```

### 2. Executar a aplicação
#### Adicionar um gasto:
```sh
python main.py adicionar --nome "Pizza" --valor 30.0
```

#### Visualizar todos os gastos:
```sh
python main.py visualizar
```

#### Editar um gasto (mudar valor):
```sh
python main.py editar --id 1 --valor 39.5
```

## Estrutura do Projeto
```
controle-despesas-cli/
├── main.py          # Código principal
├── gastos.json      # Arquivo onde os gastos são armazenados
├── README.md        # Documentação do projeto
```

## Licença
Este projeto está sob a licença MIT.


# TPC5: Máquina de Vending  
## 2024-03-14

## Autor:
- A100827
- Tiago Granja Rodrigues

## Resumo
Construir um programa que simule uma máquina de vending.
A máquina tem um stock de produtos: uma lista de triplos, nome do produto, quantidade e preço, que estão guardados num json:
```bash
{ "stock" :[
    {"cod": "A23", "nome": "água 0.5L", "quant": 8, "preco": 0.7},
    ...
]
}
```
**Comandos:**

- Listar Produtos
```bash
>> LISTAR
maq:
Cod  |    Nome        |  Quantidade  |  Preço
----------------------------------------------
A23  | água 0.5L      | 8            | 0.7
A24  | sumo 0.5L      | 8            | 0.9
A25  | bolo           | 4            | 1.2
```

- Inserir Moedas
```bash
>> Moeda 1e,20c,2c.
maq: Saldo = 1e22c
```

- Selecionar Produto
```bash
>> Selecionar A23
maq: Pode retirar o produto dispensado:  água 0.5L
maq: Saldo = 52c
```

- Sair e receber o troco
```bash
>> Sair
maq: Pode retirar o troco:
maq: 1x 50c, 1x 2c
maq: Até à próxima
```
import ply.lex as lex
import sys
import json
import re

with open("stock.json", "r", encoding="utf-8") as file:
    stock_data = json.load(file)
    stock = {produto["cod"]: produto for produto in stock_data["stock"]}

tokens = ("LISTAR",
          "MOEDA",
          "SELECIONAR",
          "SAIR")

global saldo 
saldo = 0

def t_LISTAR(t):
    r'(?i:listar)'
    print("maq:")
    print("Cod  |    Nome        |  Quantidade  |  Preço")
    print("----------------------------------------------")
    for produto in stock.values(): 
        cod = produto["cod"]
        nome = produto["nome"]
        quantidade = produto["quant"]
        preco = produto["preco"]
        print(f"{cod:<4} | {nome:<14} | {quantidade:<12} | {preco}")
    return t

def t_MOEDA(t):
    r'(?i:moeda)(\s*(2e|1e|50c|20c|10c|5c|2c|1c)\s*,\s*)*(\s*(2e|1e|50c|20c|10c|5c|2c|1c))\s*\.?'
    valores_moeda = t.value
    moedas = re.findall(r'\b(2e|1e|50c|20c|10c|5c|2c|1c)\b', valores_moeda, flags=re.IGNORECASE)
    global saldo
    for moeda in moedas:
        if moeda.endswith('e'):
            saldo += int(moeda[:-1]) * 100
        elif moeda.endswith('c'):
            saldo += int(moeda[:-1])
    imprime_saldo()
    return t


def t_SELECIONAR(t):
    r'(?i:selecionar)\s+(\w+)'
    cod = t.value.split()[1]
    if cod not in stock:
        print("maq: Este produto não existe")
        return
    produto = stock[cod]
    global saldo
    if produto["quant"] <= 0:
        print("maq: Não existe stock")
    elif (produto["preco"]*100) > (saldo):
        print("maq: Saldo insufuciente para satisfazer o seu pedido")
        pedido_euro = int(produto["preco"] // 100)
        pedido_cent = int(round((produto["preco"] - pedido_euro) * 100))
        print(f"maq: Pedido = {pedido_euro}e{pedido_cent}c")
        imprime_saldo()
    else: 
        saldo -= produto["preco"]*100
        print("maq: Pode retirar o produto dispensado: ", produto["nome"])
        imprime_saldo()
        produto["quant"] -= 1
        
    return t

def t_SAIR(t):
    r'(?i:sair)'
    global saldo
    troco = saldo
    saldo = 0.0
    
    if troco > 0:
        print("maq: Pode retirar o troco:")
        moedas = [("2e", 200), ("1e", 100), ("50c", 50), ("20c", 20), ("10c", 10), ("5c", 5), ("2c", 2), ("1c", 1)]
        troco_moedas = []
        for moeda, valor in moedas:
            qtd = troco // valor
            if qtd > 0:
                troco_moedas.append((qtd, moeda))
                troco -= qtd * valor

        troco_formatado = ", ".join([f"{int(qtd)}x {moeda}" for qtd, moeda in troco_moedas])
        print(f"maq: {troco_formatado}")
    
    print("maq: Até à próxima")

    # Guardar no json
    stock_data = {"stock": list(stock.values())}
    with open("stock.json", "w", encoding="utf-8") as file:
        json.dump(stock_data, file, indent=4, ensure_ascii=False)

def imprime_saldo():
    global saldo
    euros = int(saldo // 100)
    cent = int(saldo % 100)
    if euros>0:
        print(f"maq: Saldo = {euros}e{cent}c")
    else:
        print(f"maq: Saldo = {int(cent)}c")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

t_ignore = " \n\t"

lexer = lex.lex()

for line in sys.stdin:
    lexer.input(line)

    while True:
        token = lexer.token()
        if not token:
            break
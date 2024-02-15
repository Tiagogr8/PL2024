import sys


modalidades = set()
n_atletas = 0
aptos = 0
inaptos = 0
distribuicao = {}
#with open("emd.csv", encoding="utf-8") as file:
    #next(file)
sys.stdin.readline() # cabecalho

for line in sys.stdin.readlines():
    coluna = line.strip().split(',')

    # modalidades
    modalidades.add(coluna[8])

    # aptos/inaptos
    n_atletas+=1
    if (coluna[12].lower() == 'true'):
        aptos+=1

    # escalao etario
    idade = int(coluna[5])
    escalao = (idade // 5) * 5
    if (escalao in distribuicao):
        distribuicao[escalao] +=1
    else: distribuicao[escalao] = 1

print("Modalidades:")
for modalidade in sorted(list(modalidades)):
    print(modalidade.encode('utf-8').decode(sys.stdout.encoding))

inaptos = n_atletas - aptos
p_aptos = (aptos/n_atletas) * 100
p_inaptos = (inaptos/n_atletas) * 100


print(f"\nPercentagem atletas aptos: {p_aptos}%")
print(f"Percentagem atletas inaptos: {p_inaptos}%\n")

print("Distribuição de atletas por escalão etário:")
for escalao, total in sorted(distribuicao.items()):
    i = escalao
    s = escalao+4
    print(f"{i}-{s}: {total} -> {round((total/n_atletas)*100,2)}%")

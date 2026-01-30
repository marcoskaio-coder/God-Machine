import csv
import os
from collections import Counter

def analisar():
    arquivo = "diario_bordo.csv"
    if not os.path.isfile(arquivo):
        print("Dataset vazio. Realize consultas primeiro.")
        return

    consultas = []
    with open(arquivo, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            consultas.append(row)

    total = len(consultas)
    cartas = Counter([c['CARTA'] for c in consultas])
    orixas = Counter([c['ORIXA'] for c in consultas])
    raizes = Counter([c['RAIZ'] for c in consultas])

    print("="*40)
    print("   RELATÓRIO DE SINCRONICIDADE (IA)")
    print("="*40)
    print(f"Total de Consultas Processadas: {total}")
    
    print("\n[CARTAS MAIS ATIVAS]")
    for carta, qtd in cartas.most_common(3):
        print(f"-> {carta}: {qtd} vezes ({(qtd/total)*100:.1f}%)")

    print("\n[REGÊNCIA DE ORIXÁS DOMINANTE]")
    for orixa, qtd in orixas.most_common(3):
        print(f"-> {orixa}: {qtd} vezes")

    print("\n[FREQUÊNCIA VIBRATÓRIA (RAIZ)]")
    for raiz, qtd in raizes.most_common(3):
        print(f"-> Raiz {raiz}: {qtd} ocorrências")
    print("="*40)

if __name__ == "__main__":
    analisar()

import csv
import os
from collections import Counter

def analisar_axe():
    arquivo = "diario_bordo.csv"
    if not os.path.exists(arquivo):
        print("\n[!] Banco de dados não encontrado.")
        return

    consultas = []
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            # Normaliza os nomes das colunas para evitar o KeyError
            reader.fieldnames = [name.strip().upper() for name in reader.fieldnames]
            for linha in reader:
                consultas.append(linha)
    except Exception as e:
        print(f"\n[!] Erro na leitura: {e}")
        return

    if not consultas:
        print("\n[!] O arquivo está vazio.")
        return

    # Tenta encontrar a coluna de Orixá, independente do nome exato
    possiveis_colunas = ['ORIXA', 'ORIXA_REGENTE', 'REGENCIA', 'ORIXA_REGENCIA']
    col_orixa = next((c for c in possiveis_colunas if c in consultas[0]), None)
    
    if not col_orixa:
        print(f"\n[!] Coluna de Orixá não encontrada. Colunas atuais: {list(consultas[0].keys())}")
        return

    # --- PROCESSAMENTO ---
    total = len(consultas)
    cartas = Counter([c.get('CARTA', 'Desconhecida') for c in consultas])
    orixas = Counter([c.get(col_orixa, 'Desconhecido') for c in consultas])

    print("\n" + "=".center(45, "="))
    print(" RELATÓRIO DE SINCRONICIDADE ".center(45, "="))
    print(f"\n[+] TOTAL DE LEITURAS: {total}")
    print(f"\n[+] ORIXÁ MAIS ATIVO: {orixas.most_common(1)[0][0]}")
    print(f"[+] CARTA FREQUENTE: {cartas.most_common(1)[0][0]}")
    
    print("\n" + "[ TENDÊNCIAS DETECTADAS ]".center(45, "-"))
    # Padrão: Orixá -> Carta
    for o, qtd in orixas.items():
        relacionadas = [c.get('CARTA') for c in consultas if c.get(col_orixa) == o]
        mais_provavel = Counter(relacionadas).most_common(1)[0][0]
        print(f" Quando {o:8} rege -> A IA prevê: {mais_provavel}")
    
    print("=".center(45, "="))

if __name__ == "__main__":
    analisar_axe()

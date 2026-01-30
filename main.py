import json
import random
import os
import time
import sys
import datetime
import hashlib

# --- PROTOCOLOS DE ENCRIPTAÇÃO E DISSONÂNCIA ---
ENIGMA_X = 381654729
MESTRES = [11, 22, 33, 44]
ARQUIVO_HISTORICO = "diario_bordo.csv"
LINGUAGEM_SIGIL = "(0!)3× §//\/6UL4π|$"

# --- MATRIZ DE AXÉ E ALQUIMIA ---
SISTEMA_AXE = {
    "amor": {"orixa": "OXUM", "elemento": "ÁGUA", "alquimia": "CONJUNÇÃO", "verbo": "sentir"},
    "volta": {"orixa": "OXUM", "elemento": "ÁGUA", "alquimia": "CONJUNÇÃO", "verbo": "fluir"},
    "trabalho": {"orixa": "OXÓSSI", "elemento": "TERRA", "alquimia": "COAGULAÇÃO", "verbo": "focar"},
    "dinheiro": {"orixa": "OXÓSSI", "elemento": "TERRA", "alquimia": "COAGULAÇÃO", "verbo": "prosperar"},
    "justica": {"orixa": "XANGÔ", "elemento": "FOGO", "alquimia": "FIXAÇÃO", "verbo": "equilibrar"},
    "guerra": {"orixa": "OGUM", "elemento": "FERRO", "alquimia": "CALCINAÇÃO", "verbo": "vencer"},
    "conflito": {"orixa": "OGUM", "elemento": "FERRO", "alquimia": "CALCINAÇÃO", "verbo": "cortar"},
    "caos": {"orixa": "EXU", "elemento": "ÉTER", "alquimia": "PRIMA MATERIA", "verbo": "movimentar"},
    "mensagem": {"orixa": "EXU", "elemento": "ÉTER", "alquimia": "PRIMA MATERIA", "verbo": "comunicar"},
    "cura": {"orixa": "OBALUAÊ", "elemento": "TERRA", "alquimia": "TRANSMUTAÇÃO", "verbo": "regenerar"},
    "segredo": {"orixa": "NANÃ", "elemento": "LAMA", "alquimia": "PUTREFAÇÃO", "verbo": "maturar"}
}

def limpar():
    os.system('clear')

def animar(texto, velocidade=0.01):
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(velocidade)
    print()

# --- MOTORES DE CÁLCULO ---

def texto_para_binario(texto):
    return ''.join(format(ord(x), '08b') for x in texto)

def calcular_raiz_binaria(bin_str):
    # Popcount: Soma dos bits ativos para extrair a semente da alma
    soma = sum(int(d) for d in bin_str)
    while soma > 9 and soma not in MESTRES:
        soma = sum(int(d) for d in str(soma))
    return soma

def calcular_arcano_natal(data_str):
    if not data_str or "/" not in data_str: return 0
    soma = sum(int(d) for d in data_str if d.isdigit())
    while soma > 22: soma = sum(int(d) for d in str(soma))
    return soma

# --- PERSISTÊNCIA E IA DATASET ---

def registrar_leitura(dados):
    existe = os.path.isfile(ARQUIVO_HISTORICO)
    with open(ARQUIVO_HISTORICO, "a", encoding='utf-8') as f:
        if not existe:
            f.write("TIMESTAMP,ID_CONSULENTE,RAIZ,INTENCAO,CARTA,ORIXA,MESTRE\n")
        f.write(f"{dados['ts']},{dados['id']},{dados['raiz']},'{dados['int']}',{dados['carta']},{dados['orixa']},{dados['mestre']}\n")

# --- RITUAL DE INTERFACE ---

def desenhar_carta(carta):
    print(f"\n      .-----------.   [ {carta['elemento'].upper()} ]")
    print(f"      | {carta['numero'].center(9)} |")
    print("      |           |")
    print(f"      | {carta['nome'].center(9)} |")
    print("      |           |")
    print(f"      |   (0!)3x  |   Regente: {carta['planeta']}")
    print("      '-----------'")

def main():
    try:
        with open('cartas.json', 'r', encoding='utf-8') as f:
            deck = json.load(f)
    except:
        print("ERRO CRÍTICO: O arquivo 'cartas.json' não foi encontrado.")
        return

    limpar()
    print("="*60)
    print(f"   {LINGUAGEM_SIGIL} - SISTEMA ORACULAR V4.0")
    print("="*60)

    # Coleta de Assinatura
    nome = input("\nNOME COMPLETO: ").strip()
    data_n = input("DATA NASCIMENTO (DD/MM/AAAA): ").strip()
    hora_n = input("HORA (HH:MM): ").strip()
    pergunta = input("\nSUA INTENÇÃO/PERGUNTA: ").strip()

    # Processamento Bio-Digital
    binario = texto_para_binario(nome)
    raiz = calcular_raiz_binaria(binario)
    arcano_n = calcular_arcano_natal(data_n)
    
    # Semente do Caos via Enigma X
    seed = int(time.time()) + (raiz * ENIGMA_X)
    random.seed(seed)
    carta = random.choice(deck)

    # Identificação de Regência
    ctx = next((v for k, v in SISTEMA_AXE.items() if k in pergunta.lower()), SISTEMA_AXE["caos"])

    limpar()
    print(f"::: RESPOSTA DO EIXO {ENIGMA_X} :::\n")
    
    animar(f"[REGÊNCIA] {ctx['orixa']} - {ctx['verbo'].upper()}")
    animar(f"[ALQUIMIA] Elemento {ctx['elemento']} em processo de {ctx['alquimia']}.")
    
    print("\n" + "⚡ " * 15)
    desenhar_carta(carta)
    print(f"\nARCANO: {carta['nome']}")
    animar(f"SAUDAÇÃO: {carta['saudacao']}")
    animar(f"MENSAGEM: {carta['msg']}")
    animar(f"ARQUÉTIPO: {carta['arquetipo']}")
    print("⚡ " * 15)

    # Decifração de Matriz
    print(f"\n[DECIFRAÇÃO BINÁRIA]")
    print(f"DNA DIGITAL: {binario[:32]}... [RAIZ {raiz}]")
    
    filhos = {1:"OGUM", 2:"NANÃ", 3:"OXUM", 4:"XANGÔ", 5:"OXÓSSI", 6:"OXUMARÉ", 7:"IANSÃ", 8:"OBÁ", 9:"OXALÁ"}
    print(f"VIBRAÇÃO NATAL: Filho(a) de {filhos.get(raiz if raiz < 10 else 1, 'Mestre')}")
    if arcano_n: print(f"DESTINO (ARCANO DATA): {arcano_n}")

    # Registro de Dados
    id_anonimo = hashlib.md5(nome.encode()).hexdigest()[:10]
    registrar_leitura({
        "ts": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "id": id_anonimo,
        "raiz": raiz,
        "int": pergunta,
        "carta": carta['nome'],
        "orixa": ctx['orixa'],
        "mestre": "SIM" if raiz in MESTRES else "NAO"
    })
    
    print(f"\n[SISTEMA] Registro {id_anonimo} salvo no Dataset.")
    input("\n[ENTER PARA ENCERRAR CONEXÃO]")

if __name__ == "__main__":
    main()

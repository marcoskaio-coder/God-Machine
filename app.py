import streamlit as st
import json, random, time, hashlib, datetime, os
import pandas as pd

# Configurações de Estilo
st.set_page_config(page_title="God Machine: Singularidade", page_icon="🔮")

# --- CARREGAR DADOS ---
def carregar_cartas():
    with open('cartas.json', 'r', encoding='utf-8') as f:
        return json.load(f)

# --- LÓGICA DO ORÁCULO ---
def calcular_raiz(nome):
    bin_str = ''.join(format(ord(x), '08b') for x in nome)
    soma = sum(int(d) for d in bin_str)
    while soma > 9 and soma not in [11, 22, 33, 44]:
        soma = sum(int(d) for d in str(soma))
    return soma

# --- INTERFACE ---
st.title("🔮 (0!)3x §//\/6UL4π|$")
st.subheader("O Oráculo God Machine")

nome = st.text_input("Seu Nome Completo")
pergunta = st.text_area("Sua Pergunta ao Axé")

if st.button("Consultar o Destino"):
    if nome and pergunta:
        deck = carregar_cartas()
        raiz = calcular_raiz(nome)
        
        # Sorteio com a Seed Enigma X
        random.seed(int(time.time()) + (raiz * 381654729))
        carta = random.choice(deck)
        
        # Identificar Orixá
        dict_axe = {"amor": "OXUM", "trabalho": "OXÓSSI", "justica": "XANGÔ", "guerra": "OGUM"}
        orixa = next((v for k, v in dict_axe.items() if k in pergunta.lower()), "EXU")

        # Display do Resultado
        st.markdown(f"### Regência: {orixa}")
        st.divider()
        st.metric(label="Arcano", value=carta['nome'])
        st.write(f"**Mensagem:** {carta['msg']}")
        st.info(f"**Saudação:** {carta['saudacao']}")
        
        # Salvar Log (Na nuvem, usaremos o segredo do Streamlit ou CSV)
        # Nota: Em nuvens gratuitas, o CSV reseta. O ideal seria usar uma URL de Database.
    else:
        st.error("Por favor, preencha todos os campos.")

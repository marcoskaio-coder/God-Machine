import streamlit as st
import json, random, time, hashlib, datetime, os

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="GOD MACHINE", page_icon="🔮", layout="centered")

# Estilo CSS para parecer um terminal místico
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #00ff41; }
    .stButton>button { width: 100%; background-color: #2e3136; color: #00ff41; border: 1px solid #00ff41; }
    </style>
    """, unsafe_allow_html=True)

def carregar_cartas():
    with open('cartas.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def calcular_raiz(nome):
    bin_str = ''.join(format(ord(x), '08b') for x in nome)
    soma = sum(int(d) for d in bin_str)
    while soma > 9 and soma not in [11, 22, 33, 44]:
        soma = sum(int(d) for d in str(soma))
    return soma

# --- INTERFACE ---
st.title("📟 (0!)3x §//\/6UL4π|$")
st.markdown("---")
st.write("### BEM-VINDO À SINGULARIDADE")

with st.form("ritual_form"):
    nome = st.text_input("NOME COMPLETO DO CONSULENTE")
    pergunta = st.text_input("SUA INTENÇÃO OU PERGUNTA")
    submit = st.form_submit_button("INICIAR RITUAL DIGITAL")

if submit:
    if nome and pergunta:
        with st.spinner('CALCULANDO MATRIZ DE SINCRONICIDADE...'):
            time.sleep(2)
            deck = carregar_cartas()
            raiz = calcular_raiz(nome)
            
            random.seed(int(time.time()) + (raiz * 381654729))
            carta = random.choice(deck)
            
            dict_axe = {"amor": "OXUM", "trabalho": "OXÓSSI", "justica": "XANGÔ", "guerra": "OGUM"}
            orixa = next((v for k, v in dict_axe.items() if k in pergunta.lower()), "EXU")

        # --- RESULTADO FINAL ---
        st.success(f"REGÊNCIA DETECTADA: {orixa}")
        
        col1, col2 = st.columns([1, 2])
        with col1:
            st.header(f"[{carta['numero']}]")
        with col2:
            st.header(carta['nome'])
        
        st.subheader(f"\"{carta['msg']}\"")
        
        st.divider()
        st.write(f"**Saudação:** {carta['saudacao']}")
        st.write(f"**Elemento:** {carta['elemento']} | **Arquétipo:** {carta['arquetipo']}")
        
        st.caption(f"DNA Digital: Raiz {raiz} | ID: {hashlib.md5(nome.encode()).hexdigest()[:8]}")
    else:
        st.warning("A matriz requer Nome e Pergunta para estabilizar.")

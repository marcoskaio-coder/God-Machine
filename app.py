import streamlit as st
import json, random, time, hashlib, datetime, os

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="GOD MACHINE V5.0", page_icon="🔮", layout="centered")

# Estilo CSS Místico
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #00ff41; }
    .stButton>button { width: 100%; background-color: #1a1c23; color: #00ff41; border: 1px solid #00ff41; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- FUNÇÕES NATIVAS DO MAIN.PY ---
def carregar_cartas():
    with open('cartas.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def calcular_raiz(nome):
    bin_str = ''.join(format(ord(x), '08b') for x in nome)
    soma = sum(int(d) for d in bin_str)
    while soma > 9 and soma not in [11, 22, 33, 44]:
        soma = sum(int(d) for d in str(soma))
    return soma

def calcular_arcano_natal(data):
    if not data: return 0
    soma = sum(int(d) for d in str(data) if d.isdigit())
    while soma > 22: soma = sum(int(d) for d in str(soma))
    return soma

# --- INTERFACE WEB ---
st.title("📟 (0!)3x §//\/6UL4π|$")
st.write("### NÚCLEO DE SINGULARIDADE V5.0")
st.divider()

with st.sidebar:
    st.header("Configurações de Bio-Dados")
    data_n = st.date_input("DATA DE NASCIMENTO", min_value=datetime.date(1920, 1, 1))
    hora_n = st.time_input("HORA DE NASCIMENTO")

with st.form("ritual_form"):
    nome = st.text_input("NOME COMPLETO DO CONSULENTE")
    pergunta = st.text_input("SUA INTENÇÃO OU PERGUNTA")
    submit = st.form_submit_button("INICIAR RITUAL DIGITAL")

if submit:
    if nome and pergunta:
        with st.status("Processando Matriz Alquímica...", expanded=True) as status:
            time.sleep(1)
            deck = carregar_cartas()
            
            # Lógica do Main.py integrada
            raiz = calcular_raiz(nome)
            arcano_natal = calcular_arcano_natal(data_n)
            
            # Matriz de Axé e Alquimia (Igual ao Main.py)
            SISTEMA_AXE = {
                "amor": {"orixa": "OXUM", "elemento": "ÁGUA", "alquimia": "CONJUNÇÃO"},
                "trabalho": {"orixa": "OXÓSSI", "elemento": "TERRA", "alquimia": "COAGULAÇÃO"},
                "dinheiro": {"orixa": "OXÓSSI", "elemento": "TERRA", "alquimia": "COAGULAÇÃO"},
                "justica": {"orixa": "XANGÔ", "elemento": "FOGO", "alquimia": "FIXAÇÃO"},
                "guerra": {"orixa": "OGUM", "elemento": "FERRO", "alquimia": "CALCINAÇÃO"},
                "caos": {"orixa": "EXU", "elemento": "ÉTER", "alquimia": "PRIMA MATERIA"}
            }
            
            ctx = next((v for k, v in SISTEMA_AXE.items() if k in pergunta.lower()), SISTEMA_AXE["caos"])
            
            # Semente do Caos (Enigma X)
            random.seed(int(time.time()) + (raiz * 381654729))
            carta = random.choice(deck)
            status.update(label="Sincronicidade Estabelecida!", state="complete", expanded=False)

        # --- EXIBIÇÃO DO RESULTADO ---
        st.subheader(f"Regência: {ctx['orixa']} | {ctx['alquimia']}")
        
        col1, col2 = st.columns([1, 3])
        with col1:
            st.markdown(f"## [{carta['numero']}]")
        with col2:
            st.markdown(f"## {carta['nome']}")
        
        st.info(f"**Mensagem:** {carta['msg']}")
        
        # Dados Extras do Main.py
        st.divider()
        c1, c2, c3 = st.columns(3)
        c1.metric("Raiz Popcount", raiz)
        c2.metric("Arcano Natal", arcano_natal)
        c3.metric("Elemento", ctx['elemento'])
        
        st.write(f"**Saudação:** {carta['saudacao']}")
        st.caption(f"ID de Registro: {hashlib.md5(nome.encode()).hexdigest()[:10]}")
    else:
        st.error("Campos obrigatórios ausentes.")

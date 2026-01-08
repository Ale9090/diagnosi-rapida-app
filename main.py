import streamlit as st
import pandas as pd

# CONFIGURAZIONE PAGINA
st.set_page_config(page_title="AI Mechanic Pro", layout="centered")

# CSS PER DESIGN NIDO D'APE E LED
st.markdown("""
    <style>
    .stApp {
        background-color: #050a0f;
        color: #00e5ff;
    }
    .stSelectbox, .stNumberInput {
        border: 1px solid #00e5ff;
        border-radius: 5px;
        background-color: #0e1621;
    }
    h1 {
        text-shadow: 0 0 10px #00e5ff;
        text-align: center;
        font-family: 'Courier New', Courier, monospace;
    }
    /* Effetto cornice LED per i risultati */
    .diagnosi-box {
        border: 2px solid #ff0055;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 0 15px #ff0055;
        background-color: #1a0505;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("⬢ DIAGNOSI RAPIDA AUTOMOTIVA ⬢")
st.write("---")

# --- INPUT UTENTE ---
st.subheader("📋 Scheda Veicolo")
col1, col2 = st.columns(2)

with col1:
    tipo = st.selectbox("Alimentazione", ["Diesel", "Benzina", "Ibrida", "GPL"])
    km = st.number_input("Chilometri totali", min_value=0, value=100000)

with col2:
    cilindrata = st.text_input("Cilindrata / Modello", "1.6 MultiJet")
    kw = st.number_input("Potenza (kW)", min_value=0, value=88)

# --- SELEZIONE SINTOMO ---
st.subheader("🔍 Analisi del Sintomo")
problema = st.selectbox("Cosa riscontri?", [
    "Seleziona un'opzione...",
    "Intasamento FAP/DPF",
    "Spia Olio Rossa",
    "Spia Motore Gialla",
    "Taglio Potenza (Recovery)"
])

# --- LOGICA DI RISPOSTA ---
if problema != "Seleziona un'opzione...":
    st.markdown('<div class="diagnosi-box">', unsafe_allow_html=True)
    st.subheader("💡 Verdetto del Tecnico:")
    
    if problema == "Spia Olio Rossa" and km > 80000:
        st.error("ATTENZIONE: Se hai una cinghia a bagno d'olio, il calo di pressione indica la decomposizione della cinghia che intasa la succheruola. NON ACCENDERE IL MOTORE!")
    
    elif problema == "Intasamento FAP/DPF" and tipo == "Diesel":
        st.warning(f"Su un {cilindrata} Diesel con {km} km, l'intasamento è frequente. Prova una rigenerazione forzata o controlla il sensore di pressione differenziale.")
    
    else:
        st.info("Sintomo analizzato. In base ai dati inseriti, è consigliata un'ispezione elettronica tramite presa OBD2.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# --- MONETIZZAZIONE ---
st.write("---")
st.markdown("### 🛠️ Hai bisogno di un'analisi dettagliata?")
st.write("Invia il log della tua diagnosi OBD per una consulenza video personalizzata.")
st.link_button("Prenota Consulenza (PayPal)", "https://paypal.me/tuolink")

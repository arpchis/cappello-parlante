import streamlit as st


st.set_page_config(
    page_title="Il Cappello Parlante di Hogwarts",
    page_icon="🎩",
    layout="centered",
)

# CSS 
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Almendra:ital,wght@0,400;0,700;1,400&family=MedievalSharp&display=swap');

    /* Sfondo Magico con animazione soffusa */
    .stApp {
        background: radial-gradient(circle at center, #1e1e2f 0%, #0a0a0a 100%);
        background-attachment: fixed;
    }

    /* Effetto particelle/fumo magico via CSS */
    .stApp::before {
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background: url('https://www.transparenttextures.com/patterns/stardust.png');
        opacity: 0.3;
        pointer-events: none;
    }

    /* Testi e Titoli */
    h1, h2, h3, p, span, label {
        font-family: 'Almendra', serif !important;
        color: #e0c8a0 !important;
        text-align: center;
    }

    .stTitle {
        font-family: 'MedievalSharp', cursive !important;
        color: #ffd700 !important;
        text-shadow: 0px 0px 15px rgba(255, 215, 0, 0.6);
        font-size: 4rem !important;
        letter-spacing: 3px;
        margin-bottom: 0.5rem !important;
    }

    /* Card della Domanda - Effetto Vetro (Glassmorphism) */
    .question-card {
        background: rgba(30, 20, 10, 0.6);
        backdrop-filter: blur(10px);
        padding: 40px;
        border-radius: 20px;
        border: 1px solid rgba(255, 215, 0, 0.3);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5), inset 0 0 20px rgba(255, 215, 0, 0.05);
        margin-bottom: 30px;
        transition: all 0.5s ease;
    }

    /* Personalizzazione Radio Buttons */
    .stRadio label {
        background: rgba(255, 255, 255, 0.03);
        margin: 8px 0;
        padding: 15px !important;
        border-radius: 12px;
        border: 1px solid rgba(255, 215, 0, 0.1);
        transition: 0.3s;
        display: block;
        cursor: pointer;
    }
    
    .stRadio label:hover {
        background: rgba(255, 215, 0, 0.1);
        border-color: #ffd700;
        transform: translateX(10px);
    }

    /* Pulsante Magico */
    .stButton>button {
        background: linear-gradient(135deg, #4a3721 0%, #2a1f13 100%) !important;
        color: #ffd700 !important;
        border: 1px solid #ffd700 !important;
        border-radius: 50px !important;
        padding: 15px 30px !important;
        font-family: 'MedievalSharp', cursive !important;
        text-transform: uppercase;
        letter-spacing: 2px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.4);
    }

    .stButton>button:hover {
        box-shadow: 0 0 25px rgba(255, 215, 0, 0.4) !important;
        transform: scale(1.02);
        background: #ffd700 !important;
        color: #1a1a1a !important;
    }

   /* Risultato Finale ridimensionato */
    .final-result {
        border: 3px double #ffd700;
        padding: 25px; /* Ridotto da 40px */
        border-radius: 15px;
        background: rgba(0,0,0,0.6);
        max-width: 500px; /* Limita la larghezza massima */
        margin: 0 auto;   /* Centra il box */
    }

    .result-title {
        color: #ffd700 !important; 
        font-size: 2.5rem !important; /* Ridotto da 4rem */
        margin-bottom: 5px !important;
    }

    .result-desc {
        font-size: 1.2rem !important; /* Ridotto da 1.5rem */
        font-style: italic;
        line-height: 1.3;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
    """, unsafe_allow_html=True)

# =================================================================
# DATASET DOMANDE E PUNTEGGI
# =================================================================

def prepara_domande():
    return [
        {
            "testo": "Ti trovi da solo, di notte, in un bosco antico e senti un rumore improvviso tra i cespugli. Come reagisci?",
            "opzioni": [
                "Sguaino la bacchetta e avanzo con decisione verso il rumore.",
                "Mi immobilizzo e cerco di analizzare il rumore per capire di cosa si tratti.",
                "Mi dileguo silenziosamente nell'ombra, osservando da una posizione sicura.",
                "Resto calmo e attendo, pronto ad offrire aiuto a chiunque sia in difficoltà."
            ],
            "punteggi": {0: "Grifondoro", 1: "Corvonero", 2: "Serpeverde", 3: "Tassorosso"}
        },
        {
            "testo": "Quando la tua vita sarà giunta al termine, come vorresti essere ricordato dai posteri?",
            "opzioni": [
                "Come il Coraggioso, colui che ha affrontato ogni pericolo senza esitare.",
                "Come il Saggio, colui la cui conoscenza ha illuminato le tenebre.",
                "Come il Grande, colui che ha lasciato un segno indelebile nel mondo.",
                "Come il Leale, colui che non ha mai abbandonato un amico."
            ],
            "punteggi": {0: "Grifondoro", 1: "Corvonero", 2: "Serpeverde", 3: "Tassorosso"}
        },
        {
            "testo": "Un tuo caro amico ha commesso un errore che potrebbe danneggiare altri. Cosa decidi di fare?",
            "opzioni": [
                "Lo affronto apertamente: l'onestà viene prima di ogni legame personale.",
                "Studio una soluzione logica per rimediare al danno senza far soffrire nessuno.",
                "Cerco il modo più efficace per proteggere il mio amico ed evitare lo scandalo.",
                "Gli resto accanto incondizionatamente, aiutandolo a riparare ai suoi sbagli."
            ],
            "punteggi": {0: "Grifondoro", 1: "Corvonero", 2: "Serpeverde", 3: "Tassorosso"}
        },
        {
            "testo": "Ti viene offerta una scorciatoia magica per ottenere ciò che più desideri, ma a scapito di un altro. Cosa fai?",
            "opzioni": [
                "La rifiuto con sdegno: il vero valore risiede nell'onestà del percorso.",
                "La rifiuto dopo aver analizzato le conseguenze morali e logiche.",
                "La valuto seriamente: a volte il fine giustifica i mezzi per la grandezza.",
                "La rifiuto immediatamente: non potrei mai ferire qualcuno per il mio tornaconto."
            ],
            "punteggi": {0: "Grifondoro", 1: "Corvonero", 2: "Serpeverde", 3: "Tassorosso"}
        },
        {
            "testo": "Qual è la caratteristica che trovi più inaccettabile in una persona?",
            "opzioni": [
                "La codardia: chi non ha il fegato di difendere ciò in cui crede.",
                "L'ignoranza: chi sceglie di restare nel buio rifiutando la verità.",
                "La mediocrità: chi si accontenta di una vita comune senza ambizioni.",
                "La slealtà: chi tradisce la fiducia e il patto di amicizia."
            ],
            "punteggi": {0: "Grifondoro", 1: "Corvonero", 2: "Serpeverde", 3: "Tassorosso"}
        },
        {
            "testo": "Se potessi possedere un unico dono magico tra i seguenti, quale sceglieresti?",
            "opzioni": [
                "Il mantello dell'invisibilità, per agire eroicamente senza essere visto.",
                "La biblioteca infinita, per conoscere ogni segreto dell'universo.",
                "La bacchetta di sambuco, per possedere il potere assoluto.",
                "La pozione della guarigione, per curare e proteggere chi amo."
            ],
            "punteggi": {0: "Grifondoro", 1: "Corvonero", 2: "Serpeverde", 3: "Tassorosso"}
        },
        {
            "testo": "Sei l'unico a conoscere un'ingiustizia commessa da un potente mago. Nessuno ti crederebbe. Cosa fai?",
            "opzioni": [
                "Grido la verità al mondo intero, pronto a subirne le conseguenze.",
                "Ricerco prove inconfutabili per smascherarlo attraverso la logica.",
                "Attendo nell'ombra, accumulando potere per spodestarlo al momento giusto.",
                "Cerco il sostegno di persone fidate per agire con discrezione e bontà."
            ],
            "punteggi": {0: "Grifondoro", 1: "Corvonero", 2: "Serpeverde", 3: "Tassorosso"}
        },
        {
            "testo": "Come preferisci affrontare una sfida estremamente complessa?",
            "opzioni": [
                "Con istinto e determinazione, lanciandomi nell'azione.",
                "Con una pianificazione meticolosa e uno studio approfondito.",
                "Individuando i punti deboli degli avversari a mio vantaggio.",
                "Lavorando duramente, passo dopo passo, con infinita pazienza."
            ],
            "punteggi": {0: "Grifondoro", 1: "Corvonero", 2: "Serpeverde", 3: "Tassorosso"}
        },
        {
            "testo": "Un tuo insegnante ti assegna un compito che sembra impossibile. Qual è il tuo primo pensiero?",
            "opzioni": [
                "È una sfida d'onore: dimostrerò di essere all'altezza.",
                "Devo trovare un metodo alternativo e geniale per risolverlo.",
                "Troverò il modo di trarre vantaggio da questa situazione difficile.",
                "Mi metterò subito al lavoro con costanza, senza lamentarmi."
            ],
            "punteggi": {0: "Grifondoro", 1: "Corvonero", 2: "Serpeverde", 3: "Tassorosso"}
        },
        {
            "testo": "In fondo al tuo cuore, cosa cerchi veramente in questa vita?",
            "opzioni": [
                "Avventura e il coraggio di lottare per una causa giusta.",
                "La comprensione dei misteri che governano il mondo.",
                "L'ascesa verso il successo e il riconoscimento del mio valore.",
                "La pace, la casa e la fedeltà delle persone che amo."
            ],
            "punteggi": {0: "Grifondoro", 1: "Corvonero", 2: "Serpeverde", 3: "Tassorosso"}
        }
    ]

# =================================================================
#  LOGICA DI SESSIONE
# =================================================================

if "punteggi" not in st.session_state:
    st.session_state.punteggi = {"Grifondoro": 0, "Serpeverde": 0, "Corvonero": 0, "Tassorosso": 0}
if "step" not in st.session_state:
    st.session_state.step = 0

def reset():
    st.session_state.punteggi = {"Grifondoro": 0, "Serpeverde": 0, "Corvonero": 0, "Tassorosso": 0}
    st.session_state.step = 0
    st.rerun()

# =================================================================
# UIX
# =================================================================

domande = prepara_domande()

# --- INTRODUZIONE ---
if st.session_state.step == 0:
    st.title("IL CAPPELLO PARLANTE")
    st.markdown("""
    <div style='background: rgba(0,0,0,0.4); padding: 30px; border-radius: 15px; border-left: 5px solid #ffd700; margin-bottom: 20px;'>
        <p style='font-size: 1.8rem; font-style: italic; color: #ffd700 !important;'>
            "Ogni pensiero, per quanto nascosto, sarà dal mio sguardo presto esposto...<br>
            Siediti qui, non aver timore, leggerò nel tuo destino e nel tuo cuore."
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Creiamo tre colonne: quella centrale ospiterà il pulsante
    col1, col2, col3 = st.columns([1, 2, 1]) 
    
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        # Il pulsante ora apparirà centrato rispetto alla pagina
        if st.button("✨ Inizia lo Smistamento ✨", use_container_width=True):
            st.session_state.step = 1
            st.rerun()

# --- FASE QUIZ ---
elif 1 <= st.session_state.step <= 10:
    idx = st.session_state.step - 1
    domanda = domande[idx]
    
    # Barra di progresso
    st.markdown(f"### Prova di Valore {st.session_state.step} di 10")
    st.progress(st.session_state.step / 10)
    
    # Card della domanda
    st.markdown(f"""
    <div class="question-card">
        <h2 style='color: #ffd700; margin-top: 0; line-height: 1.4;'>{domanda['testo']}</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Centriamo i pulsanti delle risposte
    col_a, col_b, col_c = st.columns([1, 4, 1])
    
    with col_b:
        
        # Creiamo un pulsante per ogni opzione
        for i, opzione in enumerate(domanda['opzioni']):
            if st.button(opzione, key=f"btn_{st.session_state.step}_{i}", use_container_width=True):
                # Logica di assegnazione punti
                casata_vincitrice = domanda['punteggi'][i]
                st.session_state.punteggi[casata_vincitrice] += 10
                
                # Avanzamento automatico
                st.session_state.step += 1
                st.rerun()

# --- RISULTATO ---
else:
    casata = max(st.session_state.punteggi, key=st.session_state.punteggi.get)
    simboli = {"Grifondoro": "🦁", "Serpeverde": "🐍", "Corvonero": "🐦‍⬛", "Tassorosso": "🦡"}
    descrizioni = {
        "Grifondoro": "Dimora dei coraggiosi di cuore, dove l'audacia s'intreccia alla nobiltà d'animo.",
        "Serpeverde": "Culla di ambizione e astuzia, dove la volontà domina il destino.",
        "Corvonero": "Orizzonte di sapienza e intelligenza, dove il sapere è legge sovrana.",
        "Tassorosso": "Santuario di lealtà e giustizia, dove il lavoro onesto è vanto dei giusti."
    }
    
    st.balloons()
    
    # Box risultato 
    st.markdown(f"""
    <div class="final-result">
        <h1 class="result-title">{simboli[casata]} {casata.upper()} {simboli[casata]}</h1>
        <p class="result-desc">"{descrizioni[casata]}"</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Grafico leggermente più basso per non occupare troppo spazio
    st.write("#### Equilibrio delle tue virtù:")
    st.bar_chart(st.session_state.punteggi, height=200)
    
    col_r1, col_r2, col_r3 = st.columns([1, 1, 1])
    with col_r2:
        if st.button("Ricomincia", use_container_width=True):
            st.session_state.punteggi = {"Grifondoro": 0, "Serpeverde": 0, "Corvonero": 0, "Tassorosso": 0}
            st.session_state.step = 0
            st.rerun()

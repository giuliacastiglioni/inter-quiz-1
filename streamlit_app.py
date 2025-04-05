import streamlit as st
import time

st.set_page_config(page_title="Quale calciatore dell'Inter sei?", page_icon="⚽", layout="centered")

if "pagina" not in st.session_state:
    st.session_state.pagina = "intro"

if "caricamento" not in st.session_state:
    st.session_state.caricamento = False

def vai_al_quiz():
    st.session_state.caricamento = True
    time.sleep(1.5)
    st.session_state.pagina = "quiz"
    st.session_state.caricamento = False

def torna_home():
    st.session_state.pagina = "intro"

# Pagina INTRO
if st.session_state.pagina == "intro":
    st.markdown("""
        <div style='
            background: linear-gradient(to bottom right, #001f3f, #0074D9);
            padding: 4rem;
            border-radius: 20px;
            text-align: center;
            color: white;
        '>
            <h1 style='font-size: 3em;'>⚫🔵 Quale calciatore dell'Inter sei?</h1>
            <p style='font-size: 1.3em;'>Scopri quale nerazzurro ti rappresenta di più!<br>Rispondi a qualche domanda e trova il tuo gemello in campo.</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    placeholder = st.empty()
    if placeholder.button("Inizia il test 👉", type="primary"):
        with st.spinner("Caricamento domande... 🧐"):
            vai_al_quiz()

# Pagina QUIZ
elif st.session_state.pagina == "quiz":
    st.markdown("<h1 style='text-align: center; color: #001f3f;'>⚫🔵 Quale calciatore dell'Inter sei?</h1>", unsafe_allow_html=True)

    punteggi = {
        "Lautaro Martinez": 0,
        "Nicolò Barella": 0,
        "Yann Sommer": 0,
        "Federico Dimarco": 0,
        "Hakan Çalhanoğlu": 0,
        "Alessandro Bastoni": 0,
        "Denzel Dumfries": 0,
        "Marcus Thuram": 0
    }

    domande = [
        {
            "domanda": "1. Cosa ti descrive meglio?",
            "opzioni": [
                ("Leader silenzioso", "Lautaro Martinez"),
                ("Instancabile e passionale", "Nicolò Barella"),
                ("Freddo e affidabile", "Yann Sommer"),
                ("Tifoso in campo", "Federico Dimarco"),
                ("Regista elegante", "Hakan Çalhanoğlu"),
                ("Difensore con visione", "Alessandro Bastoni"),
                ("Forza e velocità", "Denzel Dumfries"),
                ("Tecnico e imprevedibile", "Marcus Thuram"),
            ]
        },
        {
            "domanda": "2. Qual è il tuo punto forte?",
            "opzioni": [
                ("Finalizzazione", "Lautaro Martinez"),
                ("Resistenza", "Nicolò Barella"),
                ("Posizionamento", "Yann Sommer"),
                ("Cross precisi", "Federico Dimarco"),
                ("Controllo del gioco", "Hakan Çalhanoğlu"),
                ("Anticipo e passaggi", "Alessandro Bastoni"),
                ("Accelerazione", "Denzel Dumfries"),
                ("Dribbling e fantasia", "Marcus Thuram"),
            ]
        },
        {
            "domanda": "3. Cosa fai dopo una vittoria?",
            "opzioni": [
                ("Resto concentrato", "Yann Sommer"),
                ("Carico i compagni", "Nicolò Barella"),
                ("Esulto sotto la curva", "Federico Dimarco"),
                ("Penso già alla prossima", "Hakan Çalhanoğlu"),
                ("Festeggio con stile", "Marcus Thuram"),
                ("Mando un messaggio alla squadra", "Lautaro Martinez"),
                ("Faccio gruppo", "Denzel Dumfries"),
                ("Mi riguardo le azioni", "Alessandro Bastoni"),
            ]
        },
        {
            "domanda": "4. Qual è il tuo motto?",
            "opzioni": [
                ("Parlo coi fatti", "Lautaro Martinez"),
                ("Sempre a tutta!", "Nicolò Barella"),
                ("Testa fredda, cuore caldo", "Yann Sommer"),
                ("Nato per questi colori", "Federico Dimarco"),
                ("Controllo e visione", "Hakan Çalhanoğlu"),
                ("Dietro ma decisivo", "Alessandro Bastoni"),
                ("Spinta continua", "Denzel Dumfries"),
                ("Creatività in corsa", "Marcus Thuram"),
            ]
        },
        {
            "domanda": "5. Come ti vesti fuori dal campo?",
            "opzioni": [
                ("Elegante sobrio", "Yann Sommer"),
                ("Casual chic", "Lautaro Martinez"),
                ("Sportivo comodo", "Nicolò Barella"),
                ("Minimal ma di classe", "Alessandro Bastoni"),
                ("Streetwear nerazzurro", "Federico Dimarco"),
                ("Giacca e stile", "Hakan Çalhanoğlu"),                
                ("Look atletico", "Denzel Dumfries"),
                ("Sempre fashion", "Marcus Thuram"),
            ]
        },        
        {
            "domanda": "6. Come ti comporti durante un allenamento?",
            "opzioni": [
                ("Spingo sempre al massimo, voglio migliorare ogni giorno.", "Lautaro Martinez"),
                ("Cerco di perfezionare ogni mio movimento, come un maestro.", "Alessandro Bastoni"),
                ("Siamo una squadra, mi piace lavorare in gruppo.","Federico Dimarco"),
                ("Faccio riscaldamento e stretching, prima di spingere forte.", "Yann Sommer"),
                ("Studio il mio avversario, voglio sapere tutto sui suoi punti deboli.", "Hakan Çalhanoğlu" ),
                ("Cerco di divertirmi e mantenere l’atmosfera leggera.", "Marcus Thuram"),
                ("Mi alleno intensamente, ma mi prendo anche momenti per scherzare.","Nicolò Barella" ),
                ("Mi concentro su ciò che devo migliorare, senza distrazioni.", "Denzel Dumfries"),
            ]
        },
        {
            "domanda": "7.  Come reagisci quando la partita è difficile e la tua squadra sta perdendo?",
            "opzioni": [
                ("Mi concentro ancora di più, non smetto mai di lottare.", "Nicolò Barella"),
                ("Continuo a lavorare in silenzio, non voglio che la mia frustrazione si noti.", "Lautaro Martinez"),
                ("Cerco di restare calmo e fare il mio gioco senza farmi distrarre.", "Yann Sommer"),
                ("Mi faccio sentire in campo, alzo la voce per motivare i compagni.", "Federico Dimarco"),
                ("Provo a fare il giocatore decisivo, è il momento giusto per un cambio di ritmo.", "Hakan Çalhanoğlu"),
                ("Incito la squadra a non mollare mai, non è finita finché non suona il fischio finale.", "Alessandro Bastoni"),
                ("Cerco di prendermi una pausa mentale, mi concentro su ogni singola azione.", "Denzel Dumfries"),
                ("Mi impegno ancora di più, so che una partita può cambiare in un attimo.", "Marcus Thuram"),
            ]
        },
        {
            "domanda": "8. Come reagisci quando segni un gol?",
            "opzioni": [
                ("Pugno in aria e occhi pieni di grinta, il gol è solo l'inizio.", "Federico Dimarco"),
                ("Faccio un gesto discreto, mi inchino alla mia squadra.", "Yann Sommer"),
                ("Corro verso la curva con le mani alzate, grido a squarciagola!", "Lautaro Martinez"),
                ("Esulto con il gruppo, il gol è il frutto del lavoro di squadra.","Nicolò Barella" ),
                ("Mi inginocchio e faccio un segno di ringraziamento.", "Hakan Çalhanoğlu"),
                ("Mi metto le mani sulla testa e guardo verso il cielo, pensando alla squadra.", "Alessandro Bastoni"),
                ("Scivolo sul ginocchio, come un’esultanza da campione.", "Marcus Thuram"),
                ("Faccio un salto con un’espressione da guerriero, sono pronto per la guerra!", "Denzel Dumfries"),
            ]
        },
        {
            "domanda": "9. Se potessi scegliere un superpotere, quale sceglieresti?",
            "opzioni": [
                ("Teletrasporto, così posso essere ovunque al momento giusto.", "Lautaro Martinez"),
                ("Super velocità, voglio essere il più veloce in campo.", "Nicolò Barella"),
                ("Leggerezza, posso saltare e volare più in alto di tutti.", "Yann Sommer"),
                ("Super intelligenza, per leggere il gioco come un campione.", "Hakan Çalhanoğlu"),
                ("Invisibilità, per fare il mio gioco senza che gli avversari mi vedano.", "Federico Dimarco"),
                ("Super forza, nessun avversario mi supera.", "Alessandro Bastoni"),
                ("Super resistenza, per correre senza fermarmi mai.", "Denzel Dumfries"),
                ("Volare, per superare gli ostacoli più facilmente.", "Marcus Thuram"),
            ]
        },
        {
            "domanda": "10. Se fossi un cibo, quale saresti?",
            "opzioni": [
                ("Una pizza margherita, semplice ma iconica.", "Lautaro Martinez"),
                (" Un bel piatto di pasta, sempre pronto a dare energia.", "Nicolò Barella"),
                ("Un'insalata leggera, ma nutriente.", "Yann Sommer"),
                ("Un dolce al cioccolato, per quando ho bisogno di energia extra.", "Federico Dimarco"),
                ("Un gelato, sempre pronto a regalare un sorriso.", "Denzel Dumfries"),
                ("Un piatto di sushi, elegante e sempre in movimento.", "Alessandro Bastoni"),
                ("Un kebab, il comfort food per eccellenza.", "Hakan Çalhanoğlu"),
                ("Un panino con hamburger, sostanzioso e pronto a nutrire.", "Marcus Thuram"),
            ]
        },
        {
            "domanda": "11. Quale animale ti rappresenta meglio?",
            "opzioni": [
                
                ("Un cane, per la mia fedeltà e impegno.", "Nicolò Barella"),
                ("Un delfino, per la mia agilità e intelligenza.", "Hakan Çalhanoğlu"),
                ("Un'aquila, per la mia visione e capacità di adattarmi.", "Yann Sommer"),
                (" Un leone, per la mia forza e determinazione.", "Lautaro Martinez"),
                ("Un elefante, per la mia forza tranquilla e la presenza in campo.", "Federico Dimarco"),
                ("Un puma, per la mia agilità e determinazione.", "Marcus Thuram"),
                ("Un gufo, per la mia saggezza e precisione.", "Alessandro Bastoni"),
                ("Un cavallo, per la mia velocità e resistenza.", "Denzel Dumfries"),
            ]
         },        
         {
            "domanda": "12. Qual è il tuo tipo di caffè preferito?",
            "opzioni": [
                ("Un espresso forte, senza fronzoli, mi sveglia subito!", "Nicolò Barella"),
                ("Un caffè con latte, per quando voglio qualcosa di morbido e confortante.", "Yann Sommer"),
                ("Un caffè decaffeinato, per quando voglio il gusto senza l'effetto stimolante.", "Federico Dimarco"),
                (" Un cappuccino cremoso, dolce e avvolgente, per iniziare la giornata con calma.", "Lautaro Martinez"),
                ("Un caffè nero, intenso e deciso, niente mezze misure.", "Hakan Çalhanoğlu"),
                ("Un caffè freddo, per quando voglio qualcosa di rinfrescante e diverso.", "Marcus Thuram"),
                ("Un macchiato, una via di mezzo tra dolce e forte, sempre equilibrato.", "Alessandro Bastoni"),
                ("Un caffè americano, lungo e rinfrescante, per quando ho bisogno di carburante extra.", "Denzel Dumfries"),
                
            ]
        },
        {
            "domanda": "Finale. Giulia, la creatrice di questo quiz, cosa fa quando non sta creando quiz su calciatori?",
            "opzioni": [
                ("Disegna cose a caso e le manda alle sue amiche.","Nicolò Barella"),
                ("Si perde a guardare video di formula 1 su Internet, ovviamente.","Federico Dimarco"),
                (" Colleziona tazze di caffè vuote per fare un museo.", "Yann Sommer"),
                ("Si allena con il trike e diventa un’esperta di acrobazie.", "Lautaro Martinez"),
                ("Scivola sul pavimento di casa con le calze antiscivolo come se fosse un’ala.", "Hakan Çalhanoğlu"),
                ("Si traveste da allenatore di calcio e fa finta di essere il capo della squadra.", "Alessandro Bastoni"),
                ("Organizza una maratona di serie TV, senza interruzioni, solo snack.", "Denzel Dumfries"),
                ("Insegna a sua sorella a giocare a calcio, ma lei non è molto brava.", "Marcus Thuram"),
            ]
        },
    ]

    for d in domande:
        st.markdown(f"### {d['domanda']}")
        risposta = st.radio("", [opt[0] for opt in d["opzioni"]], key=d["domanda"])
        for testo, giocatore in d["opzioni"]:
            if risposta == testo:
                punteggi[giocatore] += 1

    if st.button("🏆 Scopri chi sei!"):
        giocatore = max(punteggi, key=punteggi.get)

        descrizioni = {
            "Lautaro Martinez": "Grinta, leadership e tanti gol. Sei il Toro dell'Inter!",
            "Nicolò Barella": "Energia pura, cuore e passione. Sei l’anima del centrocampo!",
            "Yann Sommer": "Sempre freddo e lucido. Una roccia tra i pali.",
            "Federico Dimarco": "Nerazzurro nel sangue. Un sinistro che canta!",
            "Hakan Çalhanoğlu": "Intelligenza tattica e piedi educati. Sei il cervello della squadra.",
            "Alessandro Bastoni": "Difensore moderno, elegante e sempre attento.",
            "Denzel Dumfries": "Potenza e spinta sulla fascia. Sei imprendibile!",
            "Marcus Thuram": "Fantasia, fisico e tanta classe. L'attacco è il tuo regno!"
        }

        immagini = {
            "Lautaro Martinez": "https://editorial.uefa.com/resources/0281-18077e90b09c-34e04cb3012e-1000/fc_internazionale_v_ac_milan_semi-final_second_leg_-_uefa_champions_league.jpeg",
            "Nicolò Barella": "https://th.bing.com/th/id/OIP.dmGOuN6EvRM8LRYbXF3RYgHaFq?rs=1&pid=ImgDetMain",
            "Yann Sommer": "https://st1.uvnimg.com/50/d5/09aadcfe4892a8d4871877cdd306/yann-sommer-bayern-munich.jpg",
            "Federico Dimarco": "https://th.bing.com/th/id/OIP.77WuVTSHp1-PgUQyUh5lZAHaFF?rs=1&pid=ImgDetMain",
            "Hakan Çalhanoğlu": "https://icdn.sempreinter.com/wp-content/uploads/2024/04/Hakan-Calhanoglu-Inter-Milan-2.jpg",
            "Alessandro Bastoni": "https://sportal.eu/wp-content/uploads/2023/03/bastoni-inter_11987001190x786.jpg",
            "Denzel Dumfries": "https://cdn1.unitedinfocus.com/uploads/14/2022/06/GettyImages-1398681168-scaled.jpg",
            "Marcus Thuram": "https://icdn.sempreinter.com/wp-content/uploads/2023/10/Inter-Milan-Marcus-Thuram-10-scaled.jpg"
        }

        st.markdown("---")
        st.markdown(f"<h2 style='text-align: center;'>🥳 Sei {giocatore}! 🥳</h2>", unsafe_allow_html=True)

        # Emojis e testuale grafico
        st.markdown("""
            <div style='font-size: 2em; text-align: center;'>🎉🎉🎉</div>
        """, unsafe_allow_html=True)

        # GIF esultanza
        gif_url = "https://media1.tenor.com/m/FFGP5kg4f_AAAAAC/simone-inzaghi.gif"
        st.image(gif_url, caption="YAY!!!", use_container_width=True)

        # Descrizione giocatore
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(immagini[giocatore], use_container_width=True)
        with col2:
            st.markdown(f"<div style='padding: 1rem; background-color: #e6f2ff; border-left: 5px solid #001f3f; font-size: 1.2em;'>{descrizioni[giocatore]}</div>", unsafe_allow_html=True)

        # Anima la celebrazione
        st.balloons()

        # Pulsante per tornare alla home
        st.button("↩️ Torna alla home", on_click=torna_home)

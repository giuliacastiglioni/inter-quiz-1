import streamlit as st
import time

st.set_page_config(page_title="Quiz!!!", page_icon="⚽", layout="centered")

# Imposta la sessione per tenere traccia della pagina corrente
if "pagina" not in st.session_state:
    st.session_state.pagina = "home"

if "caricamento" not in st.session_state:
    st.session_state.caricamento = False

def vai_al_quiz_inter():
    st.session_state.caricamento = True
    time.sleep(1.5)
    st.session_state.pagina = "quiz_inter"
    st.session_state.caricamento = False

def vai_al_quiz_piloti():
    st.session_state.caricamento = True
    time.sleep(1.5)
    st.session_state.pagina = "quiz_piloti"
    st.session_state.caricamento = False

def vai_al_quiz_canzoni():
    st.session_state.caricamento = True
    time.sleep(1.5)
    st.session_state.pagina = "quiz_canzoni"
    st.session_state.caricamento = False

def vai_al_quiz_1D():
    st.session_state.caricamento = True
    time.sleep(1.5)
    st.session_state.pagina = "quiz_1D"
    st.session_state.caricamento = False

def vai_al_quiz_allenatori():
    st.session_state.caricamento = True
    time.sleep(1.5)
    st.session_state.pagina = "quiz_allenatori"
    st.session_state.caricamento = False

def vai_al_quiz_calciatrici():
    st.session_state.caricamento = True
    time.sleep(1.5)
    st.session_state.pagina = "quiz_calciatrici"
    st.session_state.caricamento = False

def vai_al_quiz_cocomere():
    st.session_state.caricamento = True
    time.sleep(1.5)
    st.session_state.pagina = "quiz_cocomere"
    st.session_state.caricamento = False

def torna_home():
    st.session_state.pagina = "home"

# Pagina HOME
if st.session_state.pagina == "home":
    st.markdown("""
        <div style='background: linear-gradient(to bottom right, #001f3f, #0074D9); padding: 4rem; border-radius: 20px; text-align: center; color: white;'>
            <h1 style='font-size: 3em;'>Scegli il tuo quiz!</h1>
            <p style='font-size: 1.3em;'>Benvenuto! Puoi scegliere di fare tanti quiz e test diversi! Giulia non ha niente da fare nella vita! </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
        <style>
        .stButton>button {
            font-size: 30px;
            padding: 24px;
            margin: 10px;
            width: 100%;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
        }
        .stButton>button:hover {
            background-color: #0056b3;
        }
        </style>
        """, unsafe_allow_html=True
    )
    # Pulsanti per scegliere il quiz
    if st.button("Quale calciatore dell'Inter sei?    👉"):
        with st.spinner("Caricamento quiz... 🧐"):
            vai_al_quiz_inter()

    if st.button("Quale pilota di Formula 1 sei?    👉"):
        with st.spinner("Caricamento quiz... 🧐"):
            vai_al_quiz_piloti()

    if st.button("Quale canzone dei 1D sei?    👉"):
        with st.spinner("Caricamento quiz... 🧐"):
            vai_al_quiz_canzoni()

    if st.button("Che cantante degli One Direction sei?    👉"):
        with st.spinner("Caricamento quiz... 🧐"):
            vai_al_quiz_1D()

    if st.button("Quale allenatore del VJ Open Femminile sei?    👉"):
        with st.spinner("Caricamento quiz... 🧐"):
            vai_al_quiz_allenatori()

    if st.button("Quale calciatrice del VJ Open Femminile sei?    👉"):
        with st.spinner("Caricamento quiz... 🧐"):
            vai_al_quiz_calciatrici()

    if st.button("Quale cocomera sei?    👉"):
        with st.spinner("Caricamento quiz... 🧐"):
            vai_al_quiz_cocomere()

# Pagina QUIZ INTER
elif st.session_state.pagina == "quiz_inter":
    # Inserisci qui il codice del quiz sull'Inter che hai già scritto
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
            "domanda": "Giulia, la creatrice di questo quiz, cosa fa quando non sta creando quiz su calciatori?",
            "opzioni": [
                ("Disegna cose a caso e le manda alle sue amiche.","Nicolò Barella"),
                ("Si perde a guardare video di formula 1 su Internet, ovviamente.","Federico Dimarco"),
                (" Colleziona tazze di caffè vuote per fare un museo.", "Yann Sommer"),
                ("Si allena con il trike e diventa un’esperta di acrobazie.", "Lautaro Martinez"),
                ("Suona canzoni a caso e le posta su instagram senza successo.", "Hakan Çalhanoğlu"),
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
    
    pass  # Mantieni il codice già esistente per il quiz dell'Inter
# Pagina QUIZ PILOTI
elif st.session_state.pagina == "quiz_piloti":
    # Inserisci qui il codice del quiz sull'Inter che hai già scritto
    st.markdown("<h1 style='text-align: center; color: #001f3f;'>⚫ Quale pilota di Formula 1 sei?🔴 </h1>", unsafe_allow_html=True)

    punteggi_piloti = {
        "Verstappen": 0,
        "Leclerc": 0,
        "Norris": 0,
        "Piastri": 0,
        "Kimi Antonelli": 0,
        "Alonso": 0,
        "Hamilton": 0,
        "Sainz": 0
    }

    domande_piloti = [
        {
            "domanda": "1. Sei in una serata con amici e ti chiedono di scegliere il karaoke. Qual è la tua mossa?",
            "opzioni": [
                ("Prendo il microfono senza pensarci due volte e faccio un'entrata trionfale!", "Verstappen"),
                ("Mi prendo un momento per osservare e poi, quando tutti sono distratti, spacco con una canzone classica!", "Hamilton"),
                ("Sto calmo all'inizio, ma quando arrivo sul palco do il massimo! Una performance da ricordare!", "Leclerc"),
                ("Non sono sicuro, ma mi faccio influenzare dal gruppo. Se tutti si divertono, mi unisco!", "Sainz"),
                ("Non sono il tipo che si lancia subito, ma se c'è una canzone che mi piace, la faccio mia!", "Norris"),
                ("Mi prendo il mio tempo, e quando decido, vado a tutta birra. Nessuno si aspetta il mio gran finale!", "Piastri"),
                ("Accetto la sfida, ma prima osservo gli altri. Mi piace tenere un basso profilo, poi arrivo!", "Kimi Antonelli"),
                ("Se qualcuno canta una canzone epica, mi unisco immediatamente, non posso restare a guardare!", "Alonso")
            ]
        },

        {
            "domanda": "2. Immagina di avere una giornata libera e puoi fare qualsiasi cosa. Cosa scegli?",
            "opzioni": [
                ("Esploro nuove città, mi piace scoprire luoghi e assaporare la cultura locale!", "Leclerc"),
                ("Mi lancio in una sfida sportiva, magari una gara di go-kart o una partita di tennis!", "Verstappen"),
                ("Mi rilasso e passo una giornata tranquilla, magari con un libro e una buona tazza di tè.", "Norris"),
                ("Lavoro su qualcosa di nuovo, ma lo faccio sempre con passione e concentrazione.", "Piastri"),
                ("Mi concedo una giornata di puro relax con gli amici, un buon film e magari una pizza!", "Sainz"),
                ("Preferisco stare in compagnia, fare quattro chiacchiere e godermi un buon pranzo.", "Alonso"),
                ("Faccio un'escursione in montagna per staccare la mente e ricaricare le energie.", "Kimi Antonelli"),
                ("Vado a fare un giro in bici per la città, mi piace sentirsi libero e in movimento.", "Hamilton")
            ]
        },

        {
            "domanda": "3. Sei al supermercato, ma il carrello è già pieno e non sai cosa comprare di più. Qual è la tua scelta finale?",
            "opzioni": [
                ("Non c'è alcun dubbio! Più snack per tutti, dobbiamo fare scorta!", "Verstappen"),
                ("Scelgo con calma, ma sempre con la qualità. Frutta, verdura e qualche dolcetto, non si sa mai!", "Leclerc"),
                ("Vado sul sicuro: prodotti pratici e veloci, niente di troppo complicato!", "Norris"),
                ("Metto qualcosa di esotico, qualcosa che non avrei mai pensato, ma che potrebbe sorprendere.", "Piastri"),
                ("Penso ai miei amici e compro sempre qualcosa che possa fare felici tutti!", "Sainz"),
                ("Prendo solo ciò che mi serve per una settimana comoda, niente sprechi!", "Hamilton"),
                ("Cerco qualcosa di diverso, un po' di cultura gastronomica in più!", "Alonso"),
                ("Mi faccio coinvolgere dall'atmosfera e prendo qualche snack extra per fare festa!", "Kimi Antonelli")
            ]
        },

        {
            "domanda": "4. Se potessi inventare una nuova regola per il mondo, quale sarebbe?",
            "opzioni": [
                ("Ogni settimana deve esserci un giorno in cui tutte le scuole e i lavori sono chiusi per una giornata di relax!", "Hamilton"),
                ("Ogni viaggio deve essere un'avventura, quindi bisogna fermarsi sempre a fare una foto in ogni angolo.", "Leclerc"),
                ("Una giornata di pura creatività, dove tutti devono inventare una nuova invenzione o gioco ogni anno!", "Verstappen"),
                ("Voglio un mondo in cui le sfide siano sempre giuste e ogni individuo possa esprimere la sua unicità.", "Piastri"),
                ("Farei in modo che ogni mattina inizi con un'ora di esercizio fisico per tutti, per cominciare la giornata al massimo!", "Norris"),
                ("Ogni tanto dobbiamo fermarci e riflettere su quanto siamo fortunati. Una giornata di gratitudine ogni mese.", "Sainz"),
                ("Che nessuna gara sia mai decisa prima del tempo. Tutto può cambiare in un attimo!", "Alonso"),
                ("La musica deve essere il cuore di ogni incontro. Dobbiamo sempre suonare un po' di musica!", "Kimi Antonelli")
            ]
        },

        {
            "domanda": "5. Se fossi un supereroe, quale sarebbe il tuo superpotere?",
            "opzioni": [
                ("La capacità di volare e andare ovunque voglio in un batter d'occhio!", "Verstappen"),
                ("La supervelocità! Ogni cosa che faccio deve essere fatta velocemente e con stile.", "Hamilton"),
                ("L'invisibilità. A volte è meglio stare dietro le quinte e osservare senza essere visto.", "Norris"),
                ("Il superdono! Aiutare gli altri è il mio superpotere segreto.", "Sainz"),
                ("La telecinesi, in modo da poter fare mille cose contemporaneamente!", "Leclerc"),
                ("La superintelligenza, per risolvere qualsiasi problema in un attimo.", "Piastri"),
                ("Il potere di fermare il tempo, per potermi rilassare quando voglio.", "Alonso"),
                ("La capacità di risolvere qualsiasi situazione con una risata!", "Kimi Antonelli")
            ]
        },
        {
            "domanda": "6. Immagina di essere in un film d'azione: quale sarebbe il tuo superpotere completamente inutile ma divertente?",
            "opzioni": [
                ("Il potere di apparire e scomparire ogni volta che qualcuno pronuncia il mio nome, tipo magico ma inutile!", "Verstappen"),
                ("Essere sempre in grado di fare un'entrata trionfale, con tanto di effetti speciali, ma solo per entrare in un negozio!", "Leclerc"),
                ("Controllare il traffico con il mio sguardo. Peccato che non mi serva mai, visto che mi piace sempre arrivare in ritardo!", "Hamilton"),
                ("Il potere di creare una pila infinita di cuscini, così posso sempre addormentarmi in ogni situazione!", "Norris"),
                ("Essere in grado di fare le pernacchie a distanza per distrarre chiunque, in qualsiasi momento!", "Piastri"),
                ("La capacità di ordinare sempre il gelato sbagliato, ma continuare a mangiarlo con entusiasmo!", "Sainz"),
                ("Il potere di far partire una canzone romantica ogni volta che faccio un passo, come se fossi in un musical!", "Kimi Antonelli"),
                ("Fare apparire una pioggia di confetti ogni volta che dico una battuta, anche se nessuno la trova divertente!", "Alonso")
            ]
        },

        {
            "domanda": "7. Se potessi inventare un nuovo sport da praticare in pista, quale sarebbe?",
            "opzioni": [
                ("Gara di karaoke a 300 km/h, con un microfono gigante che ti fa cantare a tutto volume mentre corri!", "Verstappen"),
                ("Competizione di salto con la corda in macchina, ma solo se la corda è fatta di spaghetti!", "Leclerc"),
                ("Una corsa a chi riesce a mangiare più pizza mentre guida, e il premio è una pizza gigante!", "Hamilton"),
                ("Un rally di go-kart in cui l'obiettivo è non ridere mentre gli altri piloti fanno battute", "Norris"),
                ("Una sfida di velocità ma con uno scooter elettrico, perché perché no?", "Piastri"),
                ("Fuga da una pioggia di popcorn giganti, e l'unico modo per vincere è non farsi travolgere!", "Sainz"),
                ("Sfidarsi a chi riesce a fare più acrobazie in macchina mentre ascolta la musica disco!", "Kimi Antonelli"),
                ("Una gara di velocità in cui, a ogni curva, la macchina cambia colore, ma nessuno sa perché!", "Alonso")
            ]
        },

        {
            "domanda": "8. Se ti trovassi in una stanza piena di cuscini, quale sarebbe la tua reazione?",
            "opzioni": [
                ("Mi tuffo subito dentro, perché un buon cuscino è la mia dimensione naturale!", "Verstappen"),
                ("Mi trovo un angolino tranquillo e mi faccio un pisolino. Non c'è posto migliore per un relax veloce.", "Hamilton"),
                ("Mi fingo un'ombra e inizio a fare capriole, giusto per vedere chi mi segue.", "Leclerc"),
                ("Prendo un cuscino, faccio finta di essere un ninja e inizio a fare colpi di karate!", "Norris"),
                ("Vedo una montagna di cuscini e la prima cosa che faccio è creare un fortino!", "Piastri"),
                ("Lancio un cuscino come se fosse una palla da rugby, ma senza alcuna coordinazione!", "Sainz"),
                ("Faccio una montagna di cuscini e poi prendo un selfie, perché è troppo fotogenico!", "Kimi Antonelli"),
                ("Mi sdraio e mi faccio una mini sessione di meditazione, ma il cuscino diventa il mio miglior amico.", "Alonso")
            ]
        },

        {
            "domanda": "9. Se dovessi partecipare a un talent show, quale sarebbe la tua esibizione?",
            "opzioni": [
                ("Ballerei un tango super elegante, ma alla fine inciamperei su una scarpa!", "Verstappen"),
                ("Mi esibisco in una performance di mimesi: imito un pilota di F1, ma ogni movimento è esagerato!", "Leclerc"),
                ("Farei un monologo divertente dove parlo di come guidare con stile mentre bevo una tazza di tè.", "Hamilton"),
                ("Canto una canzone pop a squarciagola, ma con un microfono che non funziona mai!", "Norris"),
                ("Improvviso una performance da ballerino e la concludo con una coreografia strana e assurda!", "Piastri"),
                ("Eseguo una danza ritmica con un pallone da calcio, cercando di non farlo cadere.", "Sainz"),
                ("Mimerei le reazioni di un pilota durante una gara, aggiungendo dei colpi di scena esagerati.", "Kimi Antonelli"),
                ("Racconterei un'epica storia di come ho vinto una gara, ma con tanto di effetti speciali e drammatizzazione!", "Alonso")
            ]
        },

        {
            "domanda": "10. Se dovessi scegliere il tuo 'superpotere' per affrontare la vita quotidiana, quale sarebbe?",
            "opzioni": [
                ("Il potere di dormire 10 ore in un minuto, così posso affrontare la giornata con la giusta energia.", "Verstappen"),
                ("Il potere di avere sempre la risposta giusta quando qualcuno ti fa una domanda strana!", "Leclerc"),
                ("Il potere di fare sparire tutto ciò che è in disordine, specialmente quando sono in ritardo!", "Hamilton"),
                ("Il potere di fare il caffè perfetto, indipendentemente da dove mi trovo!", "Norris"),
                ("Il potere di fare il doppio dei compiti in metà tempo, così posso passare più tempo a divertirmi!", "Piastri"),
                ("Il potere di non sbagliare mai una freccia quando guido, senza mai farmi perdere!", "Sainz"),
                ("Il potere di parlare con gli animali e chiedere loro consigli sulla vita!", "Kimi Antonelli"),
                ("Il potere di teletrasportarmi in qualsiasi posto dove c'è una festa!", "Alonso")
            ]
        },
        {
            "domanda": "Se Giulia fosse una pit stop in una gara di F1, come sarebbe?",
            "opzioni": [
                ("Super veloce, tutto perfetto e con un tocco di precisione in ogni mossa!", "Leclerc"),
                ("Un po' imprevedibile, ma comunque efficace, riesce sempre a sorprendere!", "Verstappen"),
                ("Un pit stop pieno di energia positiva, con un sorriso che illumina tutto!", "Norris"),
                ("Il pit stop più creativo di sempre, con qualche mossa fuori dal comune.", "Piastri"),
                ("Elegante e preciso, anche sotto pressione, è sempre tutto sotto controllo.", "Hamilton"),
                ("Rapido ma un po' misterioso, lascia tutti a chiedersi come abbia fatto.", "Kimi Antonelli"),
                ("Un pit stop che sa adattarsi a qualsiasi situazione, sempre con determinazione.", "Sainz"),
                ("Flessibile e reattiva, trova sempre la giusta strategia per rimettersi in pista!", "Alonso")
            ]
        }
    ]

    for d in domande_piloti:
        st.markdown(f"### {d['domanda']}")
        risposta = st.radio("", [opt[0] for opt in d["opzioni"]], key=d["domanda"])
        for testo, pilota in d["opzioni"]:
            if risposta == testo:
                punteggi_piloti[pilota] += 1

    if st.button("🏆 Scopri chi sei!"):
        pilota = max(punteggi_piloti, key=punteggi_piloti.get)

        descrizioni = {
            "Verstappen": "Sei una persona determinata, che non si ferma mai davanti agli ostacoli. Hai una mentalità da vincente, sempre focalizzato sull'obiettivo, e ogni volta che scendi in campo dimostri che la tua concentrazione è imparagonabile.",
            "Leclerc": "La tua velocità è sorprendente, proprio come quella di un pilota che ama superare i limiti. Sei un mix di talento naturale e passione inarrestabile, sempre pronto a dare il massimo, anche nelle sfide più difficili.",
            "Norris": "Hai una personalità che conquista tutti! La tua energia è contagiosa e non hai paura di far vedere il tuo lato più simpatico. La tua freschezza e spontaneità ti rendono uno dei piloti più amati dal pubblico.",
            "Piastri": "La tua calma e lucidità ti permettono di affrontare ogni situazione con estrema precisione. Sei pronto a raccogliere i frutti del tuo lavoro duro, e la tua costanza ti porterà sicuramente lontano.",
            "Alonso": "Con una mentalità da veterano, sei un pilota che sa come sfruttare ogni occasione. Non ti arrendi mai e la tua esperienza è la chiave del tuo successo, anche nelle circostanze più difficili.",
            "Sainz": "Con un mix perfetto di determinazione e agilità mentale, sei un pilota che sa sempre come adattarsi. La tua strategia è sempre sul pezzo, e sai fare la differenza quando è necessario.",
            "Hamilton": "Eleganza, talento e una dedizione infinita. Sei un pilota che ha visto e vissuto ogni aspetto della Formula 1. La tua leadership e la capacità di ispirare gli altri sono una fonte di ammirazione per tutti.",
            "Kimi Antonelli": "Sei giovane, ma con una personalità da veterano. Ti distingue un'energia dirompente e una capacità di restare concentrato anche nei momenti più critici. Il futuro della Formula 1 è sicuramente nelle tue mani!"
        }


        immagini = {
            "Verstappen": "https://www.bing.com/th/id/OGC.46a021b71bbe33997086938daa81458d?pid=1.7&rurl=https%3a%2f%2fmedia.tenor.com%2fmEI0LWZRrr0AAAAC%2fverstappen-max-verstappen.gif&ehk=CS9RERJ5ooVBRw1OSMhbe7%2bXL2QMEE9n%2bW26D%2buOXPc%3d",
            "Leclerc": "https://www.bing.com/th/id/OGC.6cca03741a0846ab20740c6541ab8ed0?pid=1.7&rurl=https%3a%2f%2fi.pinimg.com%2foriginals%2fbb%2f1a%2f85%2fbb1a8584e6630894dabca8b236d907f7.gif&ehk=z2r9eFVAYn%2bExad3zmuzhMhyOSZYlQIw7%2bA6PWibhxQ%3d",
            "Norris": "https://www.bing.com/th/id/OGC.49f83dbbcfb78734421383121c49edd0?pid=1.7&rurl=https%3a%2f%2fmedia1.tenor.com%2fm%2frkT7ajLiyE0AAAAC%2flando-norris-lando.gif&ehk=CvWu1oUUtRGYC6jsqLxHDlDEpihqb%2bDSvyga%2bQlWxp0%3d",
            "Piastri": "https://www.bing.com/th/id/OGC.794cb544fffdadee832f3ca5b85091c6?pid=1.7&rurl=https%3a%2f%2fpreview.redd.it%2fa-short-sequence-to-appreciate-some-oscar-piastri-reactions-v0-9swgky4gmt6d1.gif%3fwidth%3d268%26auto%3dwebp%26s%3d8c2bb28cf2b91ae351866320adee0ab1567588c9&ehk=4pTV8iQoqwIdY%2bUegqLC3brQ8VzOvpSXX3%2bL9LNZxVY%3d",
            "Alonso": "https://th.bing.com/th/id/R.33fd842fa195974144d583f8c2aaa02d?rik=yka48mcQ8Hy85Q&pid=ImgRaw&r=0",
            "Sainz": "https://www.bing.com/th/id/OGC.806310ae38905fb86d5078fca7cd8086?pid=1.7&rurl=https%3a%2f%2fmedia1.giphy.com%2fmedia%2fv1.Y2lkPTc5MGI3NjExODNiMWM1ZWYzY2NlNGNhNDk4MWM3ODc5YjQ4ZjBkOTk4M2NjNDgwOCZjdD1n%2fIELPp4xE7W04RHU6oq%2fgiphy.gif&ehk=h32HdL8a47r82sOLWci7U1qlMGyIPoxp4uW%2fzf7VKco%3d",
            "Hamilton": "https://www.bing.com/th/id/OGC.5fce92952cb9914c2a547d25f010c67a?pid=1.7&rurl=https%3a%2f%2fmedia3.giphy.com%2fmedia%2f1luYFM8UXcE9TYgXVS%2fgiphy.gif&ehk=zwYucQagYqLmjMGAJer3nrb3BVzICf9xZzbhJH3obB4%3d",
            "Kimi Antonelli": "https://www.bing.com/th/id/OGC.996a75ade4019d8a911540e32ac021df?pid=1.7&rurl=https%3a%2f%2fc.tenor.com%2fCf6MunLw0NEAAAAM%2fkimi-antonelli-prema.gif&ehk=8Txpo%2flH7O4DNg25aHTyhCAobC2t4Yg17gUXM5E0GRE%3d"
        }

        st.markdown("---")
        st.markdown(f"<h2 style='text-align: center;'>🥳 Sei {pilota}! 🥳</h2>", unsafe_allow_html=True)

        # Emojis e testuale grafico
        st.markdown("""
            <div style='font-size: 2em; text-align: center;'>🎉🎉🎉</div>
        """, unsafe_allow_html=True)


        # Descrizione giocatore
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(immagini[pilota], use_container_width=True)
        with col2:
            st.markdown(f"<div style='padding: 1rem; background-color: #e6f2ff; border-left: 5px solid #001f3f; font-size: 1.2em;'>{descrizioni[pilota]}</div>", unsafe_allow_html=True)
        
        # GIF esultanza

        gif_url = "https://www.bing.com/th/id/OGC.537407970e23722a91c6075932a15545?pid=1.7&rurl=https%3a%2f%2fmedia.giphy.com%2fmedia%2f1X8865dbCf8xNrDPG6%2fgiphy-downsized.gif&ehk=c3%2bBi7T%2bGB0ujmgxGndgKyh%2fWrvTZ2G%2b8s2CMlBnfDs%3d"
        st.image(gif_url, caption="YAY!!!", use_container_width=True)

        # Anima la celebrazione
        st.balloons()

        # Pulsante per tornare alla home
        st.button("↩️ Torna alla home", on_click=torna_home)

# Pagina QUIZ ALLENATORI VJ
elif st.session_state.pagina == "quiz_allenatori":
    st.markdown("<h1 style='text-align: center; color: #001f3f;'> 🔴⚪ Quale allenatore Open Femminile del VJ sei?</h1>", unsafe_allow_html=True)

    punteggi_allenatori = {
        "Marco": 0,
        "Davide": 0,
        "Andrea": 0,
        "Franco": 0
    }

    domande_allenatori = [
        {
            "domanda": "1. Immagina di essere alla vigilia di una partita importante, come ti prepari mentalmente?",
            "opzioni": [
                ("Cerco di concentrarmi sulle cose pratiche, ma mi sento sempre un po' nervoso riguardo a come andrà.", "Davide"),
                ("Mi piace mantenere la calma, penso che la tranquillità sia la chiave per affrontare qualsiasi situazione.", "Andrea"),
                (" Preferisco non essere troppo presente, ma quando arrivo, voglio che tutti siano focalizzati sulla strategia.", "Franco"),
                ("Mi piace fare un bel discorso motivazionale, anche se a volte rischio di parlare troppo a lungo.", "Marco"),
            ]
        },
        {
            "domanda": "2. Se dovessi dare un consiglio a un compagno di squadra che si sta preparando per una sfida, come ti comporteresti?",
            "opzioni": [
                ("Gli direi di rimanere fedele a sé stesso, che la calma è la miglior arma.", "Andrea"),
                ("Gli direi di pensare a se stesso e di concentrarsi sull'ottenere il massimo da ogni momento.", "Marco"),
                ("Gli darei un consiglio pratico e tecnico, basato su ciò che potrebbe davvero fare meglio nella partita.", "Franco"),
                ("Cercherei di rassicurarlo, anche se il mio nervosismo potrebbe emergere nelle parole.", "Davide"),
                               
            ]
        },
        {
            "domanda": "3. Come preferisci allenare?",
            "opzioni": [
                ("Con esercizi che migliorano la tattica e il gioco di squadra", "Franco"),
                ("Con sessioni di gruppo per lavorare sull'unione della squadra", "Davide"),
                ("Con allenamenti intensi e molto dinamici", "Andrea"),
                ("Con esercizi mirati alla tecnica individuale", "Marco"),
            ]
        },
        {
            "domanda": "4. Dopo una lunga giornata di allenamento, come ti rilassi?",
            "opzioni": [
                ("Cerco un po' di tempo per me stesso, magari con un drink in mano per rilassarmi e fare due chiacchiere.", "Marco"),
                (" Cerco di staccare dalla tensione, magari pensando a come posso migliorare la squadra", "Andrea" ),
                ("Mi piace andare a letto presto, ma se devo fare due chiacchiere, sono sempre pronto a ascoltare gli altri.","Davide"),
                ("Probabilmente sono già a casa, ma quando sono con la squadra, cerco sempre di offrire consigli e supporto.", "Franco"),
            ]
        },
        {
            "domanda": "5. In un gruppo di amici, come ti comporteresti se qualcuno facesse una battuta divertente?",
            "opzioni": [
                ("Non riuscirei a fare a meno di raccontare la mia versione della storia, aggiungendo dettagli che potrebbero renderla ancora più lunga!", "Marco"),
                ("Mi farei una bella risata, ma non forzerei nulla. L'importante è essere naturali.", "Andrea"),
                ("Probabilmente riderei e magari aggiungerei qualche commento sul fatto che non sempre le cose vanno come vorremmo.", "Davide"),
                ("Sorriderei e forse farei qualche commento divertente, ma sempre con il mio stile più serio.", "Franco"),
            ]
        },
        {
            "domanda": "6. Se un tuo compagno fosse in difficoltà, come reagiresti?",
            "opzioni": [
                ("Gli direi con calma cosa fare per risolvere il problema, ma magari dimenticherei qualche dettaglio!", "Franco"),
                ("Cercherei di aiutarlo, anche se potrei diventare un po' troppo insistente nel dirgli cosa fare.", "Marco"),
                ("Gli darei qualche consiglio, ma non senza sentirmi agitato nel vedere che non sta facendo tutto perfettamente.", "Davide"),
                ("Lo incoraggerei a mantenere la calma e lo rassicurerei che ce la farà se rimane tranquillo.", "Andrea"),
                
            ]
        },
        {
            "domanda": "7. Quando ti trovi di fronte a una decisione importante, come ti comporti?",
            "opzioni": [
                ("Mi sento sempre sotto pressione, ma cerco comunque di fare del mio meglio, anche se sono un po' ansioso.", "Davide"),
                ("Mi piace prendere il controllo della situazione, a volte anche troppo, per essere sicuro che tutto vada come voglio.", "Marco"),
                ("Penso che la calma e la riflessione siano le cose più importanti. Non mi piace affrettare le decisioni.", "Andrea"),
                ("Preferisco osservare un po' da lontano e poi intervenire con un piano che mi sembri giusto, ma non sempre mi ricordo ogni dettaglio.", "Franco"),
            ]
        },
        {
            "domanda": "8. Immagina di dover scegliere un leader per la squadra: quale qualità considereresti più importante?",
            "opzioni": [
                ("Qualcuno che sappia sempre come attirare l'attenzione, parlare tanto e, soprattutto, che non abbia paura di mettersi in mostra.", "Marco"),
                ("Qualcuno che riesca a mantenere la calma anche nelle situazioni più stressanti, ma che sappia far capire la sua ansia senza risultare invadente.", "Davide"),
                ("Qualcuno che sappia ascoltare, dare consigli senza far sentire nessuno sotto pressione e che sia un punto di riferimento per tutti.", "Andrea"),
                ("Qualcuno che sia serio, ma con una buona conoscenza della tattica, che sia sempre pronto a intervenire quando necessario.", "Franco"),
            ]
        }, 
        {
            "domanda": "9. Se qualcosa va storto e le cose non vanno come previsto, come reagisci?",
            "opzioni": [
                ("Mi prendo il mio tempo per riflettere, cercando di mantenere la calma e risolvere con tranquillità.", "Andrea"),
                ("Cerco di analizzare la situazione con lucidità, anche se a volte posso sembrare distante.", "Franco"),
                ("Sbuffo, ma cerco sempre di fare in modo che la situazione si sistemi... anche se mi lamento un po’.", "Marco"),
                ("Mi sento agitato, ma faccio del mio meglio per rimanere calmo e risolvere il problema.", "Davide"),
                
            ]
        },
        {
            "domanda": "10. Quando ti arrabbi, come reagisci?",
            "opzioni": [
                ("La mia rabbia esplode subito.", "Marco"),
                ("Cerco di non arrabbiarmi mai, ma se succede, sono più introverso e cerco di riflettere sulla situazione.", "Franco"),
                ("Mi arrabbio, ma cerco di non farlo vedere troppo.", "Davide"),
                ("Cerco di rimanere calmo, anche se la rabbia è dentro di me. Preferisco non mostrarla.", "Andrea"),
                
            ]
        },
        {
            "domanda": "11. Se qualcuno ti chiedesse di organizzare una festa, cosa faresti?",
            "opzioni": [
                ("Pianificherei una festa super tranquilla, magari con un po’ di musica soft… e tanta fanta.", "Davide"),
                ("Probabilmente mi preoccuperei di come farli sentire a loro agio, cercando di non farla diventare troppo “seriosa", "Andrea"),
                (" Organizzerei tutto alla perfezione, ma mi assicurerei che tutti sappiano che la festa è mia.", "Marco"),
                ("Se mi invitano, ok. Se no… beh, direi che non sono poi così tanto interessato a fare il party planner.", "Franco"),
            ]
        },
        {
            "domanda": "12. Quando senti parlare di una vacanza all’improvviso, cosa fai?",
            "opzioni": [
                ("Mi precipito a prendere le valigie, perché mi serve un po’ di relax… e un po’ di riconoscimento.", "Marco"),
                ("Inizio a fare mille piani e a pensare a tutte le cose che dovrò organizzare. Più stressante che rilassante.", "Davide"),
                ("Vado al volo! Non mi preoccupo di nulla. Se qualcuno ha bisogno di aiuto, vado a darlo.", "Andrea"),
                (" Se posso portare il mio lavoro con me, va bene. Se no… chi se ne importa!", "Franco"),
            ]
        },
        {
            "domanda": "13. Se dovessi descrivere la tua giornata ideale, come sarebbe?",
            "opzioni": [
                ("Una giornata chill con gli amici.", "Andrea"),
                ("Un giorno in cui sono il centro dell'attenzione e tutti si accorgono di quanto sia fantastico ciò che faccio!", "Marco"),
                ("Una giornata lontano da tutto, con il tempo per pensare e fare quello che voglio senza fretta.", "Franco"),
                ("Una giornata perfetta sarebbe una che non mi faccia ansiare troppo, magari con una bella serata di relax.", "Davide"),
                
            ]
        },
        {
            "domanda": "14. Se qualcuno ti chiede un favore, come rispondi?",
            "opzioni": [
                ("Eh, se mi va di farlo, lo farò. Se no, non posso promettere nulla.", "Franco"),
                ("Cerco di farlo. O almeno ci provo.", "Davide"),
                ("Va bene, ma sappi che tutto ciò che faccio ha un prezzo. Ah, ma lo faccio per te!", "Marco"),
                ("Non c'è problema, aiutarti è la cosa più naturale!", "Andrea"),
                
            ]
        },

        {
            "domanda": "Giulia, la creatrice di questo quiz sugli allenatori, cosa fa quando non sta creando quiz su allenatori?",
            "opzioni": [
                ("Si perde a suonare canzoni che nessuno ascolterà.", "Franco"),
                ("Si diverte a fare imitazioni di allenatori e scoppia a ridere da sola.", "Davide"),
                ("Passa il tempo a inventare quiz su argomenti che nemmeno sa bene.", "Marco"),
                ("Si allena a risolvere enigmi impossibili e si sente un genio.", "Andrea"), 
            ]        
        }
        # Aggiungi altre domande come queste
    ]

    for d in domande_allenatori:
        st.markdown(f"### {d['domanda']}")
        risposta = st.radio("", [opt[0] for opt in d["opzioni"]], key=d["domanda"])
        for testo, allenatore in d["opzioni"]:
            if risposta == testo:
                punteggi_allenatori[allenatore] += 1

    if st.button("🏆 Scopri chi sei!"):
        allenatore = max(punteggi_allenatori, key=punteggi_allenatori.get)

        descrizioni_allenatori = {
            "Marco": "Autocentrato, loquace, competitivo.",
            "Andrea": "Calmo, riflessivo, riesce a gestire ogni situazione.",
            "Davide": "Energico, sempre pronto a dare il massimo.",
            "Franco": "Equilibrato e sempre alla ricerca della soluzione giusta.",
        }

            
        st.markdown(f"<h2 style='text-align: center;'>🥳 Sei {allenatore}! 🥳</h2>", unsafe_allow_html=True)

        # Descrizione allenatore
        st.markdown(f"<div style='padding: 1rem; background-color: #e6f2ff; border-left: 5px solid #001f3f; font-size: 1.2em;'>{descrizioni_allenatori[allenatore]}</div>", unsafe_allow_html=True)

        # Anima la celebrazione
        if allenatore == "Marco":
            st.snow()  # La neve appare se l'allenatore è Marco
        else:
            st.balloons()  # Altrimenti, i palloncini appaiono
        # Pulsante per tornare alla home
        st.button("↩️ Torna alla home", on_click=torna_home)

# Pagina QUIZ CALCIATRICI
elif st.session_state.pagina == "quiz_calciatrici":
    st.markdown("<h1 style='text-align: center; color: #001f3f;'> 🔴⚪ Quale calciatrice del VJ Open Femminile sei? </h1>", unsafe_allow_html=True)

    punteggi_calciatrici = {
        "Faccio": 0,
        "Babi": 0,
        "Cla": 0,
        "Vero&Vale": 0,
        "Gloria": 0,
        "Giada": 0,
        "Gaudi": 0,
        "Mame": 0,
        }

    domande_calciatrici = [
        {
            "domanda": "1. Durante un allenamento, ti chiedono di improvvisare un passaggio difficile. Tu:",
            "opzioni": [
                ("Sei pronta a fare il passaggio perfetto e urli a tutti Seguitemi! anche se non è il momento giusto.", "Faccio"),
                ("Provi, ma la palla vola fuori dal campo… però ci metti sempre impegno!", "Babi"),
                ("Corri come una pazza da una parte all’altra del campo per cercare di arrivare alla palla! ", "Cla"),
                ("Cerchi di fare il passaggio, ma poi inizi a parlare di mille altre cose che non c’entrano.", "Vero&Vale"),
                ("Chiedi aiuto a tutti, ma nel frattempo continui a correre in modo scoordinato.", "Gloria"),
                ("Tentativo di dribbling… ma finisco per ingarbugliarmi da sola.", "Giada"),
                ("Arrivi all’ultimo minuto, con un passaggio spettacolare, ma fai un po’ di caos prima di farlo.", "Gaudi"),
                ("Guardi le ragazze giocare, fai il tifo e ti prendi un po’ di pausa. ", "Mame"),
            ]
        },

        {
            "domanda": "2. Immagina di essere a un compleanno di squadra, quale attività faresti?",
            "opzioni": [
                ("Organizzerei tutto, ma poi sarei la prima al centro della pista con un bicchiere in mano!", "Faccio"),
                ("Proverei a vincere al gioco della pignatta, anche se ogni tanto mando tutto in aria!", "Babi"),
                ("Mi farei trovare al centro della pista a ballare!", "Cla"),
                ("Parlerei per ore con le altre, raccontando la mia teoria su tutto! ", "Vero&Vale"),
                ("Mi impegnerò in tutto, ma probabilmente mi dimentico di essere un po' scoordinata!", "Gloria"),
                ("Mi farei coinvolgere in tutto, ma alla fine farò un piccolo spettacolo di dribbling.", "Giada"),
                ("Arriverò in ritardo, ma almeno avrò portato una torta gigante!", "Gaudi"),
                ("Sono quella che porta il massimo del tifo e la risata contagiosa! ", "Mame"),
            ]
        },
        {
            "domanda": "3. Come ti prepari mentalmente prima di una partita importante?",
            "opzioni": [
                ("Mi concentro sul mio ruolo da leader, cerco di trasmettere forza alla squadra.", "Faccio"),
                ("Mi concentro sul passaggio perfetto. ", "Babi"),
                ("Faccio un bel respiro e cerco di motivare tutte, perché la squadra prima di tutto! ", "Cla"),
                ("Parlo un sacco, mi piace spiegare tutto, anche quando forse non è il momento giusto.", "Vero&Vale"),
                ("Chiedi aiuto a tutti, ma nel frattempo continui a correre in modo scoordinato.", "Gloria"),
                ("Mi faccio prendere dall'emozione e provo a dribblare in ogni situazione, anche se rischio di perdere palla.", "Giada"),
                ("Arrivo all'ultimo minuto, ma non vedo l'ora di scendere in campo e fare quello che so fare meglio. ", "Gaudi"),
                ("Faccio il tifo dalla panchina e sono pronta a urlare con tutta la forza! ", "Mame"),
            ]
        },
        {
            "domanda": "4. Quando un tuo compagno o compagna fa un errore in partita, tu:",
            "opzioni": [
                ("Urlo un po’, ma cerco di spronarlo a migliorare! ", "Faccio"),
                ("Gli dico di non mollare, lo sprono a fare meglio, anche se a volte sono un po' brusca.", "Babi"),
                ("Mi avvicino e cerco di motivarlo, ricordandogli che siamo una squadra e che dobbiamo lavorare insieme.", "Cla"),
                ("Parto con mille discorsi e analisi, ma in fondo cerco di farlo con calma, anche se parlo un po' troppo.", "Vero&Vale"),
                ("Faccio un sorriso e lo incoraggio a continuare, senza farmi troppi problemi, anche perchè di solito sono io.", "Gloria"),
                ("Gli faccio capire che può fare di meglio...", "Giada"),
                ("Arrivo a gambe levate e lo incoraggio,ma un po' aggressiva.", "Gaudi"),
                ("Mi metto a tifare dalla panchina, cercando di farlo sorridere senza troppa pressione. ", "Mame"),
            ]
        },
        {
            "domanda": "5. Se dovessi descrivere la tua personalità con un animale, quale sarebbe?",
            "opzioni": [
                ("Un leone, perché sono sempre pronto a comandare e a guidare la squadra!", "Faccio"),
                ("Un lupo, forte e determinata, ma a volte un po' irruenta!", "Babi"),
                ("Un cane da caccia, sempre in movimento e sempre pronta ad aiutare gli altri! ", "Cla"),
                ("Un pappagallo, che parla sempre e ha sempre qualcosa da dire.", "Vero&Vale"),
                ("Una scimmia, agile e pronta a saltare da una parte all'altra, anche se un po’ disordinata.", "Giada" ),
                ("Un orso, che si fa sentire, ma che alla fine trova sempre la sua strada.","Gloria"),
                ("Una tigre, che arriva sempre al momento giusto per fare il colpo finale.", "Gaudi"),
                ("Un delfino, che tifa e sorride senza mai perdere l'entusiasmo! ", "Mame"),
            ]
        },
        {
            "domanda": "6. Se avessi un giorno libero e potessi fare qualsiasi cosa, come lo passeresti?",
            "opzioni": [
                ("Penso che farei una giornata super organizzata: un po' di relax, un po' di socializzazione, tutto al momento giusto.", "Faccio"),
                ("Organizzerei un'uscita con le amiche e, se riesco, cercherei di non mandare il pallone in cielo!", "Babi"),
                ("Correrei senza sosta in un parco, poi probabilmente mi fermerei per un bel picnic con le amiche.", "Cla"),
                ("Passerei la giornata a parlare di qualsiasi cosa, magari anche discutendo delle ultime novità!", "Vero&Vale"),
                ("Probabilmente farei yoga o qualcos’altro che mi aiuti a migliorare la mia coordinazione", "Gloria"),
                ("Vorrei rimanere tranquilla a casa, fare qualche dribbling tra i cuscini e guardare serie TV.", "Giada"),
                ("Mi sveglierei tardi, prenderebbe il mio tempo per fare tutto, e poi uscirei con le amiche per un po' di svago. ", "Gaudi"),
                ("Andrei a vedere una partita di calcio, ma mi limito a tifare per la squadra. ", "Mame"),
            ]
        },
        {
            "domanda": "7. Se potessi essere un personaggio storico o famoso per un giorno, chi sceglieresti?",
            "opzioni": [
                ("Cleopatra, per la leadership e il carisma che ha mostrato nel suo regno.", "Faccio"),
                ("Albert Einstein, per la sua genialità, anche se un po' distratto nella vita quotidiana.", "Babi"),
                ("Amelia Earhart, per il coraggio di volare e fare qualcosa di straordinario!", "Cla"),
                ("Oprah Winfrey, per essere in grado di motivare milioni di persone con parole di saggezza.", "Vero&Vale"),
                ("Leonardo da Vinci, perché, pur essendo un po' scoordinato, aveva tante passioni e un talento incredibile!", "Gloria"),
                ("Frida Kahlo, per il suo spirito indomito e la sua capacità di esprimere sé stessa in ogni situazione.", "Giada"),
                ("Audrey Hepburn, per l'eleganza e il cuore che metteva in tutto ciò che faceva.", "Gaudi"),
                ("Charlie Chaplin, per il suo umorismo e la sua capacità di far ridere tutti con pochi gesti.", "Mame"),
            ]
        },
        {
            "domanda": "8. Come reagisci quando qualcuno ti dà un consiglio che non hai chiesto?",
            "opzioni": [
                ("Lo ascolto, ma se non mi va lo mando a quel paese. ", "Faccio"),
                ("Faccio finta di ascoltare, ma alla fine mando la palla fuori, letteralmente e figurativamente.", "Babi"),
                ("Non dico mai nulla, ma penso sempre: “Ok, va bene, ma io faccio come voglio!”", "Cla"),
                ("A volte rispondo con un commento sferzante, ma non smetto mai di parlare e alla fine divento la chiacchierona della situazione.", "Vero&Vale"),
                ("Non capisco nemmeno se sia un consiglio o una critica… ma continuo comunque per la mia strada.", "Gloria"),
                ("Continuo a fare il mio, anche se i consigli non sono proprio i migliori. Ma vabbè, a volte è il pensiero che conta!", "Giada"),
                ("Mi faccio dare il consiglio, ma lo faccio sempre come dico io! ", "Gaudi"),
                ("Resto in silenzio e annuisco, così nessuno si arrabbia con me.", "Mame"),
            ]
        },
        {
            "domanda": "9. Quando sei in ritardo, come ti giustifichi?",
            "opzioni": [
                ("Semplice, dico che ero impegnata a fare qualcosa di importante e non volevo disturbare il gruppo.", "Faccio"),
                ("Era tutto pronto, ma il pallone è volato fuori e ho dovuto andare a prenderlo!", "Babi"),
                ("Stavo solo correndo per tenere il ritmo! Peccato che ero solo in ritardo. ", "Cla"),
                ("Scusate, avevo un sacco di cose da dire!", "Vero&Vale"),
                ("Ok, forse sono un po’ scoordinata con il tempo, ma sono pronta per darvi il massimo!", "Gloria"),
                ("Mi stavo concentrando sul dribbling!", "Giada"),
                ("Ho fatto tardi perché sono troppo brava e devo fare tutto per prima!", "Gaudi"),
                ("Mi sono distratta guardando la partita!", "Mame"),
            ]
        },
    ]

    for d in domande_calciatrici:
        st.markdown(f"### {d['domanda']}")
        risposta = st.radio("", [opt[0] for opt in d["opzioni"]], key=d["domanda"])
        for testo, giocatrice in d["opzioni"]:
            if risposta == testo:
                punteggi_calciatrici[giocatrice] += 1

    if st.button("🏆 Scopri chi sei!"):
        giocatrice = max(punteggi_calciatrici, key=punteggi_calciatrici.get)

        descrizioni = {
            "Faccio": "Leader grintosa, sempre pronta a dare tutto!",
            "Babi": "Mancina, forte a volte un po’ brusca, ma dal cuore grande e tenera.",
            "Cla": "Instancabile, capocannoniere, umile e sempre nel posto giusto al momento giusto.",
            "Vero&Vale": "2in1, Chiacchierone e fastidiose, ma fanno sempre il loro dovere in difesa.",
            "Gloria": "Scombinata ma testarda, non molla mai anche quando è fuori tempo.",
            "Giada": "Centrocampo di dribbling e parole, fa il suo ma potrebbe fare meno chiacchiere.",
            "Gaudi": "Ritardataria, ribelle, ma segna sempre nei momenti decisivi.",
            "Mame": "Ex velocissima, ora tifosa appassionata, sempre positiva e piena di energia!"
        }

        st.markdown(f"<h2 style='text-align: center;'>🥳 Sei {giocatrice}! 🥳</h2>", unsafe_allow_html=True)

        # Emojis e testuale grafico
        st.markdown("""
            <div style='font-size: 2em; text-align: center;'>🎉🎉🎉</div>
        """, unsafe_allow_html=True)

        st.markdown(f"<div style='padding: 1rem; background-color: #e6f2ff; border-left: 5px solid #001f3f; font-size: 1.2em;'>{descrizioni[giocatrice]}</div>", unsafe_allow_html=True)

        # Anima la celebrazione
        st.balloons()

        # Pulsante per tornare alla home
        st.button("↩️ Torna alla home", on_click=torna_home)
    
# COCOMERE
elif st.session_state.pagina == "quiz_cocomere":
    st.markdown("<h1 style='text-align: center; color: #001f3f;'> 🌸🥒 Quale cocomera sei? </h1>", unsafe_allow_html=True)

    punteggi_cocomere = {
        "Faccio": 0,
        "Babi": 0,
        "Cla": 0,
        "Mame": 0,
        "Marti Russo": 0,
        "Marti Casella": 0,
        "Cata": 0,
        "Ele": 0,
        "Giulia": 0,
        }

    domande_cocomere = [
        {
            "domanda": "1. È sabato sera: cosa stai facendo?",
            "opzioni": [
                ("Sono a una festa in spiaggia con un Gin in mano e l’Inter nel cuore!", "Faccio"),
                ("Sto preparando un allenamento fichissimo per le ragazze con la mia partner in crime.", "Babi"),
                ("Sto guardando una partita NCAA mentre faccio esperimenti di fisica nucleare.", "Cla"),
                ("Porto a spasso Dante mentre racconto una storia buffa su Mario.", "Mame"),
                ("Invento una parola nuova mentre ballo e rido in mezzo a tutti.", "Marti Russo"),
                ("Scrivo la mia tesi mentre sistemo i portieri e organizzo l’uscita scout.", "Marti Casella"),
                ("Sto esplorando Utrecht o organizzando il mio viaggio in Finlandia.", "Cata"),
                ("Sono a una riunione scout o sto risolvendo equazioni mentre curo il mio ginocchio.", "Ele"),
                ("Guardo un documentario sulla Formula 1 mentre disegno una cocomera epica.", "Giulia")
            ]
        },
        {
            "domanda": "2. Che tipo di allenatrice saresti?",
            "opzioni": [
                ("Grintosa, diretta e sempre con un caffè in mano.", "Faccio"),
                ("Dolce ma determinata: ti sprono con il cuore!", "Babi"),
                ("Tecnica, precisa e con un pizzico di basket power!", "Cla"),
                ("Ironica, allegra e con il fischietto sempre pronto (magari mentre porto Dante).", "Mame"),
                ("Urlante d’entusiasmo e piena di frasi in italo-inglese!", "Marti Russo"),
                ("Organizzatissima, ma attenta a ogni dettaglio… e occhio se mi arrabbio!", "Marti Casella"),
                ("Connessa su Zoom mentre alleno in finlandese e faccio il tifo in milanese.", "Cata"),
                ("Scout style: empatia, rispetto e mille impegni!", "Ele"),
                ("Ansiosa all’inizio, ma con tanto cuore e voglia di far bene.", "Giulia")
            ]
        },
        {
            "domanda": "3. Il tuo outfit ideale per una gita in montagna?",
            "opzioni": [
                ("Un costume sotto i pantaloncini, non si sa mai si finisce al mare.", "Faccio"),
                ("Tuta da ginnastica e scarpe comode, pronta a tutto!", "Babi"),
                ("Pantaloni tecnici, scarponi e cuffiette con podcast sportivo.", "Cla"),
                ("Qualcosa che Dante non possa distruggere mentre salgo il sentiero.", "Mame"),
                ("Qualcosa di colorato e comodo, da scattare selfie!", "Marti Russo"),
                ("Scarponcini, zaino pieno e fischietto: sono sempre l’allenatrice anche in montagna.", "Marti Casella"),
                ("Zaino da escursionismo olandese, tabella meteo finlandese e via!", "Cata"),
                ("Zaino scout, borraccia, kit pronto soccorso e… una corda di sicurezza.", "Ele"),
                ("Pantaloni tecnici, taccuino per appunti e un libro nello zaino, nel caso.", "Giulia")
            ]
        },
        {
            "domanda": "4. Sei in vacanza con le cocomere: che tipo di viaggio scegli?",
            "opzioni": [
                ("Un weekend sportivo con tornei di calcetto e basket, ovviamente!", "Cla"),
                ("Un viaggio culturale tra musei e città d’arte… ma con tappa obbligata in uno stadio!", "Faccio"),
                ("Un’avventura in tenda tra le montagne, con falò e chitarra!", "Giulia"),
                ("Un viaggio mare, sole e relax, magari con un bel cocktail in mano!", "Babi"),
                ("Un interrail in Nord Europa con tappe casuali e sorprese continue!", "Cata"),
                ("Un on the road tra Irlanda e Scozia per cercare la vera me stessa!", "Marti Russo"),
                ("Un viaggio organizzato al minuto, ma con il cuore aperto a ogni imprevisto!", "Ele"),
                ("Un viaggio di studio che diventa anche vacanza… basta avere il cane dietro!", "Mame"),
                ("Un ritiro spirituale tra scout, montagna e silenzio… ma portando il pallone!", "Marti Casella")
            ]
        },
        {
            "domanda": "5. Che ruolo hai nel gruppo?",
            "opzioni": [
                ("Sono quella che si prende cura di tutti, magari con un po’ troppa energia!", "Marti Russo"),
                ("Organizzo tutto e tengo i conti in ordine, anche se sembro un po’ burbera!", "Marti Casella"),
                ("Faccio battute a raffica e sdrammatizzo ogni momento!", "Mame"),
                ("Sono quella che ha sempre lo zaino pronto e una canzone da suonare.", "Giulia"),
                ("Sono l’ancora nei momenti di crisi, tranquilla e presente.", "Ele"),
                ("Sono quella che spinge tutti a dare il massimo e crederci fino in fondo!", "Cla"),
                ("Ho sempre il telefono in mano, ma sto mandando messaggi motivazionali!", "Babi"),
                ("Capitano non solo in campo, ma anche nel cuore delle cocomere!", "Faccio"),
                ("Spunto da una nazione diversa ogni mese, ma ci sono sempre!", "Cata")
            ]
        },
        {
            "domanda": "6. È venerdì sera, che fai?",
            "opzioni": [
                ("Sono al lavoro… ma con una playlist calcistica e la testa al weekend!", "Babi"),
                ("Mi rilasso con una tisana, Netflix e mille sogni in testa.", "Ele"),
                ("Sono a una festa, e probabilmente sto parlando metà in inglese e metà in italiano.", "Marti Russo"),
                ("Sto scrivendo la tesi, ma sogno di essere a San Siro.", "Giulia"),
                ("Ho allenamento… o una partita… o un’altra squadra da gestire!", "Cla"),
                ("Sto facendo i bagagli per una nuova meta (forse nordica).", "Cata"),
                ("Sono a cena con un gin in mano e discorsi accesi su calcio e giustizia.", "Faccio"),
                ("Sto portando il cane fuori, ma mentalmente sono già in campo con i nanetti!", "Mame"),
                ("Sto preparando il programma scout per il weekend con i miei ragazzi!", "Marti Casella")
            ]
        },
        {
            "domanda": "7. Il cetriolo del gruppo prende vita e vi chiede di seguirlo in una missione epica. Cosa fai?",
            "opzioni": [
                ("Lo seguo senza pensarci, ma prima organizzo le tappe su Excel.", "Marti Casella"),
                ("Gli offro un gin tonic e chiedo se ha il biglietto per lo stadio.", "Faccio"),
                ("Gli insegno a fare pressing alto e poi lo porto in campo con le allieve.", "Giulia"),
                ("Chiedo se ci sono montagne lungo il tragitto, altrimenti passo.", "Cata"),
                ("Lo porto da Mario e gli faccio raccontare barzellette.", "Mame"),
                ("Lo intervisto in inglese inventato per il mio podcast mentale.", "Marti Russo"),
                ("Lo iscrivo a un torneo e lo schiero mezzala.", "Cla"),
                ("Gli faccio fare stretching e poi lo alleno con le bimbe!", "Babi"),
                ("Controllo se ha fatto la cresima, poi si può partire.", "Ele")
            ]
        },
        {
            "domanda": "8. Sei trasformata in una bevanda magica. Quale sei?",
            "opzioni": [
                ("Un caffè triplo ristretto che fa svegliare anche i morti.", "Faccio"),
                ("Un frullato energizzante con 12 ingredienti, tutti healthy.", "Marti Russo"),
                ("Un gin lemon, elegante ma che spacca.", "Giulia"),
                ("Un'acqua frizzante con una scorza di ironia.", "Mame"),
                ("Un infuso rilassante che però ha anche la caffeina dentro, just in case.","Cla" ),
                ("Un matcha latte instagrammabile ma con sostanza.", "Babi"),
                ("Un tè caldo bevuto in tenda durante un'escursione alpina.", "Cata"),
                ("Un succo ACE shakerato mentre scrivo la tesi sotto stress.","Ele" ),
                ("Un integratore liquido super bilanciato con tabella Excel allegata.", "Marti Casella")
            ]
        },
        {
            "domanda": "9. Una sera le cocomere si trasformano tutte in animali da fattoria. Chi sei?",
            "opzioni": [
                ("Il gallo che canta troppo presto ma è già sveglio da ore con la lista della spesa.", "Ele"),
                ("Il cane da pastore che cerca di tenere tutte in riga, anche se scappano.", "Babi"),
                ("La capra che salta ovunque con energia infinita e urla in tre lingue.", "Marti Russo"),
                ("L’asino che lavora in silenzio e ogni tanto scappa in Finlandia.", "Cata"),
                ("La mucca zen che rumina in pace, ma attenzione se la fai arrabbiare.", "Marti Casella"),
                ("Il coniglio che corre dappertutto con mille cose da fare ma sempre sorridente.", "Cla"),
                ("La gallina che chioccia tutte ma a volte si nasconde nel pollaio.", "Giulia"),
                ("Il maiale simpaticone che si rotola nella fanghiglia della vita con ironia.", "Mame"),
                ("Il cavallo fiero che guida la carovana, criniera al vento.", "Faccio")
            ]
        },
        {
            "domanda": "10. Ti svegli e scopri di essere diventata... un oggetto da spogliatoio. Cosa sei?",
            "opzioni": [
                ("Lo speaker Bluetooth sempre a palla con canzoni motivazionali.", "Marti Russo"),
                ("Il ghiaccio spray, sempre pronto nei momenti critici.", "Ele"),
                ("Il pallone sgonfio che però sa ancora segnare.", "Cla"),
                ("Il borsone perfettamente piegato con dentro tutto… e anche Excel stampato.", "Marti Casella"),
                ("Il cronometro che detta i tempi, anche quelli della merenda.", "Babi"),
                ("Il caffè che gira tra tutte prima della partita.", "Giulia"),
                ("Il cerotto messo a caso che però funziona.", "Mame"),
                ("La borraccia da montagna termica che non perde mai un colpo.", "Cata"),
                ("La fascia da capitano sudata e sempre al posto giusto.", "Faccio")
            ]
        },
        {
            "domanda": "11. Un giorno scopri che tutte le cocomere hanno dei superpoteri. Qual è il tuo?",
            "opzioni": [
                ("Teletrasporto istantaneo per arrivare sempre in tempo alla partita, ma solo se c'è il gin.", "Faccio"),
                ("Super velocità per fare 100 cose in 10 minuti, ma spesso inciampo per troppa energia.", "Mame"),
                ("Invocare l'energia della montagna per fare lunghe escursioni, anche sotto la pioggia.", "Cata"),
                ("Lanciare un pallone da calcio in modo così preciso che tutte le compagne segnano.", "Babi"),
                ("Controllare il tempo e farlo sempre perfetto per una partita all'aperto.", "Marti Casella"),
                ("Prevedere ogni mossa dell'avversario, anticipando ogni passaggio.", "Cla"),
                ("Creare la magia del caffè, che fa passare ogni momento difficile.", "Giulia"),
                ("Moltiplicare il tempo, così posso fare tutto senza stress.", "Ele"),
                ("Parlare tutte le lingue del mondo… e anche inventarne di nuove!", "Marti Russo")
            ]
        },
        {
            "domanda": "12. Se le cocomere fossero un piatto tipico, cosa sareste?",
            "opzioni": [
                ("Una pizza margherita, semplice ma con la perfezione di un impasto fatto a mano.", "Faccio"),
                ("Una pasta alla carbonara, bella sostanziosa ma anche super divertente.", "Babi"),
                ("Un hamburger con mille ingredienti che non ti aspetti, ma alla fine è il migliore.", "Marti Russo"),
                ("Un risotto ai funghi che sa di montagna e di tramonto.", "Cata"),
                ("Un gelato artigianale, sempre fresco e pronto a farti sorridere.", "Ele"),
                ("Un piatto di sushi elegante ma che ti sorprende con la sua freschezza.", "Giulia"),
                ("Un tiramisù con mille strati, ognuno con una sorpresa.", "Marti Casella"),
                ("Un’insalata mista con tutto il possibile, ma con un dressing segreto che cambia ogni volta.", "Cla"),
                ("Un smoothie verde, sano, ma che ti dà la carica per tutta la giornata.", "Mame")
            ]
        },
        {
            "domanda": "13. La cocomera si trova in un’isola deserta, cosa porta con sé per sopravvivere?",
            "opzioni": [
                ("Un cagnolino, così non sarò mai sola!", "Mame"),
                ("Un taccuino per scrivere tutto ciò che mi passa per la testa e motivarmi.","Cla" ),
                ("Un kit da montagna per rifugi e fare trekking!", "Giulia"),
                ("Una macchina fotografica per immortalare ogni momento, perché la vita è bella.", "Marti Russo"),
                ("Un libro per studiare anche lì!", "Cata"),
                ("Un cucchiaio gigante per scavare e cercare caffè ovunque.", "Faccio"),
                ("Un karaoke portatile per non perdere mai la voglia di cantare.", "Babi"),
                ("Un pallone da calcio, ovviamente, per fare partitelle sotto il sole.", "Ele"),
                ("Una radio per sentire sempre la musica giusta in ogni momento.", "Marti Casella")
            ]
        },
        {
            "domanda": "14. Se la cocomera fosse una danza, quale sarebbe?",
            "opzioni": [
                ("La salsa, perché so come comandare il ritmo!", "Faccio"),
                ("Il rock'n'roll, sempre energica ma pronta a improvvisare.", "Marti Russo"),
                ("Una danza del ventre, sempre agile e pronta a sorprendere.", "Cata"),
                ("Il balletto, che richiede precisione, ma c'è sempre spazio per la creatività.", "Giulia"),
                ("La breakdance, con acrobazie e tanto divertimento.", "Ele"),
                ("Il tango, perché so come coniugare passione e precisione.", "Cla"),
                ("Un passo di danza folk che unisce tutti in un abbraccio di gioia.", "Babi"),
                ("La danza moderna, sempre un passo avanti rispetto agli altri.", "Mame"),
                ("Una danza tribale, che unisce corpo e anima, ma con molta energia!", "Marti Casella")
            ]
        },
        {
            "domanda": "15. Immagina di poter scrivere una lettera alle tue amiche cocomere, cosa ci scriveresti?",
            "opzioni": [
                ("Vi voglio bene più di quanto possiate immaginare, grazie per essere sempre le mie compagne di avventure!", "Faccio"),
                ("Siamo una squadra unica, e sono grata di far parte di un gruppo che mi fa sentire così amata e sostenuta.", "Marti Russo"),
                ("Ogni momento insieme è un regalo, e non vedo l'ora di vivere ancora tante esperienze con voi, cocomere!", "Cata"),
                ("Anche quando le cose sono difficili, voi mi fate sempre sentire forte e in grado di superare tutto.", "Giulia"),
                ("Vi ringrazio per esserci sempre, per supportarmi e per rendere ogni giorno migliore con la vostra dolcezza.", "Ele"),
                ("Con tutte voi ho imparato a crescere, a sorridere anche nei momenti più difficili. Siete uniche!", "Babi"),
                ("Non c'è nulla che non riuscirei a fare con voi al mio fianco, mi fate sentire che insieme possiamo conquistare il mondo.", "Cla"),
                ("Ogni risata, ogni abbraccio, ogni sguardo ci rende più forti, e non potrei chiedere niente di meglio che essere insieme a voi.", "Mame"),
                ("Siete il mio sostegno in ogni momento e vi voglio tanto bene. Grazie per essere le cocomere che rendono ogni giorno speciale.", "Marti Casella")
            ]
        }
    ]

    for d in domande_cocomere:
        st.markdown(f"### {d['domanda']}")
        risposta = st.radio("", [opt[0] for opt in d["opzioni"]], key=d["domanda"])
        for testo, cocomera in d["opzioni"]:
            if risposta == testo:
                punteggi_cocomere[cocomera] += 1

    if st.button("🏆 Scopri chi sei!"):
        cocomera = max(punteggi_cocomere, key=punteggi_cocomere.get)

        descrizioni = {
            "Faccio": "Sei la leader del gruppo, quella che sa sempre cosa fare e come fare! Con la tua forza e determinazione, sei il punto di riferimento per tutte le cocomere. Non c'è mai un momento noioso quando sei in giro: sei sempre pronta a comandare con eleganza e a fare il tifo per la tua squadra, dentro e fuori dal campo!",
            
            "Babi": "Sei la dolcezza incarnata, ma anche una persona che sa quando essere decisa e tenere testa a chiunque! Il tuo cuore grande ti fa essere il supporto migliore per le tue amiche, e il tuo spirito generoso e il tuo amore per la squadra non passano mai inosservati. Ogni volta che ti vediamo in campo, siamo sicure che non ci deluderai mai!",
            
            "Cla": "Il tuo spirito sportivo è un faro per tutte noi cocomere! Ogni tua mossa è carica di determinazione, ma non dimentichi mai di essere gentile e pronta ad aiutare le altre. Sei il mix perfetto tra cervello e forza fisica, e la tua energia ci contagia tutte!",
            
            "Mame": "La tua dolcezza è infinita, ma anche il tuo spirito ironico ci fa sempre ridere! Non ti lasci mai abbattere dalle difficoltà, e con la tua battuta pronta e la tua gentilezza, fai sorridere tutti. Anche se ti ferma una tallonite, il tuo amore per le cocomere e per la vita è indomabile!",
            
            "Marti Russo": "Sei l'energia fatta persona, sempre pronta a spronare tutti e a dare il massimo in ogni situazione. La tua energia frizzante è contagiosa e rende ogni momento insieme indimenticabile. E anche se parli in un misto di italiano e inglese, ti vogliamo bene proprio per come sei!",
            
            "Marti Casella": "Sei la persona che non ha paura di prendere in mano la situazione. Che tu stia giocando in porta o facendo la capo scout, ci puoi sempre contare. La tua dolcezza è accompagnata da una determinazione feroce e una voglia di fare che non ti lascia mai. E ci senti sempre, con i tuoi occhi attenti e il tuo cuore grande!",
            
            "Cata": "Anche a distanza, riesci a fare sentire la tua presenza. La tua energia e la tua passione per il calcio sono inarrestabili, e non importa dove ti trovi, la tua forza e il tuo entusiasmo illuminano sempre la nostra squadra. Sei la cocomera che riesce a vivere mille esperienze in un solo giorno!",
            
            "Ele": "La tua dedizione e il tuo impegno non hanno limiti! Sei una cocomera che sa cosa significa supportare e amare il gruppo, sempre pronta a fare il tifo, anche nei momenti più difficili. La tua dolcezza e il tuo spirito scout rendono ogni momento speciale, e non vediamo l'ora di averti di nuovo in campo!",
            
            "Giulia": "Sei quella che riesce sempre a farci ridere, anche nei momenti più tesi. La tua energia è unica e, nonostante le tue insicurezze, hai un cuore enorme che batte per le tue cocomere. Ti butti in ogni cosa con passione, sia che si tratti di calcio che di chitarra, sempre pronta a fare il tifo per tutte noi. La tua dolcezza e il tuo spirito creativo rendono ogni momento con te speciale!"

        }


        st.markdown(f"<h2 style='text-align: center;'>🥳 Sei {cocomera}! 🥳</h2>", unsafe_allow_html=True)

        # Emojis e testuale grafico
        st.markdown("""
            <div style='font-size: 2em; text-align: center;'>🎉🎉🎉</div>
        """, unsafe_allow_html=True)

        st.markdown(f"<div style='padding: 1rem; background-color: #e6f2ff; border-left: 5px solid #001f3f; font-size: 1.2em;'>{descrizioni[cocomera]}</div>", unsafe_allow_html=True)

        # Anima la celebrazione
        st.balloons()

        # Pulsante per tornare alla home
        st.button("↩️ Torna alla home", on_click=torna_home)

# CANZONI
elif st.session_state.pagina == "quiz_canzoni":
    st.markdown("<h1 style='text-align: center; color: #001f3f;'> Quale canzone dei 1D sei? </h1>", unsafe_allow_html=True)

    punteggi_canzoni = {
                "What Makes You Beautiful": 0,
                "Little Things": 0,
                "Story of My Life": 0, 
                "Perfect": 0,
                "Live While We're Young": 0,
                "Kiss You": 0,
                "Night Changes": 0,
                "No Control": 0,
                "You & I": 0,
                "Drag Me Down": 0,
        }

    domande_canzoni = [
       {
            "domanda": "1. Se potessi descrivere il tuo modo di affrontare le difficoltà, quale sarebbe la tua strategia?",
            "opzioni": [
                ("Non mi fermo mai e continuo a lottare, anche se le cose sembrano difficili.", "What Makes You Beautiful"),
                ("Cerco di prendere tutto con calma e di apprezzare anche le piccole cose.", "Little Things"),
                ("Penso che ogni difficoltà sia solo una parte della mia storia, qualcosa che mi rende più forte.", "Story of My Life"),
                ("Cerco di essere perfetto, cercando di dare il massimo in ogni situazione.", "Perfect"),
                ("Voglio godermi il viaggio, senza pensare troppo al risultato finale.", "Live While We're Young"),
                ("Affronto tutto con un sorriso, cercando di rendere ogni momento speciale.", "Kiss You"),
                ("Accetto che le cose cambiano e cerco di adattarmi senza paura.", "Night Changes"),
                ("A volte sento di non avere il controllo, ma cerco di lasciare che le cose fluiscano.", "No Control"),
                ("Credo nell’amore incondizionato, e so che insieme possiamo superare ogni ostacolo.", "You & I"),
                ("Anche se mi sento abbattuto, so che non è la fine, ma solo l'inizio di qualcosa di nuovo.", "Drag Me Down")
            ]
        },
        {
            "domanda": "2. Se dovessi scegliere un modo per esprimere il tuo amore, quale sarebbe?",
            "opzioni": [
                ("Con ogni sorriso, con ogni parola gentile.", "What Makes You Beautiful"),
                ("Nei piccoli gesti quotidiani che fanno la differenza.", "Little Things"),
                ("Scrivendo una storia che racconti tutte le nostre esperienze insieme.", "Story of My Life"),
                ("In ogni momento che condividiamo, cercando di rendere tutto perfetto.", "Perfect"),
                ("Facendo qualcosa di folle e divertente, senza preoccupazioni.", "Live While We're Young"),
                ("Con gesti spontanei e divertenti, senza prendersi troppo sul serio.", "Kiss You"),
                ("Condividendo il cambiamento, accettando che l’amore evolve.", "Night Changes"),
                ("Lasciando che l’amore mi prenda senza condizioni.", "No Control"),
                ("Condividendo una connessione profonda, senza paure o dubbi.", "You & I"),
                ("Con il cuore aperto, pronto ad affrontare qualsiasi cosa insieme.", "Drag Me Down")
            ]
        },
        {
            "domanda": "3. Se avessi la possibilità di viaggiare, dove andresti?",
            "opzioni": [
                ("In un posto esotico dove ogni giorno è diverso, pieno di avventure.", "What Makes You Beautiful"),
                ("In un luogo tranquillo, dove posso apprezzare le piccole cose che la vita mi offre.", "Little Things"),
                ("In un posto che racconti una grande storia, dove il passato e il futuro si incontrano.", "Story of My Life"),
                ("In un posto perfetto, dove tutto sembra essere come dovrebbe.", "Perfect"),
                ("In un posto dove posso essere libero, senza pensieri, solo divertirmi.", "Live While We're Young"),
                ("Ovunque, purché ci sia divertimento e amici con cui condividerlo.", "Kiss You"),
                ("In un luogo che cambia continuamente, per imparare a vivere il presente.", "Night Changes"),
                ("In un posto dove posso essere senza freni e vivere ogni istante al massimo.", "No Control"),
                ("In un luogo dove posso essere me stesso, senza maschere, con chi amo.", "You & I"),
                ("In un posto dove posso essere libero e affrontare qualsiasi cosa mi venga incontro.", "Drag Me Down")
            ]
        },
        {
            "domanda": "4. Cosa ti fa sentire veramente vivo?",
            "opzioni": [
                ("Ogni attimo che vivo, cercando di godere di ogni bellezza che mi circonda.", "What Makes You Beautiful"),
                ("Le piccole cose che rendono ogni giorno speciale.", "Little Things"),
                ("Ogni esperienza che mi cambia, ogni viaggio che mi segna.", "Story of My Life"),
                ("Quando tutto sembra andare per il meglio, come un sogno che si avvera.", "Perfect"),
                ("Quando sento la libertà e l’energia di vivere il momento.", "Live While We're Young"),
                ("Quando riesco a fare qualcosa di spontaneo e divertente con gli altri.", "Kiss You"),
                ("Quando vedo che tutto cambia, ma sono pronto ad adattarmi e ad affrontarlo.", "Night Changes"),
                ("Quando non posso fare a meno di seguire le mie passioni, senza alcun freno.", "No Control"),
                ("Quando posso condividere momenti speciali con qualcuno di veramente importante.", "You & I"),
                ("Quando tutto sembra crollare, ma trovo la forza di andare avanti.", "Drag Me Down")
            ]
        },
        {
            "domanda": "5. Se fossi un libro, quale sarebbe il titolo?",
            "opzioni": [
                ("La bellezza nelle piccole cose.", "What Makes You Beautiful"),
                ("Storie di un cuore che non smette mai di battere.", "Little Things"),
                ("La storia di un viaggio senza fine.", "Story of My Life"),
                ("Perfezione in ogni dettaglio.", "Perfect"),
                ("Giovani e senza paura.", "Live While We're Young"),
                ("Ridere, amare e vivere.", "Kiss You"),
                ("Cambiamenti e nuove avventure.", "Night Changes"),
                ("Senza limiti, senza paura.", "No Control"),
                ("Amore che supera ogni barriera.", "You & I"),
                ("Forza che non si arrende mai.", "Drag Me Down")
            ]
        },
        {
            "domanda": "6. Immagina di avere un superpotere, ma solo per una giornata. Cosa faresti?",
            "opzioni": [
                ("Vorrei il potere di fare brillare ogni stanza con un sorriso! (E forse farebbe bene anche alla mia autostima).", "What Makes You Beautiful"),
                ("Trasformerei i piccoli momenti in qualcosa di speciale, tipo quando i dettagli fanno la differenza.", "Little Things"),
                ("Mi piacerebbe viaggiare nel tempo e riscrivere la mia storia, per vedere dove sarei ora!", "Story of My Life"),
                ("Trasformerei qualsiasi cosa in qualcosa di perfetto. Anche un giorno piovoso, diventerà bellissimo.", "Perfect"),
                ("Voglio il potere di far scatenare una festa, ovunque vada. È l'ora di vivere come se non ci fosse un domani!", "Live While We're Young"),
                ("Mi piacerebbe moltiplicarmi in mille versioni di me stesso, così posso essere ovunque contemporaneamente!", "Kiss You"),
                ("Vorrei fermare il tempo e vivere ogni secondo senza fretta, proprio come quando le cose più belle accadono in un battito di ciglia.", "Night Changes"),
                ("Rendere il caos perfetto: trasformerei ogni disastro in qualcosa che ti fa sorridere.", "No Control"),
                ("Vorrei fondere due cuori in uno, per dimostrare che insieme possiamo fare qualsiasi cosa.", "You & I"),
                ("Mi piacerebbe volare sopra il mondo, guardando tutto dall'alto, sentendomi invincibile.", "Drag Me Down")
            ]
        },
        {
            "domanda": "7. Immagina di avere una macchina del tempo. Dove andresti?",
            "opzioni": [
                ("Tornerei indietro nel tempo e mi troverei nella mia prima performance davanti a tante persone.", "What Makes You Beautiful"),
                ("Andrei a scoprire tutti quei piccoli segreti della vita che ancora non ho capito del tutto.", "Little Things"),
                ("Voglio andare in un periodo passato, magari una festa degli anni '80, e rivivere quella spensieratezza!", "Story of My Life"),
                ("Andrei nel futuro, dove tutto è perfetto, e il mondo è come una favola.", "Perfect"),
                ("Vorrei andare nel cuore dell’estate, per vivere a pieno ogni momento come una grande festa.", "Live While We're Young"),
                ("Viaggerei nel passato per rivedere la mia prima volta al karaoke e urlare a squarciagola!", "Kiss You"),
                ("Voglio visitare il futuro per vedere come sarò fra dieci anni, pronto a fare ancora il colpo!", "Night Changes"),
                ("Mi piacerebbe tornare a un momento in cui mi sentivo completamente libero e senza alcuna preoccupazione.", "No Control"),
                ("Andrei in un posto speciale dove solo io e qualcuno a cui tengo possiamo essere noi stessi.", "You & I"),
                ("Viaggerei indietro nel tempo per incontrare il me stesso di dieci anni fa e raccontargli tutte le cose che ho imparato.", "Drag Me Down")
            ]
        },
        {
            "domanda": "8. Se fossi una pianta, quale saresti?",
            "opzioni": [
                ("Un girasole, sempre alla ricerca della luce, anche quando tutto attorno sembra buio.", "What Makes You Beautiful"),
                ("Un cactus, con una bellezza che si vede solo nei dettagli, ma che è anche forte e resistente.", "Little Things"),
                ("Un albero secolare, che racconta la sua storia con ogni ramo e ogni foglia.", "Story of My Life"),
                ("Una pianta sempreverde, che non perde mai il suo fascino e si adatta a ogni stagione.", "Perfect"),
                ("Un fiore di campo, spontaneo, libero e pronto a sbocciare in ogni occasione.", "Live While We're Young"),
                ("Una pianta rampicante, che cresce e si evolve ogni giorno, trovando sempre nuove strade.", "Kiss You"),
                ("Un fiore che sboccia solo di notte, come se ogni cambio fosse una sorpresa.", "Night Changes"),
                ("Un albero che cresce senza paura, trovando sempre nuove radici e nuovi sogni.", "No Control"),
                ("Un cactus fiorito, perché il fiore che sboccia da me è sempre una sorpresa per chiunque mi conosca.", "You & I"),
                ("Un bonsai, che cresce lentamente ma in modo costante e con una forza straordinaria.", "Drag Me Down")
            ]
        },
        {
            "domanda": "9. Se fossi un personaggio di un film, quale sarebbe il tuo ruolo?",
            "opzioni": [
                ("Il protagonista che salva tutti con un sorriso e dimostra che la bellezza è dentro di te.", "What Makes You Beautiful"),
                ("Il migliore amico che ha sempre un consiglio speciale, proprio quando ne hai più bisogno.", "Little Things"),
                ("L'eroe che supera le difficoltà e trova la sua strada in un'avventura che non dimenticherai mai.", "Story of My Life"),
                ("Il personaggio che ha tutto sotto controllo, ma che non perde mai il suo lato perfetto.", "Perfect"),
                ("Il ribelle che si diverte senza freni, ma con un cuore grande e pronto a fare il colpo.", "Live While We're Young"),
                ("L'amicone che ti fa ridere in ogni situazione, anche quando la scena è un po' imbarazzante.", "Kiss You"),
                ("L'amico che cambia e cresce con ogni passo che fai, ma che ti accompagna in ogni cambiamento.", "Night Changes"),
                ("Il personaggio che sfida tutte le convenzioni e vive secondo le proprie regole.", "No Control"),
                ("Il romantico che sa che, a volte, solo con una persona specialissima puoi essere davvero te stesso.", "You & I"),
                ("Il coraggioso che affronta ogni difficoltà a testa alta e non si arrende mai.", "Drag Me Down")
            ]
        },
        {
            "domanda": "Se dovessi scrivere una lettera al futuro, cosa ti diresti?",
            "opzioni": [
                ("‘Non dimenticare mai di essere te stesso, perché sei fantastico così!’", "What Makes You Beautiful"),
                ("‘Apprezza le piccole cose, sono quelle che rendono la vita speciale.’", "Little Things"),
                ("‘Non dimenticare mai da dove vieni, la tua storia è ciò che ti ha reso forte.’", "Story of My Life"),
                ("‘Sogna in grande e non avere paura di prendere il volo, la perfezione arriva solo se ci credi.’", "Perfect"),
                ("‘Fai sempre ciò che ti rende felice, vivi senza rimpianti e con il cuore leggero.’", "Live While We're Young"),
                ("‘Non preoccuparti troppo delle regole, lascia che la tua energia ti porti ovunque!’", "Kiss You"),
                ("‘Le cose cambiano, ma tu sei abbastanza forte per affrontarle tutte.’", "Night Changes"),
                ("‘A volte il caos è necessario, ma in fondo troverai sempre la tua strada.’", "No Control"),
                ("‘L’amore è la chiave di tutto, continua a crederci.’", "You & I"),
                ("‘Sii coraggioso, prendi il volo e non fermarti mai, la vita ti sta aspettando.’", "Drag Me Down")
            ]
        }
]

        
    for d in domande_canzoni:
        st.markdown(f"### {d['domanda']}")
        risposta = st.radio("", [opt[0] for opt in d["opzioni"]], key=d["domanda"])
        for testo, canzone in d["opzioni"]:
            if risposta == testo:
                punteggi_canzoni[canzone] += 1

    if st.button("🏆 Scopri qual è la tua canzone!"):
        canzone = max(punteggi_canzoni, key=punteggi_canzoni.get)

        descrizioni = {
                "What Makes You Beautiful": "Sei la persona che illumina la stanza, sempre pronta a far brillare gli altri. Ti piace mostrare il meglio di te e lo fai con una naturalezza disarmante. La tua bellezza è unica, ma non è solo quella fisica: è la tua luce interiore che conquista chi ti sta intorno.",
                "Little Things": "Sei il tipo di persona che trova gioia nelle piccole cose. Apprezzi i dettagli, la semplicità e le sfumature della vita. Hai un cuore grande e sei sempre lì per chi hai vicino, anche nei momenti più delicati. Le piccole cose sono quelle che davvero contano per te.",
                "Story of My Life": "La tua vita è un viaggio di esperienze che ti hanno reso la persona che sei oggi. Non hai paura di guardarti indietro e riflettere su ciò che ti ha formato, e ti fidi del percorso che hai scelto. Le tue storie sono quelle che ti rendono autentico e forte.",
                "Perfect": "Sei il tipo di persona che cerca sempre la perfezione, ma senza mai perderti nel tentativo. La tua passione per la vita ti spinge a dare il massimo, e le persone ti ammirano per la tua dedizione e il tuo spirito instancabile. Sei un esempio di equilibrio tra il sogno e la realtà.",
                "Live While We're Young": "Non ti prendi troppo sul serio e sai come goderti la vita! Ti piace l'avventura, non hai paura di rischiare e sei sempre pronto a vivere il momento al massimo. La tua energia è contagiosa, ed è impossibile non voler essere parte del tuo mondo spensierato.",
                "Kiss You": "Sei la persona che non si prende mai troppo sul serio e ama divertirsi. Hai un’anima libera e un cuore aperto, sempre pronto a fare nuove esperienze. La tua spontaneità è il tuo superpotere, e non c’è mai un momento noioso quando sei nei paraggi.",
                "Night Changes": "Le cose possono cambiare, ma tu sei sempre pronto a adattarti. Accogli il cambiamento con una calma sorprendente, perché sai che la vita è fatta di alti e bassi. Ogni esperienza ti rende più forte e consapevole, e riesci a trovare bellezza anche nei momenti più inaspettati.",
                "No Control": "La vita è un po' come una corsa senza freni per te. Ti piace l’adrenalina e spesso ti ritrovi a lanciarti in nuove avventure senza pensare troppo alle conseguenze. Sei il tipo che non ha paura di perdere il controllo, perché sai che alla fine troverai sempre un modo per uscirne alla grande.",
                "You & I": "Credi nel potere delle connessioni e sei convinto che l’amore possa superare ogni ostacolo. Sei la persona che sa che, quando ci si trova, nulla è impossibile. Le tue relazioni sono sempre sincere e genuine, e credi che la forza delle persone si trovi nell’essere uniti.",
                "Drag Me Down": "Non ti lasci mai abbattere dalle difficoltà. La tua forza è incredibile e sei sempre pronto a superare qualsiasi ostacolo ti si presenti. Non hai paura di affrontare la sfida e ogni giorno ti spinge ad essere più forte, perché sai che nessuno può fermarti."
            }

        canzoni_audio = {
                "What Makes You Beautiful": "/workspaces/inter-quiz-1/data/ytmp3free.cc_one-direction-what-makes-you-beautifullyrics-youtubemp3free.org.mp3",
                "Little Things": "/workspaces/inter-quiz-1/data/ytmp3free.cc_one-direction-little-things-lyrics-peepop-youtubemp3free.org.mp3",
                "Story of My Life": "/workspaces/inter-quiz-1/data/ytmp3free.cc_one-direction-story-of-my-life-lyrics-youtubemp3free.org.mp3",
                "Perfect": "/workspaces/inter-quiz-1/data/ytmp3free.cc_one-direction-perfect-lyrics-youtubemp3free.org.mp3",
                "Live While We're Young": "/workspaces/inter-quiz-1/data/ytmp3free.cc_live-while-were-young-one-direction-lyrics-youtubemp3free.org.mp3",
                "Kiss You": "/workspaces/inter-quiz-1/data/One Direction - Kiss You (Lyric Video) [XAXE3JANcsU].mp3",
                "Night Changes": "/workspaces/inter-quiz-1/data/One Direction - Night Changes (Lyrics) [bMBdqvJWofQ].mp3",
                "No Control": "/workspaces/inter-quiz-1/data/ytmp3free.cc_no-control-one-direction-lyrics-youtubemp3free.org.mp3",
                "You & I": "/workspaces/inter-quiz-1/data/You & I - One Direction (Lyrics) 🎵 [iF3UguVMD_I].mp3",
                "Drag Me Down": "/workspaces/inter-quiz-1/data/Drag Me Down - One Direction (Lyrics) [ZU0px2oUO7A].mp3"
            }
        

        st.markdown(f"<h2 style='text-align: center;'>🥳 Sei {canzone}! 🥳</h2>", unsafe_allow_html=True)
 
 
        # Riproduci la musica della canzone
        #st.audio(canzoni_audio[canzone], format='audio/mp3')


        # Emojis e testuale grafico
        st.markdown("""
            <div style='font-size: 2em; text-align: center;'>🎉🎉🎉</div>
        """, unsafe_allow_html=True)

        st.markdown(f"<div style='padding: 1rem; background-color: #e6f2ff; border-left: 5px solid #001f3f; font-size: 1.2em;'>{descrizioni[canzone]}</div>", unsafe_allow_html=True)






        # Anima la celebrazione
        st.balloons()

        # Pulsante per tornare alla home
        st.button("↩️ Torna alla home", on_click=torna_home)

# Pagina QUIZ 1D
elif st.session_state.pagina == "quiz_1D":
    # Inserisci qui il codice del quiz sull'Inter che hai già scritto
    st.markdown("<h1 style='text-align: center; color: #001f3f;'> Quale cantante degli 1D sei?  </h1>", unsafe_allow_html=True)

    punteggi_1D = {
        "Louis": 0,
        "Harry": 0,
        "Zayn": 0,
        "Liam": 0,
        "Niall": 0,
    }

    domande_1D = [
        {
            "domanda": "1. Quale di queste frasi potresti tatuarti senza pensarci due volte?",
            "opzioni": [
                ("'Vas happenin?!'", "Zayn"),
                ("'I'm Harry. Styles.'", "Harry"),
                ("'Just chillin' out, me box.'", "Niall"),
                ("'CATS, MATE. CATS.'", "Louis"),
                ("'I once cried because I saw a baby goat.',", "Liam"),
            ]
        },
        {
            "domanda": "2. Se fossi un tweet iconico degli 1D, saresti...",
            "opzioni": [
                ("Louis che urla 'Always in my heart @Harry_Styles. Yours sincerely, Louis.'", "Louis"),
                ("Zayn che twitta solo emoji confuse e sparisce.", "Zayn"),
                ("Niall che scrive 'CAN’T BELIEVE THIS IS OUR LIFE. THANK YOU.' 100 volte.", "Niall"),
                ("Harry che twitta 'All the love as always.' enigmatico come sempre.", "Harry"),
                ("Liam che cambia username ogni tre mesi e confonde tutti.", "Liam"),
            ]
        },
        {
            "domanda": "3. Qual è la tua energy durante un'intervista con i ragazzi?",
            "opzioni": [
                ("Rispondi con sarcasmo e sguardi in camera come se fossi in The Office.", "Louis"),
                ("Cerchi di calmare tutti e rispondi come un angelo.", "Liam"),
                ("Ti parte una battuta fuori luogo e ridi da solo per 10 minuti.", "Niall"),
                ("Ti limiti a sorridere e poi dici qualcosa di profondo e silenzioso.", "Zayn"),
                ("Fai il misterioso e ogni tanto parli di poesia.", "Harry"),
            ]
        },
        {
            "domanda": "4. Sei intrappolato in una fanfic Wattpad del 2013… cosa succede?",
            "opzioni": [
                ("Sono il bad boy misterioso con un passato difficile, ma cambio per amore. I capelli? Neri ovviamente.", "Zayn"),
                ("Sono il tuo compagno di banco che ti prende in giro ma in realtà ti ama. Alla fine ti bacia sotto la pioggia.", "Louis"),
                ("Sono il nuovo studente che scrive canzoni su di te e ti guarda intensamente da lontano.", "Harry"),
                ("Sono il fratello del tuo migliore amico. Ti proteggo sempre, e ho una cotta segreta per te da anni.", "Liam"),
                ("Sono il vicino irlandese simpatico che ti invita a mangiare pancakes e poi ti porta a un concerto segreto.", "Niall"),
            ]
        },
        {
            "domanda": "5. Quale oggetto sacro del fandom custodiresti come reliquia?",
            "opzioni": [
                ("La maglietta a righe di Louis del 2011. Sta in un cassetto sotto chiave.", "Louis"),
                ("Il cardigan beige di Harry. Irriconoscibile senza di lui.", "Harry"),
                ("La chitarra rossa di Niall autografata. L’ho sognata.", "Niall"),
                ("Il piercing al naso di Zayn. Letteralmente arte moderna.", "Zayn"),
                ("Una pagella del liceo di Liam stampata da Twitter nel 2012. Studio.", "Liam"),
            ]
        },
        {
            "domanda": "6. Ti regalano un cucciolo. Che nome gli dai?",
            "opzioni": [
                ("Kevin, ovvio. E parlo con lui tipo *sempre*.", "Louis"),
                ("Hemsworth. Gli sta bene, no?", "Harry"),
                ("Guinness, perché è irlandese dentro. Anche se è un golden retriever.", "Niall"),
                ("Ziggy. Gli piacciono i dischi di Bowie. E sì, è un cane hipster.", "Zayn"),
                ("Apollo. Perché è un atleta, corre tipo il vento. Anche troppo.", "Liam"),
            ]
        },
        {
            "domanda": "7. Devi scegliere un outfit da concerto: cosa metti?",
            "opzioni": [
                ("Camicia sbottonata fino all’ombelico, mille anelli e capelli al vento.", "Harry"),
                ("Maglietta basic, jeans, e quel sorriso che fa perdere la voce al pubblico.", "Niall"),
                ("T-shirt a righe, skinny jeans e Converse consumate. Non si cambia.", "Louis"),
                ("Bomber oversize, sguardo enigmatico, tatuaggi in vista. Non parlo, ma spacco.", "Zayn"),
                ("Canotta, occhiali da sole anche di notte, e salto atletico a metà set.", "Liam"),
            ]
        },
        {
            "domanda": "8. Ti svegli in una AU in cui fai parte dei 1D. Cosa porti al gruppo?",
            "opzioni": [
                ("L’ironia costante e quella risata che contagia tutti anche a 4AM.", "Louis"),
                ("La calma zen e il mood da cantautore. Scrivo ballate nel retro del bus.", "Harry"),
                ("L’energia instancabile: chitarra, risate, e qualche passo di danza goffo.", "Niall"),
                ("Un’aura di mistero, un diario pieno di disegni e versi segreti.", "Zayn"),
                ("Il piano B per ogni disastro: sono l’organizzatore, l’ancora, il papà.", "Liam"),
            ]
        },
        {
            "domanda": "9. È mezzanotte. Ti beccano online… cosa stai facendo?",
            "opzioni": [
                ("Sto facendo live su Instagram, leggendo fanfiction su me stesso.", "Louis"),
                ("Sto facendo pane fatto in casa ascoltando Fleetwood Mac.", "Harry"),
                ("Sto giocando a FIFA e mandando selfie con filtri assurdi.", "Niall"),
                ("Sto componendo su GarageBand con luci soffuse e incenso acceso.", "Zayn"),
                ("Sto rispondendo ai commenti con emoji mentre faccio squat.", "Liam"),
            ]
        },
        {
            "domanda": "10. In un sogno ricorrente, ti ritrovi nel backstage del TMH tour. Cosa stai facendo?",
            "opzioni": [
                ("Sto nascondendo cucchiai di plastica ovunque nel camerino di Harry.", "Louis"),
                ("Sto scaldando la voce con Ed Sheeran e preparando una tisana alla camomilla.", "Harry"),
                ("Sto cercando disperatamente il mio ukulele rosa. L’ha preso Liam, lo so.", "Niall"),
                ("Sto scrivendo versi sulle pareti con eyeliner nero mentre nessuno guarda.", "Zayn"),
                ("Sto sistemando le scalette dello show con tre walkie-talkie attivi.", "Liam"),
            ]
        },
        {
            "domanda": "11. È il 2013 e sei bloccato in aeroporto con i ragazzi. Che fai?",
            "opzioni": [
                ("Inizio a giocare a 'nascondino estremo' tra i gate. Viene coinvolta anche la security.", "Louis"),
                ("Sto facendo una playlist chill su Spotify e offro caramelle alla crew.", "Harry"),
                ("Ho organizzato un mini torneo di Uno con regole modificate da me.", "Niall"),
                ("Scrivo il testo di una nuova canzone sul retro di una boarding pass.", "Zayn"),
                ("Controllo il tempo d’attesa, ordino cibo per tutti e tengo calmi i fan.", "Liam"),
            ]
        },
        {
            "domanda": "12. Sei intrappolato dentro un videoclip degli 1D. Quale scena stai vivendo?",
            "opzioni": [
                ("Sto cercando di non affogare nella piscina di *Live While We’re Young* mentre urlo 'HELP!'", "Louis"),
                ("Sto fissando la telecamera intensamente sotto la neve in *Night Changes*, come se potesse leggere la mia anima.", "Harry"),
                ("Mi sto rotolando in mezzo al prato con una GoPro attaccata al petto come in *You & I*.", "Niall"),
                ("Sto guidando una barca in *Kiss You*, ma non so nuotare e nessuno mi ha detto dove andare.", "Zayn"),
                ("Sto scrivendo il copione di *Story of My Life* e piango mentre lo recitiamo. Tutti piangono.", "Liam"),
            ]
        },
        {
            "domanda": "13. Quale tweet dimenticato del 2012 ti rappresenta di più spiritualmente?",
            "opzioni": [
                ("'Cats are cool.'", "Harry"),
                ("'I like girls who eat carrots.'","Louis" ),
                ("'Tuna is nice.'", "Niall"),
                ("'Just chilling on the roof, thinking about stuff.'", "Zayn"),
                ("'I just burnt my toast.'", "Liam"),
            ]
        },
        {
            "domanda": "14. In quale momento della tua vita ti sei sentito davvero visto?",
            "opzioni": [
                ("Quando ho capito che potevo farcela da solo, anche se nessuno ci credeva.", "Zayn"),
                ("Quando qualcuno mi ha detto che la mia gentilezza era la mia forza.", "Harry"),
                ("Quando ho fatto ridere gli altri anche se dentro mi sentivo fragile.", "Louis"),
                ("Quando sono riuscito a essere me stesso senza chiedere scusa.", "Niall"),
                ("Quando ho messo da parte le mie paure per prendermi cura degli altri.", "Liam"),
            ]
        },
        {
            "domanda": "15. Cosa significa per te 'casa'?",
            "opzioni": [
                ("Una chitarra, il suono delle risate, le cose semplici.", "Niall"),
                ("Un abbraccio che non ha bisogno di parole.", "Zayn"),
                ("Un luogo in cui posso ballare in mutande e nessuno mi giudica.", "Harry"),
                ("Un gruppo di amici che mi prende in giro ma mi ama più di ogni cosa.", "Louis"),
                ("Un posto dove le responsabilità si alleggeriscono perché siamo insieme.", "Liam"),
            ]
        },
        {
            "domanda": "16. Quando ti senti perso, cosa ti riporta a te stesso?",
            "opzioni": [
                ("Scrivere canzoni che non farò mai ascoltare a nessuno.", "Zayn"),
                ("Mettere le cuffie, uscire a camminare, respirare.", "Harry"),
                ("Fare qualcosa per qualcun altro, anche solo un messaggio carino.", "Liam"),
                ("Guardare indietro e ricordare tutto ciò che ho già superato.", "Louis"),
                ("Parlare con qualcuno che mi conosce davvero.", "Niall"),
            ]
        },
        {
            "domanda": "17. Quale frase descrive la tua idea di amore?",
            "opzioni": [
                ("Ti vedo in tutte le cose belle, anche quando non sei qui.", "Zayn"),
                ("È una risata condivisa sotto le stelle, anche se domani piove.", "Niall"),
                ("Amore è libertà. È sapere che posso andare via… ma scelgo di restare.", "Harry"),
                ("È restare anche nei giorni in cui non sono facile da amare.", "Louis"),
                ("È proteggere, anche da lontano. Sempre.", "Liam"),
            ]
        },
        {
            "domanda": "18. Se potessi inviare un messaggio alla tua versione di 10 anni fa, cosa diresti?",
            "opzioni": [
                ("Non cambiare per nessuno, anche se a volte sarà difficile.", "Harry"),
                ("Le cicatrici che hai oggi saranno le medaglie di domani.", "Louis"),
                ("Va tutto bene anche se non lo capisci adesso.", "Zayn"),
                ("Ridi più che puoi. Davvero, non smettere.", "Niall"),
                ("Sii forte, ma ricorda che puoi anche crollare.", "Liam"),
            ]
        },
        {
            "domanda": "19. In quale canzone trovi la tua storia?",
            "opzioni": [
                ("'Little Things'. Perché le parole più semplici mi hanno salvato.","Liam" ),
                ("'If I Could Fly'. Perché ci sono pensieri che ho detto solo col silenzio.", "Zayn"),
                ("'Through The Dark'. Perché voglio essere la luce per qualcun altro.", "Louis"),
                ("'Don't Forget Where You Belong'. Perché a volte ci si perde per ritrovarsi meglio.", "Niall"),
                ("'Fine Line' (anche se è da solista). Perché ogni fine ha il suo modo di essere bella.", "Harry"),
            ]
        },
        {
            "domanda": "20. Cos’è per te la forza?",
            "opzioni": [
                ("Restare gentile anche quando il mondo ti cambia.", "Harry"),
                ("Alzarsi ogni volta che cadi, anche se nessuno applaude.", "Louis"),
                ("Saper dire di no quando tutti si aspettano un sì.", "Zayn"),
                ("Essere lì per gli altri, anche quando tu ne avresti bisogno.", "Liam"),
                ("Continuare a sperare, anche quando non c’è nessun motivo evidente.", "Niall"),
            ]
        },
        {
            "domanda": "21. Quando pensi agli One Direction, qual è la verità che porti nel cuore?",
            "opzioni": [
                ("Eravamo cinque, ma siamo diventati milioni. E siamo ancora qui.", "Liam"),
                ("Non importa se si sono separati. Ci hanno insegnato ad amarci tra sconosciuti.", "Niall"),
                ("Non ho mai conosciuto nessuno di loro, ma mi hanno fatto sentire visto.", "Harry"),
                ("Anche nei giorni peggiori, bastava una loro canzone per respirare.", "Zayn"),
                ("Non si tratta solo di musica. Si tratta di crescere insieme, anche a distanza.", "Louis"),
            ]
        },      


        
    ]

    for d in domande_1D:
        st.markdown(f"### {d['domanda']}")
        risposta = st.radio("", [opt[0] for opt in d["opzioni"]], key=d["domanda"])
        for testo, cantante in d["opzioni"]:
            if risposta == testo:
                punteggi_1D[cantante] += 1

    if st.button("🏆 Scopri chi sei!"):
        cantante = max(punteggi_1D, key=punteggi_1D.get)

        descrizioni= {
            "Liam": "Sei il tipo di persona che preferisce non essere al centro dell'attenzione, ma quando parla, tutti ti ascoltano. La tua leadership è discreta ma solida, e anche se tendi a metterti in secondo piano, chi ti conosce sa che sei un pilastro su cui si può sempre contare. Dietro alla tua serietà c'è un cuore che batte forte per chi ama veramente. Senti sempre il peso della responsabilità, ma il tuo desiderio di far crescere gli altri è ciò che ti rende davvero speciale.",
            
            "Niall": "Il tuo sorriso è contagioso e la tua risata è un rifugio sicuro per tutti. Sei la persona che sa come alleggerire una giornata, ma dietro quella facciata spensierata c'è una profondità che solo chi ti conosce davvero riesce a vedere. Ti piace ascoltare gli altri, prendersi cura delle persone e condividere con chi ti sta accanto. Il tuo cuore è grande, e l'unica cosa che ami più di un bel momento di divertimento è vedere gli altri felici accanto a te.",
            
            "Harry": "Sei il sognatore che riesce a rendere tangibile l'impossibile. Con i tuoi occhi sempre alla ricerca di qualcosa di più grande, non hai paura di esprimere chi sei veramente. Il tuo cuore è aperto al mondo e la tua vulnerabilità è la forza che ispira chi ti ama. Sei un vero artista, ma la tua profondità non si limita alla musica – ti mostri per quello che sei, senza paura di essere giudicato. La tua autenticità è la tua più grande bellezza, e chi ti segue sa che non esistono maschere con te.",
            
            "Zayn": "Sei l'anima misteriosa che lascia un'impressione indelebile. Il tuo silenzio parla più di mille parole e quando parli, c'è sempre una verità che colpisce dritto al cuore. Non ti preoccupi di conformarti alle aspettative degli altri, e la tua visione del mondo è unica. Sei l'artista che crea in modo autentico e senza compromessi, e mentre il mondo ti guarda da lontano, tu preferisci essere lontano dai riflettori. Ma chi ha il privilegio di conoscerti sa che dietro la tua riservatezza si cela una passione travolgente.",
            
            "Louis": "Sei il ribelle con un cuore grande e una passione che non si può ignorare. Ogni cosa che fai è guidata da un'emozione autentica, ed è difficile non essere coinvolti dalla tua energia. Non hai paura di lottare per ciò che è giusto, anche se a volte questo ti rende più vulnerabile. La tua sincerità è ciò che ti rende speciale, e chi ti conosce sa che sei un amico che non tradisce mai. In ogni battaglia che affronti, riesci sempre a portare un po' di luce, anche nei momenti più oscuri.",
        }


        immagini = {
            "Louis": "https://www.bing.com/th/id/OGC.bf42f8846b9c43e9ff3988d8904574e0?pid=1.7&rurl=https%3a%2f%2fmedia1.tenor.com%2fimages%2fbf42f8846b9c43e9ff3988d8904574e0%2ftenor.gif%3fitemid%3d17969872&ehk=LoxWJrw5uFWymoWu5xycjiUsfiWpRO1azUaUiDg%2fxQQ%3d",
            "Harry": "https://www.bing.com/th/id/OGC.da39af0fba0654cdde29f08ec0ebd69e?pid=1.7&rurl=https%3a%2f%2fi.pinimg.com%2foriginals%2f68%2f8c%2fe8%2f688ce861c57c432e787346669c5de201.gif&ehk=2hAe%2fpXZJYnhRFvUfrk2jC01oBCcWkSfxHywRtQinrc%3d",
            "Niall": "https://www.bing.com/th/id/OGC.d8417aabfcca87f39d8926ff501c102f?pid=1.7&rurl=https%3a%2f%2fgiffiles.alphacoders.com%2f207%2f207268.gif&ehk=GmQpKOwL2ZZu2JfAXAUXuVbJrMprH9CBoepx7zK0HB8%3d",
            "Liam": "https://www.bing.com/th/id/OGC.85a1d04ee651763f79ca1fa7d03fe8d3?pid=1.7&rurl=https%3a%2f%2fmedia.tenor.com%2fGepYe1THHXoAAAAC%2fliam-payne-smiling-and-laughing.gif&ehk=P3rTG65G9Cl9DW4Q72igK%2fipdmpykzFjlX7GK%2fn0FMg%3d",
            "Zayn": "https://www.bing.com/th/id/OGC.3dd72a1b5ded59790388e6bd2c58d3a4?pid=1.7&rurl=https%3a%2f%2fmedia.giphy.com%2fmedia%2f2kS4wNFnntUju%2fgiphy.gif&ehk=QmFyxh%2bpBnKbfvgS1ClVU158ZbAhNQGHySZX8TC%2fc7A%3d",
        }

        st.markdown("---")
        st.markdown(f"<h2 style='text-align: center;'>🥳 Sei {cantante}! 🥳</h2>", unsafe_allow_html=True)

        # Emojis e testuale grafico
        st.markdown("""
            <div style='font-size: 2em; text-align: center;'>🎉🎉🎉</div>
        """, unsafe_allow_html=True)


        # Descrizione giocatore
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(immagini[cantante], use_container_width=True)
        with col2:
            st.markdown(f"<div style='padding: 1rem; background-color: #e6f2ff; border-left: 5px solid #001f3f; font-size: 1.2em;'>{descrizioni[cantante]}</div>", unsafe_allow_html=True)
        
        # GIF esultanza

        gif_url = "https://www.bing.com/th/id/OGC.411dcc394eb0384bfd8765cccf3ace12?pid=1.7&rurl=https%3a%2f%2fbestgifs.makeagif.com%2fwp-content%2fuploads%2f2015%2f06%2fezgif.com-resize.gif&ehk=EpByc1km7VoOU3RThu1a6HbudidvdAZLuEy7%2fifFKrQ%3d"
        st.image(gif_url, caption="YAY!!!", use_container_width=True)

        # Anima la celebrazione
        st.balloons()

        # Pulsante per tornare alla home
        st.button("↩️ Torna alla home", on_click=torna_home)
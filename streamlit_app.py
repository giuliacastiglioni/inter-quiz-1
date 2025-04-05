import streamlit as st
import time

st.set_page_config(page_title="**Quiz!!!**", page_icon="⚽", layout="centered")

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

def vai_al_quiz_allenatori():
    st.session_state.caricamento = True
    time.sleep(1.5)
    st.session_state.pagina = "quiz_allenatori"
    st.session_state.caricamento = False

def torna_home():
    st.session_state.pagina = "home"

# Pagina HOME
if st.session_state.pagina == "home":
    st.markdown("""
        <div style='background: linear-gradient(to bottom right, #001f3f, #0074D9); padding: 4rem; border-radius: 20px; text-align: center; color: white;'>
            <h1 style='font-size: 3em;'>Scegli il tuo quiz!</h1>
            <p style='font-size: 1.3em;'>Benvenuto! Puoi scegliere di scoprire quale calciatore dell'Inter sei o quale allenatore della squadra Vittoria Junior ti somiglia di più!</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Pulsanti per scegliere il quiz
    if st.button("Quale calciatore dell'Inter sei?    👉"):
        with st.spinner("Caricamento quiz... 🧐"):
            vai_al_quiz_inter()

    if st.button("Quale allenatore del VJ Open Femminile sei?    👉"):
        with st.spinner("Caricamento quiz... 🧐"):
            vai_al_quiz_allenatori()

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

# TPSIT_5AROB
Esercizi di TPSIT della classe quinta


## Progetto alphabot (20/12/2023)
Il progetto relativo all'alphabot presenta diverse versioni: quella integrale e finale si trova nella seguente cartella: 
  ## alpha_flask_final_version
Il codice contenuto in app.py permette una volta eseguito di creare un server web Flask al quale si può accedere dall'indirizzo ip dell'host che avvia il programma.
Si presenta una pagina di login, tramite la quale si controllano le credenziali salvate in db.db, database nel quale le password sono hashate. Una volta immesse le credenziali
avviene il controllo, se sono presenti nel database l'utente viene direzionato alla pagina principale composta da bottoni per il controllo dei movimenti del robot.
Se le credenziali non dovessero essere presenti, viene riportato l'errore a schermo.
Per rafforzare il sistema ed evitare operazioni di bruteforce, l'index presenta una url composta da un token di 40 cifre alfanumeriche generato casualemente.
Il robot può svolgere i classici movimenti (avanti, indietro, destra, sinistra) e delle sequenze di movimenti (es. inversione di marcia ...)

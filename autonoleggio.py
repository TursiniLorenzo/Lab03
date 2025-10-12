from automobile import Automobile
import csv

class Autonoleggio:

# Lista, che inizializzo vuota, in cui andrò a memorizzare tutti i noleggi
# Lista, che inizializzo vuota, in cui andrò a memorizzare tutte le automobili dell'autonoleggi

    def __init__(self, nome, responsabile):
        self.nome = nome
        self.responsabile = responsabile
        self.automobili = []
        self.noleggi = []

    def __str__ (self) :
        return f"{self.responsabile}"

    def carica_file_automobili(self, file_path):
        with open(file_path, "r", encoding="utf-8") as infile:
            reader = csv.reader(infile)
            for row in reader:
                self.automobili.append(row)
        return

    def aggiungi_automobile(self, marca, modello, anno, num_posti):
        if not self.automobili :
            nuovo_codice = "A1"
        else :
            ultimo_codice = self.automobili[-1][0]
            codice_numerico = int (ultimo_codice [1:])
            nuovo_codice = f"A{codice_numerico + 1}" # In questo modo il codice della nuova auto sarà quello dell'ultima
                                                 # auto ma incrementato di uno

        nuova_auto = [str (nuovo_codice), marca, modello, str (anno), str (num_posti)]
        self.automobili.append (nuova_auto)
        return " | ".join (nuova_auto)

    def automobili_ordinate_per_marca(self):
        marche_automobili = [] # Creo una lista vuota che conterrà tutte le marche di automobili
                               # presenti nell'autonoleggio
        for riga in self.automobili :
            marche_automobili.append (riga [1])

        marche_automobili_ordinate = sorted (marche_automobili) # Ordino le marche di automobili in ordine alfabetico
        automobili_ordinate = []

        for marca in marche_automobili_ordinate :
            for riga in self.automobili :
                if riga [1] == marca :
                    automobili_ordinate.append (riga) # Inserisco una a una le automobili in base alla marca,
                                                      # in ordine alfabetico

        return automobili_ordinate

    def nuovo_noleggio(self, data, id_automobile, cognome_cliente):
        noleggio = [] # Lista in cui inserirò i dati del noleggio, che a sua volta sarà poi inserita nella lista
                      # noleggi inizializzata come lista di classe
        id_automobili = [] # Lista che conterrà tutti gli id delle auto
        id_automobili_noleggiate = [] # Lista che conterrà solo gli id delle auto noleggiate

        for riga in self.automobili :
            id_automobili.append (riga [0])

        for riga in self.noleggi :
            id_automobili_noleggiate.append (riga [1])

        if id_automobile not in id_automobili : # Se l'id fornito dall'utente non è presente nella lista contenente
                                                # tutti gli id, vuol dire che l'auto non esiste
            return "L'automobile non esiste."
        else :
            if id_automobile not in id_automobili_noleggiate : # Se invece l'id fornito dall'utente è presente nella
                                                               # lista contenente tutti gli id, ma non è presente nella
                                                               # lista contenente solo gli id delle auto noleggiate,
                                                               # allora vuol dire che esiste e può essere noleggiata
                noleggio = [data, id_automobile, cognome_cliente]
                self.noleggi.append (noleggio)
            else :
                return "L'automobile è già stata noleggiata"

        return noleggio

    def termina_noleggio(self, id_noleggio):
        """Termina un noleggio in atto"""
        # TODO
        for riga in self.noleggi :
            if riga [1] == id_noleggio : # Se l'id fornito dall'utente coincide con quello presente nella lista dei
                                         # noleggi, allora va rimossa quella riga dalla lista dei noleggi
                self.noleggi.remove (riga)
                return True

        return False









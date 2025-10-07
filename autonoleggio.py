from automobile import Automobile
import csv

class Autonoleggio:

    automobili = []

    def __init__(self, nome, responsabile):
        self.nome = nome
        self.responsabile = responsabile

    def __str__ (self) :
        return f"{self.responsabile}"

    def carica_file_automobili(self, file_path):
        with open(file_path, "r", encoding="utf-8") as infile:
            reader = csv.reader(infile)
            for row in reader:
                Autonoleggio.automobili.append(row)
        return

    def aggiungi_automobile(self, marca, modello, anno, num_posti):
        ultimo_codice = Autonoleggio.automobili[-1][0]
        codice_numerico = int (ultimo_codice [1:])
        nuovo_codice = f"A{codice_numerico + 1}"

        nuova_auto = [str (nuovo_codice), marca, modello, str (anno), str (num_posti)]
        Autonoleggio.automobili.append (nuova_auto)
        return " | ".join (nuova_auto)

    def automobili_ordinate_per_marca(self):
        """Ordina le automobili per marca in ordine alfabetico"""
        # TODO

    def nuovo_noleggio(self, data, id_automobile, cognome_cliente):
        """Crea un nuovo noleggio"""
        # TODO


    def termina_noleggio(self, id_noleggio):
        """Termina un noleggio in atto"""
        # TODO

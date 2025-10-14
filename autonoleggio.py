import csv
import operator
from automobile import Automobile
from noleggio import Noleggio

class Autonoleggio:

    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile
        self.automobili = []
        self.noleggi = []

    @property
    def nome (self) :
        return self._nome

    @property
    def responsabile (self) :
        return self._responsabile

    @responsabile.setter
    def responsabile (self, nome_responsabile):
        self._responsabile = nome_responsabile

    def __str__ (self) :
        return f"{self._responsabile}"

    def carica_file_automobili(self, file_path) :
        self.automobili =Automobile.carica_automobili (file_path)
        return

    def aggiungi_automobile(self, marca, modello, anno, num_posti):
        if not self.automobili :
            nuovo_codice = "A1"
        else :
            ultimo_codice = self.automobili[-1].cod_univoco
            codice_numerico = int (ultimo_codice [1:])
            nuovo_codice = f"A{codice_numerico + 1}"
        nuova_auto = Automobile (str (nuovo_codice), marca, modello, str (anno), str (num_posti))
        self.automobili.append (nuova_auto)
        return nuova_auto

    def automobili_ordinate_per_marca(self):
        automobili_ordinate = sorted (self.automobili, key=operator.attrgetter ("marca"))
        return automobili_ordinate

    def nuovo_noleggio(self, cod_univoco, data, cognome_cliente):
        auto_esistente = False
        for auto in self.automobili :
            if auto.cod_univoco == cod_univoco :
                auto_esistente = True
                break

        if not auto_esistente :
            return "Codice auto inesistente"

        for noleggio in self.noleggi :
            if noleggio.id_auto == cod_univoco :
                return "L'auto è già stata noleggiata."


        if not self.noleggi :
            id_noleggio = "N1"
        else :
            ultimo_id = self.noleggi[-1].id_noleggio
            codice_numerico = int (ultimo_id[1:])
            id_noleggio = f"N{codice_numerico + 1}"

        noleggio = Noleggio(id_noleggio, cod_univoco, data, cognome_cliente)
        self.noleggi.append (noleggio)
        return noleggio

    def termina_noleggio(self, id_noleggio):
        for noleggio in self.noleggi :
            if noleggio.id_noleggio == id_noleggio :
                self.noleggi.remove (noleggio)
                return True
        return False









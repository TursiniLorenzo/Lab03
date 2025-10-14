import csv

class Automobile :
    def __init__(self, cod_univoco, marca, modello, anno_immatricolazione, posti):
        self._cod_univoco = cod_univoco
        self._marca = marca
        self._modello = modello
        self._anno_immatricolazione = anno_immatricolazione
        self._posti = posti

    @property
    def cod_univoco (self) :
        return self._cod_univoco

    @property
    def marca (self) :
        return self._marca

    @property
    def modello (self) :
        return self._modello

    @property
    def anno_immatricolazione (self) :
        return self._anno_immatricolazione

    @property
    def posti (self) :
        return self._posti

    @classmethod
    def carica_automobili (cls, file_path) :
        automobili = []
        with open (file_path, "r", encoding="utf-8") as infile :
            reader = csv.reader (infile)
            for riga in reader :
                automobile = cls (riga [0], riga [1], riga [2], riga [3], riga [4])
                automobili.append (automobile)

        return automobili

    def __str__ (self) :
        return (f"Codice univoco:  {self._cod_univoco}, "
                f"Marca: {self._marca}, "
                f"Modello: {self._modello},"
                f"Anno di immatricolazione: {self._anno_immatricolazione},"
                f"Posti: {self._posti}")

import csv

class Automobile :
    def __init__(self, cod_univoco, marca, modello, anno_immatricolazione, posti):
        self.cod_univoco = cod_univoco
        self.marca = marca
        self.modello = modello
        self.anno_immatricolazione = anno_immatricolazione
        self.posti = posti

    def __str__ (self) :
        return (f"Codice univoco:  {self.cod_univoco}, "
                f"Marca: {self.marca}, "
                f"Modello: {self.modello},"
                f"Anno di immatricolazione: {self.anno_immatricolazione},"
                f"Posti: {self.posti}")

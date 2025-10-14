class Noleggio :

    def __init__ (self, id_noleggio, cod_univoco, data, cognome_cliente) :
        self.id_noleggio = id_noleggio
        self._id_auto = cod_univoco
        self._data = data
        self._cognome_cliente = cognome_cliente

    @property
    def id_auto (self) :
        return self._id_auto

    @property
    def data (self) :
        return self._data

    @property
    def cognome_cliente (self) :
        return self._cognome_cliente

    def __str__(self) :
        return (f"{self.id_noleggio},"
                f"{self.id_auto},"
                f"{self.data},"
                f"{self.cognome_cliente}")






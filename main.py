from autonoleggio import Autonoleggio
from automobile import Automobile
from datetime import datetime

def menu():
    print("\n--- MENU AUTONOLEGGIO ---")
    print("1. Modifica nome del responsabile dell’autonoleggio")
    print("2. Carica automobili da file")
    print("3. Aggiungi nuova automobile (da tastiera)")
    print("4. Visualizza automobili ordinate per marca")
    print("5. Noleggia automobile")
    print("6. Termina noleggio automobile")
    print("7. Esci")
    return input("Scegli un'opzione >> ")

def main():
    autonoleggio = Autonoleggio("Polito Rent", "Alessandro Visconti")

    while True:
        scelta = menu()

        if scelta == "1":
            nuovo_responsabile = input("Inserisci il nuovo responsabile: ")
            # TODO: Aggiorna responsabile nel sistema
            autonoleggio = Autonoleggio ("Polito Rent", nuovo_responsabile)
            print (f"Il nuovo responsabile è: {autonoleggio.__str__()}")

        elif scelta == "2":
            while True:
                try:
                    file_path = input("Inserisci il path del file da caricare: ").strip()
                    autonoleggio.carica_file_automobili(file_path)
                    for row in autonoleggio.automobili:
                        automobile = Automobile(row[0], row[1], row[2], str(row[3]), str(row[4]))
                        print(automobile)
                    break
                except Exception as e:
                    print(e)

        elif scelta == "3":
            marca = input("Marca: ")
            modello = input("Modello: ")
            try:
                anno = int(input("Anno di Immatricolazione: ").strip())
                posti = int(input("Numero di posti: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno, pagine e sezione.")
                continue
            automobile = autonoleggio.aggiungi_automobile(marca, modello, anno, posti)
            print(f"Automobile aggiunta: {automobile}")

        elif scelta == "4":
            automobili_ordinate = autonoleggio.automobili_ordinate_per_marca()
            for a in automobili_ordinate:
                print(f'- {" | ".join (a)}')

        elif scelta == "5":
            id_auto = input("ID automobile: ")
            cognome_cliente = input("Cognome cliente: ")
            data = datetime.now().date()
            try:
                noleggio = autonoleggio.nuovo_noleggio(data, id_auto, cognome_cliente)
                print(f"Noleggio andato a buon fine: {noleggio}")
            except Exception as e:
                print(e)

        elif scelta == "6":
            id_noleggio = str (input("ID noleggio da terminare: "))
            try:
                risultato = autonoleggio.termina_noleggio(id_noleggio)
                if risultato :
                    print(f"Noleggio {id_noleggio} terminato con successo.")
                else :
                    print (f"Il noleggio {id_noleggio} non è mai stato effettuato.")

            except Exception as e:
                print(e)

        elif scelta == "7":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida!")

if __name__ == "__main__":
    main()

from pojisteny import Pojisteny                                         #externi modul
from pojistenci import Pojistenci


def main():
    pojistenci = Pojistenci()

    while True:                                                         #loop
        print("1 - Pridat noveho pojisteneho")                          #vyzva
        print("2 - Vypsat vsechny pojistene")
        print("3 - Vyhledat pojisteneho")
        print("4 - Konec")
        volba = input("Vyberte si akci (1-4): ")                        #input

        if volba == "1":
            jmeno = input("Zadejte jmeno pojisteneho: ")
            prijmeni = input("Zadejte prijmeni: ")
            vek = int(input("Zadejte vek: "))
            telefon = input("Zadejte telefonni cislo: ")
            pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
            pojistenci.pridat_pojistence(pojisteny)

        elif volba == "2":
            pojistenci.seznam_zobrazit()

        elif volba == "3":
            jmeno = input("Zadejte jmeno: ")
            prijmeni = input("Zadejte prijmeni: ")
            pojistenci.najit_pojisteneho(jmeno, prijmeni)

        elif volba == "4":
            break                                                               #vypnuti programu

        else:
            print("Neplatna volba.")


if __name__ == "__main__":
    main()

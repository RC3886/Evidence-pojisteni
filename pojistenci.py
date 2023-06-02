
class Pojistenci:
    def __init__(self):
        self.seznam_pojistencu = []                                         #prazdny seznam

    def pridat_pojistence(self, pojisteny):                                 #funkce pro pridani
        self.seznam_pojistencu.append(pojisteny)
        print("Data byla ulozena.")
        print()

    def najit_pojisteneho(self, jmeno, prijmeni):                           #funkce pro hledani
        for pojisteny in self.seznam_pojistencu:
            if pojisteny.jmeno == jmeno and pojisteny.prijmeni == prijmeni:
                print(f"{pojisteny.jmeno}\t{pojisteny.prijmeni}\t{pojisteny.vek}\t{pojisteny.telefon}")
            else:
                print("Hledany nebyl nalezen.")                                     #pro pripad, ze nebyl nalezen
        print()

    def seznam_zobrazit(self):                                              #vypsani seznamu
        for pojisteny in self.seznam_pojistencu:
            print(f"{pojisteny.jmeno}\t{pojisteny.prijmeni}\t{pojisteny.vek}\t{pojisteny.telefon}")
            print()
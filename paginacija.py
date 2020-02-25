
def paginacija(lista_stranica):

    prva_stranica = 0
    poslednja_stranica = int(input("Unesi koliko stranica zelis da prikazes: "))
    if poslednja_stranica < 0 or poslednja_stranica > len(lista_stranica):
        print("Unos nije validan,unesi ponovo: ")
        poslednja_stranica = int(input("Unesi koliko stranica zelis da prikazes"))

    else:

        N = poslednja_stranica
        print("N: ",N)

        print("Pocetne stranice:")
        ispisi_stranice(lista_stranica,prva_stranica,poslednja_stranica)

        print("\nPomeranje za jednu stranicu u napred: n")
        print("\nPomeranje za jednu stranicu u nazad: b")
        print("\nPomeranje za N stranica u napred: nn")
        print("\nPomeranje za N stranica u nazad: bb")
        print("\nIzlaz: e")

        opcija = input("Unesi opciju: ")
        while opcija != "e":
            if opcija.lower() not in ("n","b","nn","bb","e","c"):
                print("Izabrali ste pogresnu opciju")
                opcija = input("Unesi opciju: ")
            else:
                if opcija.lower() == "n":

                    if poslednja_stranica + 1 == len(lista_stranica):
                        print("Dosli ste do poslednje stranice")
                        prva_stranica = prva_stranica + 1
                        poslednja_stranica = poslednja_stranica + 1
                    elif poslednja_stranica == len(lista_stranica):
                        print("Ne mozete ici vise u napred")
                    else:
                        prva_stranica = prva_stranica + 1
                        poslednja_stranica = poslednja_stranica + 1
                elif opcija.lower() == "b":

                    if prva_stranica - 1 == 0:
                        print("Dosli ste do prve stranice")
                        poslednja_stranica = poslednja_stranica - 1
                        prva_stranica = prva_stranica -1
                    elif prva_stranica == 0:
                        print("Ne mozete ici vise u nazad")
                    else:
                        poslednja_stranica = poslednja_stranica - 1
                        prva_stranica = prva_stranica - 1
                elif opcija.lower() == "nn":
                        if poslednja_stranica + N > len(lista_stranica):
                            #dodaj = len(lista_stranica) - poslednja_stranica
                            #poslednja_stranica = poslednja_stranica + dodaj
                            #prva_stranica = poslednja_stranica - dodaj
                            prva_stranica = len(lista_stranica)-N
                            poslednja_stranica = len(lista_stranica)
                            print("Ne mozete ici vise u napred ")
                        else:
                            prva_stranica = prva_stranica + N
                            poslednja_stranica = poslednja_stranica + N

                elif opcija.lower() == "bb":
                        if prva_stranica - N <= 0:
                            #oduzmi = poslednja_stranica - N
                            #poslednja_stranica = poslednja_stranica - N
                            #prva_stranica = prva_stranica - oduzmi
                            prva_stranica = 0
                            poslednja_stranica = N
                            print("Ne mozete ici vise u nazad")
                        else:
                            poslednja_stranica = poslednja_stranica - N
                            prva_stranica = prva_stranica - N

                elif opcija.lower() == "c":
                    N  = int(input("Unesi broj stranica koji zelis da prikazes: "))
                    if int(N) < len(lista_stranica) and N>0:
                        prva_stranica = 0
                        poslednja_stranica = N
                    else:
                        print("Broj mora biti pozitivan i manji od broja stranica u listi")


                print("--Opcija uneta--")
                print("Trenutni prikaz sranica:")
                ispisi_stranice(lista_stranica, prva_stranica, poslednja_stranica)
                print(prva_stranica)
                print(poslednja_stranica)
                opcija = input("Unesi opciju: ")

def ispisi_stranice(lista,prva,poslednja):
        for i in range(prva,poslednja,1):
            print("Stranica ",i+1," : ",lista[i])

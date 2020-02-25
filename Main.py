from strukture.Trie import *
from strukture.graph import *
from funkcionalnosti.ParsiranjeUpita import ParsirajUpit
from funkcionalnosti.rangiranje import *
from funkcionalnosti.sortiranje import *
from funkcionalnosti.paginacija import *
import os
import time

def rang(lista_stranica,d):
    ukupan_rang1 = []
    for j in range(0, len(lista_stranica)):
        rang_pomocna = 0
        rang_pomocna2 = 0
        pomocna_promenljiva = 0
        for i in range(0, len(d)):
            if d[i].upper() in ("AND", "OR", "NOT"):
                continue
            else:
                pomocna_promenljiva = nadji_rang(lista_stranica[j], d[i])
                rang_pomocna += nadji_rang(lista_stranica[j], d[i])
                rang_pomocna2 += nadji_rang(lista_stranica[j], d[i])
        if pomocna_promenljiva < rang_pomocna2 and pomocna_promenljiva != 0:
            rang_pomocna += 5
        ukupan_rang1.append(rang_pomocna * 2)

    # 2)

    ukupan_rang2 = []
    for i in range(0, len(lista_stranica)):
        brojac = 0
        for j in graph[lista_stranica[i]].ulazni_linkovi:
            brojac = brojac + 1
        ukupan_rang2.append(brojac)

    # 3)
    dict = {}
    for i in range(0, len(lista_stranica)):
        nova_lista_stranica = []
        for key in graph:
            if lista_stranica[i] in graph[key].izlazni_linkovi:
                nova_lista_stranica.append(key)
        dict[lista_stranica[i]] = nova_lista_stranica

    ukupan_rang3 = []
    for i in dict:
        rang_pomocna = 0
        for j in dict[i]:
            pomocna_promenljiva = 0
            rang_pomocna2 = 0
            for k in range(0, len(d)):
                if d[k].upper() in ("AND", "OR", "NOT"):
                    continue
                else:
                    pomocna_promenljiva = nadji_rang(j, d[k])
                    rang_pomocna += nadji_rang(j, d[k])
                    rang_pomocna2 += nadji_rang(j, d[k])
            if pomocna_promenljiva < rang_pomocna2 and pomocna_promenljiva != 0:
                rang_pomocna += 5
        ukupan_rang3.append(rang_pomocna * 3)

    return ukupan_rang1,ukupan_rang2,ukupan_rang3


def dodaj_ulaznu_granu():
    for key1 in graph:
        for key2 in graph:
            for key2_izlazni in graph[key2].izlazni_linkovi:
                if key1 == key2_izlazni:
                    if key2 not in graph[key1].ulazni_linkovi:
                        graph[key1].ulazni_linkovi.append(key2)


if __name__ == "__main__":
    print("Trenutno se nalazite u direktorijumu: " + os.getcwd())
    userInput = 1
    while userInput != "0":
        print("")
        print("1. Unos direktorijuma i parsiranje fajlova")
        print("2. Unos i parsiranje upita")
        print("3. Ispis ulaznih/izlaznih linkova i rangiranje")
        print("4. Paginacija")
        print("0. Izlaz")
        userInput = input("Izaberite opciju: ")
        if userInput == "1":
            print("Unesite direktorijum koji zelite da parsirate: ")
            dir = input()
            while(not os.path.isdir(dir)):
                print("Direktorijum koji ste uneli ne postoji!")
                dir = input()
            if not os.path.isabs(dir):
                dir = os.path.abspath(dir)

            parser1 = Parser()
            root = Trie()
            g = Graph()
            graph = {}

            start = time.time()
            b = 0
            for dirpath, dirnames, files in os.walk(str(dir)):
                print(f"Pronadjen direktorijum: {dirpath}")
                for f in files:
                    if("%s\\%s"%(dirpath, f)).endswith(".html"):
                        parser1.parse("%s\\%s"%(dirpath, f))
                        graph["%s\\%s"%(dirpath,f)] = Linkovi()
                        graph["%s\\%s"%(dirpath,f)].izlazni_linkovi = parser1.links
                        g.dodaj_cvor("%s\\%s"%(dirpath, f))

                        print("Parsiram:  " + "%s\\%s"%(dirpath, f))
                        b = b + 1
                        for word in parser1.words:
                            root.dodavanjeReci(word, dirpath + '\\' + f)
            end = time.time()
            print("Vreme parsiranja: ")
            print(end - start)
            print("Broj rezuultata: ",b)
            for key in graph:
                g.dodaj_izlaznu_granu(key, graph[key].izlazni_linkovi)

            dodaj_ulaznu_granu()

            for key in graph:
                g.dodavanje_ulazne_grane(key,graph[key].ulazni_linkovi)
            print("********************** GRAF *********************")
            print(g.graph)
            print("*************************************************")

        if userInput == "2":
            # noinspection PyUnboundLocalVariable
            [s, d] = ParsirajUpit(root)
            s.ispis2()
        if userInput == "3":
            try:
                # noinspection PyUnboundLocalVariable
                s
            except NameError:
                print("Morate prvo uneti upit!")
                break
            # noinspection PyUnboundLocalVariable
            for key in graph:
                print("Kljuc: ")
                print(key)
                print("Ulazni link: ")
                print(graph[key].ulazni_linkovi)
                print("Izlazni linkovi: ")
                print(graph[key].izlazni_linkovi)

            # noinspection PyUnboundLocalVariable
            print(g.graph)
            print("Graf formiran")
            lista_stranica = s.ispis()

            rang_ret = rang(lista_stranica, d)
            ukupan_rang1 = rang_ret[0]
            ukupan_rang2 = rang_ret[1]
            ukupan_rang3 = rang_ret[2]

            for i in range(0, len(lista_stranica)):
                print("Stranica: ", lista_stranica[i], " rang1: ", ukupan_rang1[i], " rang2: ", ukupan_rang2[i]," rang3: ", ukupan_rang3[i],"ukupan rang: ", ukupan_rang1[i] + ukupan_rang2[i] + ukupan_rang3[i])
            print("\n\n")

            ukupan_rang = []
            for i in range(0, len(lista_stranica)):
                ukupan_rang.append(ukupan_rang1[i]+ukupan_rang2[i]+ukupan_rang3[i])
            rang = {}
            for i in range(0, len(lista_stranica)):
                rang[ukupan_rang[i]]=lista_stranica[i]

            merge_sort(ukupan_rang)
            print("Sortiranje zavrseno")


            print("Sortiran ispis: ")
            for i in range(0, len(lista_stranica)):
                 print(rang[ukupan_rang[i]],"   ",ukupan_rang[i])
        if userInput == "4":
            # noinspection PyUnboundLocalVariable
            paginacija(lista_stranica)
        if userInput =="0":
            break

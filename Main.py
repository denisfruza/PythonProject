from Trie import *
from parser2 import *
from graph import *
from ParsiranjeUpita import ParsirajUpit
from rangiranje import *
from set import *
import os
import time


if __name__ == "__main__":
    print("Trenutno se nalazite u direktorijumu: " + os.getcwd())
    print("Unesite direktorijum koji zelite da parsirate: ")
    dir = input()

    while(not os.path.isdir(dir)):
        print("Direktorijum koji ste uneli ne postoji!")
        dir = input()

    parser1 = Parser()
    root = Trie()
    start = time.time()
    g = Graph()
    graph = {}


    for dirpath, dirnames, files in os.walk(str(dir)):
        print(f"Pronadjen direktorijum: {dirpath}")
        for f in files:
            if("%s\\%s"%(dirpath,f)).endswith(".html"):
                parser1.parse("%s\\%s"%(dirpath,f))
                graph["%s\\%s"%(dirpath,f)] = Linkovi()
                graph["%s\\%s"%(dirpath,f)].izlazni_linkovi = parser1.links
                g.dodaj_cvor("%s\\%s"%(dirpath,f))

                print("Parsiram:  " + "%s\\%s"%(dirpath,f))
                for word in parser1.words:
                    root.dodavanjeReci(word, dirpath + '\\' +f)

    for key1 in graph:
        for key2 in graph:
            for key2_izlazni in graph[key2].izlazni_linkovi:
                if key1 == key2_izlazni:
                    if key2 not in graph[key1].ulazni_linkovi:
                        graph[key1].ulazni_linkovi.append(key2)
    for key in  graph:
       g.dodaj_granu(key,graph[key].izlazni_linkovi)



    for key in graph:
        print("Kljuc: ")
        print(key)
        print("Ulazni link: ")
        print(graph[key].ulazni_linkovi)
        print("Izlazni linkovi: ")
        print(graph[key].izlazni_linkovi)

    print(g.graph)
    print("Graf formiran")
    end = time.time()
    print("Vreme parsiranja: ")
    print(end-start)
    [s,d]= ParsirajUpit(root)
    lista_stranica = s.ispis()

    # --- RANGIRANJE ---
    ukupan_rang1 = []
    for j in range(0,len(lista_stranica)):
        rang_pomocna = 0
        rang_pomocna2 = 0
        pomocna_promenljiva = 0
        for i in range(0, len(d)):
            if d[i].upper() in ("AND","OR","NOT"):
                continue
            else:
                pomocna_promenljiva = nadji_rang(lista_stranica[j], d[i])
                rang_pomocna += nadji_rang(lista_stranica[j], d[i])
                rang_pomocna2 += nadji_rang(lista_stranica[j], d[i])
        if pomocna_promenljiva < rang_pomocna2:
            rang_pomocna += 5
        ukupan_rang1.append(rang_pomocna)
    #2)

    ukupan_rang2 = []
    for i in range(0,len(lista_stranica)):
        brojac = 0
        for j in graph[lista_stranica[i]].ulazni_linkovi:
            brojac = brojac + 1
        ukupan_rang2.append(brojac*2)

    #3)
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
            for k in range(0,len(d)):
                if d[k].upper() in ("AND", "OR", "NOT"):
                    continue
                else:
                    pomocna_promenljiva = nadji_rang(j,d[k])
                    rang_pomocna += nadji_rang(j,d[k])
                    rang_pomocna2 += nadji_rang(j,d[k])
            if pomocna_promenljiva < rang_pomocna2:
                rang_pomocna += 5
        ukupan_rang3.append(rang_pomocna)

    for i in range(0, len(lista_stranica)):
        print("Stranica: ", lista_stranica[i], " rang1: ", ukupan_rang1[i], " rang2: ", ukupan_rang2[i]," rang3: ", ukupan_rang3[i])
    print("\n\n")
    for i in range(0, len(lista_stranica)):
        print("Stranica: ", lista_stranica[i], " ukupan_rang: ", ukupan_rang1[i] + ukupan_rang2[i] + ukupan_rang3[i])
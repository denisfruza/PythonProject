from Trie import *
from parser2 import *
from graph import *
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
    stranica = list()
    izlazni_linkovi = list()
    lista_izlaznih_linkova = list()
    graph = {}


    for dirpath, dirnames, files in os.walk(str(dir)):
        print(f"Pronadjen direktorijum: {dirpath}")
        for f in files:
            if("%s\\%s"%(dirpath,f)).endswith(".html"):
                parser1.parse("%s\\%s"%(dirpath,f))
                stranica.append("%s\\%s"%(dirpath,f))
                izlazni_linkovi.append(parser1.links)
                lista_izlaznih_linkova.append(izlazni_linkovi)
               # print("Parsiram:  " + "%s\\%s"%(dirpath,f))
                for word in parser1.words:
                    root.dodavanjeReci(word, f)

    for i in range(0,len(stranica)):
        graph[stranica[i]] = Linkovi()
        graph[stranica[i]].izlazni_linkovi = lista_izlaznih_linkova[i]

    print("Pronalazenje ulaznih linkova: ")
    for key1 in graph:
        for key2 in graph:
            for key2_izlazni in graph[key2].izlazni_linkovi:
                if key1 == key2_izlazni:
                    if key2 not in graph[key1].ulazni_linkovi:
                        graph[key1].ulazni_linkovi.append(key2)

    for key in graph:
        print("Kljuc: "+key)

    print("Graf formiran")

    end = time.time()
    print("Vreme parsiranja: ")
    print(end-start)
from Trie import *
from parser2 import *
from graph import *
from ParsiranjeUpita import ParsirajUpit
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
                '''
                stranica.append("%s\\%s"%(dirpath,f))
                izlazni_linkovi.append(parser1.links)
                lista_izlaznih_linkova.append(izlazni_linkovi)
                '''
                graph["%s\\%s"%(dirpath,f)] = Linkovi()
                graph["%s\\%s"%(dirpath,f)].izlazni_linkovi = parser1.links
                g.dodaj_cvor("%s\\%s"%(dirpath,f))

                #print("Parsiram:  " + "%s\\%s"%(dirpath,f))
                for word in parser1.words:
                    root.dodavanjeReci(word, dirpath + '\\' +f)
    '''
    for i in range(0,len(stranica)):
        graph[stranica[i]] = Linkovi()
        graph[stranica[i]].izlazni_linkovi = lista_izlaznih_linkova[i]
    '''


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
    s.ispis()
    print(d)
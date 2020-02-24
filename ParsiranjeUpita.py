from set import *
from Trie import *

def ParsirajUpit(root):
    print("Unesite upit: ")
    upit = input()
    delovi = upit.split(' ')
    rezultat = [None] * len(delovi)
    logickiOperatori = ["AND", "OR", "NOT"]

    if len(delovi) == 0:
        print("Niste pravilno uneli upit! ")
        ParsirajUpit(root)
    elif len(delovi) > 3:
        for word in delovi:
            if word.upper() in logickiOperatori:
                print("Upit nije ispravan. Ukoliko upit ima logicki operator mora biti u formatu 'rec1 logOp rec2'")
                ParsirajUpit(root)
    else:
        # ako se logicki operator nalazi na prvom ili poslednjem mestu
        if delovi[0].upper() in logickiOperatori or delovi[-1].upper() in logickiOperatori:
            print("Upit nije ispravan. Ukoliko upit ima logicki operator mora biti u formatu 'rec1 logOp rec2'")
            ParsirajUpit(root)
    i = 0
    for word in delovi:
        if word.upper() in logickiOperatori:
            rezultat[i] = word.upper()
            i += 1
        else:
            if not root.pretragaReci(word):
                rezultat[i] = Set()
                i += 1
            else:
                rezultat[i] = root.pretragaReci(word)[2].intoSet()
                i += 1
    s = Set()
    i = 0
    #ukoliko je u pitanju skupovna operacija, prvo cemo uci u else i radi se unija(ubacuje se rec u set)
    #zatim  ce rez[1] biti logicki operator, i tada na osnovu logickog operatora radimo operaciju(presek,unija,komp) sa rez[2]
    #ukoliko u upitu ne postoje logicki operatori, ulazice samo u else i samo ce raditi uniju dok ne prodje kroz sve delove upita
    while i<len(rezultat):
        if rezultat[i] == logickiOperatori[0]:
            s = s.presek(rezultat[i+1])
            break
        elif rezultat[i] == logickiOperatori[1]:
            s = s.unija(rezultat[i+1])
            break
        elif rezultat[i] == logickiOperatori[2]:
            s = s.komplement(rezultat[i+1])
            break
        else:
            s = s.unija(rezultat[i])
            i += 1
    return s, delovi
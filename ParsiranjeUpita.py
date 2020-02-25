from Trie import *


# noinspection PyTypeChecker
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
    """ukoliko se radi o obicnom upitu (bez logickih operatora) ulazi se samo u else i unijom se dodaju rezultati 
    pretrage u S, a ukoliko se radi o upitu sa logickim operatorom, nakon sto naidjemo na logicki operator, 
    rade se operacije(presek, unija, komplement) i u S ubacuju rezultati pretrage za upit sa logickim operatorom """
    while i < len(rezultat):
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

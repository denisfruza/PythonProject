from parser2 import *

def nadji_rang(stranica,rec):
    brojac = 0
    p = Parser()
    parser = p.parse(stranica)
    for w in parser[1]:
        if w == rec:
            brojac = brojac + 1
    rang = brojac*2
    return rang

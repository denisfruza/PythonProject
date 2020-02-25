
class Graph():

    def __init__(self):
        self.graph = {}

    def sadrzi(self,v):
        if v in self.graph:
            return True
        else:
            return False

    def dodaj_cvor(self,v):

        if v not in self.graph:
            self.graph[v] = []
        else:
            print("Cvor vec postoji")

    def dodaj_izlaznu_granu(self,v,e):

        if not self.sadrzi(v):
            print("Ne postoji cvor")
        else:
            self.graph[v] = e

    def dodavanje_ulazne_grane(self,v,e):
        self.graph[v] = e




class Linkovi(Graph):

    def __init__(self):
        self.ulazni_linkovi = []
        self.izlazni_linkovi = []

class Graph():

    def __init__(self):
        self.graph = {}
        self.vertices_no = 0

    def dodaj_cvor(self,v):

        if v in self.graph:
            print("Cvor ", v, " vec postoji.")
        else:
            self.vertices_no = self.vertices_no + 1
            self.graph[v] = []

    def dodaj_granu(self,v1, v2, e):
        '''
        if v1 not in self.graph:
            print("Vertex ", v1, " ne postoji.")
        elif v2 not in self.graph:
            print("Vertex ", v2, " ne postoji.")
        else:
        '''
        temp = [v2, e]
        self.graph[v1].append(temp)

class Linkovi(Graph):

    def __init__(self):
        self.ulazni_linkovi = []
        self.izlazni_linkovi = []
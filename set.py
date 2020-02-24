import copy

class Set:

    def __init__(self):
        self.dict={}
        self.lista = []

    def __len__(self):
        return len(self.dict)

    def sadrzi(self,vrednost):
       for i in self.dict:
           if i == vrednost:
               return True
           else:
               return False

    def obrisi(self,vrednost):
        if self.sadrzi(vrednost):
            del self.dict[vrednost]

    def dodaj(self,vrednost):
        if not self.sadrzi(vrednost):
            self.dict[vrednost] = vrednost

    def unija(self,set2):

        kopija = copy.copy(self)

        if set2 is not None:
            for i in set2.dict:
                kopija.dodaj(i)

        return kopija

    def presek(self,set2):
        if len(self) > len(set2):
            self, set2 = set2, self
        result = Set()
        for x in self.dict:
            if x in set2.dict:
                result.dodaj(x)
        return result

    def komplement(self,set2):
        kopija = copy.copy(self)

        if set2 is not None:
            for i in set2.dict:
                if kopija.sadrzi(i):
                    kopija.obrisi(i)

        return kopija

    def ispis(self):
        for i in self.dict:
            print(i)
            self.lista.append(i)
        return self.lista


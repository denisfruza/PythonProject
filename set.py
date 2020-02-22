import copy

class Set:

    def __init__(self):
        self.dict={}

    def len(self):
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

        if not set2 is None:
            for i in set2.dict:
                kopija.dodaj(i)

        return kopija

    def presek(self,set2):

        presek = {}

        for i in self.dict:
            if i in set2.dict:
                    presek.dodaj(i)

        return presek

    def komplement(self,set2):
        kopija = copy.copy(self)

        if not set2 is None:
            for i in set2.dict:
                if kopija.sadrzi(i):
                    kopija.obrisi(i)

        return kopija

    def ispis(self):
	for i in self.dict:
	   print(i)
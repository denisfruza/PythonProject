from Trie import *
from parser2 import *
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
    links = []
    start = time.time()
    for dirpath, dirnames, files in os.walk(str(dir)):
        print(f"Pronadjen direktorijum: {dirpath}")
        for f in files:
            if("%s\\%s"%(dirpath,f)).endswith(".html"):
                parser1.parse("%s\\%s"%(dirpath,f))
                print("Parsiram:  " + "%s\\%s"%(dirpath,f))
                for word in parser1.words:
                    root.dodavanjeReci(word, f)

    end = time.time()
    print("Vreme parsiranja: ")
    print(end-start)
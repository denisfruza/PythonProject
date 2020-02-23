from collections import defaultdict
from  set import Set

class TrieNode:

    def __init__(self):
        self.children = defaultdict()
        self.endOfWord = (False, 0)
        self.links = {}  # recnik

    def intoSet(self):
        s = Set()
        for item in self.links:
            s.dodaj(item)
        return s

class Trie:

    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def charToIndex(self, char):
        return ord(char) - ord('a')  # ord() funkcija vraca unicode vrednost datog karaktera - integer (ASCII tabela)

    def dodavanjeReci(self, word, link):
        word = word.lower()
        node = self.root
        for i in range(len(word)):
            index = self.charToIndex(word[i])

            if index not in node.children:
                node.children[index] = self.getNode()
            node = node.children[index]
        n = node.endOfWord[1] + 1
        node.endOfWord = (True, n)

        if link not in node.links:
            node.links[link] = 1
        else:
            node.links[link] += 1

    def pretragaReci(self, word):
        word = word.lower()
        node = self.root
        for i in range(len(word)):
            index = self.charToIndex(word[i])

            if index not in node.children:
                return None
            node = node.children[index]
        return node.endOfWord, node.links, node

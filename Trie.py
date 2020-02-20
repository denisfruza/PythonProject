class TrieNode(object):
    def __init__(self,char):
        self.char = char
        self.children = []
        self.links = []

    def dodavanjeReci(self, word, link):
        word = word.upper()
        node=self
        for char in word:
            child_found = False
            for child in node.children:
                if child.char==char:
                    node=child
                    child_found = True
                    break
            if not child_found:
                new_node = TrieNode(char)
                node.children.append(new_node)
                node = new_node
                node.links.append(link)

    def pretragaReci(self, word):
        word=word.upper()
        node=self
        for char in word:
            child_found=False
            for child in node.children:
                if char == child.char:
                    node=child
                    child_found = True
                    break
                if not child_found:
                    return None
            return  node

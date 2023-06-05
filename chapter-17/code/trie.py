from typing_extensions import Self
from typing import Dict
from typing import List

class TrieNode:
    def __init__(self):
        self.children: Dict[str, Self | None] = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # O(K)
    # we say search takes O(K) where K is the size of the word
    # the search doesn't take longer with more data in the tri
    # it only increases when the word we are searching for gets bigger
    def search_prefix(self, word: str) -> TrieNode | None:
        current = self.root
        for character in word:
            next = current.children.get(character)
            if next is None:
                return None
            else:
                current = next
        return current

    def search(self, word: str) -> bool:
        current = self.root
        for character in word:
            next = current.children.get(character)
            if next is None:
                return False
            else:
                current = next
        return "*" in current.children.keys()

    def insert(self, word: str) -> None:
        current = self.root
        for character in word:
            next = current.children.get(character)
            if next is None:
                new_node = TrieNode()
                current.children[character] = new_node
                current = new_node
            else:
                current = next
        current.children["*"] = None

    def collect_all_words(self, node: TrieNode | None = None, word: str = "", words: List[str] = []):
        current = node or self.root
        for key, child_node in current.children.items():
            if key == "*":
                words.append(word)
            else:
                self.collect_all_words(child_node, word + key, words)
        return words

    def auto_complete(self, word: str) -> List[str] | None:
        current = self.search_prefix(word)
        if not current:
            return None
        return self.collect_all_words(current)
    

mytrie = Trie()
mytrie.insert("cat")
mytrie.insert("frog")
mytrie.insert("catnip")
mytrie.insert("carrot")

print(mytrie.collect_all_words())
print(mytrie.auto_complete("ca"))
print(mytrie.auto_complete("fr"))
print(mytrie.auto_complete("fr"))
print(mytrie.auto_complete("fr"))

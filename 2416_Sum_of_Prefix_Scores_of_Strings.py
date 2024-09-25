# https://leetcode.com/problems/sum-of-prefix-scores-of-strings

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0 

    
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1 

    def get_prefix_scores(self, word):
        node = self.root
        total_score = 0
        for char in word:
            if char in node.children:
                node = node.children[char]
                total_score += node.count
            else:
                break
        return total_score


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        result = []
        for word in words:
            result.append(trie.get_prefix_scores(word))

        return result


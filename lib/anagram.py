# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words_list):
        def is_anagram(word1, word2):
            return sorted(word1) == sorted(word2)
        
        return [word for word in words_list if is_anagram(self.word, word)]

    def __str__(self):
        return f"Anagram(word={self.word})"
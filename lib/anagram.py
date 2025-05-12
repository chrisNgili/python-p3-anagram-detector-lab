# your code goes here!
class Anagram:
    def __init__(self, wordlist):
        self.wordlist = wordlist

    def match(self, words):
        anagrams = []
        for word in words:    
            if  sorted(word) == sorted(self.wordlist) and word != self.wordlist:
                anagrams.append(word)
        return anagrams


print(Anagram("enlist").match(["listen", "poison", "hello"]))      
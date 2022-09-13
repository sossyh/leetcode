class Solution:
    def countVowels(self, word: str) -> int:
        vowels=['a','e','i','o','u']
        count=0
        n=len(word)
        for i in range(n):
            if word[i] in vowels:
                count += (i*(n-i)) + (n-i)
        return count
                
                
        
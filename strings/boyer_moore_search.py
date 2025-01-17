"""
The algorithm finds the pattern in given text using following rule.

The bad-character rule considers the mismatched character in Text. 
The next occurrence of that character to the left in Pattern is found, 

If the mismatched character occurs to the left in Pattern, 
a shift is proposed that aligns text block and pattern. 

If the mismatched character does not occur to the left in Pattern, 
a shift is proposed that moves the entirety of Pattern past 
the point of mismatch in the text. 

If there no mismatch then the pattern matches with text block.

Time Complexity : O(n/m)
    n=length of main string
    m=length of pattern string
"""


class BoyerMooreSearch:


    def __init__(self, text, pattern):
        self.text, self.pattern = text, pattern
        self.textLen, self.patLen = len(text), len(pattern)


    def mismatch_in_text(self, currentPos):
        """ finds the index of mis-matched character in text when compared with pattern from last

        Paremeters : 
            currentPos (int): current index position of text
        
        Returns :
            i (int): index of mismatched char from last in text
            -1 (int): if there is no mis-match between pattern and text block
        """

        for i in range(self.patLen-1, -1, -1):
            if self.pattern[i] != self.text[currentPos + i]:
                return currentPos + i
        return -1

        
    def bad_character_heuristic(self):
        # searches pattern in text and returns index positions 
        positions = []
        for i in range(self.textLen - self.patLen + 1):
            mismatch_index = self.mismatch_in_text(i)
            if mismatch_index == -1:
                positions.append(i)
        return positions

 
text = "ABAABA"
pattern = "AB" 
bms = BoyerMooreSearch(text, pattern)
positions = bms.bad_character_heuristic()

if len(positions) == 0:
    print("No match found")
else:
    print("Pattern found in following positions: ")
    print(positions)
    


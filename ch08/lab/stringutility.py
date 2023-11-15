class StringUtility():
    def __init__(self, string):
        self.original = string
        
    def __str__(self):
        return self.original
    
    def vowels(self):
        count = 0
        vowel = ["a","e", "i", "o","u", "A", "E", "I", "O", "U"]
        for i in self.original:
            if i in vowel:
               count += 1
                 
        if count < 5:
            return str(count) 
        else:
            return "many"
        
    def bothEnds(self):
        if len(self.original) <= 2:
            return ""
        else:
            return self.original[0:2] + self.original[-2:]
        
    def fixStart(self):
        if len(self.original) <= 1:
            return self.original
        else:
            char = self.original[0]
            self.replaced = self.original.replace(char, "*")
            self.replaced = char + self.replaced[1:]
            
            return self.replaced
        
    def asciiSum(self):
        total = 0
        for i in self.original:
            total += ord(i)
            
        return total
    
    def cipher(self):
        shifted = ""
        n = len(self.original)
        for i in self.original:         
            if i.isupper():
                shifted += chr((ord(i) + n - 65) % 26 + 65)
            elif i.islower():
                shifted += chr((ord(i) + n - 97) % 26 + 97)
            else:
                shifted += i
        
        return shifted
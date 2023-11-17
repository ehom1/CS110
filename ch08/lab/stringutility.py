class StringUtility():
    def __init__(self, string):
        self.original = string
        
    def __str__(self):
        """
        Returns the string when the object is converted into a string

        Returns:
            str: string that is inputted
        """
        return self.original
    
    def vowels(self):
        """
        Counts how many vowels there are in the string

        Returns:
            str: returns the number if less than 5, but many if there is equal to or more than 5 
        """
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
        """
        Returns the concatenation first 2 letters and the last 2 letters in the string

        Returns:
            str: the concatenated string
        """
        if len(self.original) <= 2:
            return ""
        else:
            return self.original[0:2] + self.original[-2:]
        
    def fixStart(self):
        """
        Returns the string with "*" for every character that repeats the first character in the string

        Returns:
            str: the modified string
        """
        if len(self.original) <= 1:
            return self.original
        else:
            char = self.original[0]
            self.replaced = self.original.replace(char, "*")
            self.replaced = char + self.replaced[1:]
            
            return self.replaced
        
    def asciiSum(self):
        """
        Returns the sum of the ascii values in each character of the string

        Returns:
            int: sum of the ascii  values 
        """
        total = 0
        for i in self.original:
            total += ord(i)
            
        return total
    
    def cipher(self):
        """
        Shifts each character of the string by the number characters in the string 

        Returns:
            str: the shifted string 
        """
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
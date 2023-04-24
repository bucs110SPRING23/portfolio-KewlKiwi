
class StringUtility:

    def __init__(self, string):
        self.str = string
    
    def __str__(self):
        return self.str
    
    def vowels(self):
        count = 0
        for i in range(len(self.str)):
            if self.str[i] == "a" or self.str[i] == "e" or self.str[i] == "i" or self.str[i] == "o" or self.str[i] == "u":
                count += 1
        
        if count > 4:
            return "many"
        else:
            return str(count)
        
    def bothEnds(self):
        if len(self.str) < 2:
            return ""
        else:
            return str(self.str[0] + self.str[1] + self.str[int(len(self.str) - 2)] + self.str[int(len(self.str) - 1)])

    def fixStart(self):
        if len(self.str) != 0:
            first = self.str[0]
        new = ""
        count = 0
        for i in range(len(self.str)):
            if self.str[i] == first and count != 0:
                new = new + "*"
            else:
                new = new + self.str[i]
            count += 1
        return new
    
    def asciiSum(self):
        result = 0
        for i in range(len(self.str)):
            result += ord(self.str[i])
        return result
        
    def cipher(self):
         shift = len(self.str)
         result = ""
         for i in range(shift):
             char = self.str[i]
             if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                new_pos = int((ord(char) - start + shift)) % 26
                char = chr(start + new_pos)
             result += char
         return result


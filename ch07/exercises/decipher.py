import math

def decipher(text):
    """
    Encrypts or decrypts a message using the Caesar cipher technique.

    args:
        text:str = the message to encrypt or decrypt
        shift:int = the number of positions to shift each letter
    return:
        :str = the encrypted or decrypted message
    """

    result = ""
    
    for char in text:
       
        if char.isalpha():
            # Determine the case of the character
            start = ord('A') if char.isupper() else ord('a')
            # Calculate the new position of the character after the shift
            if char.isupper():
                shift = 23
                new_pos = int((ord(char) - start + shift)) % 26
            else:
                shift = 9
                new_pos = int((ord(char) - start + shift)) % 26
            # Convert the new position back to a character
            char = chr(start + new_pos)
        if char.isupper():
            char = char.lower()
        else:
            char = char.upper()
        result += char
    return result


def main():

    fptr1 = open("encrypted-#B00769826.txt", "r")
    message = str(fptr1.read())
    print(decipher(message))
    fptr2 = open("decrypted.txt", "w")
    fptr2.write(decipher(message))
    fptr2.close()

main()
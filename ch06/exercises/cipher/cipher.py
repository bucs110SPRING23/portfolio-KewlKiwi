import math

def pi_cipher(text):
    """
    Encrypts or decrypts a message using the Caesar cipher technique.

    args:
        text:str = the message to encrypt or decrypt
        shift:int = the number of positions to shift each letter
    return:
        :str = the encrypted or decrypted message
    """

    count = 0
    fptr2 = open("pi.txt", "r")
    result = ""
    
    for char in text:
        count += 1
        if count == 40:
            fptr2.close()
            fptr2 = open("pi.txt", "r")

            shift = int(fptr2.readline())
        else:
            shift = int(fptr2.readline())

        if char.isalpha():
            # Determine the case of the character
            start = ord('A') if char.isupper() else ord('a')
            # Calculate the new position of the character after the shift
            new_pos = int((ord(char) - start + shift)) % 26
            # Convert the new position back to a character
            char = chr(start + new_pos)
        result += char
    return result



#print(caesar_cipher("well hello there", 5))
def main():
    fptr1 = open("message.txt", "r")
    message = str(fptr1.read())
    print(pi_cipher(message))
    fptr2 = open("encrypted.txt", "w")
    fptr2.write(pi_cipher(message))
main()
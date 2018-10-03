#caesar cipher decoder RIGHT SHIFT

decrypt =''
encrypt =''
key = int(input("ENTER THE KEY:- "))
print(key)
encrypt = input("ENTER THE ENCRYPTED MESSAGE:- ")
for letter in encrypt:
        if(letter.islower()):
                decrypt += chr((ord(letter) - 97 - key) % 26 + 97)
        elif(letter.isupper()):
                decrypt += chr((ord(letter) - 65 - key) % 26 + 65)
        else:
                decrypt +=letter
print("DECRYPTED MESSAGE IS:- ")
print(decrypt)

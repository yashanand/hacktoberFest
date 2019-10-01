#Reverse Cipher
#ROT13
#"hello !" =========>"! olleh"
#message = 'This is a secret Msg!'
message = input('ENTER THE MESSAGE: ')
translated = ''
s = len(message) - 1 #len() to find the string length
while s >=0:
        translated = translated + message[s]
        s = s - 1
print(translated)

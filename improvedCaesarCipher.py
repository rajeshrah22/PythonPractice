#input: Line of string and an integer encryption key(within 1 to 25 inclusive)
#processing: Shifts the ASCII value of 
#  each alphabetical character by the encryption key. When the ascii is shifted past 'Z'  or 'z' ascii code, it is
#    brought back to 'A' or 'a' ascii code. All non alphabetical characters will remain untouched
#output: encrypted message


def caesarCypherImp(message, encryptionKey):
    text = ''
    for char in message:
        if not char.isalpha():
            text += char
            continue
        code = ord(char) + encryptionKey
        if char.isupper():
            if code > 90:
                code = 64 + code % 90
        else:
            if code > 122:
                code = 96 + code % 122
        text += chr(code)
    return text

cipher = input("Enter the message you want encrypted: ")
encryptionKey = int(input("Enter the shift key: "))
            
print(caesarCypherImp(cipher, encryptionKey))

    

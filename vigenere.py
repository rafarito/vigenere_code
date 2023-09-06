alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def decode(key: str, cypher:str):
    key = key.upper()
    cypher = cypher.upper()
    key_index = 0
    key_lenght = len(key)
    decrypt = ""
    for letter in cypher:
        if(letter == " "):
            decrypt += " "
        else:
            if(alphabet.index(letter) - alphabet.index(key[key_index]) < 0):
                alphabet_index = alphabet.index(letter) - alphabet.index(key[key_index]) + len(alphabet)
            else:
                alphabet_index = alphabet.index(letter) - alphabet.index(key[key_index])
            decrypt += alphabet[alphabet_index]
            key_index += 1
            if(key_index == key_lenght):
                key_index = 0
    return decrypt 


print(decode("alo","blhaeo e mcm"))
class Viginere:

    def __init__(self) -> None:
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def defaultAlphabet(self):
        self.setAlphabet("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def setAlphabet(self, alph : str):
        self.alphabet = alph

    def getAlphabet(self):
        return self.alphabet

    def verificaAlphabeto(self, frase : str):
        for letter in frase:
            for letter2 in self.alphabet:
                if (letter == letter2):
                    return
        raise Exception ("letra não consta no alphabeto")

    
    def decode(self ,key: str, cypher:str):
        key = key.upper()
        key = key.replace(" ","")
        cypher = cypher.upper()
        self.verificaAlphabeto(cypher)
        key_index = 0
        key_lenght = len(key)
        decrypt = ""
        for letter in cypher:
            if(letter == " "):
                decrypt += " "
            else:
                if(self.alphabet.index(letter) - self.alphabet.index(key[key_index]) < 0):
                    alphabet_index = self.alphabet.index(letter) - self.alphabet.index(key[key_index]) + len(self.alphabet)
                else:
                    alphabet_index = self.alphabet.index(letter) - self.alphabet.index(key[key_index])
                decrypt += self.alphabet[alphabet_index]
                key_index += 1
                if(key_index == key_lenght):
                    key_index = 0
        return decrypt

    def encode(self ,key: str, text:str):
        key = key.upper()
        key = key.replace(" ","")
        text = text.upper()
        self.verificaAlphabeto(text)
        key_index = 0
        key_lenght = len(key)
        encrypt = ""
        for letter in text:
            if(letter == " "):
                encrypt += " "
            else:
                if(self.alphabet.index(letter) + self.alphabet.index(key[key_index]) >= 26):
                    alphabet_index = self.alphabet.index(letter) + self.alphabet.index(key[key_index]) - len(self.alphabet)
                else:
                    alphabet_index = self.alphabet.index(letter) + self.alphabet.index(key[key_index])
                encrypt += self.alphabet[alphabet_index]
                key_index += 1
                if(key_index == key_lenght):
                    key_index = 0
        return encrypt

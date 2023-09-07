from vigenere import Viginere

vi = Viginere()
senha = "demolay"
mensagem = "batata com pepino"
crip = vi.encode(senha,mensagem)
print(crip)
print(vi.decode(senha,crip))
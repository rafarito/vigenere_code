from vigenere import Viginere
import PySimpleGUI as sg

sg.theme('topanga')
def Inicial():              # essas funções são responsaveis por montar os layouts
    layout = [  [sg.Text('O que deseja fazer?')],
                [sg.Button('Encriptar'), sg.Button('Decriptar'),sg.Button('Mudar alfabeto'), sg.Button('Sair')] ]
    return sg.Window("Janela Inicial", layout = layout)

def Encriptar():
    layout = [[sg.Text('Digite o texto para encriptar: '), sg.Input(key='texto', size=(50))],
              [sg.Text("digite a chave: "), sg.Input(key= 'key', size= 50)],
              [sg.Button('Confirma'), sg.Button('Voltar')]]
    return sg.Window("Encriptar", layout = layout)

def Decriptar():
    layout = [[sg.Text('Digite o texto para decriptar: '), sg.Input(key='texto', size=(50))],
              [sg.Text("digite a chave: "), sg.Input(key= 'key', size= 50)],
              [sg.Button('Confirma'), sg.Button('Voltar')]]
    return sg.Window("Decriptar", layout = layout)

def MudarAlfabeto():
    layout = [[sg.Text('Digite o novo alfabeto: '), sg.Input(key='texto', size=(50))],
              [sg.Button('Confirma'), sg.Button('Voltar'), sg.Button('Resetar alfabeto')]]
    return sg.Window("Mudar Alfabeto", layout = layout)

def Resultado(text):
    layout = [[sg.Text('O resultado da operação foi: '), sg.Text(text= text)],
              [sg.Button('Sair'), sg.Button('Voltar'),]]
    return sg.Window("Resultado", layout = layout)

#   os layouts são inicializados
inicial = Inicial()
inicial.finalize()
encriptar = None
decriptar = None
alfabeto = None
resultado = None
vi = Viginere()


while True:
    window, event, values = sg.read_all_windows()

    if event == sg.WIN_CLOSED or event == 'Sair':   # fecha a janela se o X for pressionado ou se um botão "Sair" for pressionado
        break

    if window == inicial:   #   a partir daqui é verificado qual botão foi apertado e qual janela deve aparecer
        if event == 'Encriptar':
            inicial.hide()
            encriptar = Encriptar()
            encriptar.finalize()
            encriptar.un_hide()

        elif event == 'Decriptar':
            inicial.hide()
            decriptar = Decriptar()
            decriptar.finalize()
            decriptar.un_hide()

        elif event == 'Mudar alfabeto':
            inicial.hide()
            alfabeto = MudarAlfabeto()
            alfabeto.finalize()
            alfabeto.un_hide()

    #   se o usuário apertar em voltar ele retorna pra pagina inicial
    if window in [encriptar,decriptar,alfabeto,resultado] and event == "Voltar":
        window.hide()
        inicial.un_hide()
    
    #   realiza a operção de cecriptar, encriptar ou mudar o alfabeto utilizado
    if window in [encriptar,decriptar,alfabeto] and event == "Confirma":
        title = window.TKroot.title()
        if title in ["Decriptar","Encriptar"]:
            result = vi.operacao(title,key=values['key'],text=values['texto'])
            window.hide()
            resultado = Resultado(result)
            resultado.finalize()
            resultado.un_hide()
        else:
            vi.operacao(title,text=values['texto'])
            window.hide()
            inicial.un_hide()

    #   o que acontece quando o botão "resetar alfabeto é utilizado"
    if window == alfabeto and event == "Resetar alfabeto":
        vi.defaultAlphabet()
        window.hide()
        inicial.un_hide()

window.close()
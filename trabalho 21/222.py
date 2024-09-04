import PySimpleGUI as sg
aproveitamento=[]
armazenamento=[]
erro=''
layout = [  
    [sg.Text("BEM VINDO A ESCOLA OZ")],
    [sg.Text("Digite o nome do aluno")],
    [sg.InputText(key='nome')],
    [sg.Text("Digite a nota do aluno")],
    [sg.InputText(key='numero')],
    [sg.Text("Digite a nota2 do aluno")],
    [sg.InputText(key='numero2')],
    [sg.Text('', key="erro")],
    [sg.Button('Enviar'), sg.Button('ADC.Aluno'), sg.Button('Cancel')]
]


window = sg.Window('Hello Example', layout)


while True:
    event, values = window.read()
    nome = values['nome']
    numero = values['numero']
    numero2 = values['numero2']
    
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    if event == 'Enviar':
     sg.popup("RESULTADO", nome, aproveitamento, situação)
     window['RESULTADO'].update('')
    
     if event == "ADC.Aluno":
        if nome.isdigit():
            window["erro"].update("ERRO\nDigite um texto válido")
            erro = 'EXISTE UM ERRO'
        elif len(nome) < 3:
            window["erro"].update("ERRO\nSeu nome tem que ter no mínimo 3 letras")
            erro = 'EXISTE UM ERRO'
        elif not (numero.replace(".", "").isdigit() and numero2.replace(".", "").isdigit()):
            window["erro"].update("ERRO\nDigite notas válidas")
            erro = 'EXISTE UM ERRO'
        elif not nome or not numero or not numero2:
            window["erro"].update("ERRO\nPreencha todos os campos!")
            erro = 'EXISTE UM ERRO'

        else:

            erro = ''
            nota1 = float(numero)
            nota2 = float(numero2)
            media = (nota1 + nota2) / 2
            
            if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
                if media >= 9:
                    aproveitamento = "A"
                elif media >= 8:
                    aproveitamento = "B"
                elif media >= 7:
                    aproveitamento = "C"
                elif media >= 6:
                    aproveitamento = "D"
                elif media >= 5:
                    aproveitamento = "E"
                else:
                    aproveitamento = "F"

                
                situação = "Aprovado" if media >= 7 else "Reprovado"
                sg.popup(f"Situação: {situação}\nAproveitamento: {aproveitamento}")
                window['nome'].update('')
                window['numero'].update('')
                window['numero2'].update('')
     
            else:
                window["erro"].update("ERRO\nAs notas devem estar entre 0 e 10")





 

window.close()
import PySimpleGUI as sg

# All the stuff inside your window.
layout = [  [sg.Text("BEM VINDO A ESCOLA OZ")],
            [sg.Text("Digite o nome do aluno")],
            [sg.InputText(key='nome')],
            [sg.Text("digite a nota do aluno")],
            [sg.InputText(key='numero')],
            [sg.Text('',key= "erro")],
            [sg.Text("digite a nota2 do aluno")],
            [sg.InputText(key='numero2')],
            [sg.Button('Enviar'), sg.Button('ADC.Aluno'), sg.Button('Cancel')]
]

      
# Create the Window
window = sg.Window('Hello Example', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    nome = values['nome']
    numero = values ['numero']
    numero2 = values ['numero2']
    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    if event == 'Ok':
        sg.popup()
    if event == "Enviar":
        sg.popup("RESULTADO")
    if event == "ADC.Aluno": 
        if nome.isdigit()==True:
            window["erro"].update("ERRO\n digite um texto")
        elif len(nome) <=3:
            window["erro"].update("ERRO\n seu nome tem que ter minimo 3 letras")
        if numero.replace(".","").isdigit() or numero2.replace(".","").isdigit():

        
            nota1 = values[numero]
            nota2 = values[numero2]
            media = (numero + numero2) / 2
            if  numero <=10 and numero2 <=10 :
                          
                if media >= 7:
                    situação = "Aprovado"

                elif media <=7:
                    situação = "reprovado"

                if media <= 10 and media >= 9 :
                    aproveitamento = "A"

                elif media <= 9 and media >= 8 :
                    aproveitamento = "B"

                elif media <= 8 and media >= 7 :
                    aproveitamento = "C"

                elif media <= 7 and media >= 6 :
                    aproveitamento = "D"

                elif media <= 6 and media >= 5 :
                    aproveitamento = "E"

                elif media <= 5 :
                    aproveitamento = "F"


        else: 
            window["erro"].update("corrija a nota inserida")

    1

    


      
            
            

window.close()


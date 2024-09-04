import PySimpleGUI as sg

armazenamento = []

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
    
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    if event == 'Enviar':
        if armazenamento:
            texto = ''
            for aluno in armazenamento:
                texto += f"Nome: {aluno['nome']}, Média: {aluno['media']:.2f}, Situação: {aluno['situacao']}\n"
            sg.popup("RESULTADO", texto)
        else:
            sg.popup("RESULTADO", "Nenhum dado para exibir.")
        window['erro'].update('')
    
    if event == "ADC.Aluno":
        nome = values['nome']
        numero = values['numero']
        numero2 = values['numero2']
       
        if nome.isdigit():
            window["erro"].update("ERRO\nDigite um texto válido")
        elif nome == "" or numero == "" or numero2 == "":
            window["erro"].update("ERRO\nPreencha todos os campos!")
        elif len(nome) < 3:
            window["erro"].update("ERRO\nSeu nome tem que ter no mínimo 3 letras")
        elif not (numero.replace(".", "", 1).isdigit() and numero2.replace(".", "", 1).isdigit()):
            window["erro"].update("ERRO\nDigite notas válidas")
        else:
            try:
                nota1 = float(numero)
                nota2 = float(numero2)
                if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
                    media = (nota1 + nota2) / 2
                    
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
                    
                    situacao = "Aprovado" if media >= 7 else "Reprovado"
                    
                    armazenamento.append({'nome': nome, 'nota1': nota1, 'nota2': nota2, 'media': media, 'situacao': situacao})
                    
                    sg.popup(f"Situação: {situacao}\nAproveitamento: {aproveitamento}")
                    window['nome'].update('')
                    window['numero'].update('')
                    window['numero2'].update('')
                else:
                    window["erro"].update("ERRO\nAs notas devem estar entre 0 e 10")
            except ValueError:
                window["erro"].update("ERRO\nErro inesperado ao adicionar dados.")

window.close()
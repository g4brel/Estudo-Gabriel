

def Card():
    
    layout = [
        [sg.Image(filename=pasta, subsample=9)],
        [sg.Text('Qual é a bandeira do seu cartão')],
        [sg.Combo(['Mastercard', 'Visa', 'Elo', 'American Express', 'Hipercard', 'Alelo'], key='-Bandeira-')],
        [sg.Text('Digite o Número do Cartão')],
        [sg.Input(key='-NumeroCartao-')],
        [sg.Button('Enviar'), sg.Button('Fechar')]
    ]
    
    
    window = sg.Window('Academia GM FIT', layout, background_color='black', size=(600, 300))
    
    while True:
        
        event, values = window.read()
        

        if event in (sg.WIN_CLOSED, 'Fechar'):
            break
        
        
        if event == 'Enviar':
            bandeira = values['-Bandeira-']
            numero_cartao = values['-NumeroCartao-']
            sg.popup(f'Bandeira: {bandeira}\nNúmero do Cartão: {numero_cartao}')
    
    
    window.close()


Card()


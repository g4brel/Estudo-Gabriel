import PySimpleGUI as sg
import os 
usuarios_db = []

def principal():
    armazenamento = []
    erro = ''
    texto = ''
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

    window = sg.Window('Sistema Escolar', layout)

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
                erro = 'EXISTE UM ERRO'
            elif values["nome"] == "" or values["numero"] == "" or values["numero2"] == "":
                window["erro"].update("ERRO\nOs campos estão vazios")
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
                        
                        situação = "Aprovado" if media >= 7 else "Reprovado"
                        sg.popup(f"Aluno inserido com sucesso")
                        
                        armazenamento.append({'nome': nome, 'nota1': nota1, 'nota2': nota2, 'media': media, 'situacao': situação })
                        window['nome'].update('')
                        window['numero'].update('')
                        window['numero2'].update('')
                    else:
                        window["erro"].update("ERRO\nAs notas devem estar entre 0 e 10")
                except ValueError:
                    window["erro"].update("ERRO\nErro inesperado ao adicionar dados.")
                    erro = 'EXISTE UM ERRO'

    window.close()


def tela2():
    layout = [
        [sg.Text("BEM VINDO A ESCOLA OZ ")],
        [sg.Text("Tela de Login")],
        [sg.Text("Nome do professor")],
        [sg.InputText(key='nome')],
        [sg.Text("Email")],
        [sg.InputText(key='email')],
        [sg.Text("Senha")],
        [sg.InputText(key='senha', password_char='*')],
        [sg.Text('', key='erro_login')],
        [sg.Button('Login'), sg.Button('Primeiro registro'), sg.Button('Cancelar')]
    ]
    window = sg.Window('Login', layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Cancelar':
            break
        if event == 'Primeiro registro':
            window.close()
            tela_registro()
            
        if event == 'Login':
            nome = values['nome']
            email = values['email']
            senha = values['senha']

            
            if nome == '' and email == '' and senha == '':
                sg.popup(' Usuario não cadastrado ')

            elif len(nome) < 3:
                window["erro_login"].update("ERRO\nSeu nome tem que ter no mínimo 3 letras")

            elif len(senha) < 8:
                window["erro_login"].update("ERRO\n sua senha tem que ter no minimo 8 caracteres")

            if os.path.exists('dados_armazenamento.txt'):
                with open('dados_armazenamento.txt', 'r') as file:
                    for i in file:
                        login,password = i.strip().split(',')
                        if login == nome and password == senha:

                            sg.popup('Login bem-sucedido!')
                            window.close()
                            principal()

       
            else:
                window['erro_login'].update('Não existe usuarios cadastrados')

    window.close()


def validar_campos(nome, email, cpf, senha, confirma_senha):
    if not nome or not email or not cpf or not senha or not confirma_senha:
        return 'Todos os campos são obrigatórios'
    
    if len(nome) < 3:
        return 'Nome muito curto'
    
    if '@' not in email:
        return 'Email inválido'
    
    if not (cpf.isdigit() and len(cpf) == 11):
        return 'CPF inválido'
    
    if senha != confirma_senha:
        return 'As senhas não coincidem'
    
    with open('dados_armazenamento.txt', 'a') as arquivo:
        arquivo.write(f"{nome},{senha}\n")
    return None


def tela_registro():
    global usuarios_db
    layout = [
        [sg.Text("Tela de Registro")],
        [sg.Text("Nome de usuário")],
        [sg.InputText(key='usuario')],
        [sg.Text("Email")],
        [sg.InputText(key='email')],
        [sg.Text("CPF")],
        [sg.InputText(key='cpf')],
        [sg.Text("Senha")],
        [sg.InputText(key='senha', password_char='*')],
        [sg.Text("Confirmar senha")],
        [sg.InputText(key='confirma_senha', password_char='*')],
        [sg.Text('', key='erro_registro')],
        [sg.Button('Registrar'), sg.Button('Voltar')]
    ]
    window = sg.Window('Registro', layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Voltar':
            window.close()
            tela2()
    
        
        if event == 'Registrar':
            usuario = values['usuario']
            email = values['email']
            cpf = values['cpf']
            senha = values['senha']
            confirma_senha = values['confirma_senha']
            
            erro = validar_campos(usuario, email, cpf, senha, confirma_senha)

            print('aa')
            usuarios_db.append({'usuario': usuario, 'cpf': cpf, 'senha': senha})
            sg.popup('Registro bem-sucedido!')
            window.close()
            tela2()
            

        window.close()


tela2()
import PySimpleGUI as sg


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
            # variaveis do input 
            nome = values['nome']
            numero = values['numero']
            numero2 = values['numero2']
        
        # Validacoes 

            if nome.isdigit():
                window["erro"].update("ERRO\nDigite um texto válido")
                erro = 'EXISTE UM ERRO'
            elif values["nome"] =="" or values["numero"] ==""  or values ["numero2"] =="" :
                window ["erro"].update("ERRO \n os campos estao vazios")

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
                        print (armazenamento)
                        window['nome'].update('')
                        window['numero'].update('')
                        window['numero2'].update('')
                    else:
                        window["erro"].update("ERRO\nAs notas devem estar entre 0 e 10")
                except ValueError:
                    window["erro"].update("ERRO\nErro inesperado ao adicionar dados.")
                    erro = 'EXISTE UM ERRO'

    window.close()

usuarios_db = {}
import PySimpleGUI as sg
import re

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
        [sg.Button('Login'), sg.Button('Registrar'), sg.Button('Cancelar')]
    ]
    window = sg.Window('Login', layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Cancelar':
            break
        if event == 'Registrar':
            window.close()
            tela_registro()
            return
        if event == 'Login':
            nome = values['nome']
            email = values['email']
            senha = values['senha']
            
            # Verificar se o email está no banco de dados e a senha está correta
            if email in usuarios_db and usuarios_db[email]['senha'] == senha:
                sg.popup('Login bem-sucedido!')
            else:
                window['erro_login'].update('Email ou senha inválidos')

    window.close()

# Função para validar os campos de entrada
def validar_campos(nome, email, cpf, senha, confirma_senha):
    # Verificar se todos os campos são preenchidos
    if not nome or not email or not cpf or not senha or not confirma_senha:
        return 'Todos os campos são obrigatórios'
    
    # Validar nome
    if not re.match(r'^[A-Za-z\s]+$', nome):
        return 'Nome inválido'
    
    # Validar email
    regex_email = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if not re.match(regex_email, email):
        return 'Email inválido'
    
    # Validar CPF
    if not (cpf.isdigit() and len(cpf) == 11):
        return 'CPF inválido'
    
    # Validar senhas
    if senha != confirma_senha:
        return 'As senhas não coincidem'
    
    return None


#tela registro
def tela_registro():
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
            return
        if event == 'Registrar':
            usuario = values['usuario']
            email = values['email']
            cpf = values['cpf']
            senha = values['senha']
            confirma_senha = values['confirma_senha']
            
            # Validar campos
            erro = validar_campos(usuario, email, cpf, senha, confirma_senha)
            
            if erro:
                window['erro_registro'].update(erro)
            elif email in usuarios_db:
                window['erro_registro'].update('Email já cadastrado')
            else:
                usuarios_db[email] = {'usuario': usuario, 'cpf': cpf, 'senha': senha}
                sg.popup('Registro bem-sucedido!')
                window.close()
                tela2()
                return

    window.close()

tela2()

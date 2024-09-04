import PySimpleGUI as sg
import re

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

# Função para a tela de Login
def tela_login():
    layout = [
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

# Função para a tela de Registro
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
            tela_login()
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
                tela_login()
                return

    window.close()

# Banco de dados em memória para usuários
usuarios_db = {}

# Iniciar o programa na tela de Login
tela_login()
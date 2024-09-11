# Estudo-Gabriel
**Documentação do Sistema Escolar**

**Descrição do Projeto**
O sistema escolar desenvolvido é uma aplicação gráfica que permite o gerenciamento de informações de alunos e professores em uma escola fictícia. Utiliza a biblioteca PySimpleGUI para criar interfaces gráficas intuitivas e interativas. A aplicação possui três funcionalidades principais: a tela de login para professores, a tela de registro para novos usuários e a tela principal para o gerenciamento dos dados dos alunos.

**Funcionalidades**
Tela de Login

Permite aos professores fazerem login no sistema.
Inclui campos para o nome, e-mail e senha.
Realiza a validação dos dados de login comparando com registros armazenados em um arquivo de texto (dados_armazenamento.txt).
Tela de Registro

Permite o registro de novos usuários (professores) no sistema.
Inclui campos para nome de usuário, e-mail, CPF, senha e confirmação de senha.
Realiza a validação dos dados de entrada e armazena as informações no arquivo dados_armazenamento.txt.
Tela Principal

Permite a inserção e visualização de dados de alunos, incluindo nome e notas.
Calcula a média das notas e determina a situação do aluno (aprovado ou reprovado).
Exibe as informações dos alunos cadastrados em uma janela pop-up.
Tecnologias Utilizadas
Python: Linguagem de programação usada para o desenvolvimento do sistema.
PySimpleGUI: Biblioteca para a criação de interfaces gráficas. Documentação: PySimpleGUI Documentation
Os: Biblioteca padrão do Python utilizada para manipulação de arquivos e verificação de existência de arquivos.
Funcionalidade do Código
Tela de Login

O usuário entra com o nome, e-mail e senha.
Se o usuário não estiver cadastrado ou as informações estiverem incorretas, exibe mensagens de erro apropriadas.
Caso o login seja bem-sucedido, o sistema redireciona para a tela principal.
Tela de Registro

O usuário fornece informações necessárias para o registro (nome, e-mail, CPF, senha).
Realiza validações como comprimento do nome, formato do e-mail, e se as senhas coincidem.
Registra o usuário no arquivo dados_armazenamento.txt após validação bem-sucedida.
Tela Principal

O usuário pode adicionar alunos com nome e duas notas.
Calcula a média das notas e determina a situação (aprovado/reprovado) com base na média.
Exibe os dados dos alunos e permite a visualização de todos os alunos cadastrados.
Bibliotecas e Documentação
PySimpleGUI: Documentação
Os: Documentação
Este documento fornece uma visão geral detalhada sobre as funcionalidades e o funcionamento do sistema, incluindo as tecnologias e bibliotecas utilizadas.


O Sistema Escolar é uma aplicação gráfica desenvolvida em Python para gerenciar informações de alunos e professores em uma escola fictícia. Utilizando a biblioteca PySimpleGUI, a aplicação oferece uma interface intuitiva para login, registro e gerenciamento de dados de alunos.

**Funcionalidades**
Tela de Login

Autentica professores com nome, e-mail e senha.
Valida as credenciais contra um arquivo de texto (dados_armazenamento.txt).
Tela de Registro

Permite o registro de novos usuários (professores).
Valida informações como nome, e-mail, CPF e senha antes de armazenar os dados em dados_armazenamento.txt.
Tela Principal

Gerencia informações dos alunos, incluindo nome e notas.
Calcula a média das notas e determina a situação do aluno (aprovado/reprovado).
Exibe os dados dos alunos em uma janela pop-up.
Tecnologias Utilizadas
Python: Linguagem de programação principal.
PySimpleGUI: Biblioteca para criar interfaces gráficas. Documentação
Os: Biblioteca padrão do Python para manipulação de arquivos. Documentação


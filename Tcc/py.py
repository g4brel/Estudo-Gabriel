import re

def valida_telefone(telefone):
    # Expressão regular para validar o formato +55 (código do país) seguido de 2 dígitos (DDD) e 9 dígitos do número
    padrao = r'^\+55\d{2}\d{9}$'
    
    # Verifica se o número corresponde ao padrão
    if re.match(padrao, telefone):
        return True
    else:
        return False

# Exemplo de uso
telefone = input("Digite um número de telefone com o código do Brasil (+55): ")
if valida_telefone(telefone):
    print("Número de telefone válido!")
else:
    print("Número de telefone inválido!")

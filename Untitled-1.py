def get_cpf(cpf: str) -> bool:
        clean = cpf.replace('.', '').replace('-', '').replace('/', '')
        if len(clean) == 11 and clean.isdigit() and len(set(clean)) > 1:
            return True

def get_cnpj(cnpj: str) -> bool:
        clean = cnpj.replace('.', '').replace('/', '').replace('-', '')
        if len(clean) == 14 and clean.isdigit() and len(set((clean))) > 1:
            return True

def calc_digitos(digitos: str):
    testado = digitos.split()
    return testado

'''
while True:
    entrada = input('Digite seu CPF/CNPJ:\n')
    if get_cpf(entrada):
        print('CPF Válido')
        break
    elif get_cnpj(entrada):
        print('CNPJ Valido')
        break
    else:
        print('CPF/CNPJ Inválido!')
'''

calc_digitos('1234567890')
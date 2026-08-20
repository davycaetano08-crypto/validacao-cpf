def get_cpf(cpf: str) -> bool:
        clean = cpf.replace('.', '').replace('-', '').replace('/', '')
        if len(clean) == 11 and clean.isdigit() and len(set(clean)) > 1:
            return True

def get_cnpj(cnpj: str) -> bool:
        clean = cnpj.replace('.', '').replace('/', '').replace('-', '')
        if len(clean) == 14 and clean.isdigit() and len(set((clean))) > 1:
            return True

def calc_digitos(digitos: str, pesos: list) -> int:
    total = 0
    for digito, peso in zip(digitos, pesos):
        digito = int(digito)
        total += digito * peso
    return total

def calc_verif_digit(soma: int) -> int:
    resto = soma % 11
    if resto < 2:
        digito = 0
    else:
        digito = 11 - resto
    return digito

def validar_cpf_comp(cpf: str) -> bool:
    cpf_limpo = cpf.replace('.', '').replace('-', '')

    if not (len(cpf_limpo) == 11 and cpf_limpo.isdigit() and len(set(cpf_limpo)) > 1):
        return False
    
    clean = cpf_limpo[:9]
    pesos1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]

    soma1 = calc_digitos(clean, pesos1)
    digito1 = calc_verif_digit(soma1)

    clean_10 = clean + str(digito1)

    pesos2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    soma2 = calc_digitos(clean_10, pesos2)
    digito2 = calc_verif_digit(soma2)

    clean_11 = clean_10 + str(digito2)

    return clean_11 == cpf_limpo


while True:
    entrada = input('Digite seu CPF/CNPJ:\n')
    if validar_cpf_comp(entrada):
        print('CPF Válido')
        break
    elif get_cnpj(entrada):
        print('CNPJ Valido')
        break
    else:
        print('CPF/CNPJ Inválido!')


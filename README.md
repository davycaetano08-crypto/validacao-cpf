# Validador de CPF/CNPJ

Script em Python que valida documentos brasileiros (CPF e CNPJ) usando o algoritmo oficial dos dígitos verificadores (módulo 11), não apenas checagem de formato.

## 🎯 Objetivo

Muitos validadores de CPF encontrados por aí checam só o tamanho da string. Este projeto implementa a validação matemática completa — o mesmo cálculo usado pela Receita Federal para gerar os dígitos verificadores — construído do zero, função por função, para reforçar fundamentos de lógica, funções puras e reuso de código em Python.

## ⚙️ Funcionalidades

- ✅ Validação de **formato**: 11 dígitos (CPF) / 14 dígitos (CNPJ), somente numéricos
- ✅ Rejeição de sequências repetidas (ex: `111.111.111-11`), que passam no cálculo matemático mas são inválidas na prática
- ✅ Cálculo real dos **dois dígitos verificadores** do CPF via algoritmo módulo 11
- ✅ Funções puras e reutilizáveis, sem `input()`/`print()` misturado na lógica de validação

## 🧮 Como funciona o algoritmo

O CPF tem 11 dígitos: **9 dígitos base** + **2 dígitos verificadores**.

1. Multiplica os 9 dígitos base por pesos decrescentes (10 a 2) e soma
2. Aplica `resto = soma % 11` → dígito verificador é `0` se `resto < 2`, senão `11 - resto`
3. Repete o processo incluindo o 1º dígito verificador (10 dígitos, pesos de 11 a 2) para obter o 2º
4. Compara os dígitos calculados com os informados

## 🚀 Como executar

```bash
python validador.py
```

O programa pede o CPF/CNPJ via terminal e informa se é válido.

## 🧱 Estrutura do código

| Função | Responsabilidade |
|---|---|
| `get_cpf` / `get_cnpj` | Validação de formato (tamanho, dígitos, não-repetição) |
| `calc_digitos` | Soma ponderada de dígitos por lista de pesos |
| `calc_verif_digit` | Aplica a regra do módulo 11 para obter um dígito verificador |
| `validar_cpf_comp` | Orquestra o cálculo completo dos dois dígitos verificadores do CPF |

## 📚 Aprendizados aplicados

- Separação entre lógica de negócio e I/O (funções puras vs. `input`/`print`)
- Uso de `zip()` para iterar múltiplas sequências sem indexação manual
- Evitar retorno implícito `None` em funções `-> bool`/`-> int`
- DRY: reaproveitamento de `calc_digitos` e `calc_verif_digit` em vez de código duplicado

## 🔜 Próximos passos

- [ ] Implementar `validar_cnpj_comp` com o mesmo rigor matemático (12 dígitos base + pesos específicos)
- [ ] Adicionar testes unitários (`unittest`/`pytest`)
- [ ] Empacotar como função reutilizável para uso em outros projetos (ex: [cliente_app](https://github.com/davycaetano08-crypto/cadastro-clientes.git))

---

Feito como exercício de fundamentos de Python, com foco em lógica pura antes de aplicar em um projeto Flask real.

def menu():
    return input("""
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """).lower().strip()

def solicitar_valor(operacao):
    try:
        return float(input(f"Informe o valor para {operacao}: "))
    except ValueError:
        print("Valor inválido.")
        return 0

def depositar(saldo, extrato):
    valor = solicitar_valor("depósito")
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou.")
    return saldo, extrato

def sacar(saldo, extrato, numero_saques, limite, LIMITE_SAQUES):
    valor = solicitar_valor("saque")
    if valor <= 0:
        print("Valor inválido.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    elif valor > limite:
        print("Excede o limite por saque.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Limite diário de saques atingido.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    return saldo, extrato, numero_saques

def mostrar_extrato(extrato, saldo):
    print("\n========== EXTRATO ==========")
    print(extrato if extrato else "Não foram realizadas movimentações.")
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("==============================")

# Programa principal
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = menu()

    if opcao == "d":
        saldo, extrato = depositar(saldo, extrato)
    elif opcao == "s":
        saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques, limite, LIMITE_SAQUES)
    elif opcao == "e":
        mostrar_extrato(extrato, saldo)
    elif opcao == "q":
        print("Saindo do sistema.")
        break
    else:
        print("Opção inválida.")


"Adiciona código do sistema bancário"

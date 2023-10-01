# Lê o peso de peixes informado pelo usuário
peso_peixes = float(input("Informe o peso de peixes em quilos: "))

# Define o limite estabelecido pelo regulamento
limite = 50.0

# Verifica se o peso de peixes excede o limite
if peso_peixes > limite:
    # Calcula o excesso de peso
    excesso = peso_peixes - limite
    
    # Calcula o valor da multa (R$ 4,00 por quilo excedente)
    multa = excesso * 4.00
    
    # Exibe os resultados
    print(f"Peso de peixes informado: {peso_peixes} kg")
    print(f"Limite estabelecido: {limite} kg")
    print(f"Excesso de peso: {excesso} kg")
    print(f"Valor da multa a ser pago: R$ {multa:.2f}")
else:
    # Caso o peso não exceda o limite, não há multa
    print("Peso de peixes dentro do limite estabelecido. Não há multa a ser paga.")

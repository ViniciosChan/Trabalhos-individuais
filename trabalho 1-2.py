def calcular_peso():
    a = input('Qual a sua altura em metros?: ')
    b = 72.7
    altura_formatada = round(float(a), 2)  # Formata a altura com 2 casas decimais
    resultado_peso = peso(altura_formatada, b)
    resultado_peso_arredondado = round(resultado_peso, 2)  # Arredonda o peso para 2 casas decimais
    print(f"Seu peso ideal é: {resultado_peso_arredondado} kg")

# Função para calcular o peso em razão da altura.
def peso(a, b):
    c = (b * a) - 58
    return c

calcular_peso()

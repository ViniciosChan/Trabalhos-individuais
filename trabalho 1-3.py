print('Olá!! Vamos calcular o seu peso ideal?') 
print('Para isso, vamos precisar do seu gênero e altura!')


def calcular_peso():
    genero = input('Qual é o seu gênero (H para homem, M para mulher)?: ')
    altura = input('Qual a sua altura em metros?: ')
    altura_formatada = round(float(altura), 2)  # Formata a altura com 2 casas decimais
    
    if genero.lower() == 'h':
        peso_ideal = peso_homem(altura_formatada)
    elif genero.lower() == 'm':
        peso_ideal = peso_mulher(altura_formatada)
    else:
        print("Gênero inválido.")
        return
    
    peso_formatado = f"{peso_ideal:.2f}"  # Formata o peso com 2 casas decimais
    print(f"Seu peso ideal é: {peso_formatado} kg")

# Função para calcular o peso ideal para homens.
def peso_homem(h):
    return (72.7 * h) - 58

# Função para calcular o peso ideal para mulheres.
def peso_mulher(h):
    return (62.1 * h) - 44.7

calcular_peso()

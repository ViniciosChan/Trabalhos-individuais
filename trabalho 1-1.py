#trabalho 11

print("Digite dois numeros interos e um real:")
a = input('digite um inteiro:')
b = input('digite um inteiro:')
c = input('digite um real:')

#O produto do dobro do primeiro com metade do segundo.
def produto (a,b):
    d = (int(a) * 2) * (int(b)/2)
    return 'O produto é:', d

#A soma do triplo do primeiro com o terceiro.
def soma (a,c):
    e = ((int(a)*3)+float(c))
    return 'A soma é:',e


#O terceiro elevado ao cubo.
def cubo (c):
    f = float(c)*float(c)*float(c)
    return 'O valor real elevado ao cubo é:',f

print(produto(a,b))
print(soma(a,c))
print(cubo(c))


# for variavel in range(10):
#    print(variavel)

# for variavel in range(5,11):
#    print(variavel)

# output: 1,4,7,10

# for variavel in range(1,12,3):
#    print(variavel)

soma = 0

for i in range(1, 4):
    nota = float(input(f'Informe sua nota {i}: '))

    soma += nota

print(soma/3)

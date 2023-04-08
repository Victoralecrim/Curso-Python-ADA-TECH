numero_sorteado = 15 

numero_escolhido = int(input(' Informe um numero entre 1 e 20: '))

while numero_escolhido != numero_sorteado:
   print('Voce errou o numero, tente novamente... ')
   
   numero_escolhido = int(input(' Informe um numero entre 1 e 20: '))

print('Parabens! Voce acertou!! ')

# Exemplo 02: Estrutura com contador 

contador = 0

while contador < 5:
   print(contador)
   
   contador += 1
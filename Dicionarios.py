# > DICIONARIOS

#Criando dicionarios

dicionario = {}
dicionario = dict()

dicionario = {'nome': 'Wallison', 'idade':26, 'altura': 1.77}

print(dicionario)
print(dicionario['idade'])

# Adicionando elementos em um dicionario

dicionario['programador'] = True
print(dicionario)

dicionario['altura'] = 2
print(dicionario)

# Iterando sobre um dicionario

for chave in dicionario:
   print(chave,dicionario[chave])
   
# Testando a existencia de uma chave

print('peso' in dicionario)
print('altura' in dicionario)
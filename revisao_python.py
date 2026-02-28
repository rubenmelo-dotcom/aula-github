nomes = ['luiz', 'maria', 'helena', 'joana', 'felipe']
novos_nomes = [
    f'{nome[:-1].lower()}{nome[-1].upper()}'
    for nome in nomes
]
print(nomes)
print()
print(novos_nomes)


# original = [n for n in range(10)]
# maior = [n for n in original if n > 5]
# impares = [n for n in original if n % 2 != 0]
# pares = [n for n in original if n % 2 == 0]
# print(original)
# print(maior)
# print(impares)
# print(pares)
# print()
# for x in range(10):
#     print(x, sep='\n')
#     for y in range(5):
#         print(y, end=' ')
#         if y == 4:
#             print('\n')




# produtos = [
#     {'nome': 'p1', 'preco': 10},
#     {'nome': 'p2', 'preco': 20},
#     {'nome': 'p3', 'preco': 30},
# ]

# produtos2 = [
#     {**produto, 'preco': produto['preco'] * 2}
#     if produto['preco'] > 20 else {**produto}
#     for produto in produtos
#     if produto['preco'] > 10
# ]

# list_num = [(x, y) for x in range(3) for y in range(3)]

# print(*produtos, sep='\n')
# print()
# print(*produtos2, sep='\n')
# print(list_num)
# lista = [n for n in range(10)]
# lista_gen = (n for n in range(10))
# print(lista)
# print(next(lista_gen))
# print(next(lista_gen))
# print(next(lista_gen))
# print(next(lista_gen))
# print(next(lista_gen))
# print(next(lista_gen))
# print(next(lista_gen))
# print(next(lista_gen))
# print(next(lista_gen))
# print(next(lista_gen))

# lista = [
#     {'nome': 'Ruben', 'sobrenome': 'Melo'},
#     {'nome': 'Nebur', 'sobrenome': 'Olem'},
#     {'nome': 'João', 'sobrenome': 'Silvério'},
#     {'nome': 'Oãoj', 'sobrenome': 'Oirévlis'},
# ]


# def ordena_nome(lista):
#     return lista['nome']


# def ordena_sobrenome(lista):
#     return lista['sobrenome']


# lista_nome = sorted(lista, key=ordena_nome)
# for item in lista_nome:
#     print(item)
# print()
# lista_sobrenome = sorted(lista, key=ordena_sobrenome)
# for item in lista_sobrenome:
#     print(item)
# print()
# lista_nome_lam = sorted(lista, key=lambda item: item['nome'])
# for item in lista_nome_lam:
#     print(item)
# print()
# lista_sobrenome_lam = sorted(lista, key=lambda item: item['sobrenome'])
# for item in lista_sobrenome_lam:
#     print(item)


# soma = lambda x, y: x + y
# print(soma(3,4))
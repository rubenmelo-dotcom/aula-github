
produtos = [
    {'nome': 'p1', 'preco': 10},
    {'nome': 'p2', 'preco': 20},
    {'nome': 'p3', 'preco': 30},
]

produtos2 = [
    {**produtos, produto for produto['preco'] * 2}
]

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
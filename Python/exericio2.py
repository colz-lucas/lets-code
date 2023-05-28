#Questao1
# x = int(input("Digite um número inteiro: "))

# if x < 0:
#     resp1 = "negativo"
# else:
#     resp1 = "positivo"
    
# if x % 2 == 0:
#     resp2 = "par"
# else:
#     resp2 = "impar"
    
# print("O número {} é {} e {}.".format(x, resp1, resp2))

#Questao 2
# cont = 0
# resultado = 0
# n = 1000

# while cont != n:
#     resultado = resultado + 1/(2**cont)
#     cont = cont + 1

# print(resultado, cont)

#Questao 3
# for _ in "let's code":
#   print("Olá, mundo!")
# for _ in [10]:
#     print("Olá, mundo!")

#Questao 4
# lista_inicial = [10, 5, -7, 6, -42, 63, -8, -5, 13]
# lista_final = []

# for item in lista_inicial:
#     if item % 2 == 0:
#         if item < 0:
#             lista_final.append(-item)
#         else:
#             lista_final.append(item)
#     else:
#         if item < 0:   
#             lista_final.append(-2*item)
#         else:
#             lista_final.append(2*item)

#Questao 5
animais = ['gato', 'coelho', 'macaco', 'girafa']

animais.remove('gato')
print(animais)
print(len(animais))
print(animais.index('coelho'))


#Questao 1
# var1 = 12
# var2 = 30

# var3 = var1 + var2
# print(var3)

# var3 = var3 // 2
# print(var3)

#Questao 2
# num1 = float(input("Digite um número a seguir: "))
# dobro = 2*num1
# print("O dobro do número digitado é:", dobro)

#Questao 3
# x = 10
# y = 4.2

# num = float(input("Digite um número a seguir: "))
# print(num > x*y, num <= x + y, num*y != x*y)
# print(num == x*y, num*y == x*y, y > x + num)

#Questao 4
# x = 4.2
# y = 10
# z = "42"

# print('base', not (((x * y == z) and not (x < y)) or y % 2 == 0))
# #a)
# print('a)', not (not (x < y and x * y == z)) or (x >= y or y % 2 == 0))
# #c)
# print('c)', not ((x == y or True) and ((int(z) < x*y) and (type(y) == type(int(z))))))
# #d)
# print('d)', not (((not True) or int(z) % 7 == 0) and ((str(int(x*y)) == z) and (type(x) != type(z)))))

#Questao 5
a = int(input("Digite o primeiro número inteiro: "))
b = int(input("Digite o segundo número inteiro: "))
c = int(input("Digite o terceiro número inteiro: "))

if a > b and a > c:
  resposta = a % 2 == 0
elif b > a and b > c:
  resposta = b % 2 == 0
else:
  resposta = c % 2 == 0

print(resposta)
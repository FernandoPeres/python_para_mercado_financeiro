import math

print("soma entre dois números 2+5: ",2+5)

print("subtração entre dois números 5-2: ",5-2)

print("multiplicação entre dois números, 5*2: ",5*2)

print("divisão entre dois números, 5/2: ",5/2)

#CUIDADO PARA DIVISÕES POR ZERO
try: #try inserido para evitar o erro na linha de comando.
    # essa tentativa de divisão retorna um erro: ZeroDivisionError: division by zero
    print("divisão entre dois números, 5/0: ",5/0)
except:
    print("ZeroDivisionError: division by zero")

print("exponencial entre dois números, 5**3: ",5**3)

print("retornando o resto da divisão entre dois números, 5 % 2: ",5%2)

# podemos utilizar atribuições de valores a variáves e utilizar essas variáveis nas operações matemáticas

a=1
b=2
c=3
d=4
print("imprime todas as variáveis separadas por vírgula",a,b,c,d) #imprime todas as variáveis solicitadas

#podemos efetuar todas as operações anteriores com essas variáveis.

# em python temos uma biblioteca que pode ser importada
# import math
x=5
y=10

#para utilizar essa biblioteca usamos o math.<funcao>
#retorna e elevado a x.
print("Retorna e^x: ",math.exp(x))

#retorna o logaritmo de x na base 2.
print("Retorna logaritmo de x na base 2: ",math.log2(x))

#retorna o logaritmo de x na base 10.
print("Retorna o logaritmo de x na base 10: ",math.log10(x))

#retorna o logaritmo natural de x (base e).
print("Retorna o logaritmo natural de x (base e): ",math.log(x)) 

#retorna o logaritmo de x na base b, apenas quando b é diferente de 2 e 10.
print("Retorna o logaritmo de x na base b: ",math.log(x,b))

#retorna x elevado a y.
print("Retorna x^y: ",math.pow(x,y))

#retorna a raiz quadrada de x
print("Retorna raiz quadrada de x: ",math.sqrt(x)) 

#Também há as funções trigonométricas:

#retorna o cosseno de x.
print("Retorna o cosseno de x: ",math.cos(x))
#retorna o seno de x.
print("Retorna o seno de X: ",math.sin(x))
#retorna a tangente de x.
print("Retorna a tangente de x: ",math.tan(x))
#converte o ângulo x de radianos para graus.
print("Converte o ângulo x de radianos para graus: ",math.degrees(x))
#converte o ângulo x de graus para radianos.
print("Converte o ângulo x de graus para radianos: ",math.radians(x))
#retorna o arco cosseno de x.
print("Retorna o arco cosseno de 1: ",math.acos(1))
#retorna o arco seno de x.
print("Retorna o arco seno de 1: ",math.asin(1))
#retorna o arco tangente de x
print("Retorna o arco tangente de 1: ",math.atan(1))

#para facilitar ao importar uma biblioteca podemos atribuir apelido a ela

# import math as mt
#chamando as funções da biblioteca com a utilização desse apelido
import math as mt

print("Seno de 30:",mt.sin(30))
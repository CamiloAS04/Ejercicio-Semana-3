#Nivel Basico

#1.Saludo personalizado
def saludo_personalizado(nombre):
    print(f"Hola, {nombre} !Bienvenido¡")

#2. Suma de dos números
def suma(a,b): return a + b

#3. Número par o impar
def es_par(numero): return numero %2 == 0

#4. Mayoría de edad
def es_mayor_edad(edad): 
    return "Mayor de edad" if edad >= 18 else "Menor de edad"

#5. Conversor de temperatura
def celsius_a_fahrenheit(celsius): 
    return (celsius * 9/5) + 32

#6. Área de un triángulo
def area_triangulo(base,altura): 
    return (base * altura) / 2

#7. Mayor de una lista
def mayor_de_lista(lista): 
    return max(lista)

#8. Contar letras
def contar_letras(palabra,letra): 
    return  palabra.count(letra)

#Nivel Intermedio

#9. Filtrar pares
def filtrar_pares(lista): 
    return [num for num in lista if num % 2 == 0]

#10. Palíndromo
def es_palidromo(texto):
    texto = texto.lower().replace("","")
    return texto == texto[::-1]

#11. Factorial
def factorial(n): 
    if n == 0 or n == 1: return 1 
    else: return n * factorial(n - 1)

#12. Eliminar duplicados
def eliminar_duplicados(lista):
    return list(set(lista))

#13. FizzBuzz
def fizzbuzz(numero):
    if numero % 3 == 0 and numero % 5 ==0:
        return "FizzBuzz"
    elif numero % 3 == 0:
        return "Fizz"
    elif numero % 5 == 0:
        return "Buzz"
    else:
        return str(numero)

#14. Contar vocales
def contar_vocales(cadena):
    return sum(1 for letra in cadena.lowe() if letra in 'aeiou')

#15. Invertir texto
def invertir_texto(cadena): 
    return cadena[::-1]

#Nivel Avanzado

#16. Validar contraseña segura
import random 
import string
def validar_contraseña(contraseña):
    tiene_mayus = any(c.isupper() for c in contraseña)
    tiene_minus = any(c.islower() for c in contraseña)
    tiene_num = any(c.isdigit() for c in contraseña)
    tiene_simbolo = any(c in string.punctuation for c in contraseña)
    return tiene_mayus and tiene_minus and tiene_num and tiene_simbolo

#17. Simular dado
def simular_dado():
    return random.randint(1,6)

#18. Suma de elementos únicos
def suma_elementos_unicos(lista):
    return sum(num for num in set(lista))

#19. Generador de contraseñas
import random
import string

def generar_contraseña(longitud):
    caracteres = string.ascci_latters + string.digits + string.punctuation
    contraseña = "".join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

#20. Composición de funciones
def composicion(f,g):
    def compuesta(x):
        return f(g(x))
    return compuesta
#Funciones simples con ejemplo
def doble(n):
    return n * 2

def sumar_tres(n):
    return n + 3

#Componemos las funciones
doble(sumar_tres(x))
funcion_compuesta = composicion(doble, sumar_tres)
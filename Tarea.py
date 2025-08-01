def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "No se puede dividir por cero"

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

print("Suma:", sumar(a, b))
print("Resta:", restar(a, b))
print("Multiplicación:", multiplicar(a, b))
print("División:", dividir(a, b))

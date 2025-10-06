
def evaluar_postfija(expresion):
    pila = []
    for simbolo in expresion.split():
        if simbolo.isdigit():  
            pila.append(int(simbolo))
        else:  
            b = pila.pop()
            a = pila.pop()
            if simbolo == '+': pila.append(a + b)
            elif simbolo == '-': pila.append(a - b)
            elif simbolo == '*': pila.append(a * b)
            elif simbolo == '/': pila.append(a / b)
            elif simbolo == '^': pila.append(a ** b)   
    return pila.pop()

def evaluar_prefija(expresion):
    pila = []
    for simbolo in expresion.split()[::-1]:  
        if simbolo.isdigit():
            pila.append(int(simbolo))
        else:
            a = pila.pop()
            b = pila.pop()
            if simbolo == '+': pila.append(a + b)
            elif simbolo == '-': pila.append(a - b)
            elif simbolo == '*': pila.append(a * b)
            elif simbolo == '/': pila.append(a / b)
            elif simbolo == '^': pila.append(a ** b)
    return pila.pop()


infija = "3 + 2 * 5 / 4 ^ 3"
posfija = "3 2 5 * 4 3 ^ / +"
prefija = "+ 3 / * 2 5 ^ 4 3"

print("INFija : ", infija)
print("POSfija: ", posfija)
print("PREfija: ", prefija)

print("\nResultados con pila:")
print("Postfija =", evaluar_postfija(posfija))
print("Prefija  =", evaluar_prefija(prefija))

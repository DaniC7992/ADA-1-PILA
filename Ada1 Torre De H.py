class Pila:
    def __init__(self, nombre):
        self.elementos = []
        self.nombre = nombre

    def apilar(self, valor):
        self.elementos.append(valor)

    def desapilar(self):
        if not self.esta_vacia():
            return self.elementos.pop()

    def esta_vacia(self):
        return len(self.elementos) == 0

    def mostrar(self):
        return f"{self.nombre}: {self.elementos}"


def mover_disco(origen, destino):
    disco = origen.desapilar()
    destino.apilar(disco)
    print(f"Mover disco {disco} de {origen.nombre} a {destino.nombre}")
    print(f"{origen.mostrar()} | {destino.mostrar()}")
    print("--------------------------")


def hanoi(n, origen, auxiliar, destino):
    if n == 1:
        mover_disco(origen, destino)
    else:
        hanoi(n - 1, origen, destino, auxiliar)
        mover_disco(origen, destino)
        hanoi(n - 1, auxiliar, origen, destino)



A = Pila("A")
B = Pila("B")
C = Pila("C")


for i in range(3, 0, -1):
    A.apilar(i)

print("Estado inicial:")
print(A.mostrar(), "|", B.mostrar(), "|", C.mostrar())
print("---------")

hanoi(3, A, B, C)

print("Estado final:")
print(A.mostrar(), "|", B.mostrar(), "|", C.mostrar())

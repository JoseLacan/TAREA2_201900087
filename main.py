#Tarea 2       201900087

y=0

class NodoListaC:

    def __init__(self, valor_):
        self.valor=valor_
        self.anterior=None
        self.siguiente=None

class ListaDobleC:

    def __init__(self):
        self.primero=None
        self.ultimo=None

    def push(self, valor_):
        nuevo=NodoListaC(valor_)

        if(self.primero==None):
            self.primero=nuevo
        else:
            nuevo.anterior=self.ultimo
            self.ultimo.siguiente=nuevo
        self.ultimo=nuevo

    def imprimir(self):
        print("Elementos de la lista:")
        aux=self.primero
        while(aux!=None):
            print(aux.valor)
            if(aux.siguiente==self.primero):
                return
            aux=aux.siguiente

    def buscar(self, valor_buscado):
        aux=self.primero

        while(aux!=None):
            if (aux.valor==valor_buscado):
                print("Anterior:",aux.anterior.valor, end=",")
                print(" Actual:",aux.valor, end=",")
                print(" Siguiente:",aux.siguiente.valor)

            if (aux.siguiente==self.primero):
                return
            aux=aux.siguiente

x=ListaDobleC()
x.push(10)
x.push(54)
x.push(64)
x.push(87)
x.push(354)
x.push(51)
x.push(123)
x.imprimir()
y=int(input("Seleccione un numero: "))
x.buscar(y)



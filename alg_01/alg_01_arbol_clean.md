``` py
class Nodo:
    def __init__(self, datos, hijos=None):
        self.datos = datos
        self.hijos = hijos
        self.padre = None

    def set_hijos(self, hijos):
        self.hijos = hijos
        if (self.hijos != None):
            for hij in self.hijos:
                hij.padres = self

    def get_hijos(self):
        return self.hijos

    def get_padre(self):
        self.padre

    def set_padre(self, padre):
        self.padre = padre

    def set_datos(self, datos):
        self.datos = datos

    def get_datos(self):
        return self.datos

    def igual(self, nodo):
        if (self.get_datos() == nodo.get_datos()):
            return True
        else:
            return False

    def en_lista(self, lista_nodos):
        esta_lista = False
        for n in lista_nodos:
            if (self.igual(n)):
                esta_lista = True
        return esta_lista

    def __str__(self):
        return str(self.get_datos())


def busqueda_amplitud(estado_incial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_pendientes = []
    nodoInicial = Nodo(estado_incial)
    nodos_pendientes.append(nodoInicial)
    while ((not solucionado) and (len(nodos_pendientes) != 0)):
        nodo = nodos_pendientes.pop(0)
        nodos_visitados.append(nodo)
        if (nodo.get_datos() == solucion):
            solucionado = True
            return nodo
        else:
            dato_nodo = nodo.get_datos()
            hijo = [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]]
            hijo_izq = Nodo(hijo)
            if ((not hijo_izq.en_lista(nodos_pendientes)) and (not hijo_izq.en_lista(nodos_visitados))):
                nodos_pendientes.append(hijo_izq)
            hijo = [dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]]
            hijo_centro = Nodo(hijo)
            if ((not hijo_centro.en_lista(nodos_pendientes)) and (not hijo_centro.en_lista(nodos_visitados))):
                nodos_pendientes.append(hijo_centro)
            hijo = [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]]
            hijo_der = Nodo(hijo)
            if ((not hijo_der.en_lista(nodos_pendientes)) and (not hijo_der.en_lista(nodos_visitados))):
                nodos_pendientes.append(hijo_der)
            nodo.set_hijos([hijo_izq, hijo_centro, hijo_der])


if __name__ == "__main__":
    estado_incial = [3, 2, 1, 4]
    solucion = [1, 2, 3, 4]
    nodo_solucion = busqueda_amplitud(estado_incial, solucion)
    print(nodo_solucion)
```

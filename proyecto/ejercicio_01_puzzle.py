# Clase que servira para crear los objetos nodo con los que se
# fabricará el arbol

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

# Función que busca en un arbol un determinado nodo por el
# metodo de amplitud


def busqueda_amplitud(estado_incial, solucion):
    # Bandera que sirve para saber si se ha conseguido la solución
    solucionado = False
    # Pilas de ayuda para controlar el numero de nodos que se han evaluado
    nodos_visitados = []
    nodos_pendientes = []
    # Apuntador a el nodo inicial
    nodoInicial = Nodo(estado_incial)
    nodos_pendientes.append(nodoInicial)
    # Mientras que no se haya llegado a la solución y aún haya nodos pendientes
    # se realiza el siguiente codigo
    while ((not solucionado) and (len(nodos_pendientes) != 0)):
        nodo = nodos_pendientes.pop(0)
        # Extraer el nodo y se agrega a nodos_visitados
        nodos_visitados.append(nodo)
        # Si en esta iteración se consiguió la solución, esta se retorna y se rompe
        # el bucle
        if (nodo.get_datos() == solucion):
            solucionado = True
            return nodo
        else:
            # Si en esta iteración no se consiguió la solución,
            # se aumenta la longitud del arbol
            dato_nodo = nodo.get_datos()
            # Operacion izquierda [x,x,1,4]
            hijo = [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]]
            hijo_izq = Nodo(hijo)
            if ((not hijo_izq.en_lista(nodos_pendientes)) and (not hijo_izq.en_lista(nodos_visitados))):
                nodos_pendientes.append(hijo_izq)
            # Operacion centro [3,x,x,4]
            hijo = [dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]]
            hijo_centro = Nodo(hijo)
            if ((not hijo_centro.en_lista(nodos_pendientes)) and (not hijo_centro.en_lista(nodos_visitados))):
                nodos_pendientes.append(hijo_centro)
            # Operacion derecha [3,2,x,x]
            hijo = [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]]
            hijo_der = Nodo(hijo)
            if ((not hijo_der.en_lista(nodos_pendientes)) and (not hijo_der.en_lista(nodos_visitados))):
                nodos_pendientes.append(hijo_der)
            nodo.set_hijos([hijo_izq, hijo_centro, hijo_der])


# Entrada main (entrada principal para ejecutar el programa)
if __name__ == "__main__":
    estado_incial = [3, 2, 1, 4]
    solucion = [1, 2, 3, 4]
    # Llamada a la función que hace una busqueda por apmplitud en un arbol
    # creado a partir de la clase Nodo
    nodo_solucion = busqueda_amplitud(estado_incial, solucion)
    # Impresión de resultados
    print(nodo_solucion)

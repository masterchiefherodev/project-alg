def cruzarRio():
    izquierda = [1, 1, 1, 1]
    derecha = [0, 0, 0, 0]
    posicion_izq = True
    pasos = []
    print(izquierda, "\t", derecha)

# Bucle en loop hasta que se logre la solución
    while (True):
      # Si se ha logrado la solución se sale del bucle
        if (derecha == [1, 1, 1, 1]):
            break
        if (posicion_izq):
          # Se usa la bandera para saber en que lado se encuentra el granjero
            print("Izquierda")
            # R1i: si todos los elementos están en la izquierda
            if (izquierda[0] == izquierda[1] and izquierda[1] == izquierda[2] and izquierda[2] == izquierda[3]):
                izquierda[0], izquierda[1] = 0, 0
                derecha[0], derecha[1] = 1, 1
                pasos.append("GC")
                print("R1")
                # R2i: si el elemento en la segunda posicion es diferente a los subsecuentes y el valor de pasos != C
            elif (izquierda[1] != izquierda[2] and izquierda[1] != izquierda[3] and pasos[len(pasos)-1][0] != "C"):
                izquierda[0] = 0
                derecha[0] = 1
                pasos.append("C")
                print("R2")
                # R3i: Si el primer y ultimo elemento es 1, alguno de los valores intermedios es 1 y el valor de pasos es != M
            elif (izquierda[0] == 1 and izquierda[3] == izquierda[0] and izquierda[1] != izquierda[2] and pasos[len(pasos)-1][0] != "M"):
                izquierda[0], izquierda[3] = 0, 0
                derecha[0], derecha[3] = 1, 1
                pasos.append("MC")
                print("R3")
                # R4i: si el primer y tercer elemento de la lista son 1, y al menos uno de los otros tambien, pero pasos se encuentra en valor != L
            elif (izquierda[0] == 1 and izquierda[2] == izquierda[0] and izquierda[1] != izquierda[3] and pasos[len(pasos)-1][0] != "L"):
                izquierda[0], izquierda[2] = 0, 0
                derecha[0], derecha[2] = 1, 1
                pasos.append("LC")
                print("R4")
                # R5i: Si los dos primeros son 1 y el valor de passo es != G
            elif (izquierda[0] == 1 and izquierda[0] == izquierda[1] and pasos[len(pasos)-1][0] != "G"):
                izquierda[0], izquierda[1] = 0, 0
                derecha[0], derecha[1] = 1, 1
                pasos.append("GC")
                print("R5")
        else:
          # Si se encuentra en la derecha pero no se ha terminado el problema se
          # realiza lo siguiente
            print("Derecha")
            # R1d: si todos los elementos son iguales
            if (derecha[0] == derecha[1] and derecha[1] == derecha[2] and derecha[2] == derecha[3]):
                izquierda[0], izquierda[1] = 1, 1
                derecha[0], derecha[1] = 0, 0
                pasos.append("GC")
                print("R1")
                # R2d: si el elemento en la segunda posicion es diferente a los subsecuentes y el valor de pasos != C
            elif (derecha[1] != derecha[2] and derecha[1] != derecha[3] and pasos[len(pasos)-1][0] != "C"):
                izquierda[0] = 1
                derecha[0] = 0
                pasos.append("C")
                print("R2")
                # R3d: Si el primer y ultimo elemento es 1, alguno de los valores intermedios es 1 y el valor de pasos es != M
            elif (derecha[0] == 1 and derecha[3] == derecha[0] and derecha[1] != derecha[2] and pasos[len(pasos)-1][0] != "M"):
                izquierda[0], izquierda[3] = 1, 1
                derecha[0], derecha[3] = 0, 0
                pasos.append("MC")
                print("R3")
                # R4d: si el primer y tercer elemento de la lista son 1, y al menos uno de los otros tambien, pero pasos se encuentra en valor != L
            elif (derecha[0] == 1 and derecha[2] == derecha[0] and derecha[1] != derecha[3] and pasos[len(pasos)-1][0] != "L"):
                izquierda[0], izquierda[2] = 1, 1
                derecha[0], derecha[2] = 0, 0
                pasos.append("LC")
                print("R4")
                # R5d: Si los dos primeros son 1 y el valor de passo es != G
            elif (derecha[0] == 1 and derecha[1] == derecha[0] and pasos[len(pasos)-1][0] != "G"):
                izquierda[0], izquierda[1] = 1, 1
                derecha[0], derecha[1] = 0, 0
                pasos.append("GC")
                print("R5")
        # Se invierte el valor de posicion_izq
        posicion_izq = not posicion_izq
        # se imprimen los pasos y los arreglos
        print(pasos[len(pasos)-1])
        print(izquierda, "\t", derecha)
        # Se retornan todos los pasos
    return pasos


pasosReales = cruzarRio()
# Se imprimen los pasos totales
print("-----------------------------------------------")
print(pasosReales)

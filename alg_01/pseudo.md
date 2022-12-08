``` js
class Nodo{

  constructor(datos, hijos){
    this.datos = datos;
    this.hijos = hijos;
    this.padre = None;
  }

  getHijos(this){
    return this.hijos;
  }

  setHijos(hijos){
    this.hijos = hijos;
    if(this.hijos != None){
      for( hij in this.hijos){
        hij.padres = this
      }
    }
  }

  getPadre(this){
    return this.padre;
  }

  setPadre(padre){
    this.padre = padre;
  }

  getDatos(this){
    return this.datos;
  }

  setDatos(datos){
    this.datos = datos;
  }

  igual(nodo){
    if(this.getDatos() == nodo.getDatos){
      return true;
    }
    return false;
  }

  enLista(listaNodos){
    estaEnLista = false;
    for( n in listaNodos){
      if(this.ingual(n)){
        estaEnLista = true;
      }
    }
    return estaEnLista;
  }

  dataToString(this){
    return String(this.getDatos());
  }

}

function busquedaAmplitud(inicial, solucion){
  flag = false;
  nodosVisitados = [];
  nodosPendientes = [];
  nodoInicial = Nodo(inicial);
  nodosPendientes.append(nodoInicial);
  while(!flag && len(nodosPendientes)!=0){
    nodo = nodosPendientes.pop(0)
    nodosVisitados.append(nodo)
    if (nodo.getDatos() == solucion){
      flag = true;
      return nodo
    }else{
      datoNodo = nodo.getDatos();
      hijo = [datoNodo[1], datoNodo[0], datoNodo[2], datoNodo[3]];
      hijoIzq = Nodo(hijo);
      if(not hijoIzq.enLista(nodosPendientes) && not hijoIzq.enLista(nodosVisitados)){
        nodosPendientes.append(hijoIzq);
      }
      hijo = [datoNodo[0], datoNodo[2], datoNodo[1], datoNodo[3]];
      hijoCentro = Nodo(hijo);
      if(not hijoCentro.enLista(nodosPendientes) && not hijoCentro.enLista(nodosVisitados)){
        nodosPendientes.append(hijoCentro);
      }
      hijo = [datoNodo[0], datoNodo[1], datoNodo[3], datoNodo[2]];
      hijoDer = Nodo(hijo);
      if(not hijoDer.enLista(nodosPendientes) && not hijoDer.enLista(nodosVisitados)){
        nodosPendientes.append(hijoDer);
      }
      nodo.setHijos([hijoIzq, hijoCentro, hijoDer]);
    }
  }
}

function main(){
  estadoInicial = [3, 2, 1, 4];
  solucion = [1,2,3,4];
  nodoSolucion = busquedaAmplitud(estadoInicial, solucion);
  print(nodoSolucion)
}
```

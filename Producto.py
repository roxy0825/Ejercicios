class producto:
    def __init__(self,idProducto,nombreProd,precio):
        self.idProducto = int(input("Ingrese el id del producto: "))
        self.nombreProd = input("Ingrese el nombre del producto: ")
        self.precio = int(input("Ingrese el precio del producto: "))
        
        
    def imprimirDatos(self): # Metodos
        print("_________________________")
        print("   DATOS DEL PRODUCTO    ")
        print("_________________________")
        print(f"ID DEL PRODUCTO ---> {self.idProducto}")
        print(f"NOMBRE DEL PRODUCTO   ---> {self.nombreProd}")
        print(f" PRECIO DEL PRODUCTO---> {self.precio}")
        
       
        
    def calcularSaldo (self,precioprod):
        cantidadProducto = int(input("Ingrese la cantidad del producto: "))
        calSubtotal = cantidadProducto * precioprod
        porcentajedesc = float(input("Ingrese valor del descuento: "))
        caldescuento= calSubtotal * (porcentajedesc / 100)
        saldototalpago = calSubtotal - caldescuento
        datosProceso=[cantidadProducto,calSubtotal,caldescuento,saldototalpago]
        return datosProceso
    
    def imprimir (self,datosProceso):
        print("___________________")
        print("     COLILLA       ")
        print("___________________")
        print(f"ID DEL PRODUCTO-----------> {self.idProducto}")
        print(f"NOMBRE DEL PRODUCTO-------> {self.nombreProd}")
        print(f"PRECIO DEL PRODUCTO-------> {self.precio}")
        print(f"CANTIDAD DEL PRODUCTO-----> {datosProceso[0]}")
        print(f"SUBTOTAL DEL PRODUCTO-----> {datosProceso[1]}")
        print(f"DESCUENTO DEL PRODUCTO----> {datosProceso[2]}")
        print(f"PAGO TOTAL----------------> {datosProceso[3]}")
        
      
if  __name__=="__main__":
    producto1 = producto(0, '', 0)
    producto1.imprimirDatos()
    datosProceso = producto1.calcularSaldo(producto1.precio)
    producto1.imprimir(datosProceso)
    
    
   
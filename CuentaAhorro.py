
class cuentaAhorro:
    def __init__(self,nroCuenta,nombre,sucursal,saldo):
        self.nroCuenta = nroCuenta 
        self.nombre = nombre
        self.sucursal = sucursal
        self.saldo = saldo
        
    def imprimirDatos(self): # Metodos
        print("_________________________")
        print("   DATOS DE LA CUENTA    ")
        print("_________________________")
        print(f"Numero de Cuenta  ---> {self.nroCuenta}")
        print(f"Nombre Usuario    ---> {self.nombre}")
        print(f"Sucursal Bancaria ---> {self.sucursal}")
        print(f"Saldo             ---> {self.saldo}")
        
        
    def calcularSaldo (self,valor):
        vlrConsignacion =self.saldo + valor
        vlrRetiro = self.saldo - valor
        saldototalconsig= self.vlrConsignacion + valor
        saldototalretiro= self.vlrRetiro - valor
        datosProceso=[vlrConsignacion,vlrRetiro,saldototalconsig,saldototalretiro]
        return datosProceso
    def imprimir (self,datosProceso):
        print("___________________")
        print("     COLILLA       ")
        print("___________________")
        print(f"Numero de Cuenta -----> {self.nroCuenta}")
        print(f"Nombre Usuario--------> {self.nombre}")
        print(f"Sucursal Bancaria-----> {self.sucursal}")
        print(f"Saldo-----------------> {self.saldo}")
        print(f"Valor consignacion----> {datosProceso[0]}")
        print(f"Valor Retiro----------> {datosProceso[1]}")
        print(f"saldo total consignacion-----------> {datosProceso[2]}")
        print(f"saldo total retiro-----------> {datosProceso[3]}")
      
if  __name__=="__main__":
    usuario1 = cuentaAhorro(1212, "roxy", "Bancolombia", 2800000)
    usuario1.imprimirDatos()
    datosProceso = usuario1.calcularSaldo(20000)
    usuario1.imprimir(datosProceso)
    
    
    #valro de la consignacio  5000  + 20000 = 25000
    #valor del retiro         10000 - 20000 = 10000
    #saldoTotal          
    
    # saldo actual 20000 
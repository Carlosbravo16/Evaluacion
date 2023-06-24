class Bolsillo:

    idBolsillo=''
    saldobolsillo=int
    numCelular=int
    claveBolsillo=int
    estadobolsillo=''

    def crearBolsillo(self):
        self.idBolsillo=input('Ingrese el id del bolsillo: ')
        self.saldoBolsillo=int(input('Ingrese el saldo del bolsillo: '))
        self.numCelular=int(input('Ingrese el número de telefono: '))
        self.claveBolsillo=int(input('Ingrese la clave: '))
        self.estadobolsillo=input('Ingrese el estado del bolsllo: ')
    
    def entrarBolsillo(self):
        numero=int(input("ingrese el numero de telefono: "))
        clave=int(input("ingrese la clave: "))
        
        if self.claveBolsillo == clave and self.numCelular == numero:
            print("El número de celular y la contraseña son válidos. Puedes ingresar a Nequi.")
        else:
            print("El número y contraseña ingresados no son válidos. No puedes ingresar a Nequi.")    
        
    def consultarSaldo(self): 
        print("tu saldo actual es de ",self.saldoBolsillo)
        
    def recargarSaldo(self):
        valor=int(input("Cuanto desea recargar: "))
        valorFinal=self.saldoBolsillo+valor
        print(f'Su saldo actual es: {valorFinal}')

    def sacarPlata(self):
        valor=int(input("Cuanto quiere retirar"))
        if valor<= self.saldoBolsillo:
            valorFinal=self.saldoBolsillo-valor
            print(f"El valor que saco es {valor} su saldo final es {valorFinal} ")
        else :
            print("saldo insuficiente")


        
                




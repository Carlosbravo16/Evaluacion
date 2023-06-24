from Bolsillo import Bolsillo
Nequi=Bolsillo()

class Nequi(Bolsillo):
    numCelular=int
    valor=int
    def envia(self):
        self.numCelular=int(input("ingrese el numero de telefono: "))
        self.valor=int(input("Cuanto desea enviar: "))
        if self.valor<= self.saldoBolsillo:
            self.saldoBolsillo=self.saldoBolsillo-self.valor
            print(f"El numero al que le envio el dinero es : {self.numCelular} el saldo que se envio es: {self.valor}su saldo actual es {self.saldoBolsillo}")
        else:
            print("Saldo insuficiente ")
    def pedir(self):
        self.numCelular=int(input("ingrese el numero de telefono: "))
        self.valor=int(input("Cuanto desea pedir : "))
        self.saldoBolsillo=self.saldoBolsillo+self.valor
        print(f"El numero donde llega el dinero es : {self.numCelular} el saldo que se pidio es: {self.valor}su saldo actual es {self.saldoBolsillo}")
        
from Bolsillo import Bolsillo
Nequi=Bolsillo()

Nequi.crearBolsillo()
Nequi.entrarBolsillo()
op=1 
while True:
    opcion = int(input("Bienvenidos a Nequi \n 1. Si desea consultar el saldo\n 2.Si desea recargar \n 3. Sidesea sacar plata \n 4. si desea salir"))
    if (opcion == 1):
        Nequi.consultarSaldo()
    elif (opcion==2):
      Nequi.recargarSaldo()
    elif (opcion==3):
        Nequi.sacarPlata()
    elif (opcion==4):
        print("Gracias por sus servicios")
        break




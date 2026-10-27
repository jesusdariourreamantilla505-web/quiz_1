saldo = 1000
#n= numero
opcion = ""
while opcion != "d" and opcion != "0":
    opcion = input("\na) saldo b) depositar c ) retirar d) salir: ")

    if opcion == "a":
        print("Saldo:", saldo)
    elif opcion == "b":
        n = float(input("depositar: "))
        if n > 0:
            saldo = saldo + n
    elif opcion == "c":
        n = float(input("retirar: "))
        if n > 0 and n <= 0:
            saldo = saldo



                
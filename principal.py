import turnos

def preguntar():
    print("Bienvenido a farmacia python")
    while True:
        print("[P]- Perfumería\n[F] - Farmacia\n[C] - Cosmetica")
        try:
            mi_rubro = input("Elija su rubro: ").upper()
            ["P","F","C"].index(mi_rubro)
        except ValueError:
            print("Esa no es una opcion valida")
        else:
            break

    turnos.decorador(mi_rubro)

def inicio():
    while True:
        preguntar()
        try:
            otro_turno = input("Quieres sacar otroturno? [S] [N]: ").upper()
        except ValueError:
            print("Esa no es una opcion valida")
        else:
            if otro_turno == "N":
                print("Gracias por su visita")
                break


inicio()
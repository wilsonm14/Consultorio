from collections import deque
from busqueda import buscar_por_cedula, ordenar_por_valor_atencion
from cliente import Cliente

def registrar_cliente():
    print("Registrar Cliente")
    cedula = input("Cedula: ")
    nombre = input("Nombre: ")
    telefono = input("Telefono: ")
    tipo_cliente = input("Tipo de cliente (particular, eps, prepagada): ")
    tipo_atencion = input("Tipo de atencion (limpieza, calzas, extraccion, diagnostico): ")
    cantidad = 1
    if tipo_atencion in ["calzas", "extraccion"]:
        cantidad = int(input(f"Ingrese la cantidad de {tipo_atencion} a realizar: "))
    prioridad= input("Prioridad de atencion (Normal/Urgente): ")   
    fecha = input("Fecha de la cita (DD/MM/AAAA): ")

    return Cliente(cedula, nombre, telefono, tipo_cliente, tipo_atencion, cantidad, prioridad, fecha)

def main():
    arreglo = deque()

    while True:
        print("BDD Consultorio Odontologico")
        print("1. Registrar usuario")
        print("2. Consultar usuario por CC")
        print("3. Lista de usuarios ordenados por valor de atencion")
        print("4. Ver totales generales del consultorio")
        print("5. Salir")

        opc = input("Seleccione una opcion: ")
        if opc == "1":
            nuevo = registrar_cliente()
            arreglo.append(nuevo)
            print("Cliente registrado con exito.")
        elif opc == "2":
            if not arreglo:
                print("No hay clientes registrados.")
            else:
                ordenar_por_valor_atencion(arreglo)
                cedula = input("Ingrese la cedula a buscar: ")
                encontrado = buscar_por_cedula(arreglo, cedula)
                if encontrado:
                    print("Cliente encontrado:")
                    encontrado.mostrar_informacion()
                else:
                    print(f"No se encontro el cliente con cedula {cedula}.")
        elif opc == "3":
            if not arreglo:
                print("No hay clientes registrados.")
            else:
                ordenar_por_valor_atencion(arreglo)
                print("Lista de clientes ordenados por valor de atencion:")

                for c in arreglo:
                    c.mostrar_informacion()
        elif opc == "4":
            if not arreglo:
                print("No hay clientes registrados.")
            else:
                total_clientes = len(arreglo)
                ingresos = 0
                extracciones = 0
                for c in arreglo:
                    ingresos += c.total_pagar
                    if c.tipo_atencion == "extraccion":
                        extracciones += 1

                print("Registro")
                print(f"Total clientes: {total_clientes}")
                print(f"Total ingresos: ${ingresos}")
                print(f"Clientes para extraccion: {extracciones}")

        elif opc == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida.")

if __name__ == "__main__":
    main()



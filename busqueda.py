def ordenar_por_valor_atencion(arreglo):
    n = len(arreglo)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (
                arreglo[j].val_atencion
                < arreglo[j + 1].val_atencion   
            ):
                arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]

def buscar_por_cedula(arreglo, cedula_buscar):
    for cliente in arreglo:
        if cliente.cedula == cedula_buscar:
            return cliente
    return None
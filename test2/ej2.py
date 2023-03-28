def determinante_sarrus(matriz):
    # Verificar que la matriz es de tamaño 3x3
    if len(matriz) != 3 or len(matriz[0]) != 3:
        raise ValueError("La matriz debe ser de tamaño 3x3")
    
    # Aplicar la regla de Sarrus
    diagonal_desc = matriz[0][0]*matriz[1][1]*matriz[2][2] + matriz[0][1]*matriz[1][2]*matriz[2][0] + matriz[0][2]*matriz[1][0]*matriz[2][1]
    diagonal_asc = matriz[2][0]*matriz[1][1]*matriz[0][2] + matriz[2][1]*matriz[1][2]*matriz[0][0] + matriz[2][2]*matriz[1][0]*matriz[0][1]
    determinante = diagonal_desc - diagonal_asc
    
    return determinante

def determinante_sarrus_iter(matriz):
    # Verificar que la matriz es de tamaño 3x3
    if len(matriz) != 3 or len(matriz[0]) != 3:
        raise ValueError("La matriz debe ser de tamaño 3x3")
    
    # Aplicar la regla de Sarrus
    diagonal_desc = matriz[0][0]*matriz[1][1]*matriz[2][2] + matriz[0][1]*matriz[1][2]*matriz[2][0] + matriz[0][2]*matriz[1][0]*matriz[2][1]
    diagonal_asc = matriz[2][0]*matriz[1][1]*matriz[0][2] + matriz[2][1]*matriz[1][2]*matriz[0][0] + matriz[2][2]*matriz[1][0]*matriz[0][1]
    determinante = diagonal_desc - diagonal_asc
    
    return determinante

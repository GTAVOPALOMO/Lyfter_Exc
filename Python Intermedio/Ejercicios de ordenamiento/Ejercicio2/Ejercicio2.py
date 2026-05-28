"""
Modifica el bubble_sort para que funcione de derecha a izquierda, ordenando los números menores primero.
"""
#Para este caso solo se invierte la lógica
# se recorre del final al inicio
# se compara el numero actual con el anterior
# si el numero actual es menor que el anterior

def bubble_sort(p_list):
    n = len(p_list)
    for i in range(n):
        for j in range(n-1, i, -1):
            if p_list[j] < p_list[j-1]:
                temp = p_list[j]
                p_list[j] = p_list[j-1]
                p_list[j-1] = temp
    return p_list

v_list = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", v_list)    
sorted_arr = bubble_sort(v_list)
print("Lista ordenada:", sorted_arr)

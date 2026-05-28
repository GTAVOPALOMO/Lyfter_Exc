"""
Crea un bubble_sort por tu cuenta sin revisar el código de la lección.
"""

# El bubble sort recorre desde el inicio
# hasta el final buscando el numero mas grande
# y lo va moviendo a la ultima posición
# despues itera otra vez pero esta vez sin tomar en cuenta
# el ultimo numero ya que se verificó en la primer iteracion 
# que era el más alto.

def bubble_sort(p_list):
    n = len(p_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if p_list[j] > p_list[j+1]:
                temp = p_list[j]
                p_list[j] = p_list[j+1]
                p_list[j+1] = temp
    return p_list

v_list = [64, 34, 25, 100, 22, 11, 90]
print("Lista original:", v_list)
sorted_arr = bubble_sort(v_list)
print("Lista ordenada:", sorted_arr)

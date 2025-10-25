def descuento_por_cant(products):
    total_sin_descuento = sum(product["price"] for product in products)

    # Aplicar el descuento
    if len(products) > 1:
        total_con_descuento = total_sin_descuento * 0.90
        # La función debe devolver solo el valor final.
        return total_con_descuento 
        
    return total_sin_descuento

# --- CÓDIGO FUERA DE LA FUNCIÓN ---

# 1. Definir los productos
products = [
    {"name": "Notebook", "price": 100},
    {"name": "otro", "price": 200},
    {"name": "otro_1", "price": 200}
]

# 2. Calcular el total sin descuento (se repite la lógica o se crea una función auxiliar)
# Para este ejemplo, calculamos el total sin descuento nuevamente para la impresión:
total_sin_descuento = sum(product["price"] for product in products)
total_con_descuento = descuento_por_cant(products) # Llama a la función y obtiene el resultado final

# 3. Imprimir los resultados
print(f"El total de productos es: {len(products)}")
print(f"El resultado es: Total sin descuento: ${total_sin_descuento:.2f}")
print(f"El resultado es: Total con descuento: ${total_con_descuento:.2f}") 

# Resultado de la impresión:
# El total de productos es: 3
# El resultado es: Total sin descuento: $500.00
# El resultado es: Total con descuento: $450.00
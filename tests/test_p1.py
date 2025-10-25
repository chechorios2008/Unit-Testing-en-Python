def calculate_total(products):
    total = 0
    for product in products:
        total += product["price"]
    return total


# Descuento del 10% por comprar más de 1 producto
def descuent_por_cant(products):
    total_sin_descuento = sum(product["price"] for product in products)
    # Aplicar el descuento
    if len(products) > 1:
        total_con_descuento = total_sin_descuento * 0.90
        return total_con_descuento
    return total_sin_descuento


# Prueba Descuento.
def test_descuento():
    products = [
        {
            "name": "Notebook", "price": 100
        },
        {
            "name": "otro", "price": 200
        },
        {
            "name": "otro_1", "price": 200
        }
    ]
    assert descuent_por_cant(products) == 450.0


# Prueba suma de precios. 
def test_calculate_total_with_empty_list():
    print("Prueba")
    assert calculate_total([]) == 0


def test_calculate_total_with_single_product():
    products = [
        {
            "name": "Notebook", 
            "price": 5
        }
    ]
    print(calculate_total(products))
    assert calculate_total(products) == 5


def test_calculate_total_with_multiple_product():
    products = [
        {
            "name": "Notebook", "price": 1
        },
        {
            "name": "otro", "price": 1
        }
    ]
    print(calculate_total(products))
    assert calculate_total(products) == 2


if __name__ == "__main__":
    test_descuento()
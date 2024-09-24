class Producto:
    id_producto = 0
    nombre_producto = ""
    descripcion = ""
    stock = 0
    precio = 0
    fecha_ingreso = ""
    id_categoria = 0
    
    def estado(self, n):
        print(f"El {n} está recién hecho")

def lista_productos():
    nombre_producto = ["Baguette", "Croisant", "Integral", "Blanco", "Bagel"]
    print("Panes")
    for nombre in nombre_producto:
        print(nombre)


def tupla_descripcion():
    descripcion = ("Pan largo", "Pan curvo", "Pan nutritivo", "Pan sencillo", "Pan circular")
    print("Descripción")
    for desc in descripcion:
        print(desc)

def diccionario_stock_precio():
    stock_precio={
        "Stock": [30, 10, 25, 5, 15],
        "Precio": [10, 5, 30, 10, 25]
        }
    for x, y in stock_precio.items():
        print(f"{x,y}")

def realizar():
    print("La operacion se realizó correctamente para los datos de la Panadería")

Baguette=Producto()
Croisant=Producto()
Integral=Producto()
Blanco=Producto()
Bagel=Producto()
print("-----------------")
Baguette.estado("Baguette")
Croisant.estado("Croisant")
Integral.estado("Integral")
Blanco.estado("Blanco")
Bagel.estado("Bagel")
print("-----------------")
print("Lista de productos")
lista_productos()
print("-----------------")
print("Lista de productos")
tupla_descripcion()
print("-----------------")
print("Lista de productos")
diccionario_stock_precio()
print("-----------------")
realizar()
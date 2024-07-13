dict_1 = {"nombre":"Anselmo", "edad":31, "zapato":{"talla": 42,"color":"negro"}}
dict_2 = {"nombre":"Fernanda", "edad":26,"zapato":{"talla": 36,"color":"azul"}}
dict_3 = {"nombre":"Alexandra", "edad":30, "zapato":{"talla": 36,"color":"blanco"}}

dicts = {}

dicts[1] = {"nombre": dict_1["nombre"],"edad": dict_1["edad"], "zapato":dict_1["zapato"]}
dicts[3] = {"nombre": dict_2["nombre"],"edad": dict_2["edad"], "zapato":dict_2["zapato"]}
dicts[2] = {"nombre": dict_3["nombre"],"edad": dict_3["edad"], "zapato":dict_3["zapato"]}

print(dicts)

def test_printer(element):
    return f"""
        nombre: {element["nombre"]}
        edad: {element["edad"]}
        color de zapato: {element["zapato"]["color"]}
        """


for element in dicts.values():
    print(test_printer(element))



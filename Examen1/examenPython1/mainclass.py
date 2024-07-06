
# Anselmo código
class Libro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.prestado = False

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def prestar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                if not libro.prestado:
                    libro.prestado = True
                    return f"Libro '{titulo}' prestado."
                else:
                    return f"Libro '{titulo}' ya está prestado."
        return f"Libro '{titulo}' no encontrado."

    def devolver_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                if libro.prestado:
                    libro.prestado = False
                    return f"Libro '{titulo}' devuelto."
                else:
                    return f"Libro '{titulo}' no estaba prestado."
        return f"Libro '{titulo}' no encontrado."

# Ejemplo de uso
biblio = Biblioteca()
biblio.agregar_libro(Libro("El Quijote"))
biblio.agregar_libro(Libro("1984"))

print(biblio.prestar_libro("1984"))
print(biblio.prestar_libro("1984"))
print(biblio.devolver_libro("1984"))
print(biblio.devolver_libro("1984"))
print(biblio.prestar_libro("El Quijote"))
print(biblio.devolver_libro("El Quijote"))

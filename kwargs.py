import unittest


def buscar_datos(*args, **kwargs):
    database = kwargs.get("database", None)
    if database is None:
        print("Error: Base de datos no proporcionada.")
        return None
    for key, persona in database.items():
        nombre_completo = " ".join(value for key, value in persona.items())
        nombres_apellidos_combinados = set()
        for i in range(len(args)):
            for j in range(i, len(args)):
                nombres_apellidos_combinados.add(" ".join(args[i:j+1]))
        if any(nombre_apellido in nombre_completo for nombre_apellido in nombres_apellidos_combinados):
            return key
    return None
if __name__ == "__main__":
    database = {
        1: {
            "nombre1": "Pablo",
            "nombre2": "Diego",
            "apellido1": "Ruiz",
            "apellido2": "Picasso"
        },
    }
    nombre_completo = input("Ingrese el nombre completo de la persona: ").split()
    resultado = buscar_datos(*nombre_completo, database=database)
    if resultado is not None:
        print(f"La persona con el nombre completo {nombre_completo} está en la base de datos. Su ID es: {resultado}.")
    else:
        print(f"La persona con el nombre completo {nombre_completo} no está en la base de datos.")

class TestBuscarDatos(unittest.TestCase):
    def setUp(self):
        self.database = {
            1: {
                "nombre1": "Pablo",
                "nombre2": "Diego",
                "apellido1": "Ruiz",
                "apellido2": "Picasso"
            }
        }

    def test_persona_existente(self):
        resultado = buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", database=self.database)
        self.assertEqual(resultado, 1)

    def test_persona_no_existente(self):
        resultado = buscar_datos("Juan Marcos", database=self.database)
        self.assertIsNone(resultado, 0)

    def test_busqueda_flexible(self):
        resultado = buscar_datos("Diego", "Pablo", "Picasso", "Ruiz", database=self.database)
        self.assertEqual(resultado, 1)

        resultado = buscar_datos("Ruiz", "Pablo", "Diego", "Picasso", database=self.database)
        self.assertEqual(resultado, 1)

if __name__ == "__main__":
    unittest.main()


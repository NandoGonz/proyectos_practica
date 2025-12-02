from Controllers.biblioteca_controller import BibliotecaController
from Controllers.seccion_controller import SeccionController
from Controllers.libros_controller import LibroContoller

b1 = BibliotecaController()
b1.create_biblioteca("Central", "Main 123 st")


# for row in b1.get_all_bibliotecas():
#    print(row.__dict__)

# print(b1.get_biblioteca_by_id(1).__dict__)
# table.add_row([row['nombre_seccion'], row['piso?]])
# table.title = f"Secciones de la Biblioteca {row['nombre_biblioteca']}

# print(table)

# print(b1.update_biblioteca(6, "Biblioteca central", "456 Elm st"))
# b1.delete_biblioteca(6)

# s1.create.seccion(1, "Literatura", 2)
# s1.update.seccion("Literatuta", 2, 11)

# l1 = LibroControler()
# bts = l1.buscar_por_titulo("Don Quijote de la Mancha")
# for bt in bts:
#   print(bt)

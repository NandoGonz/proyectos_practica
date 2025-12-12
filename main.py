from prettytable import PrettyTable
from Controllers.biblioteca_controller import BibliotecaController
from Controllers.seccion_controller import SeccionController

table = PrettyTable()
b1 = BibliotecaController()
# b1.create_bibliteca("GonzalezBook", "Chivolo 13-11 Centro")

# Imprimimso todas las bibliotecas usando un ciclo for y usamos el decorador __dict__
# for row in b1.get_all_bibliotecas():
#  print(row.__dict__)

s1 = SeccionController()
# s1.create_seccion(7, "Historia Co", 2)
# for row in s1.get_all_secciones():
# print(row.__dict__)
# print(s1.get_seccion_by_id(2).__dict__)
# for row in s1.get_secciones_by_bibliotecas(1):
#    print(row)

# con pretty

# table.field_names = ["Dirección", "Sección"]
# for row in s1.get_secciones_by_bibliotecas(1):
#    table.title = f"Sección de las bibliotecas {row['nombre_biblioteca']}"
#    table.add_row([row["direccion"], row["nombre_seccion"]])
# print(table)
# s1.update_seccion("Literatura", 3, 11)
# print(s1.delete_seccion(13))

from Controllers.biblioteca_controller import BibliotecaController

b1 = BibliotecaController()
# b1.create_biblioteca("Central" "Main 123 st")


# for row in b1.get_all_bibliotecas():
#    print(row.__dict__)

# print(b1.get_biblioteca_by_id(1).__dict__)

# print(b1.update_biblioteca(6, "Biblioteca contral", "456 Elm st"))
b1.delete_biblioteca(6)

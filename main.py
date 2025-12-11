from Controllers.biblioteca_controller import BibliotecaController

b1 = BibliotecaController()
# b1.create_bibliteca("GonzalezBook", "Chivolo 13-11 Centro")

# Imprimimso todas las bibliotecas usando un ciclo for y usamos el decorador __dict__
for row in b1.get_all_bibliotecas():
    print(row.__dict__)

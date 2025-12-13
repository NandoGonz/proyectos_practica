class MenuView:

    def mostrar_menu(self):
        while True:
            print("#" * 50)
            print("1. Buscar un libro")
            print("2. Ver bibliotecas")
            print("0. Salir")

            opcion = int(input("Seleccione una opción: "))
            match opcion:
                case 1:
                    self.buscar_por_libro()

    def buscar_por_libro(self):
        while True:
            print("=" * 50)
            print("====== BUSQUEDA POR LIBRO =====")
            print("1. Titulo")
            print("2. Genero")
            print("3. Autores")
            print("4. ISBN")
            print("5. Palabra")
            print("0. Salir")

            opcion = int(input("Seleccione una opción: "))
            match opcion:
                case 1:
                    self.buscar_por_libro()

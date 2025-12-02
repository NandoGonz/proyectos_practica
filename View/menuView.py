class MenuView:

    def mostrar_menu_inicial(self):
        while True:
            print("=" * 60)
            print("1. Buscar un libro")
            print("2. Ver una biblioteca")
            print("0. Salir")

            opcion = input("Seleccione una opcion: ").strip()
            match opcion:
                case 1:
                    self.busqueda_por_libro()

    def busqueda_por_libro(self):
        print("=" * 60)
        print("===== BUSQUEDA POR LIBRO=====")
        print("1. Titulo")
        print("2. Genero")
        print("3. Autor")
        print("4. ISBN")
        print("5. palabra")
        print("0. Salir")

        opcion = input("Seleccione una opcion: ").strip()
        match opcion:
            case 1:
                pass

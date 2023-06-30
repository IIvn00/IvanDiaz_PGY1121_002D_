class Libro:
    Codigo_libro=''
    Titulo_libro=''
    Autor_Libro=''
    Precio_libro=0
    Pais_libro=''
    Publicacion_libro=0

    def __int__(self):
        self.Codigo_libro='AAA-111'
        self.Titulo_libro='S/N'
        self.Autor_Libro='S/N'
        self.Precio_libro=20000
        self.Publicacion_libro=1810
        self.Pais_libro='Suiza'

    def setCodigo_libro(self,Codigo):
        if Codigo[0:3].isalpha() and Codigo[3:4]=='-' and Codigo[4:6].isdigit():
            self.Codigo_libro=Codigo
            return True
        else:
            print("Formato de codigo incorrecto Ej: AAC-123")
            return False

    def setPrecio_libro(self,Precio):
        if Precio >= 10000 and Precio <=150000:
            self.Precio_libro=Precio
            return True
        else:
            print("Precio entre 10000 y 150000")
            return False

    def setPublicacion_libro(self,Publicacion):
        if Publicacion >=1780 and Publicacion <=2023:
            if Publicacion == 1810 or Publicacion == 1840 or Publicacion == 1870 or Publicacion == 1900 or Publicacion == 1930 or Publicacion == 1960 or Publicacion == 1990 or Publicacion == 2020:
                print("----SU LIBRO ES EDICON ESPECIAL FELICIDADES----")
            self.Publicacion_libro=Publicacion
            return True
        else:
            print("Año de publicacion entre 1780 y 2023")
            return False
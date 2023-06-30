from Libro import *
import random as rn
import numpy as np
###############################################AQUI ABAJO LOS DEF
def grabarlibro(arreglo_libro):
    book = Libro()

    c = False
    while c == False:
        c = book.setCodigo_libro(input("Ingrese Codigo del Libro:"))
    book.Titulo_libro=input("Ingrese Titulo del Libro:")
    book.Autor_Libro=input("Ingrese Autor del Libro:")
    book.Pais_libro=input("Ingrese Pais del Libro:")
    c = False
    while c == False:
        c = book.setPrecio_libro(int(input("Ingrese Precio del Libro:")))
    c = False
    while c == False:
        c = book.setPublicacion_libro(int(input("Ingrese Año Publicacion del Libro:")))
    return np.append(arreglo_libro, book)

def buscarlibro(arreglo_libro):
    codigo=input("Ingrese Codigo del Libro")
    flag=False
    for book in arreglo_libro:
        if codigo == book.Codigo_libro:
            flag=True
            print("CARACTERISTICAS DEL LIBRO....")
            print(f"Titulo del Libro:   {book.Titulo_libro}")
            print(f"Autor del Libro:    {book.Autor_Libro}")
            print(f"Pais del Libro:     {book.Pais_libro}")
            print(f"Precio:            ${book.Precio_libro}")
            print(f"Año de Publicacion: {book.Publicacion_libro}")
    if flag==False:
        print("Su libro no fue encontrado......")


def pais(arreglo_libro):
    nlista=rn.randint(1500,5000)
    pais=input("Ingrese Pais de busqueda:")
    flag=False
    for book in arreglo_libro:
        if pais == book.Pais_libro:
            flag=True
            print("----SU LIBRO FUE ENCONTRADO----")
            print(f"Numero de Listado:  {nlista}")
            print(f"Titulo del Libro:   {book.Titulo_libro}")
            print(f"Autor del Libro:    {book.Autor_Libro}")
            print(f"Pais del Libro:     {book.Pais_libro}")
            print(f"Precio:            ${book.Precio_libro}")
            print(f"Año de Publicacion: {book.Publicacion_libro}")
    if flag == False:
        print("Pais no encontrado....")


def listado(arreglo_libro):
    print("-------------IMPRIMIR INFORME------------")
    print("1) Pais")
    try:
        op_lista=int(input("Ingrese (1)"))
        match op_lista:
            case 1:
                pais(arreglo_libro)
    except BaseException as error:
        print(f"ERROR: {error}")
def Salir():
    print("AUTOR: Ivan Diaz")
    print("VERSION: Python 3.11")
    return False
################################################AQUI ABAJO EL MENU
arreglo_libro=np.array([])
ciclo=True
while ciclo:
    print("----LIBRERIA MAYOR----")
    print("1) Ingresar Libro")
    print("2) Buscar Libro")
    print("3) Imprimir Listado")
    print("4) Salir")
    try:
        op=int(input("Ingrese (1-4)"))
        match op:
            case 1:
                arreglo_libro=grabarlibro(arreglo_libro)
            case 2:
                buscarlibro(arreglo_libro)
            case 3:
                listado(arreglo_libro)
            case 4:
                ciclo=Salir()
    except BaseException as error:
        print(f"ERROR: {error}")

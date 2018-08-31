
from io import open #Librería para ficheros de texto

class readScript():
    archivo = ""
    def __init_(self):
        self.texto = []
        self.archivo = "lineas.txt"

    def leeArchivo(self):
        print(self.archivo)
        file_doc = open (self.archivo,"r")
        self.texto = file_doc.readlines() #Guarda todo en la variable texto como listas. Una lista por cada linea
        #   ['1 1 3 8\n', '7 9 10 6\n', '5 1 5 8\n']    cuando solo es print(texto)
        #   1 1 3 8 cuando es print(texto[0])
        file_doc.close()
        return self.texto

#Una vez cargado todo lineas.txt, podemos dejar de usar el archivo y operar desde acá.

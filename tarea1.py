#Open terminal ATOM : ctrl + shft + P => Script => Script:Run
from io import open #Librería para ficheros de texto

def openFile():
    file_doc = open ("lineas.txt","r")
    texto = file_doc.readlines() #Guarda todo en la variable texto como listas. Una lista por cada linea
    #   ['1 1 3 8\n', '7 9 10 6\n', '5 1 5 8\n']    cuando solo es print(texto)
    #   1 1 3 8 cuando es print(texto[0])
    file_doc.close()
    return texto
#Una vez cargado todo lineas.txt, podemos dejar de usar el archivo y operar desde acá.

#Puntos = [[None,None],[None,None]]  #P1 = x,x; P2 = y,y
def anSuperior(Ysup=0,Yi=0,Yf=0,Xi=0,Xf=0):
    #Usup = (Ysup - Yi)/(Yf-Yi)
    Punto = []
    Usup = 0.0
    Usup = (Ysup - Yi)/(Yf - Yi)
    if Usup >= 0 and Usup <= 1:
        Xsup = Xi + Usup*(Xf-Xi)
        if Xsup >= Xi and Xsup <=Xf:  #Queda dentro del rango Xi <= Xsup <= Xf
            if Ysup >= Yi and Ysup <=Yf: #Queda dentro del rango Yi <= Ysup <= Yf
                Punto = [Xsup,Ysup]
    else:
        Punto = [None,None]
    return Punto

def anInferior():
    return Punto

def anIzquierdo():
    return Punto

def anDerecho():
    return Punto

def ventanear():
    print ("Valores de ventana:\n")
    ventana[0] = input("Xizq = ")
    ventana[1] = input("Yinf = ")
    ventana[2] = input("Xder = ")
    ventana[3] = input("Ysup = ")
#def Main
def main():
    p1 = [0,0]
    p2 = [None,None]
    ventana = [None,None,None,None] #(Xiz,Yinf) (Xder,Ysup)
    lineas = 0  #maximo 3

    texto = openFile()
    lineas = []
    lineas.append(texto[0].split())
    lineas.append(texto[1].split())
    lineas.append(texto[2].split())

    x1 = lineas[0][0]
    x1 = float(x1)
    y1 = lineas[0][1]
    y1 = float(y1)
    x2 = lineas[0][2]
    x2 = float(x2)
    y2 = lineas[0][3]
    y2 = float(y2)
    print (type(x1))

    p1 = anSuperior(ventana[3],y1,y2,x1,x2)

    print (p1)

main();

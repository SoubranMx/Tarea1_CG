#Open terminal ATOM : ctrl + shft + P => Script => Script:Run
from io import open #Librería para ficheros de texto

def leeArchivo():
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
"""
def anInferior():
    return Punto

def anIzquierdo():
    return Punto

def anDerecho():
    return Punto
"""

def ventanear():
    print ("Valores de ventana:\n")
    ventana = []
    ventana.append(input("Xizq = "))
    ventana.append(input("Yinf = "))
    ventana.append(input("Xder = "))
    ventana.append(input("Ysup = "))
    #ventana[0] = input("Xizq = ")
    #ventana[1] = input("Yinf = ")
    #ventana[2] = input("Xder = ")
    #ventana[3] = input("Ysup = ")
    return ventana

def readFile():
    texto = leeArchivo()
    lineas = []
    if len(texto) > 0 and len(texto) < 4:
        sttr = str(type(texto))
        #print ("Linea 55 type = "+ sttr +" dentro: "+ str(texto)+ "len = " + str(len(texto)))
        for n in texto:
            #print(n + "\n")
            l = n.split()
            l = [int(i) for i in l]
            lineas.append(l)
        print(lineas)
    else:
        if len(texto) == 0:  #0 lineas
            print("Linea 60\n")
            lineas = [None]
        else:    #mas de 3 lineas
            print("Linea 63\n")
            lineas = [None, None]
    #lineas.append(texto[1].split()) # [7 9 10 6]
    #lineas.append(texto[2].split()) # [5 1 5 8]
    return lineas

#def Main
def main():
    p1 = [0,0]
    p2 = [None,None]
    ventana = [None,None,None,None] #(Xiz,Yinf) (Xder,Ysup)
    lineas_c = 0  #maximo 3
    ventana = ventanear()
    lineas = readFile()

    lineas_c = len(lineas)
    if lineas_c > 0 and lineas_c < 4:
        #codigo
        x1 = float(lineas[0][0])
        y1 = float(lineas[0][1])
        x2 = float(lineas[0][2])
        y2 = float(lineas[0][3])

        p1 = anSuperior(ventana[3],y1,y2,x1,x2)
        if p1 == None:
            print ("La linea 2 no obtuvo punto de recorte en Analisis Superior")
    else:
        if lineas_c == 0:
            print ("El archivo lineas.txt no tiene lineas, por favor actualicelo e introduzca de 1 a 3 lineas\n")
        else:
            print ("El archivo lineas.txt tiene mas de 3 lineas, este programa solo acepta 3.\n")

main();

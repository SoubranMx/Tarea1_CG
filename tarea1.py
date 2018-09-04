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
def Analisis(ventana,Yi,Yf,Xi,Xf,no_an):    #no_an: 0=>Superior, 1=>Inferior, 2=>Izquierdo, 3=>Derecho
    
    """switch(no_an){
        case 0: #Superior
            break;
        case 1: #Inferior
            break;
        case 2: #Izquierdo
            break;
        case 3: #Derecho
            break;
    }"""
    retun algo
def anSuperior(ventana,Yi=0,Yf=0,Xi=0,Xf=0):
    #Usup = (Ysup - Yi)/(Yf-Yi)
    #ventana[0] = x1
    #ventana[1] = y1
    #ventana[2] = x2
    #ventana[3] = y2
    Xizq = ventana[0]
    Xder = ventana[2]
    Yinf = ventana[1]
    Ysup = ventana[3]
    Punto = []
    Usup = 0.0
    Usup = (Ysup - Yi)/(Yf - Yi)
    print(Usup)
    if Usup >= 0 and Usup <= 1:
        Xsup = Xi + Usup*(Xf-Xi)
        print(Xsup,Xi,Xf)
        if Xsup >= Xizq and Xsup <= Xder:  #Queda dentro del rango Xizq <= Xsup <= Xder
            if Ysup >= Yinf and Ysup <= Ysup: #Queda dentro del rango Yinf <= Ysup <= Ysup
                Punto = [Xsup,Ysup]
            else:
                Punto = [None]
        else:
            Punto = [None]
    else:
        Punto = [None]
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
    #ventana.append(float(input("Xizq = ")))
    #ventana.append(float(input("Yinf = ")))
    #ventana.append(float(input("Xder = ")))
    #ventana.append(float(input("Ysup = ")))
    ventana.append(3.0)
    ventana.append(2.0)
    ventana.append(8.0)
    ventana.append(7.0)
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
            l = n.split()
            l = [int(i) for i in l]
            lineas.append(l)
        print(lineas)
    else:
        if len(texto) == 0:  #0 lineas
            print("El archivo lineas.txt no contiene lineas a leer")
            lineas = [None]
        else:    #mas de 3 lineas
            print("El archivo lineas.txt tiene mas de 3 lineas. Por favor, introduzca hasta 3 lineas")
            lineas = [None]
    #lineas.append(texto[1].split()) # [7 9 10 6]
    #lineas.append(texto[2].split()) # [5 1 5 8]
    return lineas   # [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

#def Main
def main():
    p1 = [None,None]
    p2 = [None,None]
    ventana = [None,None,None,None] #(Xiz,Yinf) (Xder,Ysup)
    lineas_c = 0  #maximo 3
    ventana = ventanear()
    lineas = readFile()
    if lineas.count(None) != 1: #Que haya entre 1 y 3 lineas
        lineas_c = len(lineas)
        #if lineas_c > 0 and lineas_c < 4:
            #codigo
        x1 = float(lineas[0][0])
        y1 = float(lineas[0][1])
        x2 = float(lineas[0][2])
        y2 = float(lineas[0][3])
        print(x1,x2,y1,y2)
        p1 = anSuperior(ventana,y1,y2,x1,x2)
        print(p1,type(p1))
        if p1.count(None) == 1:
            print ("La linea 2 no obtuvo punto de recorte en Analisis Superior")
        """else:
            if lineas_c == 0:
                print ("El archivo lineas.txt no tiene lineas, por favor actualicelo e introduzca de 1 a 3 lineas\n")
            else:
                print ("El archivo lineas.txt tiene mas de 3 lineas, este programa solo acepta 3.\n")"""

main();

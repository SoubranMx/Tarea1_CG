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

def Analisis(ventana,Yi,Yf,Xi,Xf,no_an):
    #no_an: 0=>Superior, 1=>Inferior, 2=>Izquierdo, 3=>Derecho
    #Yi,Yf,Xi,Xf dependen de los valores de las lineas que vienen en listas
    #ventana contiene los valores de la ventana, que limitan superior,inferior,izquierdo y derecho
    Xizq = ventana[0]
    Xder = ventana[2]
    Yinf = ventana[1]
    Ysup = ventana[3]

    dx = Xf - Xi
    dy = Yf - Yi

    Punto = [None]

    if no_an == 0:
        if dy != 0:
            Ux = (Ysup-Yi)/(dy)
            if evaluaU(Ux) == True:
                Xsi = Xi + Ux*(dx)
                Punto = evaluaP([Xsi,Ysup],ventana)
            else:
                Punto = [None]
        else:
            Punto = [None]
    elif no_an == 1:
        if dy != 0:
            Ux = (Yinf-Yi)/(dy)
            if evaluaU(Ux) == True:
                Xsi = Xi + Ux*(dx)
                Punto = evaluaP([Xsi,Yinf],ventana)
            #Este else tal vez no es necesario
            else:
                Punto = [None]
        else:
            Punto = [None]
    elif no_an == 2:
        if dx != 0:
            Uy = (Xizq-Xi)/(dx)
            if evaluaU(Uy) == True:
                Yid = Yi + Uy*(dy)
                Punto = evaluaP([Xizq,Yid],ventana)
            else:
                Punto = [None]
        else:
            Punto = [None]
    elif no_an == 3:
        if dx != 0:
            Uy = (Xder-Xi)/(dx)
            if evaluaU(Uy) == True:
                Yid = Yi + Uy*(dy)
                Punto = evaluaP([Xder,Yid],ventana)
            else:
                Punto = [None]
        else:
            Punto = [None]
    return Punto #debiera regresar P=[Xizq/der/sup/inf , Yizq/der/sup/inf] o P=[none]

def evaluaU(U):
    bulean = False
    if U >= 0 and U <= 1:
        bulean = True
    else:
        bulean =False
    return bulean

def evaluaP(Puntos,ventana):
    Punto = [None]
    if Puntos[0] >= ventana[0] and Puntos[0] <= ventana[2] and Puntos[1] >= ventana[1] and Puntos[1] <= ventana[3]:
        #Xi <= X <= Xf  and Yi <= Y <= Yf
        Punto = Puntos
    else:
        Punto = [None]
    return Punto

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
        #print(lineas)
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
    p = []
    Punto = []
    texto = ["Superior","Inferior","Izquierdo", "Derecho"]
    ventana = [] #(Xiz,Yinf) (Xder,Ysup)
    lineas_c = 0  #maximo 3
    ventana = ventanear()
    lineas = readFile()
    if lineas.count(None) != 1: #Que haya entre 1 y 3 lineas
        lineas_c = len(lineas)
        #if lineas_c > 0 and lineas_c < 4:
            #codigo
        for i in range(0,lineas_c):
            print ("Linea %d :" % (i+1))
            x1 = float(lineas[i][0])
            x2 = float(lineas[i][2])
            y1 = float(lineas[i][1])
            y2 = float(lineas[i][3])
            #print(x1,x2,y1,y2)
            for i in range(0,4):
                print("\tAnalisis %s\t:  "%(texto[i]),end='')
                p = Analisis(ventana,y1,y2,x1,x2,i)
                if p.count(None) == 0 and Punto.count(p) == 0:
                    Punto.append(p)
                    print("Punto de recorte en (%2.2f,%2.2f)"%(p[0],p[1]))    #Punto de recorte en (X,Y)
                elif Punto.count(p) != 0:
                    print("Punto de recorte en (%2.2f,%2.2f)"%(p[0],p[1]))
                else:
                    print("No tiene punto de recorte")

            print("")
            if Punto.count(None) == 0:
                j=len(Punto)
                for i in range(0,j):
                    print("\tPunto P%d = (%2.2f,%2.2f)"%(i+1,Punto[0][0],Punto[0][1]))
                    x = Punto.pop(0)
            print("")
    return
main();

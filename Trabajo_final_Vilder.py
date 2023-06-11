#-*- coding: 1252 *

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import pyplot
import matplotlib.image as mpimg

#Para Graficos
Años=[]
Meses=[]
valores=[]
colors=["purple"]
color=["Green"]


print("================================================================================")
print("\n\t=========BIENVENIDO AL APLICATIVO [CHANGING LIFE]=========")
print("================================================================================")
print("\nCREADORES DEL APLICATIVO:")
print("1. Rivera Huaman, Neyson Joel     CARRERA: Ingenieria de Sistemas de informacion")
print("2. Anchante Arana, Alvaro Nicolas CARRERA: Ingenieria de Sistemas de informacion")
print("3. Sandoval Verde, Vilder Luis    CARRERA: Ingenieria de Sistemas de informacion")

continuar=True
while continuar:
    print("\n\t¿Que Desea Realizar?:")
    print("\t[1].Registros de evolucion de la probreza en el peru")
    print("\t[2].Crear estadisticas/Graficos")
    print("\t[3].Crear datos para exportar a excel")
    print("\t[4].Salir")
    print("")
    op=int(input("Ingrese una opcion:"))
    if op==1:
        print("\n\t=====SITUACION DE POBREZA DE PERU======")
        print("\t[1].Mostrar poblacion en situacion de pobreza monetaria")
        print("\t[2].Mostrar poblacion en situacion de pobreza extrema")
        print("\t[3].Mostrar departamentos con mayor nivel de pobreza/Grafico ")
        print("\t[4].Mostrar Data de poblacion de situacion de pobreza por Departamentos/Provincias/Distritos")
        opcion=int(input("Ingrese una opcion de situacion:"))
        if opcion==1:
            print("\n")
            print("POBLACIÓN EN SITUACIÓN DE POBREZA MONETARIA, SEGÚN ÁMBITO GEOGRÁFICO, 2014- 2020")
            excel=pd.read_excel(r"D:\Python\Trabajo_Final\Trabajo_Final\Pobreza_1.xlsx", sheet_name='POBREZA MONETARIA')
            print(excel)
        if opcion==2:
            print("\n")
            print("POBLACIÓN EN SITUACIÓN DE POBREZA EXTREMA MONETARIA, SEGÚN ÁMBITO GEOGRÁFICO, 2014 - 2020")
            excel=pd.read_excel(r"D:\Python\Trabajo_Final\Trabajo_Final\Pobreza_1.xlsx", sheet_name='POBREZA EXTREMA MONETARIA')
            print(excel)
        if opcion==3:
            contr=True
            while contr:
                print("\n")
                print("\nEstos departamentos la pobreza monetaria se ubica en el rango entre 41.4% a 45.9%.")
                print("[1].Ayacucho")
                print("[2].Cajamarca")
                print("[3].Huancavelica")
                print("[4].Huanuco")
                print("[5].Pasco")
                print("[6].Puno")
                op=int(input("Elije un departamento:"))
                if op==1:
                     Años=[2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022]
                     valores=[376033,349111,337554,344126,313202,360212,315153,283668,232192,340892,340898,339014,337146]
                     colors=["blue"]
                     pyplot.title("Estadistica de pobres en Ayacucho 2010-2022")
                     pyplot.bar(Años,height=valores,color=colors,width=0.5)
                     plt.xlabel("Años")
                     plt.ylabel("Numero de pobreza")
                     pyplot.show()
                if op==2:
                     Años=[2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022]
                     valores=[356033,349111,357554,344126,313202,360212,315153,383668,392192,350892,320898,359014,367146]
                     colors=["green"]
                     pyplot.title("Estadistica de pobres en Cajamarca 2010-2022")
                     pyplot.bar(Años,height=valores,color=colors,width=0.5)
                     plt.xlabel("Años")
                     plt.ylabel("Numero de pobreza")
                     pyplot.show()
                if op==3:
                    Años=[2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022]
                    valores=[376033,349111,337554,344126,313202,360212,315153,283668,232192,340992,240898,359014,367146]
                    colors=["red"]
                    pyplot.title("Estadistica de pobres en Huancavelica 2010-2022")
                    pyplot.bar(Años,height=valores,color=colors,width=0.5)
                    plt.xlabel("Años")
                    plt.ylabel("Numero de pobreza")
                    pyplot.show()
                if op==4:
                    Años=[2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022]
                    valores=[346033,369111,337554,344126,313202,360212,315153,283668,352192,380892,360898,329014,347146]
                    colors=["gray"]
                    pyplot.title("Estadistica de pobres en Huanuco 2010-2022")
                    pyplot.bar(Años,height=valores,color=colors,width=0.5)
                    plt.xlabel("Años")
                    plt.ylabel("Numero de pobreza")
                    pyplot.show()
                if op==5:
                    Años=[2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022]
                    valores=[366033,349111,337554,344126,313202,360212,315153,283668,232192,340892,340898,339014,287146]
                    colors=["purple"]
                    pyplot.title("Estadistica de pobres en Pasco 2010-2022")
                    pyplot.bar(Años,height=valores,color=colors,width=0.5)
                    plt.xlabel("Años")
                    plt.ylabel("Numero de pobreza")
                    pyplot.show()
                if op==6:
                    Años=[2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022]
                    valores=[376033,349111,337554,344126,313202,360212,315153,283668,232192,320892,340898,339014,337146]
                    colors=["blue"]
                    pyplot.title("Estadistica de pobres en PUNO 2010-2022")
                    pyplot.bar(Años,height=valores,color=colors,width=0.5)
                    plt.xlabel("Años")
                    plt.ylabel("Numero de pobreza")
                    pyplot.show()
                contr=input("Desea continuar en esta opcion[2](S/N):")=="S"
        if opcion==4:
            print()
            print("POBLACIÓN, POBREZA MONETARIA TOTAL, UBICACIÓN DE LA POBREZA TOTAL,SEGÚN PROVINCIA Y DISTRITO, 2018")
            print()
            print("[Ubigeo] [Sufijo Distrito] [Departamento/Provincia/Distrito] [Poblacion] [Intervalos] [pobreza monetaria total]")
            excel=pd.read_csv('D:\Python\Trabajo_Final\Trabajo_Final\Pobreza_1 - Poblacion.csv', sep=';')
            print(excel)
            op=input("\n¿Desea ver las imagenes?(S/N):")
            if op=="S":
               img = mpimg.imread('graficas-pobreza_vv-copy.jpg')
               imgplot = plt.imshow(img)
               plt.show()
               img = mpimg.imread('ERtMRdSWsAEk1jv.jpg')
               imgplot = plt.imshow(img)
               plt.show()
            else:
                print("Gracias por utilizar el aplicativo")
    if op==2:
        print("¿Que desea graficar?")
        print("[1]. Grafico/Estadistica por Meses/Numero de pobreza")
        print("[2]. Grafico/Estadistica por Años/Numero de pobreza")
        op=int(input("Elije una opcion:"))
        if op==1:
          
            numero=0
            dat=int(input("Cuanto datos seas ingresar:"))
            año=input("Ingrese el año:")
            Depa=input("Ingrese el departamento:")
            conti=True
            while numero<dat:
                mes=input("Ingrese un mes:")
                var=float(input("Ingrese el numero de pobreza:"))
                
                Meses.append(mes)
                valores.append(var)

                numero+=1
              
            pyplot.title("Estadisticas de " +str(Depa)+str(año))
            pyplot.bar(Meses,height=valores,color=colors,width=0.5)
            plt.xlabel("Meses")
            plt.ylabel("Numero de pobreza")
            pyplot.show()
                

                             
        if op==2:
            numero=0
            dat=int(input("Cuanto datos seas ingresar:"))
            año=input("Ingrese el año:")
            Depa=input("Ingrese el departamento:")
            conti=True
            while numero<dat:
                anio=int(input("Ingrese un año:"))
                var=float(input("Ingrese el numero de pobreza:"))
                
                Años.append(anio)
                valores.append(var)

                numero+=1

            conti=input("Desea continuar(S/N):")=="S"
            pyplot.title("Estadisticas de " +str(Depa)+str(año))
            pyplot.bar(Años,height=valores,color=colors,width=0.5)
            plt.xlabel("Años")
            plt.ylabel("Numero de pobreza")
            pyplot.show()
    if op==3:
        farm=[]
        Colun=[]
        Col_1=[]
        numero=0
        dat=int(input("Ingrese la cantidad de datos:"))
        col=input("Ingrese el nombre de la columna 1:")
        far=input("Ingrese el nombre de la columna 2:")
        colu=input("Ingrese el nombre de la columna 3:")
        while numero<dat:
            lok=input("Ingrese el nombre "+str(col)+" en la columna 1:")
            lok_1=int(input("Ingrese el nombre/numeros "+str(far)+" en la columna 2:"))
            lok_2=int(input("Ingrese el nombre/numeros "+str(colu)+" en la columna 3:"))
        
            Colun.append(lok)
            farm.append(lok_1)
            Col_1.append(lok_2)

            numero+=1
        
            df=pd.DataFrame({
                 col:Colun,
                 far:farm,
                 colu:Col_1})

            df.to_excel('D:\Python\Trabajo_Final\Trabajo_Final\Luis.xlsx',index=False)
           
             
    if op==4:
       print("Gracias por utilizar el aplicativo")
       break
    continuar=input("Desea continuar en esta opcion[1](S/N):")=="S"



    



#17- La empresa de comunicaciones Línea Segura registra el origen, el destino,
#la fecha, la hora y la duración de todas las llamadas que hacen sus
#2usuarios, para esto hace uso de cinco vectores. Se requiere un algoritmo
#para saber si desde un teléfono determinado se ha efectuado algunallamada
#a un destino y en caso afirmativo conocer la fecha, la hora y la duración de la llamada.

origen=["123","456","789","321","654"]
destino=["987","654","321","123","456"]
fecha=["01/01/2023","02/02/2023","03/03/2023","04/04/2023","05/05/2023"]
hora=["10:00","11:00","12:00","13:00","14:00"]
duracion=[5,10,15,20,25]

telefono_origen=input("Ingrese el número de teléfono de origen: ")
telefono_destino=input("Ingrese el número de teléfono de destino: ")

llamada_encontrada=False

for i in range(len(origen)):
    if origen[i]==telefono_origen and destino[i]==telefono_destino:
        print("Se encontró una llamada desde "+telefono_origen+" a "+telefono_destino+".")
        print("Fecha: "+fecha[i])
        print("Hora: "+hora[i])
        print("Duración: "+str(duracion[i])+" minutos ")
        llamada_encontrada=True
        break

if not llamada_encontrada:
    print("No se encontró ninguna llamada desde: "+telefono_origen+" a "+telefono_destino+".")


lista=[]
mensaje=None
for i in range (4):
    calificacion=int(input("ingresa la calificacion:"))
    lista.insert(i,calificacion)
    if 0 <=calificacion<=69:
        mensaje= 'Reprobado'
    elif 70 <=calificacion<=100:
        mensaje = 'aprobado'
    else:
        mensaje='Calificacion no encntrada'
print(lista)
while True:
    condicion=input("¿desea hacer otro registro?(S=si N=no):")

    print(f'tienes calificaciòn {calificacion} y', mensaje)
    lista.insert(i,calificacion)
    if condicion =="n" or condicion=="N":
        break

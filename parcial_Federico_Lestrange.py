"""La agencia de viajes "Comprame un viaje" realizó una encuesta a 1000 de sus clientes sobre qué eligen comprarle y obtuvo los siguientes datos:

a)
 400 viajan en avión y los datos se han recolectado en una tupla: (57,35,11,3,41,23,6,22,10,5,7,67,9,4,58,42)
 100 alquilan autos y los datos se han recolectado en una lista: [7,9,4,10,2,8,41,11,3,5]
 700 prefieren alojamiento de distintos tipos y los datos se han recolectado en un diccionario:
 {"Hotel": 42, "Hostel": 9, "Motel": 67, "Apart-Hotel":58, "Apartment":4, "Boutique Hotel": 135,
 "Resort": 119, "Bed and Breakfast": 68, "Guest House": 8, "Lodge":75, "Casa Rural":26, "Inn": 59,
 "Pop-up Hotel": 7, "Business Hotel":23}

b) Por otra parte se sabe que:
 210 eligen alojamiento y avión.
 28 eligen alojamiento y alquilan auto.
 90 de los que alquilan autos también eligen avión.
 20 de la población total eligen avión, alquilan auto y eligen alojamiento.

c) Resolver y responder:
 1. Cuántos entrevistados eligen alojamiento, avión y alquilan autos?
 2. Cuántos entrevistados sólo eligen alojamiento y avión?
 3. Cuántos entrevistados sólo eligen avión y alquilar autos?
 4. Cuántos entrevistados sólo eligen alojamiento y alquilar autos?
 5. Cuántos entrevistados sólo eligen alojamiento?
 6. Cuántos entrevistados sólo eligen avión?
 7. Cuántos entrevistados sólo eligen alquilar autos?
 8. Cuántos entrevistados eligen 2 de las 3 propuestas?
 9. Cuántos entrevistados no eligen alojamiento, ni avión, ni alquilar autos?"""

from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles

U = 1000
tupla_avion = (57,35,11,3,41,23,6,22,10,5,7,67,9,4,58,42)
lista_autos = [7,9,4,10,2,8,41,11,3,5]
dict_alojamiento = {"Hotel": 42, "Hostel": 9, "Motel": 67, "Apart-Hotel":58, "Apartment":4, "Boutique Hotel": 135,
 "Resort": 119, "Bed and Breakfast": 68, "Guest House": 8, "Lodge":75, "Casa Rural":26, "Inn": 59,
 "Pop-up Hotel": 7, "Business Hotel":23}

 # Comprobamos resultados
def suma(obj) :
    suma = 0
    for i in obj :
        suma += i
    return suma

suma_avion = suma(tupla_avion)
suma_autos = suma(lista_autos)
suma_alojamiento = suma(dict_alojamiento.values())

print("Comprobamos los valores dados:")
print(f"Avion: {suma_avion} \nAutos: {suma_autos} \nAlojamiento: {suma_alojamiento}")

# Pasamos las colecciones a conjuntos
def a_conjunto(coleccion) :
    col = set()
    for i in coleccion :
        col.add(i)
    return col

set_avion = a_conjunto(tupla_avion)
set_autos = a_conjunto(lista_autos)
set_alojamiento = a_conjunto(dict_alojamiento.values())

print(f"\nConjuntos obtenidos: \nAvion: {set_avion} \nAutos: {set_autos} \nAlojamiento: {set_alojamiento}")

# Operaciones sobre conjuntos 
def inter_AB(a, b) :
    ab = a & b
    suma = 0
    for i in ab :
        suma += i
    return suma

def inter_ABC(a, b, c) :
    abc = a & b & c
    suma = 0
    for i in abc :
        suma += i
    return suma

aloj_avion = inter_AB(set_alojamiento, set_avion)
aloj_auto = inter_AB(set_alojamiento, set_autos)
avion_autos = inter_AB(set_avion, set_autos)
tres_objetos = inter_ABC(set_avion, set_autos, set_alojamiento)

print("\nComprobamos los valores del punto b)")
print(f"Elijen alojamiento y avión: {aloj_avion} \nElijen alojamiento y auto: {aloj_auto} \nElijen avión y auto: {avion_autos} \nElijen las 3 cosas: {tres_objetos}")

# Solo un objeto
def solo_objeto(a, b, c) :
    a = (a - b) & (a - c)
    suma = 0
    for i in a :
        suma += i
    return suma

solo_avion = solo_objeto(set_avion, set_autos, set_alojamiento)
solo_auto = solo_objeto(set_autos, set_alojamiento, set_avion)
solo_alojamiento = solo_objeto(set_alojamiento, set_avion, set_autos)

print("\nDatos obtenidos a partir de los conjuntos")
print(f"Elijen solo avión: {solo_avion} \nElijen solo auto: {solo_auto} \nElijen solo alojamiento: {solo_alojamiento}")

# Sólo 2 objetos 
def dos_objetos(a, b, c) :
    ab = (a & b) - c
    suma = 0
    for i in ab :
        suma += i
    return suma

solo_avion_auto = dos_objetos(set_avion, set_autos, set_alojamiento)
solo_avion_alojamiento = dos_objetos(set_avion, set_alojamiento, set_autos)
solo_auto_alojamiento = dos_objetos(set_autos, set_alojamiento, set_avion)

print(f"Elijen sólo avión y auto: {solo_avion_auto} \nElijen sólo avión y alojamiento: {solo_avion_alojamiento} \nElijen sólo auto y alojamiento: {solo_auto_alojamiento}")

# 2 de los 3 objetos
def dos_de_tres() :
    return solo_avion_auto + solo_avion_alojamiento + solo_auto_alojamiento

# Ningún objeto
def ningun_objeto() :
    return U - (solo_avion + solo_auto + solo_alojamiento + dos_de_tres() + tres_objetos)

# Diagrama de Venn3

plt.figure("Parcial NZ")
plt.title("Comprame un viaje")

d = venn3({"100":1, "010":1, "001":1, "110":1, "101":1, "011":1, "111":1}, set_labels=("Avión", "Auto", "Alojamiento"))
venn3_circles(subsets = (1,1,1,1,1,1,1), linewidth=1, color="grey")

d.get_label_by_id("100").set_text(solo_avion)
d.get_label_by_id("010").set_text(solo_auto)
d.get_label_by_id("001").set_text(solo_alojamiento)
d.get_label_by_id("110").set_text(solo_avion_auto)
d.get_label_by_id("101").set_text(solo_avion_alojamiento)
d.get_label_by_id("011").set_text(solo_auto_alojamiento)
d.get_label_by_id("111").set_text(tres_objetos)

plt.text(-1.10, 0.70,
 s="Universo = " + str(U),
 size=10,
 ha="left",
 va="bottom",
 bbox=dict(boxstyle="square",
 ec=(1.0, 0.7, 0.5),
 fc=(1.0, 0.9, 0.8),))

plt.text(0.5, -0.50,
 s="Fuera del conjunto: \n1000 - (70 + 190 + 20 + 2 + 8 + 482) = " + str(ningun_objeto()),
 size=8,
 ha="left",
 va="bottom",
 bbox=dict(boxstyle="square",
 ec=(1.0, 0.7, 0.5),
 fc=(1.0, 0.9, 0.8),))

plt.text(-1.3, -0.10,
 s="Respuestas solicitadas: ",
 size=10,
 ha="left",
 va="bottom",
 bbox=dict(boxstyle="square",
 ec=(1.0, 0.7, 0.5),
 fc=(1.0, 0.9, 0.8),))

plt.text(-1.3, -0.18,
 s="Elijen las tres propuestas: " + str(tres_objetos),
 size=9,
 ha="left",
 va="bottom",
 bbox=dict(boxstyle="square",
 ec=(1.0, 0.7, 0.5),
 fc=(1.0, 0.9, 0.8),))

plt.text(-1.3, -0.26,
 s="Sólo alojamiento y avión: " + str(solo_avion_alojamiento),
 size=9,
 ha="left",
 va="bottom",
 bbox=dict(boxstyle="square",
 ec=(1.0, 0.7, 0.5),
 fc=(1.0, 0.9, 0.8),))

plt.text(-1.3, -0.34,
 s="Sólo avión y autos: " + str(solo_avion_auto),
 size=9,
 ha="left",
 va="bottom",
 bbox=dict(boxstyle="square",
 ec=(1.0, 0.7, 0.5),
 fc=(1.0, 0.9, 0.8),))

plt.text(-1.3, -0.42,
 s="Sólo alojamiento y autos: " + str(solo_auto_alojamiento),
 size=9,
 ha="left",
 va="bottom",
 bbox=dict(boxstyle="square",
 ec=(1.0, 0.7, 0.5),
 fc=(1.0, 0.9, 0.8),))

plt.text(-1.3, -0.50,
 s="Sólo alojamiento: " + str(solo_alojamiento),
 size=9,
 ha="left",
 va="bottom",
 bbox=dict(boxstyle="square",
 ec=(1.0, 0.7, 0.5),
 fc=(1.0, 0.9, 0.8),))

plt.text(-1.3, -0.58,
 s="Sólo avión: " + str(solo_avion),
 size=9,
 ha="left",
 va="bottom",
 bbox=dict(boxstyle="square",
 ec=(1.0, 0.7, 0.5),
 fc=(1.0, 0.9, 0.8),))

plt.text(-1.3, -0.66,
 s="Sólo autos: " + str(solo_auto),
 size=9,
 ha="left",
 va="bottom",
 bbox=dict(boxstyle="square",
 ec=(1.0, 0.7, 0.5),
 fc=(1.0, 0.9, 0.8),))

plt.text(-1.3, -0.74,
 s="Elijen 2 de las 3 propuestas: " + str(dos_de_tres()),
 size=9,
 ha="left",
 va="bottom",
 bbox=dict(boxstyle="square",
 ec=(1.0, 0.7, 0.5),
 fc=(1.0, 0.9, 0.8),))

plt.text(-1.3, -0.82,
 s="Ninguno: " + str(ningun_objeto()),
 size=9,
 ha="left",
 va="bottom",
 bbox=dict(boxstyle="square",
 ec=(1.0, 0.7, 0.5),
 fc=(1.0, 0.9, 0.8),))

plt.show()
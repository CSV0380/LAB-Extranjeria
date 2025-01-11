from typing import * #nueva NamedTuple que puedes darle el tipo del dato que se almacene en la tupla
import csv

RegistroExtranjeria = NamedTuple(
    "RegistroExtranjeria", 
            [("distrito",str),
             ("seccion", str),
             ("barrio", str),
             ("pais",str),
             ("hombres", int),
             ("mujeres", int)
            ]
)


#APARTADO 1
def lee_datos_extranjeria(ruta: str) -> List[RegistroExtranjeria]: #le podemos añadir la estructura para que sea más fácil de especificar y entender
    res = []
    with open(ruta, encoding = 'utf-8') as f:
        lector = csv.reader(f, delimiter = ',')
        next(lector)
        for distrito, seccion, barrio, pais, hombres, mujeres in lector:
            distrito = str(distrito)
            seccion = str(seccion)
            barrio = str(barrio)
            pais = str(pais)
            hombres = int(hombres)
            mujeres = int(mujeres)
            res.append(RegistroExtranjeria(distrito, seccion, barrio, pais, hombres, mujeres))
    return res


#APARTADO 2
def numero_de_nacionalidades_distintas(registros: List[RegistroExtranjeria]) -> int:
    res = set()
    for nacionalidad in registros:
        res.add(nacionalidad.pais)
    return len(res)


#APARTADO 3
def secciones_distritos_con_extranjeros_nacionalidades(registros: List[RegistroExtranjeria], paises: set[str]) -> List[Tuple[str, str]]:
    res = []
    paises = paises.upper()
    for persona in registros:
        if persona.pais in paises:
            res.append((persona.distrito, persona.seccion))
    return sorted(res, key = lambda x: x[0])


#APARTADO 4
def total_extranjeros_por_pais(registros: List[RegistroExtranjeria]) -> dict[str:int]: #las claves son los paises y los valores son el numero total de extranjeros
    res = {}
    for persona in registros:
        if persona.pais not in res: # aprender a añadir cosas a diccionarios
            res[persona.pais] = 0
        else:
            res[persona.pais] += persona.hombres + persona.mujeres
    res = dict(sorted(res.items(), key = lambda item: item[1], reverse = True)) #para dar un diccionario ordenado por su valor de mayor a menor (no lo pide)
    return res


#APARTADO 5
def top_n_extranjeria(registros: List[RegistroExtranjeria], n=3) -> List[Tuple[str,int]]:
    total_por_pais = total_extranjeros_por_pais(registros) #llamamos a la funcion de antes para ahorrarnos un bucle, y accedemos a los items💣💣💣💣💣
    res = sorted(total_por_pais.items(), key = lambda x: x[1], reverse = True)[:n] #el [:n] es lo mismo ponerlo aquí que en el return
    return res



#APARTADO 6 (rebuscado)
def barrio_mas_multicultural(registros: List[RegistroExtranjeria]) -> str:
    res = {}
    for persona in registros:
        if persona.barrio not in res: #queremos buscar el barrio que mas paises de nacimiento diferentes tenga
            res[persona.barrio] = set()   #creamos un conjunto de los barrios para que no se repitan
        res[persona.barrio].add(persona.pais) #le añadimos el pais
    res = max(res.items(), key = lambda item: len(item[1]))[0]
    return res


#APARTADO 7 (entretenido)
def total_extranjeros_por_barrio(registros: List[RegistroExtranjeria], tipo=None) -> dict[str, int]:
    res = {}
    for persona in registros:
        if persona.barrio not in res:
            res[persona.barrio] = 0  #inicializamos la cuenta de extranjeros para cada barrio
        if tipo == 'Hombres':
            res[persona.barrio] += persona.hombres
        elif tipo == 'Mujeres':
            res[persona.barrio] += persona.mujeres
        else:  # Si tipo es None, sumamos hombres y mujeres
            res[persona.barrio] += persona.hombres + persona.mujeres
    return res


def barrio_con_mas_extranjeros(registros: List[RegistroExtranjeria], tipo=None) -> str:
    total_por_barrio = total_extranjeros_por_barrio(registros, tipo)
    barrio = max(total_por_barrio.items(), key = lambda item: item[1])[0]
    return barrio


#APARTADO 8 (no lo conseguí sacar)
def pais_mas_representado_por_distrito(registros: List[RegistroExtranjeria]) -> dict[str,str]:
    res = {}
    for distrito in registros:
        if distrito.distrito not in res: #esto lo hacemos para crear una clave de diccionario vacía
            res[distrito.distrito] = {}
        if distrito.pais not in res[distrito.distrito]:
            res[distrito.distrito][distrito.pais] = 0
        res[distrito.distrito][distrito.pais] += distrito.hombres + distrito.mujeres
    
    resf = {res: max(paises.items(), key=lambda item: item[1])[0]for res, paises in res.items()}
    return resf







#TESTS
if __name__ == '__main__':
    datos = lee_datos_extranjeria('data\extranjeriaSevilla.csv')
    #print(datos)

    #print(f"Hay {numero_de_nacionalidades_distintas(datos)} nacionalidades distintas.")

    #print(f"{secciones_distritos_con_extranjeros_nacionalidades(datos, "Estados unidos de america, china, colombia")}")

    #print(f"{total_extranjeros_por_pais(datos)}")

    #print(f"{top_n_extranjeria(datos)}")

    #print(f"{barrio_mas_multicultural(datos)}")

    #print(f"{barrio_con_mas_extranjeros(datos, "Mujeres")}")

    print(f"{pais_mas_representado_por_distrito(datos)}")



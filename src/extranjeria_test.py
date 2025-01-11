from extranjeria import *

def test_leer_datos(ruta: str) -> List[RegistroExtranjeria]:
    datos = lee_datos_extranjeria(ruta)
    print(f"Los 5 primeros datos son: \n {datos[:5]}")



if __name__ == '__main__':
    test_leer_datos('data\extranjeriaSevilla.csv')
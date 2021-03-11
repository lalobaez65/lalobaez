import re

cadena="Vamos a aprender expresiones regulares, aprender programacion"
textobuscar="aprender"
textoencontrado=re.search(textobuscar,cadena)

if textoencontrado is not None:
    print("Funcion start(): Inicia en "+ str(textoencontrado.start()))
    print("Funcion end(): Termina en "+ str(textoencontrado.end()))
    print("Funcion span(): (inicio,termina) "+ str(textoencontrado.span()))
    print("Funcion findall(): "+ str(re.findall(textobuscar,cadena)))
    print("Funcion len-findall, Veces que repite: "+ str(len(re.findall(textobuscar,cadena))))
else:
    print("No encontro texto")

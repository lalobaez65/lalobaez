import re

cadena="Vamos a aprender expresiones regulares"
textobuscar="aprender"
textoencontrado=re.search(textobuscar,cadena)


if textoencontrado is not None:
    print(textoencontrado.start())
else:
    print("No encontro texto")

import re

cadena="Vamos a aprender expresiones regulares"
textobuscar="aprenderr"

if re.search(textobuscar,cadena) is not None:
    print("Se encontro texto")
else:
    print("No encontro texto")

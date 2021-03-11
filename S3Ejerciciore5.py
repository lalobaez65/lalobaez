import re

lista_de_nombres=['Jose Guadalupe',
                  'Eduardo Baez',
                  'Angel Arath Nuñez',
                  'José Guadalupe']

for elemento in lista_de_nombres:
    if re.findall('^Eduardo',elemento):
        print("Buscar (^Eduardo) que inicie con "+elemento)
    if re.findall('Baez$',elemento):
        print("Buscar (Baez$) que termine con "+elemento)    
    if re.findall('[ñ]',elemento):
        print("Buscar [ñ] que contega "+elemento) 
    if re.findall('Jos[eé]',elemento):
        print("Buscar [eé] que contega "+elemento) 
    if re.findall('[g-n]',elemento):
        print("Buscar [g-n] que contega g a la n "+elemento) 
    if re.findall('^[J-N]',elemento):
        print("Buscar ^[J-N] que contega g a la n "+elemento) 

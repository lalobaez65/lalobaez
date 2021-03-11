#for usando una lista, archivo en formato |

fpipe=""
for caracteres  in ["a","b","c",2,3,1]:
    fpipe +=str(caracteres)+"|"   
print(fpipe)
file = open("prueba.txt", "w")
file.write(fpipe)
file.close()

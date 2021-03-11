#for usando una lista, archivo en formato CSV

fcsv=""
for caracteres  in ["apppppppppp","333","c6666666",2,3,1]:
    fcsv +=str(caracteres)+","   
print(fcsv)
file = open("prueba.csv", "w")
file.write(fcsv)
file.close()

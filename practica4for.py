#for usando una lista, para formar un XML
fXML="<datos>"
for i  in ["a","b","c",2,3,1]:
    fXML +="<dato>"+str(i)+"</dato>"
fXML+="<datos>"
print(fXML)
file = open("prueba.xml", "w")
file.write(fXML)
file.close()

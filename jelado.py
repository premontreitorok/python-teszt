import math
sorok=[]

with open("input.txt") as file:
    for sor in file:
        sorok.append(sor.strip().split())

#print(sorok)
old_sor=["0","0","0","0","0","0","0"]

def ido(x1,y1,z1,x2,y2,z2):
    eltelt=3600*(int(x1)-int(x2))+60*(int(y1)-int(y2))+int(z1)-int(z2)
    return "eltelt idő másodpercben: "+str(eltelt).rjust(5)



with open("output.txt","w") as file:
    for sor in sorok:
        ido1=ido(sor[0],sor[1],sor[2],old_sor[0],old_sor[1],old_sor[2])
        file.write((sor[0]+" "+sor[1]+" "+sor[2]+" "+sor[3]+" "+sor[4]).ljust(20)+ido1+"\n")
        old_sor=sor

        


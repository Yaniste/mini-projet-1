from random import*

#ex 1
h=float(input("hauteur ="))
r=float(input("rayon ="))
v=3.14*r*r*h/3
print(v)

#ex 2
N=randint(1,100)
tentative=0
d=0
while d!=N:
    d=int(input("votre proposition ="))
    tentative=tentative+1
    if d<N:
          print("c'est plus grand")
    elif d>N:
          print("c'est plus petit")
    else:
          print("bravo ", tentative, " tentatives")

#ex 3
taille=int(input("taille = ?"))
n="^"
espace=""
x=1
for i in range(taille):
    x+=2
nombre_espace=x//2
for i in range(nombre_espace):
    espace+=" "
for i in range(1,taille):
    print(espace,n,espace)
    n+="^^"
    nombre_espace=nombre_espace-1
    espace=""
    for i in range(nombre_espace):
        espace+=" "

#ex 4
rep=""
ht=float(input("prix ht = ?"))
while rep!="0":
    ttc=ht*1.2
    rep=input("tapez 0 pour terminer")
print(ttc,"euros")

#ex 5
def victime(n:int, t:int)->int:
    p=n*t
    return p

poule=int(input("nombre de poule(s) = ?"))
chien=int(input("nombre de chien(s) = ?"))
vache=int(input("nombre de vache(s) = ?"))
ami=int(input("nombre d'ami(s) = ?"))
points=victime(1,poule)+victime(3,chien)+victime(5,vache)+victime(10,ami)
points2=points
x=0
while points>0:
    points=points-100
    x+=1
x=x*200
print(x,"euros pour un total de",points2, "points")


#ex 6   
p=int(input("poids de Haruchi = ?"))
q=int(input("quantité de nourriture que mange Haruchi = ?"))
n=int(input("nombre d'animaux"))
animaux=[]
a=q/p
c=0
for i in range(n):
    x=input("poids de l'animal et quantité de nourriture")
    x=x.split(" ")
    animaux.append(x)
    b=int(animaux[i][1])/int(animaux[i][0])
    if b>a:
        c+=1
print(c, "animaux mangent plus qu'elle")
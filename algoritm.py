import requests
from requests.auth import HTTPBasicAuth
from xml.etree import ElementTree as ET
import numpy as np
from numpy import exp,sqrt
import matplotlib.pyplot as plt

left = "39.439770774506606"
bottom = "52.663807275961176"
right = "40.74841850675601"
top = "52.66389056542804"

a = requests.get(f' https://api.openstreetmap.org/api/0.6/map?bbox={left},{bottom},{right},{top}', auth=HTTPBasicAuth('bol642@yandex.ru', 'Qwerty12!')).content






intersection_coordinates = []
counter = {}
children = ET.fromstring(a)
s = []
road_types = ('primary', 'secondary', 'residential', 'tertiary', 'service') 
for child in children:
    for item in child:
        if item.tag == 'tag' and item.attrib['k'] == 'highway' and item.attrib['v'] in road_types: 
            s.append(child)



x = []
y = []
for child in children.findall("node"):
    coordinate = child.attrib['lat'] + ',' + child.attrib['lon']
    a =float(child.attrib["lat"])
    b = float(child.attrib['lon'])
    x.append(a)
    y.append(b)
    intersection_coordinates.append(coordinate)



X=x[20:40]
Y=y[20:40]
n=len(X)
RS=[];RW=[];RIB=[]
s=[]
for ib in np.arange(0,n,1):
         M = np.zeros([n,n])
         for i in np.arange(0,n,1):
                  for j in np.arange(0,n,1):
                           if i!=j:
                                    M[i,j]=sqrt((X[i]-X[j])**2+(Y[i]-Y[j])**2)
                           else:
                                    M[i,j]=float('inf')
         way=[]
         way.append(ib)
         for i in np.arange(1,n,1):
                  s=[]
                  for j in np.arange(0,n,1):                  
                           s.append(M[way[i-1],j])
                  way.append(s.index(min(s)))
                  for j in np.arange(0,i,1):
                           M[way[i],way[j]]=float('inf')
                           M[way[i],way[j]]=float('inf')         
         S=sum([sqrt((X[way[i]]-X[way[i+1]])**2+(Y[way[i]]-Y[way[i+1]])**2) for i in np.arange(0,n-1,1)])+ sqrt((X[way[n-1]]-X[way[0]])**2+(Y[way[n-1]]-Y[way[0]])**2)                      
         RS.append(S)
         RW.append(way)
         RIB.append(ib)
         print(RIB)

S=min(RS)
way=RW[RS.index(min(RS))]
ib=RIB[RS.index(min(RS))]       
X1=[X[way[i]] for i in np.arange(0,n,1)]
Y1=[Y[way[i]] for i in np.arange(0,n,1)]
S=min(RS)
way=RW[RS.index(min(RS))]
ib=RIB[RS.index(min(RS))]       
X1=[X[way[i]] for i in np.arange(0,n,1)]
Y1=[Y[way[i]] for i in np.arange(0,n,1)]
plt.title('Общий путь-%s.номер точки-%i.Всего точек -%i.\n Координаты X,Y заданы'%(round(S,3),ib,n), size=14)
plt.plot(X1, Y1, color='r', linestyle=' ', marker='o')
plt.plot(X1, Y1, color='b', linewidth=1)   
X2=[X[way[n-1]],X[way[0]]]
Y2=[Y[way[n-1]],Y[way[0]]]
plt.plot(X2, Y2, color='g', linewidth=2,  linestyle='-', label='Путь от  последней точки \n к гаражу')
plt.legend(loc='best')
plt.grid(True)
plt.show()  
Z=sqrt((X[way[n-1]]-X[way[0]])**2+(Y[way[n-1]]-Y[way[0]])**2)
Y3=[sqrt((X[way[i+1]]-X[way[i]])**2+(Y[way[i+1]]-Y[way[i]])**2) for i in np.arange(0,n-1,1)]
X3=[i for i in np.arange(0,n-1,1)]
plt.title('Пути от точки к точке')
plt.plot(X3, Y3, color='b', linestyle=' ', marker='o')
plt.plot(X3, Y3, color='r',  linewidth=1,  linestyle='-', label='Без учёта замыкающего пути - %s'%str(round(Z,3)))
plt.legend(loc='best')
plt.grid(True)
plt.show ()        





      


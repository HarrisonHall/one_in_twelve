# How many people really live near a volcano?
# Harrison Hall

from modules.City import City
from modules.Volcano import Volcano
import csv
from math import radians, sin, cos, acos

cfile = "worldcities.csv"
vfile = "volcano.csv"

tot_pop = 0
tot_cities = 0
pop_cities = 0
total_cities = []

miles_btwn = lambda vol, cit: 3958.94 * acos(sin(vol.latitude)*sin(cit.latitude) 
                            + cos(vol.latitude)*cos(cit.latitude)*cos(vol.longitude - cit.longitude))

with open(cfile,"r") as f:
    csvfile = csv.reader(f,delimiter=",")
    for index,row in enumerate(csvfile):
        if index == 0:
            continue
        tot_cities += 1
        pop = row[9]
        if pop is not "":
            pop_cities += 1
            tot_pop += int(float(pop))
            total_cities.append(City(row))

total_volcanoes = []
tot_volcanoes = 0
            
with open(vfile,'r') as f:
    f = csv.reader(f,delimiter=" ")
    for index,row in enumerate(f):
        if index == 0:
            continue
        tot_volcanoes += 1
        total_volcanoes.append(Volcano(row))
        if total_volcanoes[-1].name == None:
            tot_volcanoes -= 1
            total_volcanoes = total_volcanoes[:-1]
        

print("Total Cities",tot_cities)
print("Population Cities",pop_cities)
print("Total Population",tot_pop)
print("Total Volcanoes",tot_volcanoes)

pop_near = 0
cit_near = 0
for c in total_cities:
    for v in total_volcanoes:
        if (miles_btwn(c,v) <= 50):
            print(c.name,"is near",v.name)
            pop_near += c.population
            cit_near += 1

print(cit_near,"cities are near a volcano")
print(pop_near/tot_pop*100,"% of people live near an active or potentially active volcano")

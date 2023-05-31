import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import cycler

def setup():
    #opens stylesheet and changes style parameters
    stylesheet = open("stylesheet.txt").read().replace(" ", "").split("\n")
    stylesheet = stylesheet[:len(stylesheet)-1]
    for i in stylesheet:
        s = i.split(":")
        mpl.rcParams[s[0]] = s[1]
    mpl.rcParams['figure.figsize'] = [10, 6]
    
    return

def sheepgraph(x):
    file = open(x)
    text = file.read()
    text = text.replace('"', '')
    text = text.replace('\n',',')
    text = text.split(',')
    print(text)
    count = 1
    year = 0
    yearlist= list()
    valuelist = list()
    dictionary = dict()
    for i in text:
        if count == 1:
            number = []
            full = "" #setup to remove commas
            count += 1
            if not i == '' and int(i) not in yearlist:
                year = float(i)
            if not i == '' and int(i) in yearlist:
                year = float(i)+0.5
                #because there are 2 versions of each year, one for jan and one for july
            if not i == '':
                yearlist.append(float(year))
        elif count == 2:
            if not i == '':
                valuelist.append(float(i))
                dictionary[year] = i
                count = 1
    #because the years should increment up down 1 year, up half a year, then down one and a half years,
    #a new dictionary must therefore be created with sorted values
    yearlist.sort()
    newvalues = []
    newdict = {}
    for year in yearlist:
        newvalues.append(float(dictionary[year]))
        print(newvalues)
    for x in range(len(yearlist)):
        newdict[yearlist[x]] = newvalues[x]    
    print(newdict)
    print(yearlist)
    print(newvalues)
    plt.plot(yearlist,newvalues)

def goatsgraph(x):
    file = open(x)
    text = file.read()
    text = text.replace('"', '')
    text = text.replace('\n',',')
    text = text.split(',')
    print(text)
    # splits population numbers with commas too
    count = 1
    year = 0
    yearlist= list()
    valuelist = list()
    dictionary = dict()
    for i in text:
        if count == 1:
            count = 2
            if not i == '':
                year = float(i)
                yearlist.append(float(year))
        elif count == 2:
            if not i == '':
                valuelist.append(float(i))
                dictionary[year] = float(i)
                count = 1 
    print(dictionary)
    print(yearlist)
    print(valuelist)
    plt.plot(yearlist,valuelist)

#hogsgraph is the same program as goatsgraph, just labeled differently for clarity
def hogsgraph(x):
    file = open(x)
    text = file.read()
    text = text.replace('"', '')
    text = text.replace('\n',',')
    text = text.split(',')
    print(text)
    # splits population numbers with commas too
    count = 1
    year = 0
    yearlist= list()
    valuelist = list()
    dictionary = dict()
    for i in text:
        if count == 1:
            count = 2
            if not i == '':
                year = float(i)
                yearlist.append(float(year))
        elif count == 2:
            if not i == '':
                valuelist.append(float(i))
                dictionary[year] = float(i)
                count = 1 
    print(dictionary)
    print(yearlist)
    print(valuelist)
    plt.plot(yearlist,valuelist)

goatsgraph("data/goats/Total_Goats_National.csv")
sheepgraph("data/sheep/Total_Sheep_National.csv")
hogsgraph("data/hogs/Total_Hogs_National.csv")

plt.ylim([0, 80000000])
plt.show()

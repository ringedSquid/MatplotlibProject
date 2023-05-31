import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import cycler
datapath = "data/cows/"
storepath = "graphs/cows/"

def setup():
    #opens stylesheet and changes style parameters
    stylesheet = open("stylesheet.txt").read().replace(" ", "").split("\n")
    stylesheet = stylesheet[:len(stylesheet)-1]
    for i in stylesheet:
        s = i.split(":")
        mpl.rcParams[s[0]] = s[1]
    mpl.rcParams['figure.figsize'] = [10, 6]
    
    return
def open_file(fp):
    #opening file, removing blank space at end and headers
    f = open(fp, "r")
    f = f.read().split("\n")
    f = f[1:len(f)-1]
    #removing all JULY entries
    f1 = [] 
    for i in range(len(f)):
        if f[i][15:18] != 'JUL':
            f1.append(f[i])
    #placing values into dictionary. {year : amnt of cows}
    f = ','.join(f1).split(",")
    d = {}
    for i in range(0, len(f), 3):
        d[f[i]] = int(f[i+2])
    return d
        
def create_graph(fp, t, c):
    plt.clf()
    d = open_file(datapath + fp)
    x = [int(i) for i in d.keys()] 
    y = list(d.values())
    plt.title(t)
    plt.xlabel("Year")
    plt.ylabel("Cows")
    plt.plot(x, y, color=c)
    plt.savefig(storepath + fp[:len(fp)-1] + ".png")
    return


def main():
    setup()
    datafiles = {
            "Total Beef Cattle" : ["TotalBeef_Cattle_National.csv", 'r'],
            "Total Cattle & Calves" : ["Total_CattleCalves_National.csv", 'b'],
            "Total Milk Cattle" : ["TotalMilk_Cattle_National.csv", 'g']
        }
    for k in datafiles.keys():
        create_graph(datafiles[k][0], k, datafiles[k][1])
    return
main()

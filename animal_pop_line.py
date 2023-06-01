import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import cycler
datapath = "data/"
storepath = "graphs/"

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
    f = ','.join(f).split(",")
    d = {}
    for i in range(0, len(f), 2):
        d[f[i]] = int(f[i+1])
    return d
        
def create_graph(fp, t, c):
    plt.clf()
    d = open_file(datapath + fp)
    x = [int(i) for i in d.keys()] 
    y = list(d.values())
    plt.title(t)
    plt.xlabel("Year")
    plt.ylabel("Amount")
    plt.plot(x, y, color=c)
    plt.savefig(storepath + fp[:len(fp)-1] + ".png")
    return

def create_big_graph(bd, t, fn):
    plt.clf()
    plt.title(t)
    plt.xlabel("Year")
    plt.ylabel("Amount")
    for k in bd.keys():
        d = open_file(datapath + bd[k][0])
        x = [int(i) for i in d.keys()]
        y = list(d.values())
        plt.plot(x, y, label=k, color=bd[k][1])

    plt.legend()
    plt.savefig(storepath + fn + ".png")


def main():
    setup()
    datafiles = {
            "Total Goats" : ["goats/Total_Goats_National.csv", 'orange'],
            "Total Hogs" : ["hogs/Total_Hogs_National.csv", 'purple'],
            "Total Sheep" : ["sheep/Total_Sheep_National.csv", 'brown'],
            "Total Beef Cattle" : ["cows/TotalBeef_Cattle_National.csv", 'r'],
            "Total Cattle & Calves" : ["cows/Total_CattleCalves_National.csv", 'b'],
            "Total Milk Cattle" : ["cows/TotalMilk_Cattle_National.csv", 'g'],
            "Total Chicken" : ["chicken/Total_Chicken_National.csv", 'cyan'],
            "Total Bison" : ["bison/Total_Bison_National.csv", "magenta"],
            "Total Horses" : ["horses/Total_Horses_National.csv", "black"]
        }
    for k in datafiles.keys():
        create_graph(datafiles[k][0], k, datafiles[k][1])

    biggraph_data = {
            "Goats" : ["goats/Total_Goats_National.csv", 'orange'],
            "Hogs" : ["hogs/Total_Hogs_National.csv", 'blue'],
            "Sheep" : ["sheep/Total_Sheep_National.csv", 'green'],
            "Cows" : ["cows/Total_CattleCalves_National.csv", 'red'],
            "Chicken": ["chicken/Total_Chicken_National.csv", 'purple'],
            "Bison" : ["bison/Total_Bison_National.csv", "magenta"],
            "Horses" : ["horses/Total_Horses_National.csv", "black"]
        }
    create_big_graph(biggraph_data, "All Animals", "All_Animals") 
    return

main()

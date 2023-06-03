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

def open_file(fp):
    #opening file, removing blank space at end and headers
    f = open(fp, "r")
    f = f.read().split("\n")
    f = f[:len(f)-1]
    f = ','.join(f).split(",")
    d = {}
    for i in range(0, len(f), 2):
        d[f[i]] = int(f[i+1])
    return d
        
def create_graph(fp, r1, r2, l):
    d = open_file(fp)
    x = [int(i) for i in d.keys()]
    interval = (x.index(int(r2)), x.index(int(r1))+1)
    y = list(d.values())
    plt.plot(x[interval[0]:interval[1]], y[interval[0]:interval[1]], label=l)
    plt.legend()
    return


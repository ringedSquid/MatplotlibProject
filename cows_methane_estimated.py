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

def animal_to_methane(d, ae):
    ch4_pwd = 28.5


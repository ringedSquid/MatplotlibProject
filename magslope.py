import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import cycler

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

def magnitude_of_change(datafiles, datapath):
    magnitudes = {}
    #traditional magnitude of change takes the (biggest value - smallest value) / smallest value
    #in this EXPERIMENTAL variation of magnitude of change, we take the total rate of change / beginning value,
    #so that the number of years are taken into account
    #Do you think that this measure of change is reliable?
    for key in datafiles.keys():
        d = open_file(datapath + datafiles[key])
        years = list(d.keys())
        yearend = int(years[0])
        yearbeg = int(years[len(d)-1])
        yeardiff = yearend - yearbeg
        populationdiff = int(d[str(yearend)]) - int(d[str(yearbeg)])
        rate = populationdiff / yeardiff
        magnitude = rate / int(d[str(yearbeg)])
        magnitudes[key] = magnitude
    return magnitudes

def magnitude_graph(datafiles, datapath):
    #setup()
    #plt.clf()
    magnitudes = magnitude_of_change(datafiles, datapath) #to fill magnitudes{} with values
    pos = {}
    neg = {}
    for key in list(magnitudes.keys()):
        if float(magnitudes[key]) > 0:
            pos[key] = float(magnitudes[key])
        else:
            neg[key] = abs(float(magnitudes[key]))
    x1 = list(pos.keys())
    y1 = list(pos.values())
    x2 = list(neg.keys())
    y2 = list(neg.values())
    print(x1)
    print(y1)
    print(x2)
    print(y2)
    plt.bar(x1, y1, label = "Positive Magnitudes of Change")
    plt.bar(x2, y2, label = "Negative Magnitudes of Change")
    plt.ylim((0, 0.05))
    plt.title("Magnitude of Change for Livestock\nFound by doing Overall Average Rate of Change / Beginning Value")
    plt.legend()
    plt.xlabel("Animals")
    plt.ylabel("Magnitude")
    


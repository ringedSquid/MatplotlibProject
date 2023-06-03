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

def magnitude_of_change(d):
    #traditional magnitude of change takes the (biggest value - smallest value) / smallest value
    #in this EXPERIMENTAL variation of magnitude of change, we take the total rate of change / beginning value,
    #so that the number of years are taken into account
    #Do you think that this measure of change is reliable?
    datafiles = {
            "Goats" : ["goats/Total_Goats_National.csv", 'orange'],
            "Hogs" : ["hogs/Total_Hogs_National.csv", 'purple'],
            "Sheep" : ["sheep/Total_Sheep_National.csv", 'brown'],
            "Cattle" : ["cows/Total_Cattle_National.csv", 'b'],
            "Bison" : ["bison/Total_Bison_National.csv", "magenta"],
            "Horses" : ["horses/Total_Horses_National.csv", "black"]
        }
    for key in datafiles.keys():
        d = open_file(MOCdatapath + datafiles[key][0])
        years = list(d.keys())
        yearend = int(years[0])
        yearbeg = int(years[len(d)-1])
        yeardiff = yearend - yearbeg
        populationdiff = int(d[str(yearend)]) - int(d[str(yearbeg)])
        rate = populationdiff / yeardiff
        magnitude = rate / int(d[str(yearbeg)])
        magnitudes[key] = magnitude

def magnitude_graph():
    #setup()
    #plt.clf()
    magnitude_of_change() #to fill magnitudes{} with valuesdef open_file(fp):
    #opening file, removing blank space at end and headers
    f = open(fp, "r")
    f = f.read().split("\n")
    f = f[1:len(f)-1]
    f = ','.join(f).split(",")
    d = {}
    for i in range(0, len(f), 2):
        d[f[i]] = int(f[i+1])
    return d

    pos = {}
    neg = {}
    for key in list(magnitudes.keys()):
        if float(magnitudes[key]) > 0:
            pos[key] = float(magnitudes[key]

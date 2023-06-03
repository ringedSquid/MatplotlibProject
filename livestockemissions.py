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
    return
setup()
def make_meanlists():
    from matplotlib import pyplot as plt
    from matplotlib import style
    file = open('All livestock emissions - Sheet1.csv')
    text = file.read()
    text = text.replace('\n',',')
    text = text.split(',')
    totallist = list()
def get_mean(first):
    skip = first
    count = 0
    meanlist = list()
    for i in text:
        if skip > 0:
            skip = skip - 1
        elif count < 7:
            meanlist.append(float(i))
            count = count + 1
        mean = sum(meanlist)/len(meanlist)
        totallist.append(mean)
    print(mean)
def all_means():
    get_mean(0)
    get_mean(7)
    get_mean(14)
    get_mean(21)
    get_mean(28)
    get_mean(35)
    get_mean(42)
    get_mean(48)
    print(totallist)
def make_livestock_emissions_graph():
    thelabels = ["Beef Cows", "Dairy Cows", "Swine", "Horses", "Sheep", "Goats", "American Bison", "Mules and Asses"]
    theexplode = [0,0,0,0,0,0.1,0.3,0.5]
    thecolors = ["saddlebrown", "lawngreen", "pink", "powderblue", "silver", "peru", "sienna", "darkred"]
    plt.pie(totallist, labels = thelabels, explode = theexplode, colors = thecolors, autopct='%.1f%%')
    plt.title("Methane emissions of all livestock in kiltons")
    plt.show()

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
def make_cow_emissions_lists():
    from matplotlib import pyplot as plt
    from matplotlib import style
    file = open('Cow methane emissions data - Sheet1 (1).csv')
    text = file.read()
    text = text.replace('\n',',')
    text = text.split(',')
    count = 1
    year = 0
    cow = 0
    beefyearlist= list()
    beefvaluelist = list()
    dairyyearlist= list()
    dairyvaluelist = list()
    beefdictionary = dict()
    dairydictionary = dict()
    for i in text:
        if count == 1:
            count = 2
            cow = i
        elif count  == 2:
            count = 3
            if not i == '':
                if cow == "beef":
                    beefyearlist.append(float(i))
                elif cow == "dairy":
                    dairyyearlist.append(float(i))
        elif count == 3:
            count = 1
            if cow == "beef":
                beefvaluelist.append(float(i))
                beefdictionary[year] = i
            elif cow == "dairy":
                dairyvaluelist.append(float(i))
                dairydictionary[year] = i
def get_means(list1,list2):
    beefmean = sum(list1)/len(list1)
    dairymean = sum(list2)/len(list2)
    print (beefmean)
    print (dairymean)
get_means(beefvaluelist,dairyvaluelist)
def make_cow_emissions_graph():        
    plt.plot(beefyearlist,beefvaluelist,linewidth = 1,color = 'saddlebrown')
    plt.plot(dairyyearlist,dairyvaluelist,linewidth = 1,color = 'lawngreen')
    plt.title('Beef and Dairy Cow Emissions in the US')
    plt.xlabel('Years')
    plt.ylabel('Methane\'s Carbon Dioxide Equivalent in kilotons')
    plt.show()
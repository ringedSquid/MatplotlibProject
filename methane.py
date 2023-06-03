import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import cycler

def make_meanlists(fp, datapath):
    file = open(datapath + fp)
    emissionstext = file.read()
    emissionstext = emissionstext.replace('\n',',')
    emissionstext = emissionstext.split(',')
    totallist = list()
    meanlist = list()
    mean = 0
    count = 0
    for i in emissionstext:
        if count < 7:
            count = count + 1
            meanlist.append(float(i))
            return (i)
        elif count == 7:
            mean = sum(meanlist)/len(meanlist)
            meanlist = list()
            count = 1
            totallist.append(mean)
            return (mean)

def compare_cows():
    plt.clf()
    numlist = np.array([4964.285714285715,1672.5714285714287])
    thelabels = ["Beef Cows", "Dairy Cows"]
    theexplode = [0, 0.2]
    thecolors = ["saddlebrown", "lawngreen"]
    plt.pie(numlist,labels = thelabels, explode = theexplode, colors = thecolors,autopct='%.1f%%')
    plt.title('Comprassion of Beef and Dairy Cow Emissions')


def cow_methane(fp, datapath):
    plt.clf()
    text = open(datapath + fp).read().replace('\n', ',')
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

    plt.plot(beefyearlist,beefvaluelist,linewidth = 1,color = 'saddlebrown')
    plt.plot(dairyyearlist,dairyvaluelist,linewidth = 1,color = 'lawngreen')
    plt.title('Beef and Dairy Cow Emissions in the US')
    plt.xlabel('Years')
    plt.ylabel('Methane\'s Carbon Dioxide Equivalent in kilotons')

    print(totallist)
def make_livestock_emissions_graph():
    thelabels = ["Beef Cows", "Dairy Cows", "Swine", "Horses", "Sheep", "Goats", "American Bison", "Mules and Asses"]
    theexplode = [0,0,0,0,0,0.1,0.3,0.5]
    thecolors = ["saddlebrown", "lawngreen", "pink", "powderblue", "silver", "peru", "sienna", "darkred"]
    plt.pie(totallist, labels = thelabels, explode = theexplode, colors = thecolors, autopct='%.1f%%')
    plt.title("Methane emissions of all livestock in kiltons")
    plt.show()

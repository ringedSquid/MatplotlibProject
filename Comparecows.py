from matplotlib import pyplot as plt
import numpy as np
from matplotlib import style
def make_compare_cows_graph():
    numlist = np.array([4964.285714285715,1672.5714285714287])
    thelabels = ["Beef Cows", "Dairy Cows"]
    theexplode = [0, 0.2]
    thecolors = ["saddlebrown", "lawngreen"]
    plt.pie(numlist,labels = thelabels, explode = theexplode, colors = thecolors,autopct='%.1f%%')
    plt.title('Comprassion of Beef and Dairy Cow Emissions')
    plt.show()
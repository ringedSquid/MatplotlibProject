import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import cycler
from tkinter import simpledialog, messagebox
from tkinter import *
import tkinter as tk

import graph
import magslope



datapath = "data/"
#SETTING UP TK
tk = Tk()

screen = Canvas(width = 1000, height = 350, bg = "LightYellow")
screen.create_text(
        500, 
        30,
        text="Effect of Livestock (ie Cows) on Methane Emissions", 
        fill="brown", 
        font=("Arial 30")
        )

screen.create_text(
        500, 
        160, 
        text = open(datapath + "gui/intromessage.txt").read(), 
        font = ("Arial 14"), 
        fill = "black", 
        justify = CENTER
        )

screen.create_text(
        500, 
        300,
        text="Methane emissions have became a growing point of concern in the recent years. \nClick on the buttons to find out more...",
        justify = CENTER, 
        font="Arial 19", 
        fill = "orange"
        )

#cowimage = PhotoImage(file = "CowImage.png")
#cowpic = Label(tk, image = cowimage, width = 1000, height = 300)
#cowpic.pack()
screen.pack()


def setup():
    #opens stylesheet and changes style parameters
    stylesheet = open("stylesheet.txt").read().replace(" ", "").split("\n")
    stylesheet = stylesheet[:len(stylesheet)-1]
    for i in stylesheet:
        s = i.split(":")
        mpl.rcParams[s[0]] = s[1]
    mpl.rcParams['figure.figsize'] = [10, 6]
    return

def choose_files(d):
    selected_data = {}
    while True:
        key = simpledialog.askstring("Dataset", "Pick from: " + ", ".join(list(d.keys())))
        if key not in d:
            messagebox.showinfo("Error!", "dataset entered does not exist!")
            continue
        
        subd = graph.open_file(datapath + d[key])
        range = simpledialog.askstring("Range", 
                                       "(Seperate with a ,) Pick intervals from: " + 
                                       ", ".join(reversed(list(subd.keys()))))
        range = range.split(",")
        print(subd)
        print(range)
        if (range[0] not in subd) or (range[1] not in subd):
            messagebox.showinfo("Error!", "invalid range or invalid format inputted!")
            continue
        selected_data[key] = [d[key], range[0], range[1], key]
        endmsg = simpledialog.askstring("End?", "End of data entry? y/n")
        if endmsg == 'y':
            break
    
    print(selected_data)
    return selected_data

def graphset(d):
    plt.clf()
    plt.xlabel("Year")
    plt.ylabel("Amount")
    title = ""
    for k in d.keys():
        title += (d[k][3] + " ")
        graph.create_graph(datapath + d[k][0], d[k][1], d[k][2], d[k][3])
    plt.title(title)
    plt.show()
    return

def graphmagnitude(d):
    plt.clf()
    magslope.magnitude_graph(d, datapath)
    plt.show()


    
 
        
        
#btn1 = Button(text = "Rate of Change of Other Livestock", command = roc_livestock)
#btn2 = Button(text = "Rate of Change for Cows", command = roc_cows)
#btn3 = Button(text = "Experimental Magnitude of Change Graph", command = magnitude_graph)


#btn4 = Button(text = "Show Average Difference Between Dairy and Cow Populations", command = main_beef_vs_milk)

#btn1.pack()
#btn2.pack()
#jbtn3.pack()

#btn4.pack()

if __name__ == "__main__":
    datafiles = {
            "goats" : "goats/Total_Goats_National.csv",
            "hogs" : "hogs/Total_Hogs_National.csv", 
            "sheep" : "sheep/Total_Sheep_National.csv",
            "beefCattle" : "cows/TotalBeef_Cattle_National.csv",
            "cattle" : "cows/Total_Cattle_National.csv", 
            "milkCattle" : "cows/TotalMilk_Cattle_National.csv",
            "chicken" : "chicken/Total_Chicken_National.csv",
            "bison" : "bison/Total_Bison_National.csv", 
            "horses" : "horses/Total_Horses_National.csv"
        }
    setup()
    btn1 = Button(text = "Graph Livestock Population", command= lambda: graphset(choose_files(datafiles)))
    btn1.pack()
    #btn2 = Button(text = "Graph Magnitudes of Change", command= lambda: graphmagnitude(datafiles))
    #btn2.pack()

    mainloop()

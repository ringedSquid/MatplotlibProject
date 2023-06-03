def main():
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    from cycler import cycler
        from matplotlib import pyplot as plt
        from matplotlib import style
        file = open('USlivestockmethanedata.csv')
        text = file.read()
        text = text.replace('\n',',')
        text = text.split(',')
        count = 1
        year = 0
        yearlist= list()
        valuelist = list()
        dictionary = dict()
        for i in text:
            if count == 1:
                count = 2
                year = i
                if not i == '':
                    yearlist.append(float(i))
            elif count == 2:
                count = 1
                valuelist.append(float(i))
                dictionary[year] = i
    def rate_of_change(numlist):
        count = 33
        lastvalue = 0
        change = 0
        changelist = list()
        predictlist = list()
        for i in numlist:
            if count == 33:
                count = count - 1
                lastvalue = i
            elif count > 0:
                count = count - 1
                change = i - lastvalue
                lastvalue = i
                changelist.append(change)
            else:
                change = i - lastvalue
                lastvalue = i
                predictlist.append(change)
        changemean = sum(changelist)/len(changelist)
        predictmean = sum(predictlist)/len(predictlist)
        print(changemean)
        print(predictmean)
        
    rate_of_change(valuelist)
    def make_US_emissions_graph():
        plt.plot(yearlist,valuelist,linewidth = 1,color = 'navy')
        plt.title('US methane levels 1990 - 2050')
        plt.xlabel('Years')
        plt.ylabel('Methane\'s Carbon Dioxide Equivalent in millions of metric tons')
    make_US_emissions_graph()

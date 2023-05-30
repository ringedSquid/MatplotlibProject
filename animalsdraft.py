from matplotlib import pyplot as plt

def animalgraph():
    file = open('Cow_beef_pop.csv')
    text = file.read()
    text = text.replace('"', '')
    text = text.replace('\n',',')
    text = text.split(',')
    # splits population numbers with commas too
    count = 1
    year = 0
    yearlist= list()
    valuelist = list()
    dictionary = dict()
    for i in text:
        if count == 1:
            number = []
            full = "" #setup to remove commas
            count += 1
            if not i == '' and int(i) not in yearlist:
                year = float(i)
            if not i == '' and int(i) in yearlist:
                year = float(i)+0.5
                #because there are 2 versions of each year, one for jan and one for july
            if not i == '':
                yearlist.append(float(year))
        elif count == 2 or count == 3 or count == 4:
            if not i == '' and len(number) != 3:
                number.append(str(i))
            if not i == '' and len(number) == 3:
                #elif does not work because when number length equaled 3 it would reset before appending full
                full = number[0] + number[1] + number[2]
                #full is the population number without any commas, only works when population is in the millions
                valuelist.append(int(full))
                dictionary[year] = full
            if not count == 4:
                count += 1
            else:
                count = 1 # to reset count for year
    #because the years should increment up down 1 year, up half a year, then down one and a half years,
    #a new dictionary must therefore be created with sorted values
    yearlist.sort()
    newvalues = []
    newdict = {}
    for year in yearlist:
        newvalues.append(int(dictionary[year]))
        print(newvalues)
    for x in range(len(yearlist)):
        newdict[yearlist[x]] = newvalues[x]    
    print(newdict)
    print(yearlist)
    print(newvalues)
    plt.plot(yearlist,newvalues)
    plt.show()
animalgraph()

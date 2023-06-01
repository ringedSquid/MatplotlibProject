datapath = "data/cows/"

def open_file(fp):
    #opening file, removing blank space at end and headers
    f = open(fp, "r")
    f = f.read().split("\n")
    f = f[1:len(f)-1]
    f = ','.join(f).split(",")
    d = {}
    for i in range(0, len(f), 2):
        d[f[i]] = int(f[i+1])
    return d

def avg_diff(d1, d2):
    return abs(sum(d1.values())-sum(d2.values()))/len(d1)

def main():
    beef = open_file(datapath + "TotalBeef_Cattle_National.csv")
    milk = open_file(datapath + "TotalMilk_Cattle_National.csv")
    print(avg_diff(beef, milk))

main()

def open_file(fp):
    file = open(fp)
    file = file.read().replace("\n", ",").split(",")
    file = file[3:len(file)-1]
    
    for i in range(0, len(file), 6):
        pass
    return file

test = open("data/cows/TotalBeef_Cattle_National.csv", "r")
test = test.read().replace("\n", ",").split(",")
print(test)


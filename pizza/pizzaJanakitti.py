def getData(file):
    with open(file, "r") as dataset:
        l = dataset.read().strip("null").strip("'").split()
    dataset = []
    for item in l:
        dataset.append(item)
    R = dataset[0]
    C = dataset[1]
    L = dataset[2]
    H = dataset[3]
    pizzaArray = []

    for i in range (4, len(dataset)):
        pizzaArray.append(list(dataset[i]))
    return(R, C, L, H, pizzaArray)

pizza = getData("d_small.txt")[4:][0]
height = int(getData("d_small.txt")[0])
width = int(getData("d_small.txt")[1])
minTopp = getData("d_small.txt")[2]
maxSize = getData("d_small.txt")[3]

def totalSliceTypes(maxSize): # Returns all legal slice dimensions
    sliceSet = []
    for area in range (1, maxSize+1):
        factorSet = []
        for i in range(1, area + 1):
            if area % i == 0:
                factorSet.append(i)
        sliceGroup = []
        for factor in factorSet:
            sliceGroup.append([factor, int(area/factor)])
        for member in sliceGroup:
            sliceSet.append(member)
    return(sliceSet)

def maxedSliceTypes(maxSize): # Returns all slice dimensions of the maximum area
    factorSet = []
    for i in range(1, maxSize + 1):
        if maxSize % i == 0:
            factorSet.append(i)
    sliceGroup = []
    for factor in factorSet:
        sliceGroup.append([factor, int(maxSize/factor)])
    return(sliceGroup)


totalSliceTypes(4)

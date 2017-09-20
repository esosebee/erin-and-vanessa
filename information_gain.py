import numpy as np 
import math 

def findValuesOfAttribute(listofdictionaries, attribute):
    basket = set()
    print('attribute is ', attribute)
    for item in listofdictionaries:
        print(item[attribute])
        basket.add(item[attribute])
    return basket

def finduniquevals(listofdictionaries, attribute):
    allvals = []
    for item in listofdictionaries:
        if attribute in item:
            allvals.append(item[attribute])
        else:
            print("attribute", attribute, "not found in data item")

    basket = set()
    for item in allvals:
        basket.add(item)

    return(basket)

def entropy(listofdictionaries, attribute):
    allvals = []
    for item in listofdictionaries:
        allvals.append(item[attribute])

    basket = set()
    for item in allvals:
        basket.add(item)

    counts = []
    for item in basket:
        counts.append(allvals.count(item))

    n = sum(counts)
    print("n is ", n)
    probs = []
    for count in counts:
        probs.append(count/n)
        print("probability: ", count/n)

    e = 0
    for prob in probs:
        print("Probability and log", prob, math.log(prob, 2))
        e = e + prob*math.log(prob, 2)
    e = -1*e 
    return e

    def sliceOfData(listofdictionaries, attribute, value):
        datalist = []
        for item in listofdictionaries:
            if item[attribute] == valu:
                datalist.append(item)
        return datalist


    def gain(listofdictionaries, feature):
        e = entropy(listofdictionaries, 'boundary')
        values = finduniquevalues(listofdictionaries, feature)

        gain = 0
        for v in valus:
            sv = sliceOfData(listofdictionaries, feature, v)
            gain =gain + size(sv) * entropy(sv, 'boundary')

        gain = e - (1/size(listofdictionaries) * gain)
        return gain
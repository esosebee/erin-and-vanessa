import numpy as np 
import math 

def find_values_of_attribute(listofdictionaries, attribute):
    # Throw all values of the given attribute in basket
    basket = set()
    print('attribute is ', attribute)
    for item in listofdictionaries:
        # print(item[attribute])
        if type(item[attribute]) is dict:
            for key in item[attribute].keys():
                basket.add(item[attribute][key])
        else: 
            basket.add(item[attribute])
    return basket

def find_unique_vals(listofdictionaries, attribute):
    allvals = []
    for item in listofdictionaries:
        if attribute in item: 
            # Attributes with dictionaries as values need to be parsed
            # in this way
            if type(item[attribute]) is dict:
                for key in item[attribute].keys():
                    allvals.append(key)
            else: 
                allvals.append(item[attribute])
        else:
            print("attribute", attribute, "not found in data item")

    # Find all unique value in allvals and throw them in basket. 
    basket = set()
    for item in allvals:
        basket.add(item)
    return basket

def entropy(listofdictionaries, attribute):
    allvals = []
    for item in listofdictionaries:
        allvals.append(item[attribute])

    # Find all unique value in allvals and throw them in basket. 
    basket = set()
    for item in allvals:
        basket.add(item)

    # Now compute the probability of each item in basket.
    counts = []
    for item in basket:
        counts.append(allvals.count(item))

    n = sum(counts)
    print("n is ", n)
    probs = []
    for count in counts:
        probs.append(count/n)
        print("probability: ", count/n)

    # Using the probabilities, compute the entropy e.
    e = 0
    for prob in probs:
        print("Probability and log", prob, math.log(prob, 2))
        e = e + prob*math.log(prob, 2)
    e = -1*e 
    return e

    def sliceOfData(listofdictionaries, attribute, value):
        ''' Construct a list of all dictionaries from listofdictionaries for which
        attribute has the specified value. '''
        datalist = []
        for item in listofdictionaries:
            if item[attribute] == value:
                datalist.append(item)
        return datalist


    def gain(listofdictionaries, feature):
        # Compute the entropy of the entire data set using the values of the
        # target function, a.k.a. boundry. 
        e = entropy(listofdictionaries, 'boundary')
        # Find all values of the feature "feature".
        values = finduniquevalues(listofdictionaries, feature)

        gain = 0
        for v in valus:
            sv = sliceOfData(listofdictionaries, feature, v)
            gain =gain + size(sv) * entropy(sv, 'boundary')

        gain = e - (1/size(listofdictionaries) * gain)
        return gain

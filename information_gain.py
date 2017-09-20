import numpy as np 
import math 

def find_values_of_attribute(training_set, key):
    # Throw all values of the given attribute in basket
    basket = set()
    print('attribute is ', attribute)
    for item in training_set:
        if type(item[attribute]) is dict:
            for k in item[key].keys():
                basket.add(item[key][k])
        else: 
            basket.add(item[key])
    return basket

def find_unique_vals(training_set, key):
    allvals = []
    for item in training_set:
        if key in item: 
            # Attributes with dictionaries as values need to be parsed
            # in this way
            if type(item[key]) is dict:
                for k in item[key].keys():
                    allvals.append(k)
            else: 
                allvals.append(item[attribute])
        else:
            print("attribute", attribute, "not found in data item")

    # Find all unique value in allvals and throw them in basket. 
    basket = set()
    for item in allvals:
        basket.add(item)
    return basket

def entropy(training_set, key):
    allvals = []
    for item in training_set:
        allvals.append(item[key])

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

    def sliceOfData(training_set, key, value):
        ''' Construct a list of all dictionaries from listofdictionaries for which
        attribute has the specified value. '''
        datalist = []
        for item in listofdictionaries:
            if item[key] == value:
                datalist.append(item)
        return datalist


    def gain(training_set, feature):
        # Compute the entropy of the entire data set using the values of the
        # target function, a.k.a. boundry. 
        e = entropy(training_set, 'boundary')
        # Find all values of the feature "feature".
        values = find_unique_vals(training_set, feature)

        gain = 0
        for v in valus:
            sv = sliceOfData(training_set, feature, v)
            gain =gain + size(sv) * entropy(sv, 'boundary')

        gain = e - (1/size(training_set) * gain)
        return gain

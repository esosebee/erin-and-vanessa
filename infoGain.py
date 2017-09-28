import numpy as np
import math 

''' Given a list of dictionaries and an attribute, return the set of all values that
attritute takes on somewhere, in some dictionarie. '''

''' Maybe give a for instance?  '''

def findValuesOfAttribute(listofdictionaries, attribute):

    basket = set()  # Going to throw all the values of the given attribute in basket.
    print('attribute is ', attribute)
    for item in listofdictionaries:
        print (item[attribute])
        basket.add(item[attribute])

    return basket



''' Find all unique values in attribute in listofdictionaries.  Returns the
set of values. '''

def finduniquevals(listofdictionaries, attribute):

    allvals = []
    for item in listofdictionaries:
        if attribute in item: 
            allvals.append(item[attribute])
        else:
            print ("attribute", attribute, "not found in data item")

    # Find all unique value in allvals and throw them in basket. 
    basket = set()
    for item in allvals:
        basket.add(item)

    return(basket)


''' Compute the experimental probability of values of the given attribute.'''
''' Returns: A list of all the probabilities of values of the attribute.'''

def compute_probabilities(listofdictionaries, attribute):

    ''' Create a list allvals of all instances of attribute.  For instance, if
    IE occurs 50 times in our data set, the value 'IE' will appear 50 times
    in the list allvals.'''

    allvals = []
    for item in listofdictionaries:
        allvals.append(item[attribute])

    '''Find all unique value in allvals and throw them in basket. '''
    basket = set()
    for item in allvals:
        basket.add(item) 

    
    # Now compute the probability of each item in basket.

    counts = []
    for item in basket:
        counts.append(allvals.count(item))

    n = sum(counts)
    print(" n is ", n)
    probs = []
    for count in counts:
        probs.append(count/n)
        print( "probability:", count/n)

    return probs


'''
def gini_impurity(listofdictionaires, attribute):

    probs = compute_probabilities(listofdictionaries, attribute)
    gini = 0
    for p in probs:
        gini = gini + p*p
    gini = 1 - gini
    return gini
    
'''


''' Given a list of dictionaries and an attribute to compute the entropy
with respect to, compute the experimental probabilities of each value of the
attribute and then compute the entropy based on this. 

Think of the list of dictionaries as an enhanced set of data elements.   Each
element (dictionary) is one record of the data set.

Returns: entropy.   
'''

def entropy(listofdictionaries, attribute):

    ''' Create a list allvals of all instances of attribute.  For instance, if
    IE occurs 50 times in our data set, the value 'IE' will appear 50 times
    in the list allvals.'''


    # Find the experimental probability of each value of the given attribute in
    # the data set listofdictionaires. Using the probabilities, compute the entropy e.

    probs = compute_probabilities(listofdictionaries, attribute)
    e = 0
    for prob in probs:
        print ("Probability and log", prob, math.log(prob,2))
        e = e + prob * math.log(prob,2)

    e = -1*e

    return e


def sliceOfData(listofdictionaries, attribute, value):

    ''' Construct a list of all dictionaries from listofdictionaries for which
    attribute has the specified value. '''

    datalist = []
    for item in listofdictionaries:
        if item[attribute] == value :
            datalist.append(item)

    return datalist

    

def gain(listofdictionaries, feature):

    # Compute the entropy of the entire data set using the values of the
    # target function, a.k.a. boundry. 
    e = entropy(listofdictionaries, 'boundary')

    # Find all values of the feature "feature".

    values = finduniquevals(listofdictionaries, feature);

    gain = 0
    for v in values:
        sv = sliceOfData(listofdictionaries, feature, v)
        gain = gain + len(sv) * entropy(sv, 'boundary')

    gain = e - (1/len(listofdictionaries) * gain)

    return gain

''' Given a data set listofdictionaries and a set of features, step through
the features to find the best information gain spliting on that feature.
Return the feature and the infromation gain.'''

'''def find_best_gain(listofdictionaries, features):

    max_gain = 0
    max_feature = NULL
    for f in features:
        for value in finduniquevals(listofdictionaries, f):
            # Split off data set with value value for the feature f.
            # Compute the gain for that split.
            # Check if it's bigger than the max_gain so far.

    # FINISH THIS!!!

    return'''


        
        

    



def main():
    print("Information gain of little data set")

    item1 = {'grade': 'steep', 'bumpiness':  'bumpy', 'speedlimit': 'yes', 'boundary': 'slow'}
    item2 = {'grade': 'steep', 'bumpiness':  'smooth', 'speedlimit': 'yes', 'boundary': 'slow'}
    item3 = {'grade': 'flat', 'bumpiness':  'bumpy', 'speedlimit': 'no', 'boundary': 'fast'}
    item4 = {'grade': 'steep', 'bumpiness':  'smooth', 'speedlimit': 'no', 'boundary': 'fast'}

    data_set = [item1, item2, item3, item4]

    print('entropy of data_set is', entropy(data_set, 'boundary'))
    
    gain_result = gain(data_set, 'grade')
    print (gain_result)

if __name__ == '__main__':
    main()

           

    
    
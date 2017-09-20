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


''' Given a list of dictionaries and an attribute to compute the entropy
with respect to, compute the experimental probabilities of each value of the
attribute and then compute the entropy based on this. 

Think of the list of dictionaries as an enhanced set of data elements.   Each
element (dictionary) is one record of the data set.

Returns: entropy.   
'''

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





def entropy(listofdictionaries, attribute):

    ''' Create a list allvals of all instances of attribute.  For instance, if
    IE occurs 50 times in our data set, the value 'IE' will appear 50 times
    in the list allvals.'''

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
    print(" n is ", n)
    probs = []
    for count in counts:
        probs.append(count/n)
        print( "probability:", count/n)

    # Using the probabilities, compute the entropy e.

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
    e = entropy(listofdictionaries, 'boundry')

    # Find all values of the feature "feature".

    values = finduniquevalues(listofdictionaries, feature);

    gain = 0
    for v in values:
        sv = sliceOfData(listofdictionaries, feature, v)
        gain = gain + size(sv) * entropy(sv, 'boundry')

    gain = e - (1/size(listofdictionaries) * gain)

    return gain
        
    



def main():
    print("yo, I'm main")
    
if __name__ == '__main__':
    main()

           

    
    

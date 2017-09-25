import numpy as np
import math 

DEBUG = True

def find_values_of_attribute(training_set, key):
    # Going to throw all the values of the given attribute in basket.
    basket = set()  
    for item in training_set:
        basket.add(item[key])
    return basket

def find_unique_values(training_set, key):

    allvals = []
    for item in training_set:
        if key in item: 
            allvals.append(item[key])
        # else:
        #     if DEBUG:
        #         print ("attribute", key, "not found in data item")

    # Find all unique value in allvals and throw them in basket. 
    basket = set()
    for item in allvals:
        basket.add(item)

    return list(basket)

def compute_probabilities(training_set, key):
    ''' Create a list allvals of all instances of attribute.  For instance, if
    IE occurs 50 times in our data set, the value 'IE' will appear 50 times
    in the list allvals.'''

    allvals = []
    for item in training_set:
        allvals.append(item[key])

    '''Find all unique value in allvals and throw them in basket. '''
    basket = set()
    for item in allvals:
        basket.add(item) 

    # Now compute the probability of each item in basket.
    counts = []
    for item in basket:
        counts.append(allvals.count(item))
    
    n = float(sum(counts))
    probs = []
    for count in counts:
        probs.append(count/n)

    return probs

def get_default_prediction(training_set, target_attr):
    ''' 
    Gets the value of the most common attribute in the dataset. 
    '''
    freq_dict = {}
    # Counts the number of occurrences for each value that appears in training_set
    for t in training_set:
        for key in t:
            if key == target_attr:
                val = t[key]
                if val in freq_dict:
                    freq_dict[val] += 1
                else:
                    freq_dict[val] = 1

    # Returns the attribute value that occurred the most
    return max(freq_dict, key=freq_dict.get)


def flatten_list(lists):
    ''' Flattens a multidimensonal list into a one-dimensional list. '''
    return [item for sublist in lists for item in sublist]

def remove_attribute_from_list(dataset, attribute):
    '''
    Removes the given attribute from the dataset.
    '''
    new_dataset = dataset
    for i in range(0, len(dataset)):
        for key in dataset[i]:
            if dataset[i][key] == attribute:
                d = dict(dataset[i])
                del d[key]
                new_dataset[i] = d 
    return new_dataset

'''
See this article about gini impurity
https://github.com/rasbt/python-machine-learning-book/blob/master/faq/decision-tree-binary.md
'''

'''
def gini_impurity(listofdictionaires, attribute):

    probs = compute_probabilities(training_set, attribute)
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

def entropy(training_set, key):

    ''' Create a list allvals of all instances of attribute.  For instance, if
    IE occurs 50 times in our data set, the value 'IE' will appear 50 times
    in the list allvals.'''

    # Find the experimental probability of each value of the given attribute in
    # the data set listofdictionaires. Using the probabilities, compute the entropy e.
    probs = compute_probabilities(training_set, key)
    e = 0
    for prob in probs:
        e = e + prob * math.log(prob,2)
    e = -1*e
    return e

def slice_of_data(training_set, key, value):

    ''' Construct a list of all dictionaries from training_set for which
    attribute has the specified value. '''
    datalist = []
    for item in training_set:
        if item[key] == value:
            datalist.append(item)
    return datalist

def split_dataset(training_set, value):
    '''
    Constructs a new dataset consisting only of attributes with a specific value.
    '''
    new_dataset = []
    for item in training_set:
        for key in item:
            if item[key] == value:
                new_dataset.append(item)
    return new_dataset


def gain(training_set, feature, target_feature):
    ''' Given a data set training_set and a set of features, step through
    the features to find the best information gain spliting on that feature.
    Return the feature and the information gain.'''

    # Compute the entropy of the entire data set using the values of the
    # target function, a.k.a. boundary. 
    e = entropy(training_set, target_feature)
    # Find all values of the feature "feature".
    values = find_unique_values(training_set, feature);

    gain = 0
    for v in values:
        sv = slice_of_data(training_set, feature, v)
        gain = gain + len(sv) * entropy(sv, 'boundary')

    gain = e - (1/len(training_set) * gain)
    return gain

def select_attribute(training_set, features, target_feature):
    '''
    Chooses which attribute to split on by choosing the 
    attribute with the highest information gain.
    '''

    ''' We're in trouble if the set attributes is empty.'''
    ''' SHOULD PUT IN AN ASSERT HERE'''
    max_gain = 0.0
    best_feature = ''

    for f in features:
        f_gain = gain(training_set, f, target_feature)
        if f_gain > max_gain:
            max_gain = f_gain 
            best_feature = f 
    return best_feature 

def main():
    print("Information gain of little data set")

    item1 = {'grade': 'steep', 'bumpiness':  'bumpy', 'speedlimit': 'yes', 'boundary': 'slow'}
    item2 = {'grade': 'steep', 'bumpiness':  'smooth', 'speedlimit': 'yes', 'boundary': 'slow'}
    item3 = {'grade': 'flat', 'bumpiness':  'bumpy', 'speedlimit': 'no', 'boundary': 'fast'}
    item4 = {'grade': 'steep', 'bumpiness':  'smooth', 'speedlimit': 'no', 'boundary': 'fast'}

    data_set = [item1, item2, item3, item4]

    print('entropy of data_set is', entropy(data_set, 'boundary'))
    
    gain_result = gain(data_set, 'grade', 'boundary')
    print (gain_result)
    print(select_attribute(data_set, {'grade', 'bumpy', 'speedlimit'}, 'boundary'))    

if __name__ == '__main__':
    main()

           

    
    

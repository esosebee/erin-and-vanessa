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
    '''
    Finds all the possible values an attribute can be given a key.
    '''
    allvals = []
    for item in training_set:
        if key in item: 
            allvals.append(item[key])

    # Find all unique value in allvals and throw them in basket. 
    basket = set()
    for item in allvals:
        basket.add(item)

    return list(basket)

def get_default_prediction(training_set, feature, feature_val, target_attr):
    '''
    Finds the default prediction by counting which boundary value happens most 
    frequently in the dataset given a specific feature and a specific value for 
    the feature.
    '''
    freq_dict = {}
    for item in training_set:
        if item[feature] == feature_val:
            if item[target_attr] not in freq_dict:
                freq_dict[item[target_attr]] = 1
            else:
                freq_dict[item[target_attr]] += 1
    return max(freq_dict, key=freq_dict.get)

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

def slice_of_data(training_set, key, value):

    ''' Construct a list of all dictionaries from training_set for which
    attribute has the specified value. '''
    datalist = []
    for item in training_set:
        if item[key] == value:
            datalist.append(item)
    return datalist

def gini(training_set, key):
    '''
    Given a training set consisting of attribute dictionaries and an attribute 
    to compute the entropy with respect to, compute the experimental probabilities of 
    each value of the attribute and then compute the entropy based on this.
    '''
    probs = compute_probabilities(training_set, key)
    gini = 0.0
    for p in probs:
        gini = gini + p*p
    gini = 1 - gini
    return gini
    
def entropy(training_set, key):
    '''
    Given a list of attribute dictionaries and an attribute to compute the 
    entropy for, compute the experimental probabilities of each value of the 
    attribute and then compute the entropy based on this.
    '''
    # Find the experimental probability of each value of the given attribute in
    # the data set listofdictionaires. Using the probabilities, compute the entropy e.
    probs = compute_probabilities(training_set, key)
    e = 0
    for prob in probs:
        e = e + prob * math.log(prob,2)
    e = -1*e
    return e

def gain(training_set, feature, target_feature):
    ''' Given a data set training_set and a set of features, step through
    the features to find the best information gain spliting on that feature.
    Return the feature and the information gain.'''

    # Compute the entropy of the entire data set using the values of the
    # target function, a.k.a. boundary. 
    e = entropy(training_set, target_feature)

    # Find all values of the feature "feature".
    values = find_unique_values(training_set, feature)
    gain = 0.0
    for v in values:
        sv = slice_of_data(training_set, feature, v)
        gain = gain + len(sv) * entropy(sv, 'boundary')

    gain = e - (1/len(training_set) * gain)
    return gain

def select_attribute(training_set, features, target_feature, gain_type):
    '''
    Chooses which attribute to split on by choosing the 
    attribute with the highest information gain.
    '''
    max_gain = 0.0 # For Information Gain
    baseline_score = 999.0 # For Gini Index
    best_feature = ''
    for f in features:
        if gain_type is 'gain': # Information gain
            f_gain = gain(training_set, f, target_feature)
            if f_gain > max_gain:
                max_gain = f_gain 
                best_feature = f 
        elif gain_type is 'gini': # Gini index
            gi = gini(training_set, f)
            if gi < baseline_score:
                basline_score = gi 
                best_feature = f 
    return best_feature 
           

    
    

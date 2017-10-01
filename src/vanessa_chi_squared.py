import information_gain as infogain

def compute_probs_with_keys(training_set, key):
    '''
    Does the same thing as infogain.compute_probabilities, but returns a dictionary
    of consisting of value: probability for all possible values of 'key' in
    the training represented in the training set. 
    '''
    allvals = []
    for item in training_set:
        allvals.append(item[key])

    ''' Find all unique values in allvals and throw them in basket. '''
    basket = set()
    for item in allvals:
        basket.add(item)
        
    probs_with_keys = { item: 0 for item in basket }

    for item in basket:
        probs_with_keys[item] = allvals.count(item)
        probs_with_keys[item] = probs_with_keys[item] *1.0 / len(training_set)
    return probs_with_keys


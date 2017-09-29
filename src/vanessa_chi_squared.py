import information_gain as infogain
# Does the same thing as infogain.compute_probabilities, but returns a dictionary
# of consisting of value: probability for all possible values of 'key' in
# the training represented in the training set. 
def compute_probs_with_keys(training_set, key):
    allvals = []
    for item in training_set:
        allvals.append(item[key])

    ''' Find all unique values in allvals and throw them in basket. '''
    basket = set()
    for item in allvals:
        basket.add(item)
        

    probs_with_keys = { item: 0 for item in basket }

    print "training set has size", len(training_set)
    for item in basket:
        probs_with_keys[item] = allvals.count(item)
        print "item", item, "has value", probs_with_keys[item]
        
        probs_with_keys[item] = probs_with_keys[item] *1.0 / len(training_set)

    return probs_with_keys



def main():
    print("Information gain of little data set")

    item1 = {'grade': 'steep', 'bumpiness':  'bumpy', 'speedlimit': 'yes', 'boundary': 'slow'}
    item2 = {'grade': 'steep', 'bumpiness':  'smooth', 'speedlimit': 'yes', 'boundary': 'slow'}
    item3 = {'grade': 'flat', 'bumpiness':  'bumpy', 'speedlimit': 'no', 'boundary': 'fast'}
    item4 = {'grade': 'steep', 'bumpiness':  'smooth', 'speedlimit': 'no', 'boundary': 'fast'}

    data_set = [item1, item2, item3, item4]

    
    print(infogain.select_attribute(data_set, {'grade', 'bumpy', 'speedlimit'}, 'boundary', 'gain'))    

    # Test probs_with_keys
    print "probabilities for bumpiness", compute_probs_with_keys(data_set, 'boundary')
    
if __name__ == '__main__':
    main()

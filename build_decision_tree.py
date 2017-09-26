import information_gain as infogain
import tree_node as node

DEBUG = True

def get_default_attribute(training_set):
    ''' 
    Gets the value of the most common attribute in the dataset. 
    '''
    freq_dict = {}
    # Counts the number of occurrences for each value that appears in training_set
    for t in training_set:
        for key in t:
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

def build_tree(training_set, target_attr, labels, depth):
    attribute_keys = training_set[0].keys() # All features to be tested on
    default_feature = get_default_attribute(training_set) # Get default feature
    
    if len(training_set) <= 1 or target_attr not in training_set:
        return node(default_feature, training_set, None, depth)
    
    
    # for t in training_set:
    #     if target_attr not in t:
    #         print 'not in training_set'
    if len(training_set) == 1:
        print 'all done'
        return
    # TODO: if target_Attr not in training_set
    # TODO: if len(training_set) == 1: return tree node with default_feature

    # Get unique attribute values
    unique_values = []
    for key in attribute_keys:
        unique_values.append(infogain.find_unique_values(training_set, key))
    unique_values = list(set(flatten_list(unique_values)))

    # Select the attribute with the highest information gain
    best_feature = infogain.select_attribute(training_set, unique_values, target_attr)

    for value in unique_values:
        # Remove the selected attribute from the dataset before recursing
        if depth == 0:
            child_dataset = training_set 
            parent = None 
        else:
            child_dataset = remove_attribute_from_list(training_set, best_feature)
        tree = node(best_feature, 
                    child_dataset, 
                    build_tree(child_dataset, target_attr, labels, depth+1),
                    depth+1)
        


        # build_tree(infogain.slice_of_data(training_set, ))
    #     print 'value: ', value 
        # build_tree(split(child_dataset....), target_attr, child_labels, depth+1)


    
    


    

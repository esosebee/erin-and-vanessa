import csv, os
import get_data
import information_gain as infogain

from build_tree import Tree
from build_tree import Node

import chi_square_test as chi 

DEBUG = False
PRINT_TREE = False

#########################
# File path information #
#########################
os.chdir('..')
path = os.getcwd()
data_path = os.path.join(path, 'Data')

###############################
# Node printing for debugging #
###############################
def print_tree(tree, indent):
    '''
    Prints string to console for debugging purposes.
    '''
    indentation = indent * ' '
    decision_indentation = (indent+2) * ' '
    if tree.children is not None:
        print indentation + str(len(tree.children))
        for child in tree.children:
            print_tree(child, indent+2)
    else:
        print indentation + str(0)
    # if tree.children is not None: 
    #     for child in tree.children:
    #         print_tree(child, indent+2)
    # else:
    #     print 'Leaf: ' + tree.node_feature_value

    # if tree.children is not None:
    #     print indentation + 'Feature: ' + str(tree.node_feature)
    #     print indentation + 'Value: ' + str(tree.node_feature_value)
    #     for child in tree.children:
    #         print_tree(child, indent+2)
    # else:
    #     print indentation + '['
    #     print decision_indentation + 'Deciding feature: ' + str(tree.node_feature)
    #     print decision_indentation + 'Deciding value: ' + str(tree.node_feature_value)
    #     print decision_indentation + 'Decision: ' + str(tree.decision)
    #     print indentation + ']'

##################
# Classification #
##################
def remove_key(dicts, key):
    d = dict(dicts)
    del d[key]
    return d

def classify(test_data, tree):
    '''
    Classifies the given data by recursively traversing the decision tree created with 
    the training data. At each node, the feature label and the feature value are 
    compared to what is present in test_data. If the test_data contains the value, 
    then this function recurses on that node.
    '''
    # At leaf node 
    if tree.children is None:
        return test_data['id'],tree.decision

    children_check = False
    for child in tree.children:
        child_label = child.node_feature 
        child_value = child.node_feature_value 
        children_check = children_check or (test_data[child_label] == child_value)
        if test_data[child_label] == child_value:
            return classify(test_data, child)

    # If a leaf node can't be reached, return the default prediction
    if children_check == False:
        return test_data['id'], tree.default_prediction

def write_to_csv(headers, data):
    '''
    Writes prediction data into a CSV file. 
    '''
    filename = 'submission.csv'
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for d in data:
            writer.writerow(d)
        f.close()

def test_dataset():
    item1 = {'altitude': 'high', 'direction': 'north', 'boundary': 'no'}
    item2 = {'altitude': 'high', 'direction': 'north', 'boundary': 'no'}    
    item3 = {'altitude': 'high', 'direction': 'south', 'boundary': 'no'}
    item4 = {'altitude': 'high', 'direction': 'south', 'boundary': 'no'}
    item5 = {'altitude': 'low', 'direction': 'north', 'boundary': 'yes'}
    item6 = {'altitude': 'low', 'direction': 'north', 'boundary': 'yes'}
    item7 = {'altitude': 'low', 'direction': 'north', 'boundary': 'yes'}
    item8 = {'altitude': 'low', 'direction': 'north', 'boundary': 'yes'}
    item9 = {'altitude': 'low', 'direction': 'south', 'boundary': 'no'}
    item10 = {'altitude': 'low', 'direction': 'north', 'boundary': 'yes'}
    
    data_set = [item1, item2, item3, item4, item5, item6, item7,
                item8, item9, item10]
    
    # def __init__(self, dataset, remaining_attribute_keys, target_attr, node_feature, node_feature_value, children, parent, decision, is_leaf, default_prediction, depth):

    attribute_keys = [ 'altitude', 'direction']
    target_attr = 'boundary'

    root_node = Node(data_set, attribute_keys, target_attr, None, None, None, None, None, False, None, 0)
    dtree = Tree(root_node)
    if PRINT_TREE: print_tree(dtree, 0)

if __name__ == '__main__':
    # Test algorithm on small dataset from class
    if DEBUG:
        test_dataset()

    training_filename = 'training.csv'
    testing_filename = 'testing.csv'

    training_data = get_data.load_dataset(training_filename, data_path)
    testing_data = get_data.load_dataset(testing_filename, data_path)

    # Get attributes for training data
    training_attributes_list = []
    for t in training_data:
        training_attributes_list.append(get_data.get_training_attributes(t))

    # Create tree with training dataset 
    target_attr = 'boundary'
    attribute_keys = training_attributes_list[0].keys()
    dtree = Node(training_attributes_list, attribute_keys, target_attr, None, None, None, None, None, False, None, 0)
    if PRINT_TREE:
        print_tree(dtree, 0)

    # Get attributes for test data
    testing_attributes_list = []
    for t in testing_data:
        testing_attributes_list.append(get_data.get_testing_attributes(t))
    
    # Classify testing data with decision tree
    predictions = []
    for t in testing_attributes_list:
        predictions.append(classify(t, dtree))
    
    # Write predictions to file 
    headers = ['id','class']
    write_to_csv(headers, predictions)
    

    








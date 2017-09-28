import os
import get_data
import information_gain as infogain
import build_tree
from build_tree import Tree

import chi_square_test as chi 

DEBUG = False

#########################
# File path information #
#########################
os.chdir('..')
path = os.getcwd()
data_path = os.path.join(path, 'Data')

###############################
# Tree printing for debugging #
###############################
def print_tree(tree, indent):
    '''
    Prints string to console for debugging purposes.
    '''
    indentation = indent * ' '
    decision_indentation = (indent+2) * ' '
    if tree.is_leaf == False:
        print indentation + 'Feature: ' + str(tree.node_feature)
        print indentation + 'Value: ' + str(tree.node_feature_value)
        for child in tree.children:
            print_tree(child, indent+2)
    else:
        print indentation + '['
        print decision_indentation + 'Deciding feature: ' + str(tree.node_feature)
        print decision_indentation + 'Deciding value: ' + str(tree.node_feature_value)
        print decision_indentation + 'Decision: ' + str(tree.decision)
        print indentation + ']'

##################
# Classification #
##################
def remove_key(dicts, key):
    d = dict(dicts)
    del d[key]
    return d

def classify(test_data, tree):
    # At leaf node 
    if tree.children is None:
        final_str = str(test_data['id']) + ',' + str(tree.decision)
        # print final_str
        return final_str

    children_check = False
    for child in tree.children:
        child_label = child.node_feature 
        child_value = child.node_feature_value 
        children_check = children_check or (test_data[child_label] == child_value)
        if test_data[child_label] == child_value:
            classify(test_data, child)

    # If a leaf node can't be reached, return the default prediction
    if children_check == False:
        final_str = str(test_data['id']) + ',' + str(tree.default_prediction)
        # print final_str 
        return final_str


if __name__ == '__main__':
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
    dtree = Tree(training_attributes_list, attribute_keys, target_attr, None, None, None, None, None, False, None, 0)
    if DEBUG:
        print_tree(dtree, 0)

    # Get attributes for test data
    testing_attributes_list = []
    for t in testing_data:
        testing_attributes_list.append(get_data.get_testing_attributes(t))

    # Get all possible predictions
    # target_values = infogain.find_unique_values(training_attributes_list, target_attr)
    
    # Classify testing data with decision tree
    predictions = []
    for t in testing_attributes_list:
        print classify(t, dtree)
        # build_tree.classify(t, dtree)
        # print build_tree.classify(t, dtree)
        # predictions.append(build_tree.classify(t, dtree))
    # print predictions
    








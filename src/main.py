import get_data
import information_gain as infogain
from build_tree import Tree

import chi_square_test as chi 

DEBUG = False

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

if __name__ == '__main__':
    training_filename = 'training.csv'
    testing_filename = 'testing.csv'

    training_data = get_data.load_dataset(training_filename)
    testing_data = get_data.load_dataset(testing_filename)

    #####################################
    # Create tree with training dataset #
    #####################################
    training_attributes_list = []
    for t in training_data:
        training_attributes_list.append(get_data.get_training_attributes(t))

    target_attr = 'boundary'
    attribute_keys = training_attributes_list[0].keys()
    dtree = Tree(training_attributes_list, attribute_keys, target_attr, None, None, None, None, None, False, 0)
    if DEBUG:
        print_tree(dtree, 0)


    # test_data = ['1995', 'GCTGAGGCCTGGCTCTCTCCCTCCCCACAGGGTGCCCGGTACGTGTGGAACCGCACTGAG', 'IE']
    # attributes = get_training_attributes(test_data)




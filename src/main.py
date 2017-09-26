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

    training_attributes_list, testing_attributes_list = [], []
    for t in training_data:
        training_attributes_list.append(get_data.get_attributes(t))

    target_attr = 'boundary'
    attribute_keys = training_attributes_list[0].keys()
    dtree = Tree(training_attributes_list, attribute_keys, target_attr, None, None, None, None, None, False, 0)
    if DEBUG:
        print_tree(dtree, 0)

    # Test on partition of data
    # if DEBUG:
    #     test_data = training_data
    #     test_attributes = training_attributes_list
    #     attribute_keys = test_attributes[0].keys()
    #     labels = list(infogain.find_values_of_attribute(test_attributes, target_attr))
    #     tree = Tree(test_attributes, attribute_keys, target_attr, labels, None, None, None, None, 0)
        # chi.chi_square_test(test_attributes, target_attr, labels, 0.05)

    # test_data = ['1995', 'GCTGAGGCCTGGCTCTCTCCCTCCCCACAGGGTGCCCGGTACGTGTGGAACCGCACTGAG', 'IE']
    # attributes = get_attributes(test_data)




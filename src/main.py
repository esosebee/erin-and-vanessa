import csv
import os, sys
import get_data
import information_gain as infogain

from build_tree import Tree
from build_tree import Node

# Debugging flags
DEBUG = False
PRINT_TREE = False

###############################
# Node printing for debugging #
###############################
def print_tree(node, indent):
    '''
    Prints string to console for debugging purposes.
    '''
    indentation = indent * ' '
    decision_indentation = (indent+2) * ' '

    if node.children is not None:
        print indentation + 'Feature: ' + str(node.node_feature)
        print indentation + 'Value: ' + str(node.node_feature_value)
        for child in node.children:
            print_tree(child, indent+2)
    else:
        print indentation + '['
        print decision_indentation + 'Deciding feature: ' + str(node.node_feature)
        print decision_indentation + 'Deciding value: ' + str(node.node_feature_value)
        print decision_indentation + 'Decision: ' + str(node.decision)
        print indentation + ']'

##################
# Classification #
##################
def classify(test_data, node):
    '''
    Classifies the given piece of data by recursively traversing the decision tree created with 
    the training data. At each node, the feature label and the feature value are 
    compared to what is present in test_data. If the test_data contains the value, 
    then this function recurses on that node.
    '''
    # At leaf node
    if node.children is None:
        return test_data['id'],node.decision

    # What is the dedicing feature in node? Which child of node has deciding
    # feature value that matches the value of that same deciding feature in node?
    #
    # The deciding feature in node is node.node_feature or
    # node.feature_value, I don't know which.
    else: 
        # Find the child that has value of node.feature_value (node.node_feature_value is a key,
        # like 'altitude')
        no_such_kid = True
        child_to_traverse = None
        for child in node.children:
            # Check which of the children has value of deciding feature matching
            # the node.  Call classify on that child.
            # If there is no such node, behave the same as in the leaf case.
            if test_data[node.node_feature] ==  child.node_feature_value:
                no_such_kid = False
                child_to_traverse = child

        if no_such_kid:
            #We didn't find a child to traverse.  Return like we're at a leaf.
            return test_data['id'],node.decision
        else: 
            return classify(test_data, child_to_traverse)

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

##############################
# Command line input parsing #
##############################

def print_usage():
    '''
    Usage statement for this program.
    '''
    print 'USAGE: python main.py -train dir/to/training_file.csv -test dir/to/testing_file.csv'

def parse_args(args):
    '''
    If command line input is valid, then parses the args and 
    gets the necessary information from them. Otherwise, displays
    a usage statement and exits the program.
    '''
    if '-train' in args and '-test' in args:
        training_filename = args['-train']
        testing_filename = args['-test']
        return training_filename, testing_filename
    else:
        print_usage()
        sys.exit(0)

def get_args(argv):
    '''
    Get options from command line input.
    '''
    opts = {}
    while argv:
        if argv[0][0] == '-':
            opts[argv[0]] = argv[1]
        argv = argv[1:]
    return opts

if __name__ == '__main__':
    # Parse command line args
    myargs = get_args(sys.argv[1:])
    training_filename, testing_filename = parse_args(myargs) # Get filenames
    
    training_data = get_data.load_dataset(training_filename)
    testing_data = get_data.load_dataset(testing_filename)

    # Get attributes for training data
    training_attributes_list = []
    for t in training_data:
        training_attributes_list.append(get_data.get_training_attributes(t))

    # Create tree with training dataset 
    target_attr = 'boundary'
    attribute_keys = training_attributes_list[0].keys()
    root_node = Node(training_attributes_list, attribute_keys, target_attr, None, None, None, None, None, False, None, 0)
    dtree = Tree(root_node)
    if PRINT_TREE:
        print_tree(root_node, 0)

    # Get attributes for test data
    testing_attributes_list = []
    for t in testing_data:
        testing_attributes_list.append(get_data.get_testing_attributes(t))
    
    # Classify testing data with decision tree
    predictions = []
    for t in testing_attributes_list:
        predictions.append(classify(t, root_node))

    # Write predictions to file 
    headers = ['id','class']
    write_to_csv(headers, predictions)
    

    








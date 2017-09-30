import csv, os
import get_data
import information_gain as infogain

from build_tree import Tree
from build_tree import Node

import chi_square_test as chi 

# Debugging flags
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
        print "node.node_feature_value", node.node_feature_value
        print "node.node_feature", node.node_feature
    
    
        # Find the child that has value of node.feature_value (node.node_feature_value is a key,
        # like 'altitude')
    
        no_such_kid = True
        child_to_traverse = None
        for child in node.children:
            # Check which of the children has value of deciding feature matching
            # the node.  Call classify on that child.
            # If there is no such node, behave the same as in the leaf case.
            print "test_data[node.node_feature]" , test_data[node.node_feature],\
                 "child.node_feature_value", child.node_feature_value
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

    testitem1 = {'altitude': 'high', 'direction': 'north'}
    testitem2 = {'altitude': 'low', 'direction': 'north'}
    testitem3 = {'altitude': 'low', 'direction': 'north'}
    
    data_set = [item1, item2, item3, item4, item5, item6, item7,
                item8, item9, item10]
    test_data_set = [testitem1, testitem2, testitem3]

    attribute_keys = [ 'altitude', 'direction']
    target_attr = 'boundary'

    root_node = Node(data_set, attribute_keys, target_attr, None, None, None, None, None, False, None, 0)
    dtree = Tree(root_node)
    if PRINT_TREE: print_tree(root_node, 0)

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
    
    for p in predictions:
        print p

    # Write predictions to file 
    headers = ['id','class']
    write_to_csv(headers, predictions)
    

    








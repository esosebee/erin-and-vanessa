import information_gain
import tree_node

def default_attribute(data, attributes):
    ''' Gets the most common value for an attribute. '''
    freq_dict = {}
    

def select_attribute(data, attributes, feature):
    '''
    Choose the attribute that yields the highest information gain.
    '''
    max_gain = 0.0
    best_attribute = attributes[0] # TODO: make default_attribute function
    for attribute in attributes:
        attr_gain = information_gain.gain(attribute, feature)
        if attr_gain > max_gain:
            max_gain = attr_gain 
            best_attribute = attribute 
    return best_attribute 

# TODO: need to know feature?
def build_tree(data, attributes, feature): 
    tree = {}
    
    # if attributes size == 1, then return 
    # attribute





    

import information_gain as infogain 

class Tree:
    dataset = None # The dataset that was tested for this node
    remaining_attributes_keys = None
    target_attr =  None # The target attribute to be tested for (a.k.a. 'boundary')
    labels = None # Target outcomes (a.k.a. 'IE', 'EI', 'N')
    node_feature = None # Feature that we're splitting on
    children = None # A list of this node's child nodes
    parent = None # Parent of the current node
    decision = None # The final prediction of the branch of the tree (only as value at leaf nodes: IE, EI, N)
    depth = None # The depth of the node in the tree

    def __init__(self, dataset, remaining_attributes_keys, target_attr, labels, node_feature, children, parent, decision, depth):
        '''
        Create decision tree node.
        '''
        self.dataset = dataset
        self.remaining_attributes_keys = remaining_attributes_keys
        self.target_attr = target_attr 
        self.labels = labels
        self.node_feature = node_feature 
        self.children = children 
        self.parent = parent
        self.decision = decision
        self.depth = depth

        # Begin building tree
        self.build_decision_tree(dataset, remaining_attributes_keys, target_attr, labels, depth)

    def build_decision_tree(self, dataset, remaining_attributes_keys, target_attr, labels, depth):
        '''
        Recursively build the decision tree.
        '''
        # print 'dataset length: ', len(dataset[0])
        # print 'remaining_attributes_keys length: ', len(remaining_attributes_keys)
        # raw_input('Press any key to continue...')

        # Remaining boundary values
        target_values = infogain.find_values_of_attribute(dataset, target_attr)

        # At leaf node - stop recursing
        if len(dataset) == 1 or len(remaining_attributes_keys) == 1 or len(target_values) == 1:
            self.decision = dataset[0][target_attr]
            return 

        # Select the attribute with the highest information gain
        best_feature = infogain.select_attribute(dataset, remaining_attributes_keys, target_attr)
        self.node_feature = best_feature
        best_feature_values = infogain.find_unique_values(dataset, best_feature)
        child_remaining_attributes_keys = remaining_attributes_keys[:]
        child_remaining_attributes_keys.remove(best_feature)

        self.children = []
        for val in best_feature_values:
            child_dataset = infogain.slice_of_data(dataset, best_feature, val)
            # print 'child_dataset length: ', len(child_dataset)
            # print child_dataset
            self.children.append(Tree(child_dataset, child_remaining_attributes_keys, target_attr, labels, best_feature, None, self, None, depth+1))

        # TODO: print tree functionality

        # default_prediction = infogain.get_default_prediction(dataset, target_attr) # Get default feature
        # if len(dataset[0]) == 1 or target_attr not in dataset[0]: # Stop splitting, there are no more features
        #     # Get decision 
        #     self.decision = defaut_prediction 
        #     return 

        # Get unique attribute values 
        # unique_values = [] 
        # attribute_keys = dataset[0].keys() # All features to be tested on
        # for key in attribute_keys:
        #     unique_values.append(infogain.find_unique_values(dataset, key))
        # unique_values = list(set(infogain.flatten_list(unique_values)))
        

        
        
        # Remove selected feature from dataset for children nodes 
        # child_dataset = infogain.remove_attribute_from_list(dataset, self.node_feature)

        # Remove selected feature from unique values
        # child_unique_values = [x for x in remaining_attributes_keys if x != self.node_feature]
        
        # Begin recursing for children 
        # self.children = []
        # for value in unique_values:
        #     child_labels = labels[:] # TODO: figure out how to split labels
        #     self.children.append(Tree(infogain.split_dataset(dataset, value), target_attr, child_labels, value, None, self, None, depth+1))





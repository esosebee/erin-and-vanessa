import information_gain as infogain 

class Tree:
    dataset = None # The dataset that was tested for this node
    target_attr =  None # The target attribute to be tested for
    labels = None # Target outcomes
    node_feature = None # The predicting attribute for the node
    children = None # A list of this node's child nodes
    decision = None # The final prediction of the branch of the tree
    depth = None # The depth of the node in the tree

    def __init__(self, dataset, target_attr, labels, node_feature, children, parent, decision, depth):
        '''
        Create decision tree node.
        '''
        self.dataset = dataset
        self.target_attr = target_attr 
        self.labels = labels
        self.node_feature = node_feature 
        self.children = children 
        self.parent = parent
        self.decision = decision
        self.depth = depth

        # Begin building tree
        self.build_decision_tree(dataset, target_attr, labels, depth)

    def build_decision_tree(self, dataset, target_attr, labels, depth):
        '''
        Recursively build the decision tree.
        '''

        # If no more data, then stop recursing
        if len(dataset) == 0:
            return 

        default_prediction = infogain.get_default_prediction(dataset, target_attr) # Get default feature
        if len(dataset[0]) == 1 or target_attr not in dataset[0]: # Stop splitting, there are no more features
            # Get decision 
            self.decision = defaut_prediction 
            return 

        # Get unique attribute values 
        unique_values = [] 
        attribute_keys = dataset[0].keys() # All features to be tested on
        for key in attribute_keys:
            unique_values.append(infogain.find_unique_values(dataset, key))
        unique_values = list(set(infogain.flatten_list(unique_values)))
        
        # Select the attribute with the highest information gain
        self.node_feature = infogain.select_attribute(dataset, unique_values, target_attr)

        # Remove selected feature from dataset for children nodes 
        child_dataset = infogain.remove_attribute_from_list(dataset, self.node_feature)

        # Remove selected feature from unique values
        child_unique_values = [x for x in unique_values if x != self.node_feature]
        
        # Begin recursing for children 
        self.children = []
        for value in unique_values:
            child_labels = labels[:] # TODO: figure out how to split labels
            self.children.append(Tree(infogain.split_dataset(dataset, value), target_attr, child_labels, value, None, self, None, depth+1))





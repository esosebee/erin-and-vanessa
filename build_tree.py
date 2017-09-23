import information_gain as infogain 

class Tree:
    dataset = None # The dataset that was tested for this node
    target_attr =  None # The target attribute to be tested for
    labels = None # All values for the target attribute
    best_feature = None # The predicting attribute for the node
    children = None # A list of this node's child nodes
    depth = None # The depth of the node in the tree

    def __init__(self, dataset, target_attr, labels, best_feature, children, parent, depth):
        '''
        Create decision tree node.
        '''
        self.dataset = dataset
        self.target_attr = target_attr 
        self.labels = labels
        self.depth = depth
        self.best_feature = best_feature 
        self.children = children 
        self.parent = parent

        # Begin building tree
        self.build_decision_tree(dataset, target_attr, labels, depth)


    # def set_attribute_value(self, attribute_value):
    #     if attribute_value is not None:
    #         self.attribute_value = attribute_value 

    # def set_dataset(self, dataset):
    #     if dataset is not None:
    #         self.dataset = dataset 

    # def set_children(self, children):
    #     if children is not None:
    #         self.children = children 

    # def set_depth(self, depth):
    #     if depth == 0:
    #         self.depth = depth + 1
    #     else:
    #         self.depth = depth

    def build_decision_tree(self, training_set, target_attr, labels, depth):
        attribute_keys = training_set[0].keys() # All features to be tested on
        default_feature = infogain.get_default_attribute(training_set) # Get default feature
        # Get unique attribute values 
        unique_values = [] 
        for key in attribute_keys:
            unique_values.append(infogain.find_unique_values(training_set, key))
        unique_values = list(set(infogain.flatten_list(unique_values)))
        
        # Select the attribute with the highest information gain
        best_feature = infogain.select_attribute(training_set, unique_values, target_attr)
        print best_feature
        # for value in unique_values:




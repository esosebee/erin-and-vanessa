import information_gain as infogain 

class Tree:
    dataset = None # The dataset that was tested for this node
    remaining_attributes_keys = None
    target_attr =  None # The target attribute to be tested for (a.k.a. 'boundary')
    node_feature = None # Feature that we're splitting on
    children = None # A list of this node's child nodes
    parent = None # Parent of the current node
    decision = None # The final prediction of the branch of the tree (only as value at leaf nodes: IE, EI, N)
    is_leaf = None # Marks if a tree is a leaf or not
    depth = None # The depth of the node in the tree

    def __init__(self, dataset, remaining_attributes_keys, target_attr, node_feature, children, parent, decision, is_leaf, depth):
        '''
        Create decision tree node.
        '''
        self.dataset = dataset
        self.remaining_attributes_keys = remaining_attributes_keys
        self.target_attr = target_attr 
        self.node_feature = node_feature 
        self.children = children 
        self.parent = parent
        self.decision = decision
        self.is_leaf = is_leaf
        self.depth = depth

        # Begin building tree
        self.build_decision_tree(dataset, remaining_attributes_keys, target_attr, is_leaf, depth)
        return

    def build_decision_tree(self, dataset, remaining_attributes_keys, target_attr, is_leaf, depth):
        '''
        Recursively build the decision tree.
        '''
        # Remaining boundary values
        target_values = list(infogain.find_values_of_attribute(dataset, target_attr))

        # At leaf node: stop recursing
        if len(dataset) == 1 or len(remaining_attributes_keys) == 1 or len(target_values) == 1:
            self.is_leaf = True    
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
            self.children.append(Tree(child_dataset, child_remaining_attributes_keys, target_attr, best_feature, None, self, None, False, depth+1))






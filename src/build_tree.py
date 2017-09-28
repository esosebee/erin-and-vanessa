import information_gain as infogain 

class Tree:
    node = None # The node to start building the tree on 

    def __init__(self, node):
        self.build_tree(node)
        return

    def build_tree(self, node):
        if node.children is not None:
            for child in node.children:
                print len(node.children)
                if child.node_feature_value == 'low':
                    new_node = Node(child.dataset, child.remaining_attribute_keys, child.target_attr, child.node_feature, child.node_feature_value, child.children, child.parent, child.decision, child.is_leaf, child.default_prediction, child.depth)
                    return self.build_tree(new_node)

class Node:
    dataset = None # The dataset that was tested for this node
    remaining_attribute_keys = None
    target_attr =  None # The target attribute to be tested for (a.k.a. 'boundary')
    node_feature = None # Feature that we're splitting on
    node_feature_value = None
    children = None # A list of this node's child nodes
    parent = None # Parent of the current node
    decision = None # The final prediction of the branch of the tree (only as value at leaf nodes: IE, EI, N)
    is_leaf = False # Marks if a tree is a leaf or not
    default_prediction = None 
    depth = 0 # The depth of the node in the tree

    def __init__(self, dataset, remaining_attribute_keys, target_attr, node_feature, node_feature_value, children, parent, decision, is_leaf, default_prediction, depth):
        '''
        Create decision tree node.
        '''
        self.dataset = dataset
        self.remaining_attribute_keys = remaining_attribute_keys
        self.target_attr = target_attr 
        self.node_feature = node_feature 
        self.node_feature_value = node_feature_value
        self.children = children 
        self.parent = parent
        self.decision = decision
        self.is_leaf = is_leaf
        self.default_prediction = default_prediction
        self.depth = depth

        # Create tree node 
        self.create_node(dataset, remaining_attribute_keys, target_attr, is_leaf, depth)
        return

    def add_children(self, dataset, best_feature, values, remaining_attribute_keys, target_attr, depth):
        '''
        Recursively add children for the current tree node.
        '''
        self.children = []
        for val in values:
            # Get node's default prediction
            default_prediction = infogain.get_default_prediction(dataset, best_feature, val, target_attr)
            child_dataset = infogain.slice_of_data(dataset, best_feature, val)
            self.children.append(Node(child_dataset, remaining_attribute_keys, target_attr, best_feature, val, None, self, None, False, default_prediction, depth+1))

    def create_node(self, dataset, remaining_attribute_keys, target_attr, is_leaf, depth):
        '''
        Create a node for the tree.
        '''
        # Get the remaining boundary values
        target_values = list(infogain.find_values_of_attribute(dataset, target_attr))
        
        # At leaf node: set decision for node 
        if len(dataset) == 1 or len(remaining_attribute_keys) == 0:
            self.is_leaf = True 
            self.decision = dataset[0][target_attr]
            return

        # Only one boundary value remains, stop recursing and set decision to the remaining value 
        if len(target_values) == 1:
            self.is_leaf = True 
            self.decision = target_values[0]
            return

        # Get node values using information gain 
        best_feature = infogain.select_attribute(dataset, remaining_attribute_keys, target_attr, 'gain')
        self.node_feature = best_feature 
        best_feature_values = infogain.find_unique_values(dataset, best_feature)
        child_remaining_attribute_keys = remaining_attribute_keys[:]
        child_remaining_attribute_keys.remove(best_feature)

        # Get node's children
        if self.children is None:
            self.add_children(dataset, best_feature, best_feature_values, child_remaining_attribute_keys, target_attr, depth)



class tree_node:
    attribute_value = None # The attribute being tested on
    dataset = None # The dataset that was tested for this node
    children = None # A list of this node's child nodes
    depth = None # The depth of the node in the tree

    def __init__(self, attribute_value, dataset, children, depth):
        self.attribute_value = set_attribute_value(attribute_value)
        self.label = set_label(label)
        self.dataset = set_dataset(dataset)
        self.children = set_children(children)
        self.parent = set_parent(parent)
        self.depth = set_level(depth)

    def set_attribute_value(attribute_value):
        if attribute_value is not None:
            self.attribute_value = attribute_value 

    def set_dataset(dataset):
        if dataset is not None:
            self.dataset = dataset 

    def set_children(children):
        if children is not None:
            self.children = children 

    def set_depth(depth):
        if depth == 0:
            self.depth = depth + 1
        else:
            self.depth = depth

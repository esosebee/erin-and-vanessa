class tree_node:
    dataset = ''
    attributes = []
    children = {}

    def __init__(self, dataset, attributes, children):
        self.set_dataset(dataset)
        self.set_attributes(attributes)
        self.set_children(children)

    def set_dataset(self, dataset):
        self.dataset = dataset 

    def set_attributes(self, attributes):
        # is this going to be a list or a dict?
        if isinstance(attributes, dict):
            self.attributes = attributes.keys()
        else:
            self.attributes = attributes 

    def set_children(self, children):
        if isinstance(attributes, dict):
            self.children = children.keys()
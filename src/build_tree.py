'''
VANESSA's build_tree
'''

import information_gain as infogain
import vanessa_chi_squared as vchi2
from scipy.stats import chi2

class Tree:
    '''
    Class that handles building the tree.
    '''
    node = None # The node to start building the tree on 

    def __init__(self, node):
        self.build_tree(node)
        return

    def build_tree(self, node):
        '''
        Recursively build a tree given a node.
        '''
        if node.children is not None:
            for child in node.children:
                new_node = Node(child.dataset, child.remaining_attribute_keys, child.target_attr, child.node_feature, child.node_feature_value, child.children, child.parent, child.decision, child.is_leaf, child.default_prediction, child.depth)
                return self.build_tree(new_node)

class Node:
    '''
    Class that represents a node in the tree.
    '''
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
        # best_feature = infogain.select_attribute(dataset, remaining_attribute_keys, target_attr, 'gini')
        self.node_feature = best_feature 
        best_feature_values = infogain.find_unique_values(dataset, best_feature)
        child_remaining_attribute_keys = remaining_attribute_keys[:]
        child_remaining_attribute_keys.remove(best_feature)

        # Get node's children
        if self.children is None:
            self.add_children(dataset, best_feature, best_feature_values, child_remaining_attribute_keys, target_attr, depth)



    # Finds and returns all the leaves of the given tree. 
    def find_leaves(self,  leaf_list):

        # If you have no parent, you're the root. Initialize the leaf list.
        if self.parent == None:
            leaf_list = []
    
        # If you have no children, you're a leaf.  Add your self to the leaf
        # set and return. 
        if self.is_leaf == True:
            #print "I'm a leaf: ", self.node_feature_value, self.decision
            leaf_list.append(self)
            #print "A:length of leaf_set" , len(leaf_set)
            return(leaf_list)
        # Otherwise, recurse through your children. 
        else:
            #print "Looking through children."
            for child in self.children:
                #print "B:length of leaf_set", len(leaf_set)
                #leaf_set.append( child.find_leaves( leaf_set) )
                leaf_list = child.find_leaves(leaf_list)
                
        return(leaf_list)


    # Count how many items from dataset have value value for the target_attribute.
    def get_count(this, dataset, target_attribute, value):

        count = 0
        for d in dataset:
            if d[target_attribute] == value:
                count += 1

        return count
        
    # Based on the chi squared value, prune the tree.  Returns the pruned tree.
    
    def prune(this, leaf_list, target_attribute, significance_level):

        #Step throught the leaf_list, deciding whether to prune the current leaf and its
        # siblings. 

        while (len(leaf_list)) > 1:
            

            # Pick the leaf with the greatest depth.
            max_leaf_depth = 0
            candidate_leaf = leaf_list[0]
            for leaf in leaf_list:
                if leaf.depth > max_leaf_depth:
                    candiate_leaf = leaf
                    max_leaf_depth = leaf.depth
                    
            leaf = candidate_leaf
            
            ''' Find the parent of the leaf
             Compute the experimental probabilities of each target_attribute
            '''

            leaf_parent = leaf.parent

            ''' Based on the distribution of the parent data, compute the probability
            that the target_attribute takes on each possible value.  This is computed
            as a dictionary with the keys the value of the target_attribute because
            some values of the target attribute may be missing. '''
            
            ''' Now, for each child of leaf_parent, compute the count of values for each
            value of the target attribute.'''

        
            total_target_attributes = infogain.find_unique_values(this.dataset, target_attribute) 
            number_of_leaves = len(leaf_parent.children)
           
            
            degrees_freedom = (len(total_target_attributes) - 1)*(number_of_leaves - 1)
        
            for child in leaf_parent.children:
                
                # If child is a leaf already, we don't need to test for pruning it.
                # I'M NOT SURE ABOUT THIS.  I think it's right. 
                '''if (child.is_leaf):
                    print child.node_feature_value, "is a leaf, so we ain't pruning it"
                    leaf_list.remove(child)
                    #print "data set for OTHERSIDE"
                    #print child.dataset
                    
                else:'''
                c = 0
          
                
                for val in list(infogain.find_values_of_attribute(leaf_parent.dataset, child.node_feature)):
                    # CHECK THE leaf.get_count thing.  This may be wrong
                
                    for decision in total_target_attributes:
                        leaf_probs = vchi2.compute_probs_with_keys(child.dataset, target_attribute)
                        
                        some_slice = infogain.slice_of_data(child.dataset, target_attribute, decision)
                        actual_count = leaf.get_count(some_slice, child.node_feature, val)
                        
                    
                        # We want the slice of child.dataset for val.
                       
                        slice_of_data = infogain.slice_of_data(child.dataset, child.node_feature, val)
                        if decision in leaf_probs: 
                            expected_count = len(slice_of_data) * leaf_probs[decision]
                        else:
                            expected_count = 0
                        
                        if expected_count > 0:
                            c = c + ( ((actual_count - expected_count)**2) / expected_count)

            # The null hypothesis is that the split was due to randome chance.
            
            our_chi2 = chi2.sf(c, degrees_freedom)
        

            if (our_chi2 <= significance_level):
                # We accept the null hypothesis.   The split is due to chance.  Ditch the children of this parent. 
                #need_to_prune = True
                leaf_parent.isleaf = True
                leaf_parent.children = []
                # This node is now a leaf, so add it in to the leaf_list
                if leaf_parent.parent != None:
                    leaf_list.append(leaf_parent)
            
            else:
                # We reject the null hypothesis. 
                need_to_prune = False
            
            # In either case, take all the children of this leaf's parent
            # out of leaf_list.

            for kid in leaf_parent.children:
                if kid in leaf_list: 
                    leaf_list.remove(kid)

        # Return the pruned tree.
        return this
        
            
        





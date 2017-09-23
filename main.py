import get_data
import information_gain as infogain
# import build_decision_tree as dtree 
from build_tree import Tree

DEBUG = True

def get_initial_tree_values(training_set, target_attr, labels, depth):
    attribute_keys = training_set[0].keys()
    d

if __name__ == '__main__':
    training_filename = 'training.csv'
    testing_filename = 'testing.csv'

    training_data = get_data.load_dataset(training_filename)
    testing_data = get_data.load_dataset(testing_filename)

    training_attributes_list, testing_attributes_list = [], []
    for t in training_data:
        training_attributes_list.append(get_data.get_attributes(t))

    target_attr = 'boundary'

    if DEBUG:
        test_data = training_data[0:10]
        test_attributes = training_attributes_list[0:10]
        labels = list(infogain.find_values_of_attribute(test_attributes, target_attr))
        tree = Tree(test_attributes, target_attr, labels, None, None, None, 0)
        # dtree.build_tree(test_attributes, 'boundary', labels, 0)
        # print len(training_data)
        # print len(training_attributes)
        # for key in training_attributes[1].keys():
            # print 'key', key
            # print 'attribute values', infogain.find_values_of_attribute(training_attributes, key)
            # print('unique values', infogain.find_unique_values(training_attributes, key))

    # test_data = ['1995', 'GCTGAGGCCTGGCTCTCTCCCTCCCCACAGGGTGCCCGGTACGTGTGGAACCGCACTGAG', 'IE']
    # attributes = get_attributes(test_data)




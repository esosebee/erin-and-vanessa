import get_data
import information_gain as infogain
from build_tree import Tree

DEBUG = True

if __name__ == '__main__':
    training_filename = 'training.csv'
    testing_filename = 'testing.csv'

    training_data = get_data.load_dataset(training_filename)
    testing_data = get_data.load_dataset(testing_filename)

    training_attributes_list, testing_attributes_list = [], []
    for t in training_data:
        training_attributes_list.append(get_data.get_attributes(t))

    target_attr = 'boundary'

    # Test on partition of data
    if DEBUG:
        test_data = training_data[0:10]
        test_attributes = training_attributes_list[0:10]
        labels = list(infogain.find_values_of_attribute(test_attributes, target_attr))
        tree = Tree(test_attributes, target_attr, labels, None, None, None, None, 0)

    # test_data = ['1995', 'GCTGAGGCCTGGCTCTCTCCCTCCCCACAGGGTGCCCGGTACGTGTGGAACCGCACTGAG', 'IE']
    # attributes = get_attributes(test_data)




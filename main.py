import get_data
import information_gain

if __name__ == '__main__':
    training_filename = 'training.csv'
    testing_filename = 'testing.csv'

    training_data = get_data.load_dataset(training_filename)
    testing_data = get_data.load_dataset(testing_filename)

    for t in training_data:
        print t

    # training_attributes, testing_attributes = [], []
    # for t in training_data:
    #     training_attributes.append(get_attributes(t))

    # test_data = ['1995', 'GCTGAGGCCTGGCTCTCTCCCTCCCCACAGGGTGCCCGGTACGTGTGGAACCGCACTGAG', 'IE']
    # attributes = get_attributes(test_data)
    # print attributes




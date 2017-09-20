import get_data
import information_gain

DEBUG = True 

if __name__ == '__main__':
    training_filename = 'training.csv'
    testing_filename = 'testing.csv'

    training_data = get_data.load_dataset(training_filename)
    testing_data = get_data.load_dataset(testing_filename)

    training_attributes, testing_attributes = [], []
    for t in training_data:
        training_attributes.append(get_data.get_attributes(t))
    
    if DEBUG:
        print 'What the keys are: ', training_attributes[1].keys()
        for v in training_attributes[1].keys():
            # information_gain.find_unique_vals(training_attributes, v)
            print('values', information_gain.finduniquevals(training_attributes, v))



    # test_data = ['1995', 'GCTGAGGCCTGGCTCTCTCCCTCCCCACAGGGTGCCCGGTACGTGTGGAACCGCACTGAG', 'IE']
    # attributes = get_attributes(test_data)
    # print attributes




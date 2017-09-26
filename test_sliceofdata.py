import decision_tree
import infoGain

# Use Erin's functions to read in the data.  Then compute lists of all data
# instances that have boundary 'IE', another list for 'EI' and another list for
# 'N'.
# Verify that the list sizes add up to 2000, the size of our training set. 

def main():

    training_filename = 'training.csv'

    training_attributes = []

    training_data = decision_tree.load_dataset(training_filename)

    for t in training_data:
        training_attributes.append(decision_tree.get_attributes(t))

    #smaller_training_attributes = training_attributes[0:10]        
    # For testing, find all data instances that have target value 'IE'

    ie_s = infoGain.sliceOfData(training_attributes, 'boundary', 'IE')

    #print ( ie_s)
    print("Number of IEs is ", len(ie_s))

    ei_s = infoGain.sliceOfData(training_attributes, 'boundary', 'EI')

    print('Number of EIs is ', len(ei_s))

    n_s = infoGain.sliceOfData(training_attributes, 'boundary', 'N')
    print('Number of Ns is ', len(n_s))


    mod3 = infoGain.sliceOfData(training_attributes, 'mod3', 2)
    print ("number of 2s mod 3 is ", len(mod3))
    print("total is ", len(ei_s) + len(ie_s) + len(n_s))
main()

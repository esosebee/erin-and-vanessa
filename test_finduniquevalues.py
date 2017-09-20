import decision_tree
import infoGain

''' Use Erin's functions to read in the data.  Then loop through all of the
keys in a record in training_attributes and print out all possible keys their
values.   

Note:  This assumes all keys appear in all the records!   If they don't, we
have another problem.

'''


def main():

    training_filename = 'training.csv'

    training_attributes = []

    training_data = decision_tree.load_dataset(training_filename)
    for t in training_data:
        training_attributes.append(decision_tree.get_attributes(t))

    #smaller_training_attributes = training_attributes[0:10]        
    # For testing, find all data instances that have target value 'IE'

    print ("What the keys are: ", training_attributes[1].keys())

                                                           
    for v in  training_attributes[1].keys():
        print("key", v)
        print("values", infoGain.finduniquevals(training_attributes, v))
    
    
 
main()

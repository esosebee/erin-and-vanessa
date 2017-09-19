import os
import csv

path = os.getcwd()
data_path = os.path.join(path, 'Data')

####################################
# Get attributes from DNA sequence #
####################################
def split_sequence_in_half(sequence):
    return sequence[:len(sequence)/2], sequence[len(sequence)/2:]

def get_letters_index(sequence, i_range, n):
    '''
    Gets n amount of characters from each index.
    '''
    index_dict = {}
    for i in range(0, len(sequence)-(n-1)):
        index_dict[i] = sequence[i:i+n]
    return index_dict

def get_attributes(data):
    sequence = data[1]
    attributes = {}
    attributes['letter_at_index'] = get_letters_index(sequence, range(0, len(sequence)), 1)
    attributes['pair_at_index'] = get_letters_index(sequence, range(0, len(sequence)), 2)
    attributes['triple_at_index'] = get_letters_index(sequence, range(0, len(sequence)), 3)
    return attributes

#############
# Load data #
#############
def load_dataset(filename):
    filepath = os.path.join(data_path, filename)
    with open(filepath) as f:
        reader = csv.reader(f)
        dataset = list(reader)
    return dataset


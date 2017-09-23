import os
import csv

path = os.getcwd()
data_path = os.path.join(path, 'Data')

####################################
# Get attributes from DNA sequence #
####################################
def split_sequence_in_half(sequence):
    ''' Splits a DNA sequence perfectly in half. '''
    return sequence[:len(sequence)/2], sequence[len(sequence)/2:]

def get_letters_index(sequence, i_range, n):
    '''
    Gets n amount of characters from each index.
    '''
    if n == 1:
        key = 'letter'
    elif n == 2:
        key = 'pair'
    elif n == 3:
        key = 'triple'

    index_dict = {}
    i = 0
    while i < len(sequence)-(n-1):
        label = key + str(i)
        index_dict[label] = (sequence[i:i+n], i)
        i += n
    return index_dict

def get_attributes(data):
    '''
    Gets the desired attributes to be tested on from the data.
    '''
    seq_id = data[0] 
    sequence = data[1] 
    boundary = data[2]

    attributes = {}
    attributes['id'] = seq_id
    attributes['sequence'] = sequence
    attributes['boundary'] = boundary
    attributes.update(get_letters_index(sequence, range(0, len(sequence)), 1))
    attributes.update(get_letters_index(sequence, range(0, len(sequence)), 2))
    attributes.update(get_letters_index(sequence, range(0, len(sequence)), 3))
    return attributes

#############
# Load data #
#############
def load_dataset(filename):
    '''
    Loads dataset from CSV file into a list.
    '''
    filepath = os.path.join(data_path, filename)
    with open(filepath) as f:
        reader = csv.reader(f)
        dataset = list(reader)
    return dataset


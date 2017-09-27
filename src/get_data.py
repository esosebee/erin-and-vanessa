import os
import csv
import random
from random import randint

#########################
# File path information #
#########################
os.chdir('..')
path = os.getcwd()
data_path = os.path.join(path, 'Data')

###############################################
# Handle ambiguous characters in DNA sequence #
###############################################

def is_ambiguous(sequence):
    '''
    Returns true if ambiguous characters are present in the DNA sequence.
    '''
    return ('D' in sequence or 'N' in sequence or 'S' in sequence or 'R' in sequence)
    

def random_replacement(sequence):
    '''
    Replace the ambiguous characters in the DNA sequence with a character 
    randomly selected from the a list of possible characters.
    '''
    new_sequence = list(sequence)
    for i in range(0, len(sequence)):
        char = sequence[i]
        if char == 'D': # A or G or T
            replacements = ['A', 'G', 'T']
            new_sequence[i] = replacements[randint(0, len(replacements)-1)]
        elif char == 'N': # A or G or C or T
            replacements = ['A', 'G', 'C', 'T']
            new_sequence[i] = replacements[randint(0, len(replacements)-1)]
        elif char == 'S': # C or G
            replacements = ['C', 'G']
            new_sequence[i] = replacements[randint(0, len(replacements)-1)]
        elif char == 'R': # A or G
            replacements = ['A', 'G']
            new_sequence[i] = replacements[randint(0, len(replacements)-1)]
    return ''.join(new_sequence)

def split_sequence_in_half(sequence):
    ''' Splits a DNA sequence perfectly in half. '''
    return sequence[:len(sequence)/2], sequence[len(sequence)/2:]

####################################
# Get attributes from DNA sequence #
####################################
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
        # index_dict[label] = (sequence[i:i+n], i)
        index_dict[label] = sequence[i:i+n]
        i += n
    return index_dict

def get_training_attributes(data):
    '''
    Gets the desired attributes to be tested on from the data.
    '''
    seq_id = data[0] 
    sequence = data[1] 
    boundary = data[2]

    # Handle ambiguous characters in sequence if present
    if is_ambiguous(sequence):
        sequence = random_replacement(sequence)
        
    attributes = {}
    attributes['id'] = seq_id
    attributes['sequence'] = sequence
    attributes['boundary'] = boundary
    attributes.update(get_letters_index(sequence, range(0, len(sequence)), 1))
    attributes.update(get_letters_index(sequence, range(0, len(sequence)), 2))
    attributes.update(get_letters_index(sequence, range(0, len(sequence)), 3))
    return attributes

########################
# Load data  from file #
########################
def load_dataset(filename):
    '''
    Loads dataset from CSV file into a list.
    '''
    filepath = os.path.join(data_path, filename)
    with open(filepath) as f:
        reader = csv.reader(f)
        dataset = list(reader)
    return dataset



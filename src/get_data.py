import os
import csv
import random
from random import randint

RAND_REPLACE = True
PROB_REPLACE = False

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

def weighted_replacement(sequence, letter_probs):
    new_sequence = list(sequence)
    print letter_probs
    for i in range(0, len(sequence)):
        char = sequence[i]
        if char == 'D': # A or G or T
            replacements = ['A', 'G', 'T']
            # new_sequence[i] = replacements[randint(0, len(replacements)-1)]
        elif char == 'N': # A or G or C or T
            replacements = ['A', 'G', 'C', 'T']
            # new_sequence[i] = replacements[randint(0, len(replacements)-1)]
        elif char == 'S': # C or G
            replacements = ['C', 'G']
            # new_sequence[i] = replacements[randint(0, len(replacements)-1)]
        elif char == 'R': # A or G
            replacements = ['A', 'G']
            # new_sequence[i] = replacements[randint(0, len(replacements)-1)]
    return ''.join(new_sequence)

####################################
# Get attributes from DNA sequence #
####################################
def get_letter_frequencies(sequence):
    freq_dict = {}
    n = len(sequence)
    valid_chars = ['A', 'C', 'G', 'T']
    for char in sequence:
        if char in valid_chars:
            if char not in freq_dict:
                freq_dict[char] = 1
            else:
                freq_dict[char] += 1
    return freq_dict

def get_letter_probabilities(sequence):
    prob_dict = {}
    n = len(sequence)
    letter_freqs = get_letter_frequencies(sequence)
    for key in letter_freqs.keys():
        prob_dict[key] = float(letter_freqs[key]) / n 
    return prob_dict

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
        if RAND_REPLACE:
            sequence = random_replacement(sequence)
        # elif PROB_REPLACE:
        #     letter_probs = get_letter_probabilities(sequence)
        #     sequence = weighted_replacement(sequence, letter_probs)
  
    attributes = {}
    attributes['id'] = seq_id
    attributes['sequence'] = sequence
    attributes['boundary'] = boundary
    attributes.update(get_letters_index(sequence, range(0, len(sequence)), 1))
    attributes.update(get_letters_index(sequence, range(0, len(sequence)), 2))
    attributes.update(get_letters_index(sequence, range(0, len(sequence)), 3))
    return attributes

def get_testing_attributes(data):
    '''
    Gets the attributes to test against the decision tree from the testing data.
    '''
    seq_id = data[0]
    sequence = data[1]

    if is_ambiguous(sequence):
        if RAND_REPLACE:
            sequence = random_replacement(sequence)

    attributes = {}
    attributes['id'] = seq_id
    attributes['sequence'] = sequence 
    attributes.update(get_letters_index(sequence, range(0, len(sequence)), 1))
    attributes.update(get_letters_index(sequence, range(0, len(sequence)), 2))
    attributes.update(get_letters_index(sequence, range(0, len(sequence)), 3))
    return attributes

########################
# Load data  from file #
########################
def load_dataset(filename, data_path):
    '''
    Loads dataset from CSV file into a list.
    '''
    filepath = os.path.join(data_path, filename)
    with open(filepath) as f:
        reader = csv.reader(f)
        dataset = list(reader)
    return dataset



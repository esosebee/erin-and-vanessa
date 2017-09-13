import os, sys
import csv
from math import log

# NOTE: 
# For boundaries:
#   - IE = intron -> exon
#   - EI = exon -> intron
#   - N = neither

# Data location information
path = os.getcwd()
data_path = os.path.join(path, 'Data')

def load_dataset(filename):
    filepath = os.path.join(data_path, filename)
    with open(filepath) as f:
        reader = csv.reader(f)
        dataset = list(reader)
    return dataset

def get_letter_frequencies(sequence):
    char_freq_dict = {}
    for letter in sequence:
        char_freq_dict[letter] = 0
    for letter in sequence: 
        char_freq_dict[letter] += 1

    return char_freq_dict

def get_letter_indexes(sequence):
    char_index_dict = {}
    for letter in sequence:
        char_index_dict[letter] = [i for i, x in enumerate(sequence) if x == letter]
    return char_index_dict

def get_sequence_chunks(sequence, n):
    return [sequence[i:i+n] for i in range(0, len(sequence), n)]

def split_sequence(sequence):
    return sequence[:len(sequence)/2], sequence[len(sequence)/2:]

def get_pair_frequencies(sequence):
    pair_freq_dict = {}
    seq_pairs = get_sequence_chunks(sequence, 2)
    for pair in seq_pairs:
        pair_freq_dict[pair] = 0
    for pair in seq_pairs:
        pair_freq_dict[pair] += 1
    
    return pair_freq_dict

def get_pair_index(sequence):
    pair_index_dict = {}
    seq_pairs = get_sequence_chunks(sequence, 2)
    for pair in seq_pairs:
        pair_index_dict[pair] = [i for i, x in enumerate(seq_pairs) if x == pair]
    return pair_index_dict

def get_pair_at_index(sequence, i_range):
    index_pairs_dict = {}
    for i in range(0, len(sequence)-1):
        index_pairs_dict[i] = sequence[i:i+2]
    return index_pairs_dict

def get_triples_position(sequence):
    triples_pos_dict = {}
    triples = get_sequence_chunks(sequence, 3)
    
    # Gets indices of values in triples
    for t in triples:
        # triples_pos_dict[t] = [(i*3,i*3+1,i*3+2) for i, x in enumerate(triples) if x == t]
        triples_pos_dict[t] = [i*3 for i, x in enumerate(triples) if x == t]
    return triples_pos_dict

def get_triple_at_index(sequence, i_range):
    index_triples_dict = {}
    for i in range(0, len(sequence)-2):
        index_triples_dict[i] = sequence[i:i+3]
    return index_triples_dict

# TODO: get triples and their position
def get_attributes(data):
    attributes = {}
    attributes['id'] = int(data[0])
    attributes['sequence'] = data[1]
    attributes['boundary'] = data[2]
    attributes['letter_frequencies'] = get_letter_frequencies(data[1])
    attributes['letter_index'] = get_letter_indexes(data[1])
    attributes['pair_frequencies'] = get_pair_frequencies(data[1])
    attributes['pair_at_index'] = get_pair_at_index(data[1], range(0, len(data[1])))
    attributes['triple_at_index'] = get_triple_at_index(data[1], range(0, len(data[1])))
    # attributes['pair_position'] = get_pair_index(data[1])
    # attributes['triples_position'] = get_triples_position(data[1])
    
    return attributes

if __name__ == '__main__':
    training_filename = 'training.csv'
    testing_filename = 'testing.csv'

    training_attributes, testing_attributes = [], []

    training_data = load_dataset(training_filename)
    testing_data = load_dataset(testing_filename)

    # for t in training_data:
    #     training_attributes.append(get_attributes(t))


    
    test_data = ['1995', 'GCTGAGGCCTGGCTCTCTCCCTCCCCACAGGGTGCCCGGTACGTGTGGAACCGCACTGAG', 'IE']
    attributes = get_attributes(test_data)
    # for key in attributes:
    #     print key
    #     print attributes[key]
    #     print '\n' 




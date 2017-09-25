
def get_attribute_frequencies(dataset):
    freq_dict = {}
    for d in dataset:
        for key in d:
            val = d[key] 
            if val in freq_dict:
                freq_dict[val] += 1
            else:
                freq_dict[val] = 1
    return freq_dict

def get_expected_values(attr_freqs, total_attrs):
    expected_vals_dict = {}
    for item in attr_freqs:
        expected_vals_dict[item] = attr_freqs[item] * (float(attr_freqs[item]) / total_attrs)
    return expected_vals_dict

def observed_expected_diff_squared(attr_freqs, expected_values):
    diffs_squared_dict = {}
    keys = attr_freqs.keys()
    for key in keys:
        diffs_squared_dict[key] = (attr_freqs[key] - expected_values[key]) ** 2
    return diffs_squared_dict

def get_chi_square_values(diffs_squared, expected_values):
    chi_dict = {}
    keys = diffs_squared.keys()
    for key in keys:
        # print 'diffs squared: ', diffs_squared[key]
        # print 'expected values: ', expected_values[key]
        chi_dict[key] = diffs_squared[key] / expected_values[key]
    return chi_dict

def chi_square_test(dataset, target_attr): # Need an alpha value?
    # TODO: Do we test on target attributes (boundary) or all attributes
    # that are used as predictors?

    # Build contingency table
    attr_freqs = get_attribute_frequencies(dataset) # Get frequency of each attribute
    expected_values = get_expected_values(attr_freqs, len(dataset[0])) # Get expected values for each attribute 
    diffs_squared = observed_expected_diff_squared(attr_freqs, expected_values) # Get squared differences between observed frequencies and expected values
    chi_square_values = get_chi_square_values(diffs_squared, expected_values) # Get chi-squared values
    attrs = chi_square_values.keys()
    
    # Get chi-squared statistic
    chi_squared_stat = 0.0
    for attr in attrs:
        chi_squared_stat += chi_square_values[attr]
    
    # Get critical values
    
    # return 1.0 - pvalue


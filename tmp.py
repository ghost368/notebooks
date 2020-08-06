import numpy as np
def my_lower(s):
    return s.lower()

def correct_strings(arr):
    output = []
    for s in arr:
        output.append(my_lower(s))
    return np.array(output)
